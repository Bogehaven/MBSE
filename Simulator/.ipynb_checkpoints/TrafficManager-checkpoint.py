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
        self.scaleFactor = 0.2
        self.y_offset = mapHeight * cellSize -58;
        self.x_offset = 118

        self.data = pandas.read_parquet(sumodata_filename)
        self.min_x = self.data['x'].min()
        self.max_x = self.data['x'].max()
        self.min_y = self.data['y'].min()
        self.max_y = self.data['y'].max()
        # self.types = self.data['type'].unique()
        # print(self.types)

        self.timesteps = []
        for t in range(int(self.data['timedelta'].unique().max())):
            self.timesteps.append(self.data[self.data['timedelta'] == t])

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
            pixel_x, pixel_y = (self.x_offset + vehicle.x * self.scaleFactor, self.y_offset - vehicle.y * self.scaleFactor)
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
            pixel_x, pixel_y = (self.x_offset + vehicle.x * self.scaleFactor, self.y_offset - vehicle.y * self.scaleFactor)
            self.pollution.insertPollution(int(min(max(0, pixel_x / self.cellSize), self.mapWidth - 1)),
                                           int(min(max(0, pixel_y / self.cellSize), self.mapHeight - 1)), vehicle.NOx / 100.0)
