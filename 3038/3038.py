"""3038"""
def main():
    """3038"""
    a = int(input())
    b = int(input())
    c = int(input())
    if a < b: #ถ้า เอ น้อยกว่าบี
        if a < c: # และถ้า เอ น้อยกว่าซี
            print(a) #print a
        else:
            print(c) #ถ้า เอไม่ได้น้อยกว่า ซี ให้ ปริ้น ซี
    else:
        if b < c: #ถ้า ถ้า บี น้อยกว่า ซี ให้ปริ้น บี
            print(b)
        else:
            print(c) #ถ้า บีไม่ได้น้อยกว่า ซี ให้ ปริ้น ซี
main()
