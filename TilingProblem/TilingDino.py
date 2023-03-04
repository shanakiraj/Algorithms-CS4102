
# CS4102 Spring 2022 -- Unit D Programming
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
# Sources: Introduction to Algorithms, Cormen
#################################
import networkx as nx
from networkx.algorithms import bipartite

class TilingDino:
    def __init__(self):
        return

    # This is the method that should set off the computation
    # of tiling dino.  It takes as input a list lines of input
    # as strings.  You should parse that input, find a tiling,
    # and return a list of strings representing the tiling
    #
    # @return the list of strings representing the tiling

    def compute(self, lines):
        graph = nx.Graph()
        set1 = []
        set2 = []
        adj = []
        source = "source"
        sink = "sink"

        #splits the pixels into 2 alternating sets based on every other pixel
        for r in range(len(lines)):
            for c in range(len(lines[r])):
                if(lines[r][c] == "#"):
                    if((r+c) % 2 == 0):
                        #graph.add_node(str(r) + " " + str(c), bipartite=1)
                        set1.append(str(c) + " " + str(r))

                    else:
                        #graph.add_node(str(r) + " " + str(c), bipartite=0)
                        set2.append(str(c) + " " + str(r))

        total = len(set1) + len(set2)


            #adds all the possible edges into the graph
        for r in set1:
            for c in set2:
                x1 = r.split()[0]
                x2 = c.split()[0]
                y1 = r.split()[1]
                y2 = c.split()[1]

                if (int(x1) == int(x2) and int(y1) == int(y2) - 1):
                    graph.add_edge(r,c, capacity = 1.0)
                if (int(x1) == int(x2) and int(y1) == int(y2) + 1):
                    graph.add_edge(r,c, capacity = 1.0)
                if (int(x1) == int(x2) - 1 and int(y1) == int(y2)):
                    graph.add_edge(r,c, capacity = 1.0)
                if (int(x1) == int(x2) + 1 and int(y1) == int(y2)):
                    graph.add_edge(r,c, capacity = 1.0)

        # flow_value, flow_dict = nx.maximum_flow(graph, source, sink)
        final = []
        covered = []
        try:
            dict = nx.bipartite.maximum_matching(graph, set1)
        except:
            return ["impossible"]

        if(len(dict) != total):
            return ["impossible"]
        else:
            for a in dict:
                if a not in covered:
                    covered.append(a)
                    covered.append(dict[a])
                    final.append(dict[a] + " " + a)

        return final
