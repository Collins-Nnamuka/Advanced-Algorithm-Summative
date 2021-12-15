#Import the Heapq function, which is needed to solve the problem
import heapq

edges = [[1, 2, 24], [1, 4, 20], [3, 1, 3], [4, 3, 12]]

#Then initialize a function that will be used to make edges into an adjacency map
def Adj_Matrix(edges):

    #Storing the graph as a list of tuples with all the different edges as keys
    graph = {}
    for i in range(1, len(edges)+1):
        graph[i] = []
    # Looping through the edges array
    for i in edges:
        x, y, z = i[0], i[1], i[2]
        #Then map them against each other because the linked edges are undirected.
        #Then connect the edges with their weight, and they are stored in tuples.
        if x not in graph or y not in graph:
            #Create an if statement to check if x in the graph or y not in the graph.
            #Then store x as key and (y,z) as value, then y as key, and (x,z) as value.

            graph[x] = (y, z)
            graph[y] = (x, z)
        else:
            # Appending to both keys
            graph[x].append((y, z))
            graph[y].append((x, z))

    #returning the adjacency matrix graph
    return graph
    
    
#Create a second function that takes in arguments the number of edges, 
#the array of edges, and the starting point and will be used to return 
#the shortest distance.
def shortestDistance(n,edges,s):

    #Then initialize the heap and add the weight and the starting node
    heap = [(0, s)]

    #Then call the function that makes the graph into an adjacency map
    graph = Adj_Matrix(edges)

    #Then create a dictionary that would help keep track of the shortest distance.
    answer    = {}
    for x in range(1, n + 1):
        answer[x] = float('inf')

    #Then since s is the starting point, initialize s to 0.
    answer[s] = 0

    #Creating a while loop to pop out the first tuple in the heap; 
    #as far as the heap is not empty
    while heap:
        t = heapq.heappop(heap)
        #use the Breadth first search technique to go through the edge.
        for h in graph[t[1]]:
            #Create an if statement where if the weight of connecting edge is greater than the 
            #original weight of the edge plus the current weight.
            #Then add the original weight of the edge and the current 
            #weight and set it to the connecting edge weight.

            if answer[h[0]] > answer[t[1]] + h[1]:
                answer[h[0]] = answer[t[1]] + h[1]
                #Create an if statement to check if the tuple is already in the heap and remove them if found.
                #Then call the heap function to help arrange them accordingly.

                if (h[1], h[0]) in heap:
                    heap.remove((h[1], h[0]))
                    heapq.heapify(heap)
                # pushing the current weight and its edge to the heap
                heapq.heappush(heap, (answer[h[0]], h[0]))

    # initializing out result array to store the shortest reach  
    shortest_distance = []
    
    #Then using the value as the shortest distance, 
    #loop through the dictionary and add the values to the result of the array.
    for i in answer:
        shortest_distance.append(answer[i])
        
    # Then return an array of with the shortest reach of each edge starting from 1
    return shortest_distance[1:]
s = 1

# calling the function and printing the final result output
print ("The shortest distance followed are: ")
print(shortestDistance(len(edges),edges,s))
