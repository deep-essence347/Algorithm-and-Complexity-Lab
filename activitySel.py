def takeInput(): #unused here...
	activities=[[],[],[]]
	n = int(input('Enter the number of activities: '))
	print('Enter Start Time(ST) and Finish Time(FT) for each activity:')
	for i in range(n):
		print('Activity', i+1,': ')
		st = int(input('ST: '))
		ft = int(input('FT: '))
		activities[0].append(i+1)
		activities[1].append(st)
		activities[2].append(ft)

	return activities

def sortByFT(activities):
	activities = list(zip(*activities))
	activities = sorted(activities,key=lambda a:a[2])
	activities = list(zip(*activities))
	return activities

def printactivities(activities):
	titles = ['activities','start time','finish time']
	for i in range(3):
		print(titles[i],end='\t|\t')
		for j in range(len(activities[0])):
			print(activities[i][j], end='\t')
		print()

def activity_selector(s,f,k,n,selected):
	m=k+1
	while m<=n and s[m]<f[k]:
		m=m+1
	if m<=n:
		selected.append((m+1,s[m],f[m]))
		activity_selector(s,f,m,n,selected)
	else:
		selected.extend([])

if __name__ =='__main__':
	activities = [
		[1,2,3,4,5,6,7,8,9,10,11],
		[1,6,3,5,3,0,12,5,8,8,2],
		[4,10,5,7,9,6,16,9,11,12,14]
	]

	activities = sortByFT(activities)
	printactivities(activities)

	selectedActivities = [(activities[0][0],activities[1][0],activities[2][0])]
	activity_selector(activities[1],activities[2],0,len(activities[0])-1,selectedActivities)
	
	print('\nSelected Activities are:')
	for activity in selectedActivities:
		print('Activity: ',activity[0],', ST: ',activity[1],', FT: ',activity[2], sep='')

