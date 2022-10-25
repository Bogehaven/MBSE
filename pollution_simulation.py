import pygame
import numpy as np
from perlin_noise import PerlinNoise
import random
import math

# parameters to play with
# =========================
mapWidth = 40
mapHeight = 40
cellSize = 15
lateralDiffusion = 0.1
selfDecay = 0.0
selfDecayValues = np.array([0.001, 0.01, 0.0])
lateralDiffusionValues = np.array([0.9, 0.01, 0.1])
showWindVectors = True
showGrid = False
windEnabled = True
isPolutionContained = False
windMagnitued = 0.1
windPerlinNoiseStep = 2.0
simulationPaused = False
# ===========================

# Buffers to store pollution
currentBuffer = 0
nextBuffer = (currentBuffer == 0) * 1

# initialize with no pollution and no wind
buffers = np.zeros(shape=(mapWidth, mapHeight, 2))
windVectors = np.zeros(shape=(mapWidth, mapHeight, 2))
buffers[:, :, nextBuffer] = buffers[:, :, currentBuffer]

# Create pygame window with no title
pygame.display.set_caption('')
pygame.init()
screen = pygame.display.set_mode([600 + 32, 600 + 32])
fontlog = pygame.font.SysFont('Menlo', 12)

# Class to generate random wind based on x, y, time and uniform speed
class WindGenerator:
    def __init__(self, seed=1):
        self.seed = seed
        self.xnoise = PerlinNoise(seed=(random.random() * seed))
        self.ynoise = PerlinNoise(seed=(random.random() * seed))

    def getVec(self, x, y, t, speed):
        xx = (x / mapWidth) * windPerlinNoiseStep
        yy = (y / mapHeight) * windPerlinNoiseStep
        return (self.xnoise([xx, yy, t]) * speed, self.ynoise([xx, yy, t]) * speed)

# Generate some random wind pattern
windgen = WindGenerator()
for x in range(mapWidth):
    for y in range(mapHeight):
        windVec = windgen.getVec(x, y, 0, windMagnitued)
        windVectors[x, y, 0] = windVec[0]
        windVectors[x, y, 1] = windVec[1]

running = True
t = 0;
while running:

    #Handle keyboard input and mouse input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # close app when X is pressed
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_v:
                showWindVectors = not showWindVectors
            if event.key == pygame.K_e:
                for x in range(mapWidth):
                    for y in range(mapHeight):
                        windVec = windgen.getVec(x, y, t * 0.1, windMagnitued)
                        windVectors[x, y, 0] = windVec[0]
                        windVectors[x, y, 1] = windVec[1]
            if event.key == pygame.K_d:
                selfDecay = selfDecayValues[0]
                selfDecayValues = np.roll(selfDecayValues, -1)
            if event.key == pygame.K_l:
                lateralDiffusion = lateralDiffusionValues[0]
                lateralDiffusionValues = np.roll(lateralDiffusionValues, -1)
            if event.key == pygame.K_g:
                showGrid = not showGrid
            if event.key == pygame.K_w:
                windEnabled = not windEnabled
            if event.key == pygame.K_p:
                simulationPaused = not simulationPaused

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if ((pos[0] < mapWidth * cellSize) and (pos[1] < mapHeight * cellSize)):  # mouse inside map
                buffers[int(pos[0] / cellSize), int(pos[1] / cellSize), nextBuffer] = 50.0  # insert pollution
    
    # clean screen with black color
    screen.fill((0, 0, 0))

    # switch buffer
    currentBuffer = nextBuffer
    nextBuffer = (currentBuffer == 0) * 1
    
    # dissipate into the atmosphere / self decay
    buffers[:, :, nextBuffer] = buffers[:, :, currentBuffer] * (1 - selfDecay)

    #Loop throw each city zone and update the pollution state + draw stuff
    for x in range(mapWidth):
        for y in range(mapHeight):
            
            if (simulationPaused == False):
                # count number of neighbours, to contain pollution inside simulation map, if wanted
                neightbours = np.array([int(x-1 >= 0), int(x + 1 < mapWidth), int(y - 1 >= 0), int(y + 1 < mapHeight)])
                neightboursCount = np.count_nonzero(neightbours)
                if (isPolutionContained == False):
                    neightboursCount = 4

                P = buffers[x, y, currentBuffer]

                # compute lateral diffusion quantity
                diffusionAmount = (P * lateralDiffusion) / neightboursCount
                buffers[x, y, nextBuffer] -= P * lateralDiffusion

                # compute amount brought away by wind
                if (windEnabled):
                    wind = (windVectors[x, y, 0], windVectors[x, y, 1])
                    
                    windCarriedAmount = (math.fabs(wind[0]) + math.fabs(wind[1])) * P

                    # move polution either left or right
                    if (wind[0] > 0):
                        buffers[min(x + 1, mapWidth-1), y, nextBuffer] += wind[0] * P
                    else:
                        buffers[max(x - 1, 0), y, nextBuffer] += -wind[0] * P

                    # move polution either up or down
                    if (wind[1] > 0):
                        buffers[x, min(y+1, mapHeight-1), nextBuffer] += wind[1] * P
                    else:
                        buffers[x, max(y-1, 0), nextBuffer] += -wind[1] * P

                    # reduce polution in current cell
                    buffers[x, y, nextBuffer] -= windCarriedAmount

                # diffuse pollution
                buffers[max(x - 1, 0), y, nextBuffer] += diffusionAmount * neightbours[0]
                buffers[min(x + 1, mapWidth-1), y, nextBuffer] += diffusionAmount * neightbours[1]
                buffers[x, max(y-1, 0), nextBuffer] += diffusionAmount * neightbours[2]
                buffers[x, min(y+1, mapHeight-1), nextBuffer] += diffusionAmount * neightbours[3]

            # draw pollution in the current city area
            if (buffers[x, y, nextBuffer] != 0):
                pygame.draw.rect(screen, (255 * min(1.0, buffers[x, y, currentBuffer]), 0, 0), (x * cellSize, y * cellSize, cellSize, cellSize))

            # draw wind vectors
            if (showWindVectors):
                wind = (windVectors[x, y, 0], windVectors[x, y, 1])
                # normalize wind vector
                windSpeed = math.sqrt(wind[0]*wind[0] + wind[1]*wind[1])
                
                # draw wind vector
                if (windSpeed != 0.0):
                    windVec = ((wind[0] / windSpeed) * cellSize/2, (wind[1] / windSpeed) * cellSize/2)
                    pygame.draw.line(screen, (0, 0, 255),
                            (x * cellSize + cellSize/2, y * cellSize + cellSize/2),
                            (x * cellSize + cellSize/2 + windVec[0], y * cellSize + cellSize/2 + windVec[1]), width=2)
    if (showGrid):
        # vertical lines
        for x in range(mapWidth):
            pygame.draw.line(screen, (150, 150, 150),
                    (x * cellSize, 0),
                    (x * cellSize, mapHeight * cellSize), width=1)
        
        for y in range(mapHeight):
            pygame.draw.line(screen, (150, 150, 150),
                    (0, y * cellSize),
                    (mapWidth * cellSize, y * cellSize), width=1)

    # Compute total current pollution in the map (just for debugging) 
    totalpolution = 0.0
    for x in range(mapWidth):
        for y in range(mapHeight):
            totalpolution += buffers[x, y, currentBuffer]
    
    # draw logging info
    logtext = fontlog.render('W:{} | H:{} | cell:{} | decay:{} | diff:{} | wind: {} | t: {} | totalp: {:.3f}'.format(mapWidth, mapHeight, cellSize, selfDecay, lateralDiffusion, windEnabled, t, totalpolution), False, (255, 255, 255))
    screen.blit(logtext, (8, mapHeight * cellSize + 8))

    # draw everything
    pygame.display.flip()
    
    # increase simulation time 
    if (simulationPaused == False):
        t += 1

pygame.quit()
