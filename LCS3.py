# type: ignore
from tkinter.tix import MAX

def main():
	X = "casella"
	Y = "rilevatore"
	W = "cavolfiore"

def LCS3_b(X,Y,W):
	m = len(X)
	n = len(Y)
	l = len(W)
	
    c = [[[0 for h in range(l+1)]for j in range(n+1)]for i in range(m+1)]
    b = [[[0 for h in range(l+1)]for j in range(n+1)]for i in range(m+1)]
	
	for i in range(0,m):
		for h in range(0,l):
			c[i][0][h] = 0
			
	for j in range(1,n):
		for h in range(0,l):
				c[0][j][h] = 0

	for i in range(1,m):
		for j in range(1,n):
			c[i][j][0] = 0

	for i in range(1,m):
		for j in range(1,n):
			for h in range(1,l):
				# le 7 direzioni che "regrediscono" verso b[0][0][0]
				# quelle possibili sarebbero 26 immaginando un cubo 3x3x3
				if X[i] == Y[j] and Y[j] == W[h]:
					c[i][j][h] = 1 + c[i-1][j-1][h-1]
					b[i][j][h] = 2 # giù in diagonale (verso lo spigolo [0,0,0])
				
				elif X[i] == Y[j]:
					c[i][j][h] = 1 + c[i-1][j-1][h]
					b[i][j][h] = 5 # in diagonale orizzontale (verso [0,0,h])
				
				elif Y[j] == W[h]:
					c[i][j][h] = 1 + c[i][j-1][h-1]
					b[i][j][h] = 3 # giù a destra
				
				elif X[i] == W[h]:
					c[i][j][h] = 1 + c[i-1][j][h-1]
					b[i][j][h] = 1 # giù a sinistra

				else:
					c[i][j][h] = max(c[i-1][j][h], c[i][j-1][h], c[i][j][h-1])
					if c[i][j][h] == c[i-1][j][h]:
						b[i][j][h] = 4
					elif c[i][j][h] == c[i][j-1][h]:
						b[i][j][h] = 6
					elif c[i][j][h] == c[i][j][h-1]:
						b[i][j][h] = 7 # 
return c[m][n][l]