ent = open("titanic3_1.txt", "r")
linea = ent.readline()
contador1 = 0
sobre1 = 0
muj1 = 0
contador2 = 0
sobre2 = 0
contador3 = 0
sobre3 = 0
while linea != '':
    linea = linea.rstrip("\n")
    # Agregar lo que deseo hacer
    if linea[0] == "1":
        contador1 = contador1 + 1
        if linea[2] == "1":
            sobre1 = sobre1 + 1
            if linea.find("female") != -1:
                muj1 = muj1 + 1

    if linea[0] == "2":
        contador2 = contador2 + 1
        if linea[2] == "1":
            sobre2 = sobre2 + 1

    if linea[0] == "3":
        contador3 = contador3 + 1
        if linea[2] == "1":
            sobre3 = sobre3 + 1
    linea = ent.readline()
print("Cantidad de pasajeros de primera clase : ", contador1)
print("Cantidad de pasajeros de primera clase que sobreviven : ", sobre1)
print("Razon de sobrevivencia: ", sobre1 / contador1)
print("Mujeres de primera clase que sobreviven: ", muj1)
print("Cantidad de pasajeros de segunda clase : ", contador2)
print("Cantidad de pasajeros de segunda clase que sobreviven : ", sobre2)
print("Razon de sobrevivencia: ", sobre2 / contador2)
print("Cantidad de pasajeros de tercera clase : ", contador3)
print("Cantidad de pasajeros de tercera clase que sobreviven : ", sobre3)
print("Razon de sobrevivencia: ", sobre3 / contador3)
