"""BrickBridge"""
def main():
    """main3058"""
    a = int(input())
    b = int(input())
    goal = int(input())
    b = b* 5 #bigbrick5
    goal = abs(goal - b)#ใช้อิฐก้อนใหญ่ใส่absforไม่ให้ค่าติดลบ
    if a >= goal  : #ถ้าใช้อิฐก้อนใหญ๋ไปแล้วยังไม่พอแล้วจำนวนอิฐก้อนเล็กมีเหลือมากกว่าgoal
        print(goal) #แสดงผลgoalจำนวนอิฐที่ต้องการ
    else:
        print("-1")
main()
