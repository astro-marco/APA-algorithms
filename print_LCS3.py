def print_LCS3(b,X,Y,W):
    i = len(X)
    j = len(Y)
    h = len(W)
    invertedLCS3 = [] # list to store characters to print

    # navigating the i x j x h cube (3D matrix)
    while i != 0 and j != 0 and h != 0:
        if b[i][j][h] == 1: # horizontal left
            j -= 1
        elif b[i][j][h] == 2: # horizontal diagonal
            i -= 1
            j -= 1
        elif b[i][j][h] == 3: # horizontal right
            i -= 1
        elif b[i][j][h] == 4: # down-left
            j -= 1
            h -= 1
        elif b[i][j][h] == 5: # down-diagonal
            invertedLCS3.append(X[i-1])
            i -= 1
            j -= 1
            h -= 1
        elif b[i][j][h] == 6: # down-right
            i -= 1
            h -= 1
        elif b[i][j][h] == 7: # vertical down
            h -= 1
		
    # Reverse the list to get the correct order of LCS
    LCS3 = ''.join(reversed(invertedLCS3))
    print(LCS3)