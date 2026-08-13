"""จำนวนสระ"""
def main():
    """3013"""
    num = int(input())
    count = 0
    for _ in range(num):
        char = input()
        if char in "aeiouAEIOU":
            count += 1
    print(count)
main()
