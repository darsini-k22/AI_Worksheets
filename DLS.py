#depth limited dfs search

def DLS(src,dest,graph,limit,path,level):
    #if the node is not found in path including it in the path
    path.append(src)
    #if depth reaches the limit we stop and returning the path
    if src==dest:
        return path
    if limit==level:
        return False
    for adj in graph[src]:
        if DLS(adj,dest,graph,limit,path,level+1):
            return path
        path.pop()
    return False

graph={
    '1':['2','3'],
    '2':['4','3','1'],
    '3':['4','5'],
    '4':['5'],
    '5':['6'],
    '6':[] 
}
path=[]
res=DLS('1','3',graph,2,path,1)
if res:
    print(path)
else:
    print('Path not found in the given limit')
        

    
    
    
    

