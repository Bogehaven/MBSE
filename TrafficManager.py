import pygame
import pandas

class TrafficSimulator:
    def __init__(self,sumodata_filename, pollution,mapWidth,mapHeight,cellSize):
        self.vehicles = []
        self.mapWidth=mapWidth
        self.mapHeight=mapHeight
        self.cellSize=cellSize
        self.pollution=pollution
        self.simulationDone = False
        
        self.data = pandas.read_parquet(sumodata_filename)
        self.min_x = self.data['x'].min()
        self.max_x = self.data['x'].max()
        self.min_y = self.data['y'].min()
        self.max_y = self.data['y'].max()
        self.center_x = (self.max_x + self.min_x) / 2
        self.center_y = (self.max_y + self.min_y) / 2
        # self.types = self.data['type'].unique()
        # print(self.types)

        # Tweak to fit the projection
        self.resolution = 11132.0 * 2                           # 1 degree = 111.32km, works as zoom
        self.center_x_offset = mapWidth * cellSize / 2 + 10         # Drawing point of reference X
        self.center_y_offset = mapHeight * cellSize / 2 - 5        # Drawing point of reference Y
        self.lat_coeff = 0.5 + 0.09                                 # Scaling of latitude
        self.long_coeff = 1.0                                       # Scaling of longitude

        self.timesteps = []
        for t in range(int(self.data['time'].unique().max())):
            self.timesteps.append(self.data[self.data['time'] == t])

    def getDegreeToPixelCoordinates(self, vehicleX, vehicleY):
        y = self.center_y_offset + -(vehicleY - self.center_y) * self.long_coeff * self.resolution
        x = self.center_x_offset + (vehicleX - self.center_x) * self.lat_coeff * self.resolution
        return (x, y)

    def getVehicleColor(self,vehicle):
        ColorMap={
            'veh_petrol': (0,0,255),#blue
            'veh_diesel':(30,144,255),#dodgerblue1
            'veh_hybrid': (0,191,255),#deepskyblue1
            'veh_ev':(135,206,235),#skyblue

            'truck_petrol': (139,105,20),#goldenrod4
            'truck_hybrid':(255,255,0)#yellow1
        }
        type=vehicle.type
        Color=ColorMap[type]
        return Color

    def draw(self, t, pollutionSurface):
        if (t >= len(self.timesteps)): return # No more data?

        vehicles = self.timesteps[t]
        for i, vehicle in vehicles.iterrows():
            pixel_x, pixel_y = self.getDegreeToPixelCoordinates(vehicle.x, vehicle.y)
            color = self.getVehicleColor(vehicle)
            pygame.draw.rect(pollutionSurface, color, (pixel_x - 3, pixel_y - 3, 6, 6))

    def isSimulationDone(self):
        return self.simulationDone

    def update(self, t):
        if (t >= len(self.timesteps)): 
            self.simulationDone = True
            return # No more data?

        vehicles = self.timesteps[t]
        for i, vehicle in vehicles.iterrows():
            pixel_x, pixel_y = self.getDegreeToPixelCoordinates(vehicle.x, vehicle.y)
            self.pollution.insertPollution(int(min(max(0, pixel_x / self.cellSize), self.mapWidth - 1)),
                                           int(min(max(0, pixel_y / self.cellSize), self.mapHeight - 1)), vehicle.NOx / 100.0)
