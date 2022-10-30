import numpy as np
import math

class PollutionSimulator:
    def __init__(self, mapWidth, mapHeight):
        self.mapWidth = mapWidth
        self.mapHeight = mapHeight
        self.currentBuffer = 0
        self.nextBuffer = (self.currentBuffer == 0) * 1
        self.isPolutionContained = False
        self.thermalDiffusion = 0.1
        self.selfDecay = 0.0

        # initialize with no pollution 
        self.buffers = np.zeros(shape=(mapWidth, mapHeight, 2))
        self.buffers[:, :, self.nextBuffer] = self.buffers[:, :, self.currentBuffer]
    
    def swapBuffer(self):
        self.currentBuffer = self.nextBuffer
        self.nextBuffer = (self.currentBuffer == 0) * 1

    # dissipate into the atmosphere / self decay
    def applySelfDecay(self):
        self.buffers[:, :, self.nextBuffer] = self.buffers[:, :, self.currentBuffer] * (1 - self.selfDecay)
    
    def updateWindEffect(self, x, y, windVec):
        P = self.buffers[x, y, self.currentBuffer]
        windCarriedAmount = (math.fabs(windVec[0]) + math.fabs(windVec[1])) * P

        # move polution either left or right
        if (windVec[0] > 0):
            self.buffers[min(x + 1, self.mapWidth-1), y, self.nextBuffer] += windVec[0] * P
        else:
            self.buffers[max(x - 1, 0), y, self.nextBuffer] += -windVec[0] * P

        # move polution either up or down
        if (windVec[1] > 0):
            self.buffers[x, min(y+1, self.mapHeight-1), self.nextBuffer] += windVec[1] * P
        else:
            self.buffers[x, max(y-1, 0), self.nextBuffer] += -windVec[1] * P

        # reduce polution in current cell
        self.buffers[x, y, self.nextBuffer] -= windCarriedAmount

    def updateThermalDiffusion(self, x, y):
        # count number of neighbours, to contain pollution inside simulation map, if wanted
        neightbours = np.array([int(x-1 >= 0), int(x + 1 < self.mapWidth), int(y - 1 >= 0), int(y + 1 < self.mapHeight)])
        neightboursCount = np.count_nonzero(neightbours)
        if (self.isPolutionContained == False):
            neightboursCount = 4

        P = self.buffers[x, y, self.currentBuffer]

        # compute lateral diffusion quantity
        diffusionAmount = (P * self.thermalDiffusion) / neightboursCount
        self.buffers[x, y, self.nextBuffer] -= P * self.thermalDiffusion

        # diffuse pollution
        self.buffers[max(x - 1, 0), y, self.nextBuffer] += diffusionAmount * neightbours[0]
        self.buffers[min(x + 1, self.mapWidth-1), y, self.nextBuffer] += diffusionAmount * neightbours[1]
        self.buffers[x, max(y-1, 0), self.nextBuffer] += diffusionAmount * neightbours[2]
        self.buffers[x, min(y+1, self.mapHeight-1), self.nextBuffer] += diffusionAmount * neightbours[3]

    def computeTotalPollution(self):
        totalpolution = 0.0
        for x in range(self.mapWidth):
            for y in range(self.mapHeight):
                totalpolution += self.buffers[x, y, self.currentBuffer]
        return totalpolution

    def insertPollution(self, x, y, amount):
        self.buffers[x, y, self.nextBuffer] = amount 

    def getPollution(self, x, y):
        return self.buffers[x, y, self.currentBuffer]

    