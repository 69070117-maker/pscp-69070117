"""pig"""
def main():
    """pig weight max sum calculation"""
    n = int(input())

    weights = []
    while len(weights) < n * 2:
        weights.extend(map(int, input().split()))

    max_weights = []
    for i in range(n):
        w1 = weights[2 * i]
        w2 = weights[2 * i + 1]
        max_weights.append(max(w1, w2))

    total_sum = sum(max_weights)

    if n == 1:
        print(total_sum)
    else:
        equation_str = " + ".join(map(str, max_weights))
        print(f"{equation_str} = {total_sum}")

main()
