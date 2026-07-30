"""2999"""
def main():
    """main"""
    text = str(input())
    row_2 = str('*' + text + '*')
    for _ in range(len(row_2)):
        print('*', end = '')
    print()
    print('*'+(text)+'*')
    for _ in range(len(row_2)):
        print('*', end = '')
main()
