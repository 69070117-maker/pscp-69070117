"""3031"""
import math
def main():
    """main"""
    S, N = map(int, input().split()) #map=กำหนดฟังก์ชันให้กลุ่มข้อมูล split=ex['10', '5']
    PI = 3.1416 #โจทย์กำหนดค่าพาย

    for _ in range(N) :
        x, y = map(int, input().split()) #รับค่าxy(พิกัด)
        r_squared = (x ** 2) +(y ** 2) # สูตรrกำลังสองเพราะหมึกขายเป็นวงกลม
        area = PI * r_squared #ขนาดพื้นที่ของวงกลมน้ำหมึก
        time_needed = area / S #ความเร็ว = ระยะทาง/เวลา > เวลา = ระยะทาง / ความเร็ว
        ans = math.ceil(time_needed) #math.ceil=ปัดเศษขึ้น
        print(ans)
main()
