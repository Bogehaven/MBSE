import numpy as np
import math
from perlin_noise import PerlinNoise
import random

class WindSimulator:
    def __init__(self, mapWidth, mapHeight, windPerlinNoiseStep, seed=1):
        self.mapWidth = mapWidth
        self.mapHeight = mapHeight
        self.vectors = windVectors = np.zeros(shape=(mapWidth, mapHeight, 2))
        self.seed = seed
        self.windPerlinNoiseStep = windPerlinNoiseStep
        self.anglenoise = PerlinNoise(seed=(random.random() * seed))

    # Generate random wind direction with speed using perlin noise
    def makeRandom(self, speed):
        for x in range(self.mapWidth):
            for y in range(self.mapHeight):
                xx = (x / self.mapWidth) * self.windPerlinNoiseStep
                yy = (y / self.mapHeight) * self.windPerlinNoiseStep
                angle = (self.anglenoise([xx, yy, self.seed]) + 1.0) * math.pi * 2
                self.vectors[x, y, 0] = math.cos(angle) * speed
                self.vectors[x, y, 1] = math.sin(angle) * speed
        self.seed = random.random() * 1000

    # Generate wind with a specific angle and speed uniform all over the map
    def makeUniform(self, angle, speed):
        for x in range(self.mapWidth):
            for y in range(self.mapHeight):
                self.vectors[x, y, 0] = math.cos(angle) * speed
                self.vectors[x, y, 1] = math.sin(angle) * speed

    # Remove the wind in all the map    
    def makeNoWind(self):
        for x in range(self.mapWidth):
            for y in range(self.mapHeight):
                self.vectors[x, y, 0] = 0
                self.vectors[x, y, 1] = 0

    # Get wind vector for a specific map zone    
    def getVec(self, x, y):
        return (self.vectors[x, y, 0], self.vectors[x, y, 1])
        
        