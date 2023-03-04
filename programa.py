# programa para determinar la igualdad entre los dos ultimos digitos

print("---------------------------------------")
print("----IGUALDAD DE LOS ULTIMOS DIGITOS----")
print("---------------------------------------")

# input

n = int(input("ingrese el entero: "))

# procesing

ultimo_digito = n % 10
penultimo = (n % 100)//10
rta = ultimo_digito == penultimo
# output

if (rta == True):
    print("los dos ultimos digitos son iguales ")
else:
    print ("los dos ultimos digitos no son iguales")