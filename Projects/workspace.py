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

def list_to_dict(input_list) :
    '''
    Input:  list of 0 or more pairs [(a_1,b_1),...,(a_n,b_n)]; each a_i, b_i can be an integer or a string
    Output: dict with keys a_1,a_2,...,a_n.
            The value associated with key a_i is the set {b_k such that a_k=a_i}
    '''
    return_dict = {}
    
    for pair in input_list:
        if return_dict.get(pair[0]) == None:
            return_dict[pair[0]]=pair[1]
        else:
            return_dict[pair[0]].add(pair[1])

    return return_dict

expectEqual(list_to_dict([]),{})
expectEqual(list_to_dict([(1,2),(3,4)]),{1:{2},3:{4}})
expectEqual(list_to_dict([(1,2),(1,3)]),{1: {2, 3}})
expectEqual(list_to_dict([('a',7),(10,'b'),('strings can be keys too','they sure can')]),{'a': {7}, 10: {'b'}, 'strings can be keys too': {'they sure can'}})