"""all the  same"""
def main():
    """"3066"""
    n_1 = int(input())
    n_2 = int(input())
    n_3 = int(input())
    if 0 <= n_1 <= 1000 and 0 <= n_2 <= 1000 and 0 <= n_3 <= 1000 :
        if n_1 == n_2 and n_2 == n_3 :
            print("all the same")
        elif  n_1 != n_2 and n_2 != n_3 and n_1 != n_3:
            print("all different")
        else:
            print("neither")
main()
