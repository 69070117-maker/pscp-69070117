"""3161"""
def main():
    """พิมพ์สัญลักษณ์"""
    number = int(input())
    answer = ""
    for i in range(number):
        if  not (i + 1) % 5  :
            answer += "X"
        else:
            answer += "*"
    print(answer)
main()
