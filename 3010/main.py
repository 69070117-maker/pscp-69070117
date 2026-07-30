"""3010"""
def main():
    """Quadrant"""
    X = int(input())
    Y = int(input())
    if X == 0 and Y == 0 :
        print('O')
    elif X == 0 :
        print("Y")
    elif Y == 0 :
        print("X")
    elif X > 0 and Y >0 :
        print("Q1")
    elif X > 0 and Y < 0:
        print("Q4")
    elif X < 0 and Y < 0:
        print ("Q3")
    elif X < 0 and Y > 0:
        print("Q2")
main()  
