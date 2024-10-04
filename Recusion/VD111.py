def TinhTong(n): #S(n) = 1 + 2 + 3 + ... + n
    if n == 1:
        return n
    else:
        return n + TinhTong(n - 1)
if __name__ == "__main__":
    n = int(input("Input n = "))
    print(TinhTong(n))