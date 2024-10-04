def ThapHaNoi(n, A, B, C):
    if (n == 1):
        print("Di chuyen dia tren cung tu", A, "den", C)
    else:
        ThapHaNoi(n - 1, A, C, B)
        print("Di chuyen dia tren cung tu", A, "den", C)
        ThapHaNoi(n - 1, B, A, C)
