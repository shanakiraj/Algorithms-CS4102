# CS4102 Spring 2022 - Unit B Programming
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
# Your Computing ID: sra9qsw
# Collaborators:
# Sources: Introduction to Algorithms, Cormen
#################################


class Supply:
    def __init__(self):

        self.adjacencylist = []
        self.numVertices = 0
        self.disjointsets = []
        self.names = []

        return

    # This is the method that should set off the computation
    # of the supply chain problem.  It takes as input a list containing lines of input
    # as strings.  You should parse that input and then call a
    # subroutine that you write to compute the total edge-weight sum
    # and return that value from this method
    #
    # @return the total edge-weight sum of a tree that connects nodes as described
    # in the problem statement

    def union(self, v1, v2):
        self.disjointsets[v1] = v2

    def find(self, i):
        if self.disjointsets[i] == i:
            return i
        else:
            return self.find(self.disjointsets[i])


    def compute(self, file_data):

        edgeWeightSum = 0
        #grabs the number of vertices from first line in test case
        self.numVertices = int(file_data[0].split()[0])

        #print(self.numVertices)

        #creates the adjacency list with 3 values, first two are the names of vertices
        #and the third is the weight
        for i in range(1, int(file_data[0].split()[1])+1):
            self.adjacencylist.append([(file_data[self.numVertices+i].split()[0]), (file_data[self.numVertices + i].split()[1]), int(file_data[self.numVertices + i].split()[2])])
        self.adjacencylist = sorted(self.adjacencylist, key = lambda index: index[2])
        print(self.adjacencylist)


        #create a hashtable for the vertex id's
        dictionary1 = {}

        #creates a hashtable for the names and type of center
        dictionary2 = {}


        #this will record the type as the key and name as value
        dictionary3 = {}

        dictionary4 = {}




        #creates the disjoint set list
        self.disjointsets = []

        #adds the names of the vertices in the dictionary as the key and the disjoint set index as the value
        for i in range(self.numVertices):
            dictionary1[file_data[i+1].split()[0]] = i
            #sets up the disjoint set
            self.disjointsets.append(i)
            dictionary2[file_data[i+1].split()[0]] = file_data[i+1].split()[1]
            dictionary3[file_data[i+1].split()[1]] = file_data[i+1].split()[0]
            dictionary4[file_data[i+1].split()[0]] = 0 #copy of dictionary2


        print(dictionary2)
        print(dictionary4)
        # print(self.disjointsets)

        for item in self.adjacencylist:
            v1 = self.find(dictionary1[item[0]])
            #print(dictionary1[item[0]])
            v2 = self.find(dictionary1[item[1]])

            # if (dictionary2[item[0]])
            # if (dictionary2[item[0]])
            # if (dictionary2[item[0]])

            if v1 != v2:
                n1 = dictionary2[item[0]] #turns the name into the type of center
                n2 = dictionary2[item[1]]
                #print(item[1])

                if(n1 == 'port'):
                    if(n2 != 'store' and n2 != 'port'):
                        self.union(v1,v2)
                        edgeWeightSum += item[2]
                if(n1 == 'rail-hub'):
                    if(n2 != 'store'):
                        self.union(v1,v2)
                        edgeWeightSum += item[2]

                if(n1== 'dist-center'):
                    if(n2 == 'store'):
                        if(dictionary4[item[1]] == 0):
                            dictionary4[item[1]] = item[0]
                            self.union(v1, v2)
                            edgeWeightSum += item[2]

                    elif(n2 != 'dist-center'):
                        self.union(v1, v2)
                        edgeWeightSum += item[2]

                if(n1 == 'store'):
                    if (n2 == 'store'):
                            self.union(v1, v2)
                            edgeWeightSum += item[2]
                    if(n2 == 'dist-center'):
                        if (dictionary4[item[0]] == 0):
                            dictionary4[item[0]] = item[1]
                            self.union(v1, v2)
                            edgeWeightSum += item[2]

        return edgeWeightSum
