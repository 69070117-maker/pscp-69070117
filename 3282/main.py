"""stats"""
def main():
    """32820"""
    num = int(input())
    total = 0
    minn = num
    maxx = num
    for i in range(num):
        num = int(input())
        total += num
        if num < minn :
            minn = num
        if num > maxx:
            maxx = num
    print(f"MIN: {minn:.3f}")
    print(f"MAX: {maxx:.3f}")
    print(f"AVG: {total:.3f}")
main()
