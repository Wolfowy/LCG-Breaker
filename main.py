from decimal import Decimal, getcontext

getcontext().prec = 600 # adjust in case you use some very big numbers
exists = False

m = 10  # known
x1 = 1  # known
x2 = 9  # known
x3 = 3  # known

examplePairCount = 10 # number of example pairs (better not too much)
nextValues = 5 # number of next values to show (0 means none)

print(f"For values:\n  m: {m}\n  x1: {x1}\n  x2: {x2}\n  x3: {x3}\n")

def euc(a, b):  
    if a == 0: return b, 0, 1
    gcd, x1, y1 = euc(b % a, a)  
    x = y1 - (b // a) * x1  
    y = x1
    return gcd, x, y

deltaX12 = x1-x2
oa = (euc(deltaX12, m))
nm = m/abs(oa[0])
deltaX23 = x2-x3
na = Decimal(deltaX23)*Decimal(oa[1])/Decimal(oa[0])
na = int(na%Decimal(nm))

print(f"Example a and b pairs:")

for i in range(abs(examplePairCount)):
    pa = Decimal((Decimal(na) + Decimal(i) * Decimal(nm))%m)
    pb = Decimal((Decimal(x2) - Decimal(pa) * Decimal(x1))%m)
    if((pa * x2 + pb) % m == x3):
        print(f"a: {pa}, b: {int(pb)%m}")
        exists = True

#------------------------------------------------

if exists:  
    try:
        pa1 = Decimal((Decimal(na)+Decimal(nm))%m)
        pa2 = Decimal((Decimal(na)+2*Decimal(nm))%m)

        pb1 = Decimal((Decimal(x2) - Decimal(pa1)*Decimal(x1))%m)
        pb2 = Decimal((Decimal(x2) - Decimal(pa2)*Decimal(x1))%m)

        if pa1 == pa2:
            print("\nx(i+1) = (a(n) * x(i) + b(n)) mod m\nwhere:\n    n is a whole number\n    x(i) is some i-th element of x' sequence\n    m is a modulus\n")

            print(f"a(n) = {int(na) % m}")
            print(f"a(n) = {int(na) % (-m)}\n")

            print(f"b(n) = {int(pb1) % m}")
            print(f"b(n) = {int(pb1) % (-m)}\n")

        else:

            aax = (pb2-pb1)/(pa2-pa1)

            bby = pb1 - aax*pa1

            print("\nx(i+1) = (a(n) * x(i) + b(n)) mod m\nwhere:\n    n is a whole number\n    x(i) is some i-th element of x' sequence\n    m is a modulus\n")

            print(f"a(n) = {int(pa1 - na) % m} * n + {int(na) % m}")
            print(f"a(n) = {int(pa1 - na) % (-m)} * n + {int(na) % (-m)}\n")

            print(f"b(n) = {int(aax) % m} * a(n) + {int(bby) % m}")
            print(f"b(n) = {int(aax) % (-m)} * a(n) + {int(bby) % (-m)}\n")

    except:
        print("Function definition for this exception not yet defined")

    #------------------------------------------------

    if nextValues:
        print(f"Next {nextValues} values:")
        lastX = x3
        for i in range(nextValues):
            lastX = int(Decimal(pa1)*Decimal(lastX)+Decimal(pb1)) % m
            print(f"  + {lastX}")
else:
    print("Not found :'(")