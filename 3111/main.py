"""sahakorn"""
from decimal import Decimal, ROUND_HALF_UP
def main():
    """3111"""
    member = input()
    nthing = int(input())
    total = 0
    for _ in range(nthing):
        price = float(input())
        total += price
    if member == "Y":
        total = total * 95 / 100
    elif member == "N" and total >= 500:
        total = total * 0.97
    ans = Decimal(str(total)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    print(ans)
main()
