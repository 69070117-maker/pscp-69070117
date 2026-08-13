"""BasicATM"""
def main():
    """main"""
    withdraw = int(input())
    thousand = withdraw // 1000
    if 100 < withdraw <= 20000 and  withdraw % 100:
        print("ERROR")
    
main()
