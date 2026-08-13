"""3010"""
def main():
    """Quadrant"""
    X = int(input())
    Y = int(input())
    if not X  and not Y  :
        print('O')
    elif not X  :
        print("Y")
    elif not Y :
        print("X")
    elif X > 0 and Y >0 :
        print("Q1")
    elif X > 0 > Y :
        print("Q4")
    elif X < 0 and Y < 0:
        print ("Q3")
    elif X < 0 < Y :
        print("Q2")
main()
