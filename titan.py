ent = open("titanic3_1.txt", "r")
contador1 = 0
contador2 = 0
contador3 = 0
linea = ent.readline()
while linea != '':
    linea = linea.rstrip('\n')
    if linea[0] == "1":
        contador1 = contador1 + 1
    if linea[0] == "2":
        contador2 = contador2 + 1
    if linea[0] == "3":
        contador3 = contador3 + 1        
    linea = ent.readline()
print("De primera clase: ", contador1)
print("De segunda clase: ", contador2)
print("De tercera clase: ", contador3)
print("Total: ", contador1 + contador2 + contador3)