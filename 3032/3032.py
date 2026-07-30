"""3032"""
def main():
    """main"""
    N = int(input())
    data_list = []
    for _ in range(N):
        data_list.append(int(input()))
    mmax_val = max(data_list)
    renny = data_list.count(mmax_val)
    print(mmax_val)
    print(renny)
main()
