"""คำนวณมูลค่าสินค้าตามอัตราเงินเฟ้อ"""


def calculate_inflation(price, years):
    """คำนวณราคาสินค้าทบต้นตามอัตราเงินเฟ้อ 3.81%"""
    # แปลงราคาสินค้าให้อยู่ในหน่วย "สตางค์" (จำนวนเต็ม)
    stang = int(round(price * 100))

    # หาก k มีจำนวนไม่มาก ให้คำนวณแบบตัดเศษทีละปี
    if years <= 100000:
        for _ in range(years):
            # มูลค่าที่เพิ่มขึ้น = (ราคาเดิม * 381) // 10000 (ตัดเศษหลักที่ 3 ทิ้งอัตโนมัติ)
            stang += (stang * 381) // 10000
        return stang / 100

    # หาก k มีขนาดใหญ่มาก ใช้สูตรยกกำลังตรงๆ
    final_price = price * (1.0381 ** years)
    return final_price


def main():
    """main"""
    price = float(input())
    years = int(input())

    final_price = calculate_inflation(price, years)
    print(f"{final_price:.2f}")


main()