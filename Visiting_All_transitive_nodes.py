from collections import defaultdict

#This class represents a directed graph

class adjacencyList:

    def __init__(self,vertices): 
        #No. of vertices 
        self.V= vertices  

        # default linked lists to store graph 
        self.adjacencyList = defaultdict(list) 

    # function to add an edge to graph 
    def ConnectNodes(self,u,v): 
        self.adjacencyList[u].append(v) 

    def iteratorPaths(self,s, t):
        countPaths = [0]*(self.V)
        #count1 = 0
        #s = s -1
        for i in range(self.V):
            print ("Following are all different paths from %d to %d :" %(s, t)) 
            self.arrayGenerator(s,t)
            countPaths[i] = count
            s += 1
        print(countPaths)
           # print(self.adjacencyList)
    def arrayGenerator(self,s, t): 

            # Mark all the vertices as not visited 
            path = [] 
            checkRecord =[False]*(self.V) 
            # Create an array to store paths 
            global count
            count = 0
            # Call the recursive helper function to print all paths 
            self.pathFinder(s, t,path, checkRecord)
            #print(count)

    def pathFinder(self, s, t, path, checkRecord): 
        global count
        # Mark the current node as visited and store in path 
        checkRecord[s]= True
        path.append(s)
        # If current vertex is same as destination, then print 
        # current path[] 
        if s == t: 
            print(path)
            count += 1
        else: 
            # If current vertex is not destination 
            #Recur for all the vertices adjacent to this vertex 
            for i in self.adjacencyList[s]: 
                if checkRecord[i]==False: 
                    self.pathFinder(i, t, path, checkRecord) 

        # Remove current vertex from path[] and mark it as unvisited 
        path.pop() 
        checkRecord[s]= False


        # Prints all paths from 's' to 'd' 
    
g = adjacencyList(6) 
g.ConnectNodes(0, 2) 
g.ConnectNodes(1, 0) 
g.ConnectNodes(1, 3) 
g.ConnectNodes(3, 2) 
g.ConnectNodes(2, 4) 
g.ConnectNodes(2, 5) 


s = 0 ; t = 3

g.iteratorPaths(s, t)
