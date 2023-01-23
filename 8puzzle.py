import collections as col
class Node:
    def __init__(self,data,g,fval):
        self.data=data
        self.g=g
        self.fval=fval
    
    #generating the children by moving the hole up, down, left, right
    def generate_children(self):
        x,y=self.find(self.data,'_')

        moves=[[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
        children=[]
        for i in moves:
            child=self.move(self.data,x,y,i[0],i[1])
            if child is not None:
                child_node=Node(child,self.g+1,0)
                children.append(child_node)
        return children
    
    #function to find the hole
    def find(self,data,target):
        for i in range(len(data)):
            for j in range(len(data[0])):
                if data[i][j]==target:
                    return [i,j]
    
    #function to move the hole up, down, left, right
    def move(self,data,x1,y1,x2,y2):
        #checking the bound of the new position of the hole, if not return null
        if x2>=0 and x2<len(self.data) and y2>=0 and y2<len(self.data):
            temp_puz=self.copy(data)
            temp=temp_puz[x1][y1]
            temp_puz[x1][y1]=temp_puz[x2][y2]
            temp_puz[x2][y2]=temp
            return temp_puz
        else:
            return None
    
    #creating a copy of the data 
    def copy(self,data):
        temp=[]
        for i in range(len(data)):
            t=[]
            for j in range(len(data[0])):
                t.append(data[i][j])
            temp.append(t)
        return temp
        
class Puzzle:
    def __init__(self,size):
        self.n=size
        self.open=[] #for all the children generated
        self.close=[] #for all the children visited
    
    def f(self,init,goal):
        #goal and start are the objects of the class node
        return self.h(init.data,goal)+init.g
    
    #calculating the heuristic value i.e. num of misplaced tiles
    def h(self,init,goal):
        misplaced=0
        for i in range(self.n):
            for j in range(self.n):
                if init[i][j]!=goal[i][j] and init[i][j]!='_':
                    misplaced+=1
        return misplaced
    
    def solve(self,init,goal):
        init=Node(init,0,0)
        init.fval=self.f(init,goal)
        self.open.append(init)
        stateNotFound=True
        while True:
            cur=self.open[0]
            #printing possible moves
            print('  ||')
            print(' \||/ ')
            print('  \/ ')
            for i in cur.data:
                for j in i:
                    print(j,end=" ")
                print("")

            #bfs
            if (self.h(cur.data,goal)==0):
                print('\n')
                print("=====================")
                print('Goal state is found!!')
                print("=====================")
                break
            else:
                for child in cur.generate_children():
                    child.fval=self.f(child,goal)
                    self.open.append(child)
                self.close.append(cur)
                del self.open[0]
                #sort the values based on the f value in open list
                self.open.sort(key=lambda x:x.fval,reverse=False)
            


initstate=[['1','2','3'],['4','5','_'],['6','7','8']]
goalstate=[['1','2','3'],['4','5','_'],['7','8','6']]

p=Puzzle(3)
p.solve(initstate,goalstate)


