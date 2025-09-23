import test

def print_hello():
    """Hier kommen Kommentare hin um die funktion zu beschreiben"""
    print("hallo Welt!!!")

def goodbye():
    print("tschuess und auf wiedersehene")


def addierer(a,b):
#typische fehler sind variablen in funktionen konkrete werte zuzuweisen
    a = 13
    b = 47
    print(a+b)

def rechnen(x,y):
    ergebnis = x+y
    return ergebnis

def zylindervolumen(radius, hoehe):
    pi = 3.141592
    volumen = (pi*radius**2)*hoehe
    return volumen

sechs_zylinder = zylindervolumen(5,20)*6
print(sechs_zylinder)

def durchschnitt(a,b):
    durchschnitt = (a+b)/2
    return durchschnitt

a = 10
b = 50

ergebnis = durchschnitt(a,b)
print(ergebnis)


def main():
    neue_liste = [23,54,76]
    gh = test.a(neue_liste)
    print(gh)


if __name__ == "__main__":
    main()