import pygame
import pandas

class TrafficSimulator:
    def __init__(self,sumodata_filename, pollution,mapWidth,mapHeight,cellSize):
        self.vehicles = []
        self.mapWidth=mapWidth
        self.mapHeight=mapHeight
        self.cellSize=cellSize
        self.pollution=pollution
        
        self.data = pandas.read_parquet(sumodata_filename)
        self.min_x = self.data['x'].min()
        self.max_x = self.data['x'].max()
        self.min_y = self.data['y'].min()
        self.max_y = self.data['y'].max()
        self.center_x = (self.max_x + self.min_x) / 2  
        self.center_y = (self.max_y + self.min_y) / 2
        self.resolution = 11132.0 * 2 ##1 degree = 111.32km
        self.long_coeff = 0.5
        print(self.min_x)
        print(self.min_y)
        print(self.max_x)
        print(self.max_y)

    def getDegreeToPixelCoordinates(self, vehicleX, vehicleY):
        y = self.mapHeight * self.cellSize / 2 + -(vehicleY - self.center_y) * self.resolution
        x = self.mapWidth * self.cellSize / 2 + (vehicleX - self.center_x) * self.long_coeff * self.resolution
        return (x, y)

    def draw(self, t, pollutionSurface):#move to the main()?
        vehicles = self.data[self.data['time'] == t]
        for i, vehicle in vehicles.iterrows():
            pixel_x, pixel_y = self.getDegreeToPixelCoordinates(vehicle.x, vehicle.y)
            pygame.draw.rect(pollutionSurface, (255, 255, 0), (pixel_x - 4, pixel_y - 4, 8, 8))

    def update(self, t):#SUMO output file(CSV/DATAFRAME) to python
        vehicles = self.data[self.data['time'] == t]
        for i, vehicle in vehicles.iterrows():
            pixel_x, pixel_y = self.getDegreeToPixelCoordinates(vehicle.x, vehicle.y)
            self.pollution.insertPollution(int(min(max(0, pixel_x / self.cellSize), self.mapWidth - 1)),
                                           int(min(max(0, pixel_y / self.cellSize), self.mapHeight - 1)), vehicle.NOx / 100.0)
