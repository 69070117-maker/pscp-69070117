"""3290"""
def main():
    """3290"""
    k = int(input())
    n = int(input())

    for i in range(0, (n + 1) // 2):
        print(" " * (n // 2 - i), end="")
        for _ in range(1, k + 1):
            print("*", end="")
        print()
    for i in range(1, (n - (n + 1) // 2) + 1):
        print(" " * i, end="")
        for _ in range(1, k + 1):
            print("*", end="")
        print()

main()
