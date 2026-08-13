"""2992"""
def main():
    """main"""
    num = input()
    sign = input()
    newnum = int(num[::-1])
    num = int(num)
    ans = num
    if sign == "+" :
        ans = num + newnum
        print(f"{num} + {newnum} = {ans}" )
    elif sign == "-" :
        ans = num  - newnum
        print(f"{num} - {newnum} = {ans}" )
    elif sign == "*" :
        ans = num  * newnum
        print(f"{num} * {newnum} = {ans}" )
    elif sign == "/" :
        ans = num  / newnum
        print(f"{num} / {newnum} = {ans}" )
main()
