paraula = "Una mosca volaba per la llum, i la llum es va apagar"
posicio = 0
contador = 0
contadorNoA= 0
while posicio < 52:
    if (paraula[posicio]=="a"):
        print(paraula[posicio])
        contador = contador + 1
    else:
        contadorNoA = contadorNoA + 1
    posicio = posicio + 1

print ("El nombre de a es: " + str(contador))

print ("El nombre de caracters NO A es: " + str(contadorNoA))
