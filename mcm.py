import math

def dictify(name,rows,cols):
	return {
		"name":name,
		"rows":rows,
		"cols":cols
	}

def printTables(m,k):
	print('\nm-Table:')
	print('-\t1\t2\t3\t4')
	for i in range(1,len(m)):
		print(i,end="\t")
		for j in range(1,len(m)):
			print(m[i][j],end='\t')
		print()
	
	print('\nk-Table:')
	print('-\t1\t2\t3\t4')
	for i in range(1,len(k)):
		print(i,end="\t")
		for j in range(1,len(k)):
			print(k[i][j],end='\t')
		print()

def MCM(m,kt,p):
	n=len(p)
	for i in range(1, n):
		m[i][i]=0
	for l in range(2, n):
		for i in range(1, n-l +1):
			j = i + l-1
			m[i][j] = math.inf
			for k in range(i, j):
				newAns = m[i][k] + m[k + 1][j] + p[i-1]*p[k]*p[j]
				if newAns < m[i][j]:
					m[i][j] = newAns
					kt[i][j] = k

def printOptSoln(k,i,j,matrices):
	if i==j:
		print(matrices[i-1]['name'],end='',sep='')
	else:
		print("(",end='')
		printOptSoln(k,i,k[i][j],matrices)
		printOptSoln(k,k[i][j]+1,j,matrices)
		print(')',end='')

if __name__ == '__main__':
	matrices = [
		dictify('A1',5,4),
		dictify('A2',4,6),
		dictify('A3',6,2),
		dictify('A4',2,7),
	]
	# matrices = [
	# 	dictify('A1',7,1),
	# 	dictify('A2',1,5),
	# 	dictify('A3',5,4),
	# 	dictify('A4',4,2),
	# ]
	n = len(matrices)
	valid = True
	for i in range(n-1):
		if(matrices[i]['cols']!=matrices[i+1]['rows']):
			valid=False
			print('The matrix chain cannot be multiplied.')
			break

	if valid:
		m_table=[[0 for i in range(n+1)] for j in range(n+1)]
		k_table=[[0 for i in range(n+1)] for j in range(n+1)]
		
		ds = [] #Dimension sequence
		for i in range(n):
			ds.append(matrices[i]['rows'])
			if i==(n-1):
				ds.append(matrices[i]['cols'])

		MCM(m_table,k_table,ds)
		printTables(m_table,k_table)

		print('\nOptimal Solution: ',end='')
		printOptSoln(k_table,1,n,matrices)
		print('\nThe number of multiplications for optimal solution is',m_table[1][n],end='.')


