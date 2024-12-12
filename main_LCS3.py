from LCS3 import LCS3_b, get_b
from print_LCS3 import print_LCS3

def main():
    X = "cammello"
    Y = "casa"
    W = "padella"
    
    LCS3_b(X, Y, W)
    b = get_b()
    print("Length of LCS is", LCS3_b(X,Y,W))
    print("One of the LCSs is")
    print_LCS3(b,X,Y,W)

main() # per poter eseguire il file