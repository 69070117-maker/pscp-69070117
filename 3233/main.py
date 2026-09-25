"""[LEARNING LOGS] สลากกินแบ่ง"""
def main():
    """main"""
    A_1,B_1 = input().split()
    A_2,B_2 = input().split()
    gift = 0
    if A_1 == A_2 and B_1 == B_2 :
        gift = 1000000
    elif A_1 != A_2 and  B_1 == B_2:
        gift = 100000
    elif A_1 == A_2 and  B_1[2:5] == B_2[2:5] :
        gift = 2000
    elif A_1 == A_2 and  B_1[3:5] == B_2[3:5] :
        gift = 1000
    elif A_1 != A_2 and  B_1[2:5] == B_2[2:5] :
        gift = 200
    elif A_1 != A_2 and  B_1[3:5] == B_2[3:5] :
        gift = 100
    elif A_1 == A_2 and B_1 != B_2:
        gift = 20
    else:
        gift = 0
    print(gift)
main()
