

def DLS(src,dest,graph,maxdepth,path):
    path.append(src)
    if src == dest: 
        return True
    if maxdepth <= 0: 
        return False
    for i in graph[src]:
        if(DLS(i,dest,graph,maxdepth-1,path)):
            return True
        path.pop()
    return False

def IDDFS(src,dest,graph,maxdepth,path):
    for i in range(maxdepth):
        if (DLS(src,dest,graph,i,path)):
            print(path)
            return True
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

res=IDDFS('1','6',graph,4,path)
if res:
    print(path)
else:
    print('No path is available in the given limit')



