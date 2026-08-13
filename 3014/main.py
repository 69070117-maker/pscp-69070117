"""3014"""
def main():
    """main"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    milk = d//a
    if not b or not c:
        total_milk = milk
    else:
        total_milk = milk
        caps = milk
        while caps >= b:
            promo_milk = (caps//b)*c
            left_caps = caps % b
            total_milk += promo_milk
            caps = left_caps + promo_milk
    print(total_milk)
main()