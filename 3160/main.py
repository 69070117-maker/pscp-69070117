"""[LEARNING LOGS] หาจำนวนเฉพาะ"""
def main():
    """main"""
    A, B = map(int, input().split())
    prime = 0
    for i in range(A, B + 1):
        if i > 1 :
            for j in range(2,i):
                if  i % j == 0 :
                        prime += 1
                        break
    print(i.slpit())
    print(f"Total primes: {prime}")
main()
