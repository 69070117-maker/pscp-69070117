"""3005"""
def main():
    """main"""
    carrot, cabbage, tomato= map(int, input().split())#รับ3ค่าใบรรทัดเดียวโดยใช้ช่องว่างเป้นตัวคั่น
    summie = (carrot * 10) + (cabbage * 25) + (tomato * 3)
    print(summie)
main()
