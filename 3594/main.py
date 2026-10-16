"""3594"""
import sys
def main():
    """main"""
    input_str = sys.stdin.read().strip()
    if not input_str:
        return
    numbers = [float(x) for x in input_str.split(", ")]                                      
    numbers.sort()

    n = len(numbers)

    # 2. หาค่ามัธยฐาน
    if n % 2 == 1:
        # กรณีจำนวนข้อมูลเป็นเลขคี่
        median = numbers[n // 2]
    else:
        # กรณีจำนวนข้อมูลเป็นเลขคู่ (ใช้วิธีหาตำแหน่งกลางตามตัวอย่าง)
        mid1 = numbers[(n // 2) - 1]
        mid2 = numbers[n // 2]
        median = (mid1 + mid2) / 2.0

    # แสดงผลเป็นทศนิยม 2 ตำแหน่ง
    print(f"{median:.2f}")