import math

n=4
# dist = [[0,16,11,6],[8,0,13,16],[4,7,0,9],[5,12,2,0]] #0-3-2-1 (23)
# dist = [[0,4,1,3],[4,0,2,1],[1,2,0,5],[3,1,5,0]] #0-2-1-3 (7)
dist = [[0,10,15,20],[5,0,9,10],[6,13,0,12],[8,8,9,0]] #0-1-3-2 (35)
# dist = [[0,10,15,20],[5,0,25,10],[15,30,0,5],[15,10,20,0]] #0-2-3-1 (35)
dp = [[-1 for i in range(4)] for j in range(16)]
visited_all = (1<<n)-1

def tsp(mask,pos):
	if(mask==visited_all):
		return dist[pos][0]
	if(dp[mask][pos] != -1):
		return dp[mask][pos]

	ans = math.inf
	for c in range(0,n):
		if((mask & (1<<c))==0):
			newAns = dist[pos][c]+tsp(mask | (1<<c),c)
			ans = min(ans,newAns)

	dp[mask][pos] = ans
	return ans

t = tsp(1,0)
# print("Path: ",travel)
print("Min: ",t)