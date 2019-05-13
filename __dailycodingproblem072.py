# -*- coding: utf-8 -*-
"""
New comment for git!!!

Created on Thu Mar 21 13:25:16 2019

@author: Weston

prompt:
In a directed graph, each node is assigned an uppercase letter. We define a path's value as the number of most frequently-occurring letter along that path. 
For example, if a path in the graph goes through "ABACA", the value of the path is 3, since there are 3 occurrences of 'A' on the path.

Given a graph with n nodes and m directed edges, return the largest value path of the graph. 
If the largest value is infinite, then return null.

The graph is represented with a string and an edge list. 
The i-th character represents the uppercase letter of the i-th node. 
Each tuple in the edge list (i, j) means there is a directed edge from the i-th node to the j-th node. 
Self-edges are possible, as well as multi-edges.

For example, the following input graph:

ABACA
[(0, 1),
 (0, 2),
 (2, 3),
 (3, 4)]
Would have maximum value 3 using the path of vertices [0, 2, 3, 4], (A, A, C, A).

The following input graph:

A
[(0, 0)]
Should return null, since we have an infinite loop.

"""
import random
"""
def askerlength():
    maxlengthset = False
    
    while maxlengthset == False:
        try:
            maxlength = int(input("Maximum number of nodes: "))
            if maxlength < 1:
                raise
            maxlengthset = True
        except:
            print("Enter only positive integers")
    
    return maxlength

def askerprobability():
    probabilityset = False
    
    while probabilityset == False:
        try:
            probability = float(input("Probability any given directed edge will form: "))
            
            if probability <= 0 or probability > 1:
                raise
            
            probabilityset = True
        except:
            print("Enter a float between 0 and 1")
    
    return probability
"""
def appender(length,array):
    x = random.randint(0,length)
    y = random.randint(0,length)
    if ((x,y) not in array and (y,x) not in array and (x != y)):
        array.append((x,y))
    
def graphconstructor():
    
    maxlength = random.randint(12,20)
    #probability = float(random.randint(10,300)/1000)
    
    print("Chose maxlength ", maxlength)
    
    #maxlength = askerlength()
    #probability = askerprobability()
    
    length = random.randint(4,maxlength)
    string = str("")
    edge_list = []

    for x in range(length):
        string = string + str(chr(random.randint(65,90)))
    
    while len(edge_list) < 0.3 * length**2:
        appender(length,edge_list)
        
    
    print(length, "nodes, ", len(edge_list), " of ", length**2, " possible directed edges --", round(float(100*len(edge_list)/(length**2)),2), "%\n")
    print(string)
    edge_list.sort()
    print(*edge_list, sep = "\n")
    
    graph = [string,edge_list]
    return graph

graph = graphconstructor()


"""
So I need to create a path... and evaluate the string created by the string index for each starting point...
I know there will be an infinite path if the reverse coordinates are also in the array...
I could start each path... and calculate the value of it
"""
def stringvalue(string):
    array = []
    for x in string:
        if x not in array:
            array.append(x)

    maxvalue = 1
    for x in array:
        count = 0
        for y in string:
            if x == y:
                count += 1
            if count > maxvalue:
                maxvalue = count
    return maxvalue
         
            
class ContinueW(Exception):
    pass


continue_working = ContinueW()

def pathfinder(graph):
    for x in graph[1]:
    
        #if the directed edge has the same values for x and y, break the loop
        if (x[1],x[0]) in graph[1]:
            print("infinite loop detected ", (x[0],x[1]), "and",(x[1],x[0]))
            return None
            break
        
        #print(x[1],x[0])
        #add the current directed edge to the path
  
    for mytuple in graph[1]:
    #create an empty path that starts at each directed edge
        path = []
        path.append(mytuple)
        #check each directed edge that starts with the same value
        #that the terminal directed edge ends with.
        working = True
        
        while working == True:
            terminal = path[(len(path))-1]
            try:
                for y in graph[1]:
                    if (y[0] == terminal[1] and y not in path):
                        path.append(y)
                        raise continue_working
                        
                    elif (y[0] == terminal[1] and y in path):
                        print("infinite loop detected ")
                        path.append(y)
                        working = False
                        return None
                    
                    else:
                        working = False
            except ContinueW:
                continue

        print(path)
    
        pathstring = ""
        for x in range(len(path)-1):
            if x < (len(path)-1):
                xvalue = path[x][0]
                print("print xvalue", xvalue)
                pathstring = pathstring + str(graph[0][xvalue])
            
            else:
                yvalue = path[x][1]
                print("print  yvalue", yvalue)
                pathstring = pathstring + str(graph[0])[yvalue]
        
        print(pathstring)
        print(stringvalue(pathstring))
            

pathfinder(graph)

        

    
    


#for x in edge_list:
    
