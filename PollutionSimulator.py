import numpy as np
import math

class PollutionSimulator:
    def __init__(self, mapWidth, mapHeight):
        self.mapWidth = mapWidth
        self.mapHeight = mapHeight
        self.currentBuffer = 0
        self.nextBuffer = (self.currentBuffer == 0) * 1
        self.isPolutionContained = False#what is the meaning???
        self.thermalDiffusion = 0.22 # 1.43 - 0.43 * math.log(100)
        self.selfDecay = 0.05

        # initialize with no pollution 
        self.buffers = np.zeros(shape=(mapWidth, mapHeight, 2))
        self.buffers[:, :, self.nextBuffer] = self.buffers[:, :, self.currentBuffer]
    
    def swapBuffer(self):#meaning???
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
            self.buffers[min(x + 1, self.mapWidth-1), y, self.nextBuffer] += windVec[0] * P#right
        else:
            self.buffers[max(x - 1, 0), y, self.nextBuffer] += -windVec[0] * P#left

        # move polution either up or down
        if (windVec[1] > 0):
            self.buffers[x, min(y+1, self.mapHeight-1), self.nextBuffer] += windVec[1] * P#up
        else:
            self.buffers[x, max(y-1, 0), self.nextBuffer] += -windVec[1] * P#down

        # reduce polution in current cell(current-carried)
        self.buffers[x, y, self.nextBuffer] -= windCarriedAmount

    def updateThermalDiffusion(self, x, y):
        # count number of neighbours, to contain pollution inside simulation map, if wanted
        neightbours = np.array([int(x-1 >= 0), int(x + 1 < self.mapWidth), int(y - 1 >= 0), int(y + 1 < self.mapHeight)])##meaning???
        neightboursCount = np.count_nonzero(neightbours)
        if (self.isPolutionContained == False):
            neightboursCount = 4##8 neighbors???

        P = self.buffers[x, y, self.currentBuffer]

        # compute lateral diffusion quantity(divide the total diffusion to 4 parts, and transfer them to its neighbours.)
        diffusionAmount = (P * self.thermalDiffusion) / neightboursCount
        self.buffers[x, y, self.nextBuffer] -=  P * self.thermalDiffusion

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
        self.buffers[x, y, self.nextBuffer] += amount 

    def getPollution(self, x, y):
        return self.buffers[x, y, self.currentBuffer]

    def showThermalDiffusionGraghHorizontal_time(self,x,y):
        import matplotlib.pyplot as plt
        import numpy as np

        y_list=[]
        p_num=10
        for i in range(p_num):
            y_list.append(self.getPollution(x+i,y))
        x=np.linspace(0,len(y_list)-1,len(y_list))
        fig,ax=plt.subplots()
        ax.plot(x,y_list,'g-.o',color='red',linewidth=1)
        plt.title('Diffusion')
        plt.show()

    def showThermalDiffusionGraghHorizontal_percentage_time(self,x,y):
        import matplotlib.pyplot as plt
        import numpy as np

        y_list = []
        y_paper=[]
        p_num = 5#The size of each grid is about 100m*100m
        for i in range(p_num):
            y_list.append(self.getPollution(x + i, y))

        # print(y_list)
        c_ref=y_list[0]
        percentage_list=[]
        for i in range(len(y_list)):
            per_y=y_list[i]/c_ref
            percentage_list.append(per_y)

        x = np.linspace(0, 400, len(percentage_list))
        print(x)

        x_paper=np.linspace(10, 400, 200)
        for i in range(len(x_paper)):
            y_val=1.45-0.45*np.log10(x_paper[i])
            y_paper.append(y_val)

        plot1=plt.plot(x, percentage_list, 'o', label='Our simulation',color='red', linewidth=1)
        plot2=plt.plot(x_paper, y_paper, '--', label='The function in the paper', color='blue', linewidth=1)
        plt.legend(loc=1)

        plt.title('Diffusion_percentage')
        plt.show()


