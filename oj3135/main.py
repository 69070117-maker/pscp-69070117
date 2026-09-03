"""3135"""
def main():
    """main"""
    n, k, t = map(int, input().split())

    if t == 1:
        print(1)
        return

    person = 1
    total = 1

    while True:
        person = (person - 1 + k) % n + 1
        total += 1

        if person in (t, 1):    
            if person == 1:
                total -= 1
            break

    print(total)

main()
