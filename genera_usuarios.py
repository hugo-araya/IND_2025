ent = open("nombres.txt", "r")
sal = open("usuarios.txt", "w")
linea = ent.readline()
while linea != '':
    linea = linea.rstrip("\n")
    lista = linea.split()
    nombre = lista[0]
    apellidop = lista[1]
    apellidom = lista[2]
    usuario = nombre[0].lower() + apellidop.lower()
    sal.write(usuario+"\n")
    linea = ent.readline()
ent.close()
sal.close()

