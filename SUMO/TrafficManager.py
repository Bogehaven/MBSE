
class Vehicle():
    def __init__(self, x, y, speed,Energy_type,Vehicle_type):
        self.x = x
        self.y = y
        self.speed = speed
        self.energy=Energy_type
        self.vehicle=Vehicle_type

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
    def __init__(self):
        self.vehicles = []

    def addVehicle(self, x, y,speed,Energy_type,Vehicle_type):
        vehicle=Vehicle()
        vehicle.x=x
        vehicle.y=y
        vehicle.speed=speed
        vehicle.energy=Energy_type
        vehicle.vehicle=Vehicle_type

        self.vehicles.append(vehicle)

    def DrawAllVehicles(self):#move to the main()?
        for i in range(len(self.vehicles)):
            single_vehicle=self.vehicles[i]
            self.UpdateAllVehicles(single_vehicle)

    def UpdateAllVehicles(self,PerVehicle):#SUMO output file(CSV/DATAFRAME) to python
        pollution.insertPollution(int(min(max(0, PerVehicle.x / cellSize), mapWidth - 1)),
                                  int(min(max(0, PerVehicle.y / cellSize), mapHeight - 1)), 0.1)
        pygame.draw.rect(pollutionSurface, (255, 255, 0), (PerVehicle.x - 4, PerVehicle.y - 4, 8, 8))



