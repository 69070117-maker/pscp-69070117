"""กระต่ายน้อยกินราเมน"""
def main():
    """main"""
    Size, type = map(str, input().split())
    pics = input().split()
    topping = pics[0]
    price = 0
    P = 15
    E = 10
    if Size == "S" :
        if type == "R" :
            price = 60
        elif type == "T" :
            price = 80
    elif Size == "M" :
        if type == "R" :
            price = 80
        elif type == "T" :
            price = 100
    elif Size == "L" :
        if type == "R" :
            price = 100
        elif type == "T" :
            price = 120
    if topping == "N" :
        price += 0
    elif topping == "P" :
        if len(pics) == 2 :
            price += P * int(pics[1])
        else:
            price += 15
    elif topping == "E" :
        if len(pics) == 2:
            price += E * int(pics[1])
        else:
            price += 10
    print(price)
main()
