"""3164"""
def main():
    """Main"""
    n = int(input())
    max_nums = []

    for _ in range(n):
        a = int(input())
        b = int(input())
        max_nums.append(max(a, b))

    if n == 1:
        print(max_nums[0])
    else:
        equation = " + ".join(map(str, max_nums))
        total = sum(max_nums)
        print(f"{equation} = {total}")


main()
