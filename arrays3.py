a = ['a','e','i','o','u']

b = []

b.append(1)
b.append(3)
b.append(2)

#print(b)
#print(a)

numeros = []

seguir = True

while seguir :
    print("Introdueix un nombre per calcular la mitjana aritmètica:")
    numeroText = input()
    if numeroText == "exit" :
        seguir = False
    else :
        numero = int(numeroText)
        numeros.append(numero)

print(numeros)

longitud = len(numeros)
print(longitud)
posicio = 0
resultat = 0
while posicio < longitud :
    resultat = numeros[posicio] + resultat
    posicio = posicio + 1

print("La mitjana aritmètica és: " +  str(resultat / longitud))





