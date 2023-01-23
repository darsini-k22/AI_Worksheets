import collections as col
def DFS(src,dest,graph,visited):
    if src not in visited:
        visited.append(src)
    if src==dest:
        print(visited)
    else:
        for adj in graph[src]:
            if adj not in visited:
                DFS(adj,dest,graph,visited)

def BFS(src,dest,graph,visited):
    q=col.deque()
    q.append(src)
    visited.append(src)
    while q:
        x=q.popleft()
        if x==dest:
            print(visited)
        else:
            for adj in graph[x]:
                if adj not in visited:
                    visited.append(adj)
                    q.append(adj)
    
graph={
    '1':['2','3'],
    '2':['4','3','1'],
    '3':['4','5'],
    '4':['5'],
    '5':['6'],
    '6':[] 
}
visited=[]
visited_bfs=[]
DFS('1','5',graph,visited)
BFS('1','5',graph,visited_bfs)


    