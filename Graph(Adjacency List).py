class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbour(self, nbrkey, weight=0):
        self.connectedTo[nbrkey] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getAllWeights(self):
        return self.connectedTo.values()

    def getWeight(self, nbrkey):
        return self.connectedTo[nbrkey]

    def __str__(self):
        return str(self.id) + " is Connected to: " + str([x.id for x in self.connectedTo])

class Graph:
    def __init__(self):
        self.verticesDict = {}
        self.numofvertices = 0

    def addVertex(self, key):
        self.numofvertices += 1
        newVertex = Vertex(key)
        self.verticesDict[key] = newVertex
        return newVertex

    def getVertex(self, key):
        if key in self.verticesDict:
            return self.verticesDict[key]
        else:
            return None

    def addEdge(self, fromVertex, toVertex, weight=0):
        if fromVertex not in self.verticesDict:
            self.addVertex(fromVertex)
        if toVertex not in self.verticesDict:
            self.addVertex(toVertex)

        self.verticesDict[fromVertex].addNeighbour(self.verticesDict[toVertex], weight)

    def getVertices(self):
        return self.verticesDict.keys()

    def __iter__(self):
        return iter(self.verticesDict.values())

    def __contain__(self, key):
        return key in self.verticesDict

g = Graph()
for i in range(6):
    print(g.addVertex(i))
print(g.getVertices())

g.addEdge(0,1,10)
print(g.getVertex(0))
g.addEdge(0,5,11)

for vertex in g:
    print(vertex)
    print(vertex.getConnections())
    print('\n')

print(6 in g.verticesDict)
print(g.verticesDict[1])
print(g.verticesDict[0].getAllWeights())
print(g.verticesDict[0].getId)
print(g.verticesDict[0].getWeight(g.verticesDict[5]))