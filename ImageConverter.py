import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

class ImC:

    def __init__(self):
        img = mpimg.imread('nine/.png')
        sectors = 28
        count = 0
        total = 0
        for i in img:
            for j in i:
                for k in j:
                    if count < 3:
                        total = total + k
                        count = count + 1
                total = total / 3
                count = 0
                for k in range(len(j)):
                    if count < 3:
                        j[k] = total
                total = 0
                count = 0

        yDiv = int(len(img)  / sectors)
        xDiv = int((len(img[0]))  / sectors)
        self.a = [[[0 for a in range(3)] for b in range(sectors)] for dc in range(sectors)]
        for i in range(sectors):
            for j in range(sectors):
                for k in range(int(xDiv)):
                    for l in range(int(yDiv)):
                        count = count + 1
                        total = img[i * yDiv + l][j * xDiv + k][0] + total
                total = total / count
                self.a[i][j] = [total, total, total]
                total = 0
                count = 0
        self.b = []
        for i in range(sectors):
            for j in range(sectors):
                self.b.append(1 - self.a[i][j][0])

    def getArray(self):
        return self.b
        #return self.b

    def show(self):
        imgplot = plt.imshow(self.a)
        #imgplot = plt.imshow(img)
        plt.show()
