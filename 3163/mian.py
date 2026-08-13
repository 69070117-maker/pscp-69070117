"""3163"""
def main():
    """main"""
    num = int(input())
    goods = []
    sumie = 0
    Even = 0
    odd = 0
    for _ in range(num):
        good = int(input())
        goods.append(good)
        sumie += good
    for i in goods:
        if not i % 2 :
            Even += 1
        else :
            odd += 1
    print(f"SUM {sumie}")
    print(f"EVEN {Even}")
    print(f"ODD {odd}")
main()
