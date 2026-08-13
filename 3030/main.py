"""saiama67"""
import math
def main():
    """"main"""
    quest_1 = int(input()) #วิดพื้น
    quest_2 = int(input()) #ซิทอัพ
    quest_3 = int(input()) #ลุกนั่ง
    quest_4 = int(input()) #วิ่ง
    quest_1_1 = int(input())#วิด
    quest_2_1 = int(input())#ซ
    quest_4_1 = int(input())#วิ่ง
    quest_3_1= int(input())#ลุก
    q1 = math.ceil(quest_1 / quest_1_1)
    q2 = math.ceil(quest_2 / quest_2_1)
    q3 = math.ceil(quest_4 / quest_4_1)
    q4 = math.ceil(quest_3 / quest_3_1)
    ans = max(q1,q2,q3,q4)
    print(ans)
main()
