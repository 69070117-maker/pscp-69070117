"""3017"""
def main():
    """main"""
    total_novat = int(input())
    service = total_novat * 10 / 100
    if service  < 50 :
        service = 50
    elif service > 1000:
        service = 1000
    total_novat2 = total_novat + service
    vat = total_novat2 * 7 / 100
    finaltotal = total_novat2  + vat
    print (f"{finaltotal:.2f}")
main()
