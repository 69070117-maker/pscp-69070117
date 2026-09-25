"""JUMPREALFROG"""
def main():
    """main"""
    X,Y = map(int, input().split())
    d = 0
    count = 0
    while X > 0:
        d += X
        count += 1
        X -= 2
        if d>= Y:
            break
    if d < Y :
        print(-1)
        return
    print(count)
main()
