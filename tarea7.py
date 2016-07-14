print("Programa Para determinar el porcentaje de inversión de tres personas")

def in1(x):
    a=(x*100)//t
    print("1° Inversionista:", a , "% del capital")
    return a
def in2(y):
    b=(y*100)//t
    print("2° Inversionista:", b , "% del capital")
    return b
def in3(z):
    c=(z*100)//t
    print("3° Inversionista:", c , "% del capital")
    return c

x=float(input("Primer inversionista:"))
y=float(input("Segundo inversionista:"))
z=float(input("Tercer inversionista:"))

t=x+y+z

print("Total de la inversion :" , t)
in1(x)
in2(y)
in3(z)

