import math
x1 = int(input("Digite um numero: "))
y1 = int(input("Digite um numero: "))
x2 = int(input("Digite um numero: "))
y2 = int(input("Digite um numero: "))
d = ((x1-x2)**2) + ((y1-y2)**2)
d = math.sqrt(d)

if (d>=10):
    print("longe")
else:
    print("perto")