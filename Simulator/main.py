from asyncore import poll
import pygame
import numpy as np
from WindSimulator import WindSimulator
from PollutionSimulator import PollutionSimulator
from TrafficManager import TrafficSimulator
import math
import random

random.seed(1)

# parameters to play with
# =========================
resolution = 100 #1 cell = 100m
cellSize = int(resolution * 0.2)
mapSizePixels = 680
mapWidth = int(mapSizePixels / cellSize)
mapHeight = int(mapSizePixels / cellSize)
thremalDiffusion = 0.1
selfDecay = 0.0
selfDecayValues = np.array([0.001, 0.01, 0.0])
lateralDiffusionValues = np.array([0.9, 0.01, 0.1])
showWindVectors = True
showGrid = False
showBackgroundMap = True
windEnabled = True
isPolutionContained = False
windSpeed = 0.001
windPerlinNoiseStep = 2.0
simulationPaused = False
drawMouseInfo = True
history_savefile = "./results_wind/pollution_history_trucks_ev20.csv"
sampled_savefile = "./results_wind/pollution_sampled_trucks_ev20.csv"
saveResults = False
# ===========================

# Create pollution simulator
pollution = PollutionSimulator(mapWidth, mapHeight)

# Create wind simulator
wind = WindSimulator(mapWidth, mapHeight, windPerlinNoiseStep)
wind.makeRandom(windSpeed)
#traffic = TrafficSimulator("/Users/carlo/Downloads/Lyngby3/processed/cars/baseline.parquet", pollution, mapWidth, mapHeight, cellSize)
#traffic = TrafficSimulator("/Users/carlo/Downloads/Lyngby3/processed/trucks/baseline.parquet", pollution, mapWidth, mapHeight, cellSize)
#traffic = TrafficSimulator("/Users/carlo/Downloads/Lyngby3/processed/cars/ev_10.parquet", pollution, mapWidth, mapHeight, cellSize)
#traffic = TrafficSimulator("/Users/carlo/Downloads/Lyngby3/processed/cars/ev_15.parquet", pollution, mapWidth, mapHeight, cellSize)
#traffic = TrafficSimulator("/Users/carlo/Downloads/Lyngby3/processed/cars/ev_20.parquet", pollution, mapWidth, mapHeight, cellSize)
#traffic = TrafficSimulator("/Users/carlo/Downloads/Lyngby3/processed/cars/ev_54.parquet", pollution, mapWidth, mapHeight, cellSize)
#traffic = TrafficSimulator("./processed/trucks/ev_10.parquet", pollution, mapWidth, mapHeight, cellSize)
traffic = TrafficSimulator("../SUMO/Lyngby/processed/trucks/ev_20.parquet", pollution, mapWidth, mapHeight, cellSize)
print("Done")

# Create pygame window with no title
pygame.display.set_caption('')
pygame.init()
screen = pygame.display.set_mode([mapWidth * cellSize + 32, mapHeight * cellSize + 32])
fontlog = pygame.font.SysFont('Menlo', 12)
fontMouseInfo = pygame.font.SysFont('Menlo', 16)

# Load background image and scale it to map 
#backgroundImg = pygame.image.load('map_osterbro_grayscale.png')
backgroundImg = pygame.image.load('map_lyngby_grayscale.png')
backgroundImg = pygame.transform.scale(backgroundImg, (mapWidth * cellSize, mapHeight * cellSize))

# Make surface to render pollution on top of map
pollutionSurface = pygame.Surface( (mapWidth * cellSize, mapHeight * cellSize ), pygame.SRCALPHA )

pollutionSample = []
pollutionHistory = []

running = True
t = 0;
drawMaxvalue = 1.0
while running:

    #Handle keyboard input and mouse input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # close app when X is pressed
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_v:
                showWindVectors = not showWindVectors
            if event.key == pygame.K_e:
                wind.makeRandom(windSpeed)
            if event.key == pygame.K_u:
                wind.makeUniform(angle=(random.random() * math.pi * 2), speed=windSpeed)
            if event.key == pygame.K_n:
                wind.makeNoWind()
            if event.key == pygame.K_d:
                pollution.selfDecay = selfDecayValues[0]
                selfDecayValues = np.roll(selfDecayValues, -1)
            if event.key == pygame.K_l:
                pollution.thermalDiffusion = lateralDiffusionValues[0]
                lateralDiffusionValues = np.roll(lateralDiffusionValues, -1)
            if event.key == pygame.K_g:
                showGrid = not showGrid
            if event.key == pygame.K_w:
                windEnabled = not windEnabled
            if event.key == pygame.K_b:
                showBackgroundMap = not showBackgroundMap
            if event.key == pygame.K_p:
                simulationPaused = not simulationPaused

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if ((pos[0] < mapWidth * cellSize) and (pos[1] < mapHeight * cellSize)):  # mouse inside map
                pollution.insertPollution(int(pos[0] / cellSize), int(pos[1] / cellSize), 2.0)

    # clean screen with black color
    screen.fill((0, 0, 0))
    pollutionSurface.fill((0, 0, 0, 0))

    # Draw map in the background
    if (showBackgroundMap):
        screen.blit(backgroundImg, (0, 0))

    # switch buffer
    pollution.swapBuffer();
    
    # dissipate into the atmosphere / self decay
    if (simulationPaused == False):
        pollution.applySelfDecay();

    #Loop throw each city zone and update the pollution state + draw stuff
    maxCellPollution = 0.0
    for x in range(mapWidth):
        for y in range(mapHeight):
            
            if (simulationPaused == False):
                # compute amount brought away by wind
                if (windEnabled):
                    windVec = wind.getVec(x, y)
                    pollution.updateWindEffect(x, y, windVec)

                # Thermal diffusion
                pollution.updateThermalDiffusion(x, y)

            # draw pollution in the current city area
            P = pollution.getPollution(x, y)
            maxCellPollution = max(maxCellPollution, P)
            if (P != 0):
                pygame.draw.rect(pollutionSurface, (255 * min(1.0, P), 0, 0, 200 * min(1.0, P / (drawMaxvalue * 0.8))), (x * cellSize, y * cellSize, cellSize, cellSize))

            # draw wind vectors
            if (showWindVectors):
                windVec = wind.getVec(x, y)

                # normalize wind vector
                windSpeed = math.sqrt(windVec[0]*windVec[0] + windVec[1]*windVec[1])

                # draw wind vector
                if (windSpeed != 0.0):
                    windVec = ((windVec[0] / windSpeed) * cellSize/2, (windVec[1] / windSpeed) * cellSize/2)
                    pygame.draw.line(pollutionSurface, (0, 0, 255),
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
    totalpolution = pollution.computeTotalPollution()
    if (simulationPaused == False):
        pollutionHistory.append(totalpolution)
        mousepos = pygame.mouse.get_pos()
        if (mousepos[0] >= 0 and mousepos[1] >= 0 and (mousepos[0] < mapWidth * cellSize) and (mousepos[1] < mapHeight * cellSize)):  # mouse inside map
            pygame.draw.rect(pollutionSurface, (0, 0, 0, 150), (mousepos[0]+16 -2, mousepos[1]-16 +2, 96, 32))
            P = pollution.getPollution(int(mousepos[0] / cellSize), int(mousepos[1] / cellSize))
        else:
            P = 0.0
        pollutionSample.append(P)

    drawMaxvalue = max(maxCellPollution, 1.0)

    # Update traffic simulator
    if (simulationPaused == False):
        traffic.update(t)
    traffic.draw(t, pollutionSurface)

    # Stop simulation when the traffic simulator is done
    if (traffic.isSimulationDone() and simulationPaused == False):
        simulationPaused = True
        if (saveResults):
            np.savetxt(history_savefile, np.array(pollutionHistory), delimiter=',')
            np.savetxt(sampled_savefile, np.array(pollutionSample), delimiter=',')

    # Draw mouse logging 
    if (drawMouseInfo):
        mousepos = pygame.mouse.get_pos()
        if (mousepos[0] >= 0 and mousepos[1] >= 0 and (mousepos[0] < mapWidth * cellSize) and (mousepos[1] < mapHeight * cellSize)):  # mouse inside map
            pygame.draw.rect(pollutionSurface, (0, 0, 0, 150), (mousepos[0]+16 -2, mousepos[1]-16 +2, 96, 32))
            P = pollution.getPollution(int(mousepos[0] / cellSize), int(mousepos[1] / cellSize))
            windVec = wind.getVec(int(mousepos[0]/cellSize), int(mousepos[1]/cellSize))
            W = math.sqrt(windVec[0]*windVec[0] + windVec[1]*windVec[1])
            pollutionIndicator = fontMouseInfo.render("P: {:.3f}".format(P), False, (255, 255, 255))
            windIndicator = fontMouseInfo.render("W: {:.3f}".format(W), False, (255, 255, 255))
            pollutionSurface.blit(pollutionIndicator, (mousepos[0]+16, mousepos[1]-16))
            pollutionSurface.blit(windIndicator, (mousepos[0]+16, mousepos[1]))


    # Draw pollution info over the map 
    screen.blit(pollutionSurface, (0, 0))
    
    # draw logging info
    logtext = fontlog.render('W:{} | H:{} | cell:{} | decay:{} | diff:{} | wind: {} | t: {} | totalp: {:.3f}'
        .format(mapWidth, mapHeight, cellSize, pollution.selfDecay, pollution.thermalDiffusion, windEnabled, t, totalpolution), False, (255, 255, 255))
    screen.blit(logtext, (8, mapHeight * cellSize + 8))

    # draw everything
    pygame.display.flip()
    
    # increase simulation time 
    if (simulationPaused == False):
        t += 1

pygame.quit()
