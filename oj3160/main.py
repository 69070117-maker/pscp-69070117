"""3160"""
def main():
    """main"""
    start_num, end_num = map(int, input().split())
    prime_list = []
    prime_count = 0

    for num in range(start_num, end_num + 1):
        if num <= 1:
            continue
        for i in range(2, num):
            if not num % i :
                break
        else:
            prime_list.append(num)
            prime_count += 1

    if prime_list:
        print(*prime_list)
    print(f"Total primes: {prime_count}")

main()
