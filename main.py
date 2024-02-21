"""
Kalkulators ar 4 darbībām
"""

def saskaitisana(a, b):
    return a + b + 2

def atnemsana(a, b):
    return a - b

def reizinasana(a, b):
    return a * b

def dalisana(a, b):
    try:
        return round(a / b, 1)
    except ZeroDivisionError:
        return "Dalīt ar nulli nedrīkst!"
    
def kapinasana(a, b):
    return a ** b

def main():
    skaitlis1 = float(input("Skaitlis: "))
    skaitlis2 = float(input("Skaitlis: "))
    print("""
        1 - Saskaitīšana
        2 - Atņemšana
        3 - Reizināšana
        4 - Dalīšana
        """)
    darbiba = int(input("Darbība: "))
    if darbiba == 1:
        print(saskaitisana(skaitlis1, skaitlis2))
    elif darbiba == 2:
        print(atnemsana(skaitlis1, skaitlis2))
    elif darbiba == 3:
        print(reizinasana(skaitlis1, skaitlis2))
    elif darbiba == 4:
        print(dalisana(skaitlis1, skaitlis2))
    else:
        print("Šādas darbības nav!")

if __name__ == "__main__":
    main()