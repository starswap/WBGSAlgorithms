<h1>Day 9</h1>
<h2>Dijkstra's Shortest Path Algorithm</h2>

Good morning everyone. Today and tomorrow on WBGS Algorithms we are looking again at networks. We will be investigating Dijkstra's Algorithm today, and the A* Search Algorithm (an extension of it) tomorrow. Both of these algorithms are required at A Level, so let's get a head start, as always through the Implementation first approach.

Before we go any further I would like to recommend the source of today's content - https://www.youtube.com/watch?v=GazC3A4OQTE. This Computerphile video explains the Dijkstra Algorithm extremely well and concisely, so check it out if you don't understand by the end.

The two algorithms both see usage in satellite navigation technology, Internet routing and many other places as their function is to search for the shortest path from one point to another on a network (as determined by the weights). The versatility of networks to represent things and the desire to always find the most efficient way of doing things make these algorithms useful.

If you haven't yet read <a href="https://github.com/starswap/WBGSAlgorithms/blob/master/Algorithms/Day%206%20Prim's%20Algorithm/problemFormulation.md">last week's post</a> on Prim's Algorithm, I recommend that you check out the terminology and implementation sections to get up to speed on networks.


<h3>Algorithm</h3>

Today's Algorithm was discovered in 1959 by Edsger W. Dijkstra.

The main idea behind Dijkstra's Algorithm is to search all of the paths through a network, but prioritising the shortest ones. This means that once we reach the end and have found the shortest path, we haven't wasted time going off in the wrong direction.

It does this by comparing the total weights of the routes taken up to this point, and always extending from the point that has been reached the most cheaply.

In order to achieve this, we have a queue-like data structure, which is ordered by total weight of journey. The items inside this data structure are the vertices. As with Prim's algorithm, use an object-oriented approach, where each vertex is represented by an object that has a connections property. This is a list of lists, whereby each internal list contains the element that we are connecting to and the weight of the connection. This will be created at the beginning of the program and will not be changed throughout as this is just the representation of the network. An obvious consequence of such a representation is that we do not have any edge elements.

Specially for Dijkstra, the Vertex class will also need to be equipped with properties totalWeight (the total weight required to get to it) and pathVia (the last vertex in the chain used to get to this point - this is key in Dijkstra as we don't have to update the whole path to Z, for example, if we find a quicker way to get to B - this will be inherited as at every stage we use the shortest possible path). Here is a Python example of the representation

It will also be useful to be able to translate from letters to Vertices and vice versa.

```Python
class Vertex():
def __init__(self,pathVia,totalWeight,connections,letter):
        self.connections = connections
        self.pathVia = pathVia
        self.totalWeight = totalWeight
	self.letter = letter

#Create Vertices
firstOne = Vertex('',-1,[],'A') #We initialise the vertices with no connections, no path and a totalPath weight of -1, which will allow us to distinguish vertices which don't yet have a weight from vertices which do.
secondOne = Vertex('',-1,[],'B')
#Build our (very small) network.
firstOne.connections.append([secondOne,4.5])
secondOne.connections.append([firstOne,4.5])
```

At the beginning of the algorithm, we have a start and an end vertex. In the Computerphile video above these are labelled S and E but they could be any vertex.

We can put the start vertex at the top of the queue because it has distance 0 from the start - this is the only known distance at this point. We don't give it a pathVia as it is the start.

We can now start the algorithm.

```
At each step until we process the end node, we process one node at the top of the queue per iteration.
	We loop through all of the edges that connect from this node that we are processing to other nodes, adding their weight to the weight required to travel to the node that we are at (node.totalWeight). 
		If the this weight is lower than the previous totalWeight for the node we are connecting to,
			We have found a new shorter path to that node. We update this node with the new total weight and the Vertex from which this path came - this is the node we are currently processing
			We also need to move this node to the right place in the queue, which will probably simply be done by looping over the queue from the top to the bottom, then inserting the node at the right place.
		Otherwise:
			We don't need to do anything because we haven't found a new shortest path.
	Now we remove this node from the queue and put it on the "done" pile.

At the end of the algorithm, we use the pathVia properties to trace back our shortest path so that it can be output. We go from the end vertex back one step at a time until we reach start (we can tell this as start has no pathVia itself, and we create a string of points which is then output.)

```

Here is some pseudocode to make the algorithm clearer:

```
FUNCTION insert(array,item,index):
	RETURN ARRAY_CONCAT(array[0:index-1],[item],array[index+1:LENGTH(array)-1])#Using inclusive ranging as always. 
ENDFUNCTION

FUNCTION dijkstra(queue,startIndex,endIndex,alphabet):
	endNodeProcessed = FALSE
	endItem= queue[endIndex]
	queue[startIndex].totalWeight = 0
	insert(queue,queue[startIndex],0)
	ARRAY_DELETE(queue,startIndex+1) #The old element was shifted by 1 place by the insertion so delete at one space later.
	processed = []
	WHILE (endNodeProcessed == FALSE):
		thisItem = queue[0]
		ARRAY_APPEND(processed,queue[0])
		ARRAY_DELETE(queue,0)
		IF (thisItem.letter == endItem.letter):
			endNodeProcessed = TRUE #We will end after this iteration of the algorithm.
		ENDIF
		FOR i <- 0 TO LENGTH(queue[0].connections)-1:
			IF (thisItem.connections[i][0].totalWeight > thisItem.totalWeight + thisItem.connections[i][1]):
				thisItem.connections[i][0].totalWeight <- thisItem.totalWeight + thisItem.connections[i][1]
				thisItem.connections[i][0].pathVia <- thisItem
				#Before we can insert the changed value into the queue in the right place we need to know where it was in the queue.
				FOR k <- 0 TO LENGTH(queue) - 1:
					IF (queue[k] == thisItem.connections[i][0]):
						BREAK
					ENDIF
				ENDFOR #k now stores the index of the item that needs to be moved and reinserted
				FOR j <- 0 TO LENGTH(queue) - 1: #Now we need to insert the changed value into the queue in the right place so it stays ordered
					IF (queue[j].totalWeight > thisItem.connections[i][0] OR queue[j].totalWeight == -1) #We treat -1 as bigger than all values that we have set.
						insert(queue,queue[k],j) #The changed value will go before the value that it is less than so that is right.
						ARRAY_DELETE(queue,k+1) #Now we have two of the same element in the list so get rid of the old one
						BREAK #We don't need to keep looking as we have found where to insert it and we have done the insertion
					ENDIF
				ENDFOR
			ENDIF
		ENDFOR
	ENDWHILE
	
	pathBuilding <- ""
	currentOne <- processed[LENGTH(processed)-1] #We start at the last value in the processed list
	WHILE (currentOne.letter != ''): #And work backwards
		STRCAT(pathBuilding,currentOne.letter)
		currentOne = currentOne.pathVia
	ENDWHILE
	RETURN pathBuilding
ENDFUNCTION


#First we need to make a network:
OUTPUT("How many vertices are there in the network?")
vertices <- STR_TO_INT(USERINPUT)
queue = []
alphabet = ['A','B','C','D',.....] #If you want to be compatible with more than 26 nodes you can just add more labels at the end of this list with as many characters as you want.

FOR i <- 1 TO vertices: #Inclusive
	ARRAY_APPEND(queue,Vertex('',-1,[],alphabet[i-1]))

FOR i <- 0 TO LENGTH(vertices)-1:
	FOR j <- 0 TO LENGTH(vertices)-1:
		OUTPUT("Enter the weight of the edge connecting " + alphabet[i] + " to " + alphabet[j] + " or N for 'this vertex is not present':")
		result <- USERINPUT
		IF (result != 'N'):
			ARRAY_APPEND(queue[i].connections,[queue[j],STR_TO_INT(result)])
		ENDIF
	ENDFOR
ENDFOR
startIndex <- 2
endIndex <- 4 #Or whatever you like
OUTPUT(dijkstra(queue,startIndex,endIndex,alphabet))

```
<h3>Problems with Dijkstra</h3>
Before ending today's post, I'd like to mention the two problems that Dr Mike Pound informs us of in the Computerphile videos on A* and Dijkstra to explain two problems with Dijkstra's Algorithm. These are both related to the fact that Dijkstra's algorithm uses only the weights on the graph. It has no perception of whether it is physically going in the right direction towards the end goal. This means that although it will always find the shortest path, in two particular situations, it can be quite inefficient.
<ol>
<li>If we have a single very expensive edge that takes us to our goal, compared to lots and lots of edges with tiny weights that go in the wrong direction, Dijkstra's Algorithm will always follow the shorter edges until eventually this path becomes more expensive than the direct route.</li>
<li>If we have a very dense graph with lots of identical edges, Dijkstra's Algorithm will end up exhaustively searching all of the possible routes through the graph, because it won't have any way to distinguish them. We need to build something in that will distinguish otherwise identical routes that will allow it to finish more quickly as it will be certain it has found the right answer.</li>
</ol>
We will solve these issues tomorrow with the A* Algorithm.

<h3>Task</h3>
Implement Dijkstra's algorithm as described above. You will need it for tomorrow when we extend it to make A* Search.
<h3>Tests</h3>
You could use the network depicted in the Computerphile video above to test your Dijkstra's algorithm, or try with this network which I reproduced from the AMSP's worksheet on Prim's Algorithm last week:

<img src="images/AMSP.png" />

<h3>Extensions</h3>
<ul>
<li>Get prepared for tomorrow's A* Search problem by watching this sequel to the above video https://www.youtube.com/watch?v=ySN5Wnu88nE</li>
<li>Build a small version of a satnav in your browser or in another programming environment. Google offers some APIs which you could use to make your graphs with and to generate the weights. (also MapQuest + Leaflet) Then you simply need to run the algorithm on this produced network, and work out how to draw the result.</li>
<li>Use some kind of network drawing library to draw the network out and then highlight the shortest path that you have produced</li>
<li>Again you might like to use file reading to build your network. I recommend creating a standard format for your network files such as:</li>
</ul>
```
7
AB 4
EF 8.3
BC 2.1
CE 3.5
```

<h3>Hints</h3>
If you are using an LLL , try the Linked List data structure 
