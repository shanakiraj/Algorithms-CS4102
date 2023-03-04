# CS4102 Spring 2022 - Unit A Programming 
#################################
# Collaboration Policy: You are encouraged to collaborate with up to 3 other
# students, but all work submitted must be your own independently written
# solution. List the computing ids of all of your collaborators in the
# comments at the top of each submitted file. Do not share written notes,
# documents (including Google docs, Overleaf docs, discussion notes, PDFs), or
# code. Do not seek published or online solutions, including pseudocode, for
# this assignment. If you use any published or online resources (which may not
# include solutions) when completing this assignment, be sure to cite them. Do
# not submit a solution that you are unable to explain orally to a member of
# the course staff. Any solutions that share similar text/code will be
# considered in breach of this policy. Please refer to the syllabus for a
# complete description of the collaboration policy.
#################################
# Your Computing ID:
# Collaborators: 
# Sources: Introduction to Algorithms, Cormen
#################################
import cmath
import math

class ClosestPair:
    def __init__(self):
        return

    # This is the method that should set off the computation
    # of closest pair.  It takes as input a list containing lines of input
    # as strings.  You should parse that input and then call a
    # subroutine that you write to compute the closest pair distances
    # and return those values from this method
    #
    # @return the distances between the closest pair and second closest pair
    # with closest at position 0 and second at position 1 
    def compute(self, file_data):
        global smallest
        pointsx = sorted(file_data, key=lambda x: float(x.split(" ")[0]))  # splits x and y coordinates and sorts the x's
        return self.Recurse(pointsx), self.SecondSmallest(pointsx)

    def Recurse(self, x):
        runway = []
        global smallest
        # base case
        if len(x) <= 3:
            return self.findDistance(x)
        # divide
        mid = len(x) // 2
        lefthalf = x[:mid]
        righthalf = x[mid:]

        # recursive call
        DistLeft = self.Recurse(lefthalf)
        DistRight = self.Recurse(righthalf)

        if(DistLeft < DistRight):
            smallest =  DistLeft
        else:
            smallest = DistRight

        midpoint = float(x[mid].split(" ")[0])

        #runway
        for i in range(len(x)):
            dist = abs(float(x[i].split(" ")[0]) - midpoint)
            if smallest > dist:
                runway.append(x[i])

        runway = sorted(runway, key=lambda x: float(x.split(" ")[1]))

        for i in range(len(runway)):
            for j in range(i + 1, (len(runway))):
                dist = self.distance(runway[i], runway[j])
                if smallest > dist:
                    smallest = dist
        return smallest

    def SecondSmallest(self, x):
        global smallest
        # base case
        if len(x) <= 3:
            return self.findDistance2(x)
        # divide
        mid = len(x) // 2
        lefthalf = x[:len(x) // 2]
        righthalf = x[len(x) // 2:]

        # recursive call
        DistLeft = self.SecondSmallest(lefthalf)
        DistRight = self.SecondSmallest(righthalf)

        smallest2 = min(DistLeft, DistRight)
        if(DistLeft < DistRight):
            smallest2 = DistLeft
        else:
            smallest2 = DistRight

        runway = []
        midpoint = float(x[mid].split(" ")[0])

        # runway
        for i in range(len(x)):
            # dist = self.distance(x[i], x[mid])
            dist = abs(float(x[i].split(" ")[0]) - midpoint)
            if smallest2 > dist:
                runway.append(x[i])

        runway = sorted(runway, key=lambda x: float(x.split(" ")[1]))

        for i in range(len(runway)):
            for j in range(i + 1, (len(runway))):
                dist = self.distance(runway[i], runway[j])
                if smallest2 > dist and dist != smallest:
                    smallest2 = dist
        return smallest2

    def distance(self, p1, p2):
        x1 = float(p1.split(" ")[0])
        x2 = float(p2.split(" ")[0])
        y1 = float(p1.split(" ")[1])
        y2 = float(p2.split(" ")[1])
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def findDistance(self, file_data):
        closest = float("inf")
        for i in range(len(file_data)):
            for j in range(i + 1, len(file_data)):
                dist = self.distance(file_data[i], file_data[j])
                if closest > dist:
                    closest = dist
        return closest

    def findDistance2(self, file_data):
        global smallest
        closest = float("inf")
        for i in range(len(file_data)):
            for j in range(i + 1, len(file_data)):
                dist = self.distance(file_data[i], file_data[j])
                if closest > dist and smallest != dist:
                    closest = dist
        return closest


