# -*- coding: utf-8 -*-
"""
@author: Yashasvi
"""

 
from collections import defaultdict 

class Course:
    def __init__(self, name, title, prof, credit, crsid):
        self.name = name
        self.title = title
        self.prof = prof
        self.credit = credit
        self.crsid = crsid
  

class Graph(object): 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list) #dictionary containing adjacency List 
        self.idmap = {}
        
    def mapit(self, name, title,prof,credit,crsid):
        node = Course(name,title,prof,credit,crsid)
        self.idmap[crsid] = node
  
    # function to add an edge to graph 
    def addEdge(self,u,v):
        self.graph[u].append(v)
        print(self.graph)
        
    def addcourse(self,newcrs):
        length = len(newcrs)-5
        name = newcrs[0]
        title = newcrs[1]
        prof = newcrs[2]
        credit = int(newcrs[3])
        crsid = int(newcrs[4])
        
        self.V += 1
        
        self.mapit(name, title, prof, credit, crsid)
        for j in range(length):
            self.addEdge(crsid, int(newcrs[j+5]))
            
            
    def semester_plan(self, stack):
        curr_credits = 0
        sem_split_index = [] 
        for i in range(len(stack)):
            curr_credits += self.idmap[stack[i]].credit
            if(curr_credits > 15):
                curr_credits = 0
                sem_split_index.append(i)
                
            sems = [stack[i : j] for i, j in zip([0] + 
          sem_split_index, sem_split_index + [None])] 
        print(sems)
        return sems 
        
      
    def topologicalSortUtil(self,v,visited,stack): 
  
        # Mark the current node as visited. 
        visited[v] = True
  
        # Recur for all the vertices adjacent to this vertex 
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.topologicalSortUtil(i,visited,stack)
  
        # Push current vertex to stack which stores result 
        stack.insert(0,v) 
  
    # The function to do Topological Sort. It uses recursive  
    # topologicalSortUtil() 
    def topologicalSort(self): 
        # Mark all the vertices as not visited 
        visited = [False]*self.V 
        stack = [] 
  
        # Call the recursive helper function to store Topological 
        # Sort starting from all vertices one by one 
        for i in range(self.V): 
            if visited[i] == False: 
                self.topologicalSortUtil(i,visited,stack) 
  
        print(stack)
            
        plan = self.semester_plan(stack)
        return plan
        
        
    def acyclic(self):
        visited = [0 for _ in range(self.V)]
        rec_stack = [0 for _ in range(self.V)]
       
        for i in range(self.V):
            if not visited[i]:
                if self.dfs( i, visited, rec_stack):
                    return 1
        return 0

    def dfs(self, x, visited, rec_stack):
        visited[x] = 1
        rec_stack[x] = 1
        for i in range(len(self.graph[x])):
            if not visited[self.graph[x][i]] and self.dfs(self.graph[x][i], visited, rec_stack):
                print("cycle detected", self.graph[x][i])
                return 1
            elif rec_stack[self.graph[x][i]]:
                print("cycle detected", self.graph[x][i])
                return 1
        rec_stack[x] = 0 
        return 0
  

import csv 
# opening the file using "with" to ensure automatic closing
def readcsv(input_filename):
    templist = input_filename.split("/")
    file = templist[len(templist)-1] 
    with open(file,'r') as data:
       vertices = len(list(csv.reader(data)))
       g = Graph(vertices)
      
    with open(file,'r') as data:
       for row in csv.reader(data):
                length = len(row)-5
                name = row[0]
                title = row[1]
                prof = row[2]
                credit = int(row[3])
                crsid = int(row[4])
                
                #mapping course object to its id
                g.mapit(name, title, prof, credit, crsid)
                
                
                for j in range(length):
                    g.addEdge(crsid, int(row[j+5]))            
       return g
                
       
