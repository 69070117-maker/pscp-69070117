"""3008"""
import math
def main():
    """docstring"""
    a = float(input()) #รับค่าเป็นจนเต็ม
    b = float(input()) #รับค่าเป็นจนเต็ม
    c = float(input()) #รับค่าเป็นจนเต็ม
    s = (a + b + c ) / 2 #ตามสูตร
    if a > 0 and b > 0 and c > 0: # if a > 0 and b > 0 and c > 0 the process can goin on
        area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        print(f"{area:.3f}") #output 3f
main()
