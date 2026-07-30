"""3027"""
def main():
    """main"""
    w, h, n = map(int,input().split())
    price =  int(input())
    process = 2*(w + h) #หาความยาวรอบรูปสี่เหลี่ยมผืนผ้าจากสูตร 2 *กว้าง+ยาว
    process_2 = process * n #ความยาว * จำนวนชั้น
    finalprice = process_2 * price #ราคาที่ต้องจ่าย = ความยาวที่ต้องใช้ * ราคาต่อเมตร
    print(process_2)
    print(finalprice)
main()
