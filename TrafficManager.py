import pygame

class Vehicle():
    def __init__(self, x, y, speed,Energy_type,Vehicle_type,Vehicle_id):
        self.x = x
        self.y = y
        self.speed = speed
        self.energy=Energy_type
        self.vehicle=Vehicle_type
        self.id=Vehicle_id

#to do(just for test)
        if self.energy=='Petrol':
            if self.vehicle=='Passenger':
                self.color='DarkSlateBlue'
                self.InsertPolltion=10
            elif self.vehicle=='Truck':
                self.color='Blue'
                self.InsertPolltion=11
            elif self.vehicle == 'Bus':
                self.color = 'DarkGoldenrod'
                self.InsertPolltion = 12

        elif self.energy=='Diesel':
            if self.vehicle == 'Passenger':
                self.color = 'SlateBlue'
                self.InsertPolltion = 9
            elif self.vehicle == 'Truck':
                self.color = 'DodgerBlue'
                self.InsertPolltion = 10
            elif self.vehicle == 'Bus':
                self.color = 'goldenrod'
                self.InsertPolltion = 11

        elif self.energy=='Hybrid':
            if self.vehicle == 'Passenger':
                self.color = 'MediumSlateBlue'
                self.InsertPolltion = 8
            elif self.vehicle == 'Truck':
                self.color = 'DeepSkyBlue'
                self.InsertPolltion = 9
            elif self.vehicle == 'Bus':
                self.color = 'LightGoldenrod'
                self.InsertPolltion = 10

        elif self.energy=='Electric':
            if self.vehicle == 'Passenger':
                self.color = 'LightSlateBlue'
                self.InsertPolltion = 7
            elif self.vehicle == 'Truck':
                self.color = 'SkyBlue'
                self.InsertPolltion = 8
            elif self.vehicle == 'Bus':
                self.color = 'LightYellow'
                self.InsertPolltion = 9


class TrafficManager:
    def __init__(self,pollution,mapWidth,mapHeight,cellSize):
        self.vehicles = []
        self.mapWidth=mapWidth
        self.mapHeight=mapHeight
        self.cellSize=cellSize
        self.pollution=pollution

    def addVehicle(self, x, y,speed,Energy_type,Vehicle_type,Vehicle_id):
        vehicle=Vehicle()
        vehicle.x=x
        vehicle.y=y
        vehicle.speed=speed
        vehicle.energy=Energy_type
        vehicle.vehicle=Vehicle_type
        vehicle.id=Vehicle_id

        self.vehicles.append(vehicle)

    def DrawAllVehicles(self,PollutionSurface):#move to the main()?
        pollutionSurface=PollutionSurface
        for i in range(len(self.vehicles)):
            single_vehicle=self.vehicles[i]
            color=single_vehicle.color
            pygame.draw.rect(pollutionSurface, color, (single_vehicle.x - 4, single_vehicle.y - 4, 8, 8))

    def UpdateAllVehicles(self):#SUMO output file(CSV/DATAFRAME) to python
        for i in range(len(self.vehicles)):
            single_vehicle = self.vehicles[i]
            OriginalPollution=single_vehicle.InsertPolltion
            self.pollution.insertPollution(int(min(max(0, single_vehicle.x / self.cellSize), self.mapWidth - 1)),
                                  int(min(max(0, single_vehicle.y / self.cellSize), self.mapHeight - 1)), OriginalPollution)



