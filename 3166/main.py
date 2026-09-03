"""Pass or Fail """
def main():
    """main"""
    n = int(input())
    scores = []
    all_passed = True

    for _ in range(n):
        score = int(input())
        scores.append(score)
        if score < 50:
            all_passed = False

    average = sum(scores) / n

    print(f"{average:.1f}")

    if all_passed and average >= 60.0:
        print("PASS")
    else:
        print("FAIL")


main()
