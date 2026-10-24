"""Module for checking prime numbers."""
def main():
    """Check if the input number is a prime number."""
    n = int(input().strip())

    if n <= 1:
        print("NO")
        return

    if n == 2:
        print("YES")
        return

    if not n % 2:
        print("NO")
        return

    limit = int(n**0.5)
    for i in range(3, limit + 1, 2):
        if not n % i:
            print("NO")
            return

    print("YES")


if __name__ == "__main__":
    main()
