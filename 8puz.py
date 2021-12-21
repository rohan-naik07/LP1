class Node:
    def __init__(self,data,level,fval):
        self.data = data
        self.level = level
        self.fval = fval

    def getChildren(self,goalState):
        goal_data = goalState
        n = len(self.data)
        x,y = self.getSpaceCoordinates()
        dirs = [
            [x,y-1],[x,y+1],[x+1,y],[x-1,y]
        ]
        children=[]
        for dir in dirs:
            data = self.copy(self.data)
            if(dir[0]>=0 and dir[0]<n and dir[1]>=0 and dir[1]<n):
                temp = data[x][y]
                data[x][y] = data[dir[0]][dir[1]]
                data[dir[0]][dir[1]] = temp
                newNode = Node(data,self.level+1,0)
                children.append(newNode)
        return children
    
    def getSpaceCoordinates(self):
        n = len(self.data)
        for i in range(n):
            for j in range(n):
                if(self.data[i][j]=='_'):
                    return i,j
    
    def copy(self,data):
        dup=[]
        n = len(self.data)
        for i in range(n):
            temp = []
            for j in range(n):
                temp.append(self.data[i][j])
            dup.append(temp)
        return dup
    


class EightPuzzle:
    def __init__(self,n):
        self.n = n
        self.startState = []
        self.goalState = []

    def f(self,node):
        return self.h(node) + node.level
    
    def h(self,node):
        result=0
        for i in range(self.n):
            for j in range(self.n):
                if(node.data[i][j]!='_' and node.data[i][j]!=self.goalState[i][j]):
                    result+=1
        return result

    def print_arr(self,data):
        print("\n")
        for i in data:
            for j in i:
                print(j, end = " ")
            print()
    
    def solve(self):
        open=[]
        self.startState = [['1','2','3'],['_','4','6'],['7','5','8']]
        self.goalState = [['1','2','3'],['4','5','6'],['7','8','_']]

        if(self.startState==self.goalState):
            print('Starting and Ending States are same...')
            return
        start = Node(self.startState,0,0)
        open.append(start)
        while True:
            cur = open[0]
            self.print_arr(cur.data)
            if(self.h(cur)==0):
                break

            if(cur.level > 1000):
                print('Unsolvable...\n')
                break

            children = cur.getChildren(self.goalState)
            for child in children:
                child.fval = self.f(child)
                open.append(child)
            del open[0]
            open.sort(key = lambda x : x.fval,reverse=False)

puz = EightPuzzle(3)
puz.solve()


            