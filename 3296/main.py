"""3296"""
def main():
    """main"""
    first_c = list(map(int, input().split()))
    second_c = list(map(int, input().split()))
    result = (first_c[0] + second_c[0]) // 2
    result2 = (first_c[1] + second_c[1]) // 2
    result3 = (first_c[2] + second_c[2]) // 2

    print(result, result2, result3)
main()
