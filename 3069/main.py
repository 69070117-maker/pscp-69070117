"""ราศี"""
def main():
    """main3069"""
    day = int(input())
    month = int(input())
    rasee = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_day = day + sum(rasee[:month])
    if  1 <= total_day <= 19 or 356 <= total_day <= 365:
        print("capricorn")
    elif  20 <= total_day <= 49:
        print("aquarius")
    elif  50 <= total_day <= 79:
        print("pisces")
    elif  80 <= total_day <= 109:
        print("aries")
    elif  110 <= total_day <= 140:
        print("taurus")
    elif  141 <= total_day <= 172:
        print("gemini")
    elif 173 <= total_day <= 203:
        print("cancer")
    elif 204 <= total_day <= 234:
        print("leo")
    elif 235 <= total_day <= 265:
        print("virgo")
    elif 266 <= total_day <= 296:
        print("libra")
    elif 297 <= total_day <= 325:
        print("scorpio")
    elif 326 <= total_day <= 355:
        print("sagittarius")
main()
