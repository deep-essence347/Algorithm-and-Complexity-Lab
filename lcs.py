# up-left = \u2B09
# up = \u2191
# left = \u2190

def LCS(s1,s2):
	dp = [[-1 for i in s2] for j in s1]
	prev = [['-' for i in s2] for j in s1]
	
	for i in range(len(s1)):
		dp[i][0] = 0
	for j in range(len(s2)):
		dp[0][j] = 0
	
	for i in range(1,len(s1)):
		for j in range(1,len(s2)):
			if s1[i]==s2[j]:
				dp[i][j] = dp[i-1][j-1]+1
				prev[i][j] = '\u2B09'
			else:
				if dp[i-1][j] >=dp[i][j-1]:
					dp[i][j]=dp[i-1][j]
					prev[i][j]='\u2191'
				else:
					dp[i][j]=dp[i][j-1]
					prev[i][j]='\u2190'
	
	return dp,prev

def outputLCS(s1,prev,i,j,lcs_string):
	if i==0 or j==0:
		return
	if prev[i][j]=='\u2B09':
		lcs_string.append(s1[i])
		outputLCS(s1,prev,i-1,j-1,lcs_string)
	elif prev[i][j]=='\u2191':
		outputLCS(s1,prev,i-1,j,lcs_string)
	else:
		outputLCS(s1,prev,i,j-1,lcs_string)

def printDP(s1,s2,dp,prev):
	for j in range(len(s2)+1):
		if(j==0):
			print('i\\j',end='\t')
		else:
			print(s2[j-1],end='\t')
	print()

	for i in range(len(s1)):
		print(s1[i],end='\t')
		for j in range(len(s2)):
				print(prev[i][j],dp[i][j],end='\t')
		print()

if __name__ == '__main__':
	string1 = 'president'
	string2 = 'providence'

	string1 = [0]+list(string1)
	string2 = [0]+list(string2)

	dp,prev = LCS(string1,string2)
	printDP(string1,string2,dp,prev)

	lcs_string=[]
	outputLCS(string1,prev,len(string1)-1,len(string2)-1,lcs_string)
	lcs_string.reverse()
	print('LCS String: ',''.join(s for s in lcs_string))

