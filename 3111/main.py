"""sahakorn"""
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
    ans = round(total, 2
                )
    print(ans)
main()
