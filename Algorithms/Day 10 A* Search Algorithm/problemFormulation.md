TL;DR - The A* Search Algorithm is an improvement on Dijkstra's shortest path algorithm for finding the shortest (lowest weight) path across a network. The only change is the addition of what we call a "heuristic" which represents the real physical distance from a given node to the destination point. We can't use the weights as the path length using these is what we are finding out. It needs to be something that can be precomputed for the relationship between every node and the destination, which is why we usually use simple (Euclidean) distance, although other heuristics are available. Most SAT-NAV systems have this kind of distance data so it isn't too challenging to build in A* functionality for them. Instead of the totalWeight property (the total weight of all of the sections of the shortest path to a given node) being used to sort  
<h1>Day 10</h1>
<h2>A* Search Algorithm</h2>
Good Morning all. Today we will be investigating the A* Search Algorithm, which turns out to be extremely close to Dijkstra's Algorithm - a very simple adjustment provides a significant efficiency improvement. This means that if you did Dijkstra yesterday you shouldn't have too many changes to make today, but equally I imagine it was challenging to finish Dijkstra, so I leave time today for the completion of both of those, as well as plenty of extensions.

As with yesterday I would like to mention my gratitude for the computerphile video on A* Search with Dr Mike Pound, which can be found <a href="https://www.youtube.com/watch?v=ySN5Wnu88nE">here</a>, and which is very informative.

I also point out that both today's and yesterday's algorithms are featured in the A Level Computing Syllabus. After today and Quick Sort on Saturday, we will have investigated all of the standard algorithms in the <a href="https://www.ocr.org.uk/Images/170844-specification-accredited-a-level-gce-computer-science-h446.pdf">OCR Computer Science A Level Specification</a> 

<h3>Problem to Solve & Solution</h3>
Dijkstra's Algorithm is a very effective algorithm for a challenging task. However, it has a problem of efficiency. This is because it has no knowledge of whether it is going in the right direction towards the end goal or not.

This means that it will follow cheap paths away from the goal if these are shorter than an expensive path to the goal. It will eventually realise where it needs to go, but this will slow the algorithm down.

In addition, it has no way to priviledge one route over another if they have the same cost. This means that it will try both, which is again very inefficient.

How might we do this?

Well, to solve this problem, we need to give the new algorithm a way of knowing whether it is going towards or away from the goal. We call the number which will do this a heuristic.

There are many possible heuristics, but the most common one is simple (Euclidean) distance from the point currently being expanded to the end, measured with a ruler. In SAT-NAV devices this information is present either precomputed or to be computed.

You may think that this is a bit of a cheat method, since we are telling it which paths are shortest. However, we are not actually looking for the "shortest" path - we are really looking for the lowest weight path (for example the one that will take the least time to travel on in a car). As such we aren't helping the algorithm too much.

Equally, if this data is not available, all of the distances can be set to zero or an equivalent number so that they are all the same, and A* becomes equivalent to the simple Dijkstra Algorithm.

Because we are using this data to "inform" the algorithm of the expected cost (because going in the wrong direction gives a larger final cost, but Dijkstra's Algorithm doesn't know that yet), it is known as an informed search algorithm.

While Dijkstra's algorithm works only on what it has seen so far to determine the shortest path, A* Search has an insight (essentially an expected cost of a given path) through the heuristic into which method of reaching the goal is likely to be the best This means it doesn't waste time on routes which would eventually have been rejected by Dijkstra.

<h3>Algorithm</h3>
Only a very limited update is required to the Dijkstra code to make this work, although we need to work out how we will get the user to input the distances. It makes sense not to waste time measuring the distance between every point because this is n! measurements which would get boring. 

As such, you will likely want to work out your end point in advance, then make measurements to the end point from every other vertex on the graph. These can be input into the program (probably through a file to save time).

Then, you can choose whichever start point you like, runnning the program multiple times to check that it works effectively.

In A* Search, every time that we were using the totalWeight property of the Vertices for Dijkstra, we will now use totalWeight + distanceToEnd. This means that we order the vertices based on a combined function f(n) = g(n) + h(n), where g(n) is the length of the path to the vertex n, and h(n) is the heuristic for the vertex n, that is to say the distance from n to the end, or the expected cost of the route n->end. These are all the same.

That is the only modification that we need to make - the queue structure and the process is all exactly the same.

Here is some pseudocode:
```
CLASS Vertex():
	PROCEDURE onInitialisaton(THIS,pathVia,totalWeight,connections,letter,distanceToEnd):
		THIS.pathVia = pathVia
		THIS.totalWeight = totalWeight
		THIS.connections = connections
		THIS.letter = letter
		THIS.distanceToEnd = distanceToEnd
	ENDPROCEDURE
ENDCLASS

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
			IF ( (thisItem.connections[i][0].totalWeight + thisItem.connections[i][0].distanceToEnd) > (thisItem.totalWeight + thisItem.connections[i][1] + thisItem.connections[i][0].distanceToEnd)):
				thisItem.connections[i][0].totalWeight <- thisItem.totalWeight + thisItem.connections[i][1]
				thisItem.connections[i][0].pathVia <- thisItem
				#Before we can insert the changed value into the queue in the right place we need to know where it was in the queue.
				FOR k <- 0 TO LENGTH(queue) - 1:
					IF (queue[k] == thisItem.connections[i][0]):
						BREAK
					ENDIF
				ENDFOR #k now stores the index of the item that needs to be moved and reinserted
				FOR j <- 0 TO LENGTH(queue) - 1: #Now we need to insert the changed value into the queue in the right place so it stays ordered
					IF (queue[j].totalWeight + queue[j].distanceToEnd > thisItem.connections[i][0].totalWeight + thisItem.connections[i][0].distanceToEnd): # Make sure that we are using the distanceToEnd value to order the items in the queue.
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
alphabet = ['A','B','C','D',.....'Z'] #If you want to be compatible with more than 26 nodes you can just add more labels at the end of this list with as many characters as you want.

FOR i <- 1 TO vertices: #Inclusive
	OUTPUT("What is the distance (heuristic value) from vertex " + alphabet[i] + " to the goal vertex?")
	a <- USERINPUT
	ARRAY_APPEND(queue,Vertex('',100000000000000000000000000000,[],alphabet[i-1],a))
ENDFOR
FOR i <- 0 TO LENGTH(vertices)-1:
	FOR j <- 0 TO LENGTH(vertices)-1:
		OUTPUT("Enter the weight of the edge connecting " + alphabet[i] + " to " + alphabet[j] + " or N (case sensitive) for 'this vertex is not present':")
		result <- USERINPUT
		IF (result != 'N'):
			ARRAY_APPEND(queue[i].connections,[queue[j],STR_TO_INT(result)])
		ENDIF
	ENDFOR
ENDFOR
startIndex <- 2
endIndex <- 4 #Or whatever you like. This is the index in the queue variable, although actually that is just the same as the letter converted to a number so A=0, B=1,C=2...
OUTPUT(dijkstra(queue,startIndex,endIndex,alphabet))

```


<h3>Advantages and Disadvantages</h3>
<table>
<tr><th>+s</th><th>-s</th></tr>
<tr><td>Like Dijkstra's Algorithm, A* Search always returns the optimal result if initialised with accurate data.</td><td>The A* Search Algorithm uses more memory/has a higher space complexity than Dijkstra because it has to read the distances as well as the costs into memory. To obtain a good time efficiency and a good memory efficiency, we would usually resort to algorithms that have precomputed routes across the network - these allow us to use Dijkstra even though it is slow, as we do that before the algorithm runs, when time is not critical.</td></tr>
<tr><td>The algorithm still functions as Dijkstra's Algorithm with no heuristic data, which means it is backwards compatible to systems without this data.</td><td>If a reasonable heuristic is not chosen, A* Search will not work effectively, producing a sub-optimal path.</td></tr>
<tr><td>Gives a reasonable performance benefit considering it isn't much harder to program than Dijkstra.</td><td>Lots more data and precomputation of heuristics is required to make this algorithm work, which could be expensive and slow.</td></tr>
<tr><td>Will always return a path if one exists (known as complete). It will not simply stop and say "no path found" as long as the heuristic is well chosen.</td><td></td></tr>
<tr><td>A* Search will be more efficient than Dijkstra's Algorithm if we have what is known as an "admissible" heuristic function. This means that it never overestimates the cost to the goal - the actual cost from point X to point E is more than the or equal to the measured distance.</td><td>With an effective heuristic, we often find that simply using that instead of the combined cost produces a result more quickly. That being said, we wouldn't be taking into accoun the weights, which represent traffic on the roads for example or accidents.</td></tr>
</table>
Source: https://stackoverflow.com/questions/13031462/difference-and-advantages-between-dijkstra-a-star#13033503
\t https://en.wikipedia.org/wiki/Admissible_heuristic

<h3>Task</h3>
Make a copy of your Dijkstra's Shortest Path algorithm function and adapt it to make A* Search.

You will need to adjust your network input code to permit a distance to end to be inputted for each of the vertices on the network.

<h3>Tests</h3>
As shown in the Computerphile video, I would recommend simply drawing out your own network with lots of paths and weights, and then physically measuring the centimetre distance 

It will be exceedingly difficult to compare Dijkstra and A* Search on the same dataset and expect to see a different result in terms of time taken, simply because computers are so fast. However, what you can do is run both algorithms against the graph you just made, one with uniform weights and one with a long path of low weights but a highly weighted path to the goal. 

Compare the costs of the final paths generated (these should be the same as long as the measurement heuristic is accurately calculated), and the number of <strong>iterations</strong> required to achieve this, because it should be possible to see a difference here.

For which type of graph does it make most sense to use A* over Dijkstra? Think about the cost required to calculate all of these values, but don't underestimate the value of pre-computation - if these values allow a sat-nav to produce the best route based on current conditions in a much quicker time, the users' experience will be improved. Sat-navs need low latency because they need to be able to react and redirect drivers before they miss a turning, for example. Finally, one mustn't forget that the Sat-Nav could now run on a lower-spec device and still be fast if it is using a more efficient algorithm. Hence, more profit can be made from these types of devices.

<h3>Extensions</h3>
<ul>
<li>Investigate the A* with Epsilon bounding Algorithm which is generally considered to produce faster results than basic A*. What are its advantages and disadvantages?</li>
<li>Having done some research and read the information in the solutions and hints section, produce your own version of A* which uses an epsilon value. Assess the paths that it comes up with and the number of iterations required (and hence the associated time efficiency), for various epsilon values.</li>
<li>Consider what different types of heuristics you could use instead of the simple physical distance to see if you can improve the algorithm for certain scenarios. Research different types of distances such as the Manhattan Distance, the Hamming Distance. Try taking a look at this <a href="https://medium.com/@kunal_gohrani/different-types-of-distance-metrics-used-in-machine-learning-e9928c5e26c7">this article</a></li>
<li>Produce an A* Search that can input and output pre-computed routes between points on a network, building on these to find a longer route.</li>
<li>Now try to produce some rudimentary AI which allows the algorithm to work out which routes are worth precomputing and which are not, so that you don't have to tell it which routes to calculate for every given network</li>
</ul>


<h3>Solutions & Hints</h3>
A* with Epsilon is faster than the A* algorithm but it produces a sub-optimal path. However, because you know how sub-optimal the path is, you are able to judge the result produced and decide whether or not this algorithm is suitable for your purpose.
<a href="https://en.wikipedia.org/wiki/A*_search_algorithm#Bounded_relaxation"Wikipedia</a> explains this, but here is a basic summary:
To make A* run faster we have it pick only one of the most likely candidates that are all quite close in final cost. This means it finishes quicker but doesn't necessarily choose the best one. There are many ways to do this, but they all involve a small value epsilon which is used in the computation of an adjusted heuristic. We guarantee that the resulting path is no more than (1+epsilon) times worse than the original path. It is usefult to be able to have this level of control over the optimality of the paths. The simplest way to do this is to multiply the heuristic value by epsilon, which must be greater than one, before using it to calculate the combined cost. 



