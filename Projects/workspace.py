def expectEqual(a, b):
    if a != b :
        print('FAIL expected:', b, ' got:', a)
        
def checkUndirected(adjList) :
    for node in adjList :
        for neighbor in adjList[node] :
            try :
                if not node in adjList[neighbor] :
                    print('FAIL: graph is not undirected: '+str(adjList))
                    return
            except KeyError :
                print('FAIL: missing node in adjacency list for graph '+str(adjList))
                return

def checkSelfLoops(adjList) :
    for node in adjList :
        if node in adjList[node] :
            print('FAIL: graph has a self-loop: '+str(adjList))
            return 

def edgeList_to_adjList(edgeList) :
    adjList = {}
    
    for edge in edgeList:
      
      #goal, assign each edge a node to mark it's adjaceny to that node
      key = edge[0]
      value = edge[1]
      if (adjList.get(key) != None):
        adjList[key].add(value)
      else:
        adjList[key]={value}

      #invert key and value to represent edge correctly
      key = edge[1]
      value = edge[0]
      if (adjList.get(key) != None):
        adjList[key].add(value)
      else:
        adjList[key]={value}

    return adjList


expectEqual(edgeList_to_adjList([]),{})
expectEqual(edgeList_to_adjList([('A','B')]),{'A': {'B'}, 'B': {'A'}})
expectEqual(edgeList_to_adjList([('A','B'),('C','D')]),{'A': {'B'}, 'B': {'A'}, 'C': {'D'}, 'D': {'C'}})
expectEqual(edgeList_to_adjList([('A','B'),('C','D'),('B','D')]),{'A': {'B'}, 'B': {'D', 'A'}, 'C': {'D'}, 'D': {'C', 'B'}})
expectEqual(edgeList_to_adjList([('A','B'),('A','C'),('A','D'),('C','D'),('B','C'),('B','D')]),{'A': {'D', 'C', 'B'}, 'B': {'D', 'A', 'C'}, 'C': {'D', 'A', 'B'}, 'D': {'A', 'C', 'B'}})