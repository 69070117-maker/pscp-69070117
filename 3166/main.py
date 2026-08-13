"""pass or fail"""
def main():
    """3166"""
    num = int(input())
    score = []
    sumscore = 0
    average = 0
    for _ in range(num):
        score_input = int(input())
        score.append(score_input)
    for i  in score:
        sumscore += i
    average = sumscore / num
    print(average)
    if average >= 50 :
        print("PASS")
    else:
        print("FAIL")
main()
