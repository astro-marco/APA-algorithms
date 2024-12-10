# type: ignore
def main():
	X = "trattore"
	Y = "rilevatore"
	W = "cavolfiore"

	print("Length of LCS is ", LCS3_b(X, Y, W))

def LCS3_b(X,Y,W):
	m = len(X)
	n = len(Y)
	l = len(W)
	
	c = [[[0 for h in range(l+1)]for j in range(n+1)]for i in range(m+1)]
	b = [[[0 for h in range(l+1)]for j in range(n+1)]for i in range(m+1)]
	
	# Fill the base cases
	for i in range(0,m+1):
		for h in range(0,l+1):
			c[i][0][h] = 0
			
	for j in range(1,n):
		for h in range(0,l+1):
			c[0][j][h] = 0

	for i in range(1,m+1):
		for j in range(1,n+1):
			c[i][j][0] = 0

	for i in range(1,m+1):
		for j in range(1,n+1):
			for h in range(1,l+1):
				# The 7 directions that 'regress' towards position b[0][0][0].
				# Total number of directions would be 26, pretending to stand
				# in the central position of a 3x3x3 cube.
				if X[i] == Y[j] and Y[j] == W[h]:
					c[i][j][h] = 1 + c[i-1][j-1][h-1]
					b[i][j][h] = 5 # down-diagonal (ideally towards [0,0,0])
				
				elif X[i] == Y[j]:
					c[i][j][h] = 1 + c[i-1][j-1][h]
					b[i][j][h] = 2 # horizontal diagonal (verso [0,0,h])
				
				elif Y[j] == W[h]:
					c[i][j][h] = 1 + c[i-1][j][h-1]
					b[i][j][h] = 6 # down-right
				
				elif X[i] == W[h]:
					c[i][j][h] = 1 + c[i][j-1][h-1]
					b[i][j][h] = 4 # down-left

				else:
					c[i][j][h] = max(c[i-1][j][h], c[i][j-1][h], c[i][j][h-1])
					if c[i][j][h] == c[i-1][j][h]:
						b[i][j][h] = 3 # horizontal right
					elif c[i][j][h] == c[i][j-1][h]:
						b[i][j][h] = 1 # horizontal left
					elif c[i][j][h] == c[i][j][h-1]:
						b[i][j][h] = 7 # vertical down
	return c[m][n][l]

main() # per poter eseguire il file