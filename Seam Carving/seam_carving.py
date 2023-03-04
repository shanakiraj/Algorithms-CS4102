# CS4102 Spring 2022 -- Unit C Programming
#################################
# Collaboration Policy: You are encouraged to collaborate with up to 3 other
# students, but all work submitted must be your own independently written
# solution. List the computing ids of all of your collaborators in the comment
# at the top of your java or python file. Do not seek published or online
# solutions for any assignments. If you use any published or online resources
# (which may not include solutions) when completing this assignment, be sure to
# cite them. Do not submit a solution that you are unable to explain orally to a
# member of the course staff.
#################################
# Your Computing ID: sra9qsw
# Collaborators: 
# Sources: Introduction to Algorithms, Cormen, https://en.wikipedia.org/wiki/Seam_carving#Process,
#################################
import math
import numpy as np

class SeamCarving:
    def __init__(self):
        self.energy = []
        self.M = []
        self.thing = []
        self.weight = 0
        return

    # This method is the one you should implement.  It will be called to perform
    # the seam carving.  You may create any additional data structures as fields
    # in this class or write any additional methods you need.
    # 
    # @return the seam's weight

    def run(self, image):
        self.thing = image
        self.energy = [[0 for i in range(len(image[0]))] for j in range(len(image))]
        self.calcNRG(image) #puts all of the energy values in self.energy
        if(max(self.energy[0:len(image)][0:len(image[0])]) == 0):
            return 0
        else:
            storeit = self.findSeam(image)
            self.weight = min(self.M[0])
            return self.weight

    def calcNRG(self, image):
        for i in range(len(image[0])):
            for j in range(len(image)):
                    if(j == 0 and i == 0): #dont move up or left
                        temp = self.compute(image, j, i, j, i + 1)  #E
                        temp += self.compute(image, j, i, j+1, i+1) #SE
                        temp += self.compute(image, j, i, j+1, i)  #S
                        temp = temp/3
                        self.energy[j][i] = temp
                    elif(j ==0 and i == len(image[0])-1):
                        temp = self.compute(image, j, i, j, i-1) #W
                        temp += self.compute(image, j, i, j+1, i-1) #SW
                        temp += self.compute(image, j, i, j+1, i)#S
                        temp = temp/3
                        self.energy[j][i] = temp
                    elif(j==0 and i != len(image[0])-1):
                        temp = self.compute(image, j, i, j, i - 1)  #W
                        temp += self.compute(image, j, i, j + 1, i - 1)  #SW
                        temp += self.compute(image, j, i, j + 1, i)  #S
                        temp += self.compute(image, j, i, j+1, i+1)  #SE
                        temp += self.compute(image, j, i, j, i+1)  #E
                        temp = temp/5
                        self.energy[j][i] = temp
                    elif(i==0 and j != len(image)-1): #this is the line thats breaking
                        tempx = self.compute(image, j, i, j-1, i) #N
                        tempx += self.compute(image, j, i, j - 1, i+1)  # NE
                        tempx += self.compute(image, j, i, j + 1, i)  # S
                        tempx += self.compute(image, j, i, j + 1, i + 1)  # SE
                        tempx += self.compute(image, j, i, j, i + 1)  # E
                        tempx = tempx / 5
                        self.energy[j][i] = tempx
                    elif(i ==0 and j == len(image)-1):
                        temp = self.compute(image, j, i, j - 1, i)  # N
                        temp += self.compute(image, j, i, j - 1, i + 1)  # NE
                        temp += self.compute(image, j, i, j, i + 1)  # E
                        temp = temp/3
                        self.energy[j][i] = temp
                    elif(j == len(image)-1 and i != len(image[0])-1):
                        temp = self.compute(image, j, i, j, i - 1)  # W
                        temp += self.compute(image, j, i, j-1, i - 1) #NW
                        temp += self.compute(image, j, i, j - 1, i)  # N
                        temp += self.compute(image, j, i, j - 1, i + 1)  # NE
                        temp += self.compute(image, j, i, j, i + 1)  # E
                        temp = temp/5
                        self.energy[j][i] = temp
                    elif(i == len(image[0])-1 and j != len(image)-1):
                        temp = self.compute(image, j, i, j - 1, i - 1)  # NW
                        temp += self.compute(image, j, i, j - 1, i)  # N
                        temp += self.compute(image, j, i, j, i - 1)  # W
                        temp += self.compute(image, j, i, j + 1, i - 1)  # SW
                        temp += self.compute(image, j, i, j + 1, i)  # S
                        temp = temp / 5
                        self.energy[j][i] = temp

                    elif(i == len(image[0])-1 and j == len(image)-1):
                        temp = self.compute(image, j, i, j - 1, i)  # N
                        temp += self.compute(image, j, i, j, i - 1)  # W
                        temp += self.compute(image, j, i, j - 1, i - 1)  # NW
                        temp = temp/3
                        self.energy[j][i] = temp
                    else:
                        temp = self.compute(image, j, i, j - 1, i)  # N
                        temp += self.compute(image, j, i, j - 1, i + 1)  # NE
                        temp += self.compute(image, j, i, j, i + 1)  # E
                        temp += self.compute(image, j, i, j + 1, i + 1)  # SE
                        temp += self.compute(image, j, i, j + 1, i)  # S
                        temp += self.compute(image, j, i, j + 1, i - 1)  # SW
                        temp += self.compute(image, j, i, j, i - 1)  # W
                        temp += self.compute(image, j, i, j - 1, i - 1)  # NW
                        temp = temp/8
                        self.energy[j][i] = temp
        return

    def compute(self, image, j, i, r, c):
        distance = math.sqrt((image[r][c][0] - image[j][i][0])**2 + (image[r][c][1] - image[j][i][1])**2 + (image[r][c][2] - image[j][i][2])**2)
        #print(distance)
        return distance

    # Get the seam, in order from top to bottom, where the top-left corner of the
    # image is denoted (0,0).
    # 
    # Since the y-coordinate (row) is determined by the order, only return the x-coordinate
    # 
    # @return the ordered list of x-coordinates (column number) of each pixel in the seam
    #         as an array

    def findSeam(self, image):
        self.M = self.energy.copy()
        for j in range(len(image) - 2, -1, -1):  # starting at second to last row
            for i in range(len(image[0])):  # starting at column 0
                if (i == 0):
                    temp = min(self.M[j + 1][i], self.M[j + 1][i + 1])
                    self.M[j][i] += temp
                elif (i == len(image[0]) - 1):
                    self.M[j][i] += min(self.M[j + 1][i - 1], self.M[j + 1][i])
                else:
                    self.M[j][i] += min(self.M[j + 1][i - 1], self.M[j + 1][i], self.M[j + 1][i + 1])


    def getSeam(self):
        return self.realSeam(self.thing)

    def realSeam(self, image):
        if (self.weight == 0):
            backtrack = [0 for i in range(len(image))]
            for j in range(len(image)):
                backtrack[j] = 1
            return backtrack

        else:
            backtrack = [0 for i in range(len(image))]
            backtrack[0] = np.argmin(self.M[0])

            i = backtrack[0]
            #print(len(image))
            for j in range(0, len(image)-1):
                if(i == 0):
                    temp = np.argmin(self.M[j+1][i:i+2])
                    backtrack[j+1] = temp + i -1
                    i = temp +i-1
                elif(i == len(image)-1):
                    temp = np.argmin(self.M[j+1][i-1:i+1])
                    backtrack[j + 1] = temp + i - 1
                    i = temp + i - 1
                else:
                    temp = np.argmin(self.M[j+1][i-1:i+2])
                    backtrack[j + 1] = temp + i - 1
                    i = temp + i - 1
            return backtrack
