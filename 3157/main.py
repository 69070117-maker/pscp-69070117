"""[LEARNING LOGS] เกมสะสมแต้ม"""
def main():
    """3157"""
    num =int(input())
    sign = " "
    for _ in range(num):
        sign += input() + " "
    if  "+" in sign:
        positive = sign.count("+")
        positive = positive * 10
    else:
        positive = 0
    if "-" in sign:
        negative = sign.count("-")
        negative = negative * -5
    else:
        negative = 0
    answer = positive + negative
    print(answer)
main()
