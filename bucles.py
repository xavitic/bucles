
print("Introdueix el número per calcular-ne el factorial:")
factorial = input()
numDecrementat = int(factorial) - 1
resultatParcial = int(factorial)


while numDecrementat >= 1:
   resultatParcial =  resultatParcial * numDecrementat
   print(resultatParcial)
   numDecrementat = numDecrementat - 1


print ("El factorial de " + factorial + " es: " + str(resultatParcial))

