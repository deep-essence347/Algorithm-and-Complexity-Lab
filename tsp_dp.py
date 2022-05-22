import math

#? Number of Nodes
n=4 

#? Distance matrix that defines the graph
# dist = [[0,16,11,6],[8,0,13,16],[4,7,0,9],[5,12,2,0]] #0-3-2-1 (23)
# dist = [[0,4,1,3],[4,0,2,1],[1,2,0,5],[3,1,5,0]] #0-2-1-3 (7)
dist = [[0,10,15,20],[5,0,9,10],[6,13,0,12],[8,0,9,0]] #0-1-3-2 (35)
# dist = [[0,10,15,20],[5,0,25,10],[15,30,0,5],[15,10,20,0]] #0-2-3-1 (35)

#? Memoization Matrix
#? 16*4 because (2^N)*N
#? Initially all values are -1
dp = [[-1 for i in range(4)] for j in range(16)] #* [[-1,-1,-1,-1],(14)*[-1,-1,-1,-1],[-1,-1,-1,-1]] -> length - 16 of 4 each

#? If all cities have been visited.
#? (1<<n) is the integer with last n bit as 1.
visited_all = (1<<n)-1 #*Value: 16-1 = 15

#? Travelling Salesman Function
#? visitedCities: set of cities (visited/unvisited) in the current path.
#? currentCity: position of the current city
def travellingSalesman(visitedCities,currentCity):
	#? If all the cities have been visited, returns the distance of going back to origin(0) from the `currentCity`
	if(visitedCities==visited_all):
		return dist[currentCity][0]

	#? If there is an unvisited node, tries to visit the unvisited node.

	#? Lookup for memoized value
	#? `!= -1` means the value has already been computed, hence returns the computed value rather than recomputing it.
	if(dp[visitedCities][currentCity] != -1):
		return dp[visitedCities][currentCity]

	#? Initially the distance is `infinity`
	ans = math.inf
	#? Try to goto unvisited city
	for city in range(0,n):
		#? If city is not visited
		if((visitedCities & (1<<city))==0):
			#? Adds the distance from `currentCity` to visiting `city` with the remaining distance.
			#? Remaining distance is the recursive call to the `travellingSalesman()` function.
			#? `visitedCities | (1<<city)` updates `city` as visited during the recursive call and `currentcity` updates to `city`.
			newAns = dist[currentCity][city]+travellingSalesman(visitedCities | (1<<city),city)

			#? Updates the distance to minimum value.
			ans = min(ans,newAns)

	#? Assigning the distance of dp value(uncomputed) to ans.
	dp[visitedCities][currentCity] = ans

	#? returns the minimum distance.
	return ans

#? Initially `visitedCities = 1` and `currentCity = 0`
#? It means, starting from the 0th city and initially the 0th city has been visited.
tsp = travellingSalesman(1,0)
print("Min: ",tsp)