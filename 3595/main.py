"""main"""
def main():
    """main"""
    a = float(input())
    b = int(input())
    c = float(input())

    total_rockets = 0
    current_meteors = 1
    current_weight = a

    while current_weight >= c:
        total_rockets += current_meteors
        current_meteors *= b
        current_weight /= b

    print(total_rockets)


main()
