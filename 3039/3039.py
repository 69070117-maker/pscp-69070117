"""3039"""
def main():
    """main"""
    N = int(input())
    ans = int(input())
    for _ in range(N-1):
        num = int(input())
        if num < ans:
            ans = num
    print(ans)
main()
