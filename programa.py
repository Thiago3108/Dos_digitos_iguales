# programa para determinar la igualdad entre los dos ultimos digitos

print("---------------------------------------")
print("----IGUALDAD DE LOS ULTIMOS DIGITOS----")
print("---------------------------------------")

# input

n = int(input("ingrese el entero: "))

# procesing

if (n>0):
    ud = (n % 10)
    p = (n % 100)//10
    if (ud == p):
       print("los dos ultimos digitos son iguales ")
    else:
     print ("los dos ultimos digitos no son iguales")
else:
    udN = -(n % 10)
    pN = -(n % 100)//10
    if (udN == pN ):
       print("los dos ultimos digitos son iguales ")
    else:
       print ("los dos ultimos digitos no son iguales")
    