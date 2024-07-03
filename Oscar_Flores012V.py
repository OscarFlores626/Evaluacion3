#evaluacion sumativa 3
import os
import csv
import random
def limpiar_pantalla():
    os.system("cls")
pedidos=[]
nropedidos=[]
santiago=[]
buin=[]
sanbernardo=[]
def ingreso_cliente():
    menusacos=0
    saco5k=0
    saco10k=0
    saco20k=0
    numero_pedido=random.randint(1,1000)
    nombre=input("Ingrese el nombre y apellido del cliente: ")
    direccion=input("Ingrese direccion del cliente: ")
    print("1>San bernardo")
    print("2>Buin")
    print("3>Santiago\n")
    try:
        comuna=int(input("Ingrese su sector: "))
        if comuna==1:
            sector="San bernardo"
        elif comuna==2:
            sector="Buin"
        elif comuna==3:
            sector="Santiago"
        else:
            print("Sector invalido")
    except ValueError:
        print("Ingrese un sector valido")
        return
    while menusacos==0:
        limpiar_pantalla()
        print("1>Saco 5kg \n2>Saco 10kg \n3>Saco 20kg \n4>Finalizar y guardar cliente.")
        respuesta=int(input("ingrese que sacos desea el cliente: "))
        try:
            if respuesta==1:
                try:
                    saco5k=int(input("Ingrese la cantidad de sacos de 5 kilos: \n"))
                    menusacos=0
                except ValueError:
                    print("Exprese la cantidad deseada en numeros porfavor.")
                    return
            elif respuesta==2:
                try:
                    saco10k=int(input("Ingrese la cantidad de sacos de 10 kilos: \n"))
                    menusacos=0
                except ValueError:
                    print("Exprese la cantidad deseada en numeros porfavor.")
                    return
            elif respuesta==3:
                try:
                    saco20k=int(input("Ingrese la cantidad de sacos de 20 kilos: \n"))
                    menusacos=0
                except ValueError:
                    print("Exprese la cantidad deseada en numeros porfavor.")
                    return
            elif respuesta==4:
                print("Guardando cliente...")
                menusacos==5
                break
        except ValueError:
            print("Ingrese una opcion valida.")
            return
    cliente={
        "Nro Pedido": numero_pedido,
        "Cliente": nombre,
        "Direccion": direccion,
        "Sector": sector,
        "Saco 5kg": saco5k,
        "Saco 10kg": saco10k,
        "Saco 20kg": saco20k,
    }
    if comuna==1:
        sanbernardo.append(cliente)
    elif comuna==2:
        buin.append(cliente)
    elif comuna==3:
        santiago.append(cliente)
    pedidos.append(cliente)
    print("Cliente agregado exitosamente!...")
def listar():
    if not pedidos:
        print("No hay pedidos ingresados")
        return
    salida="\nNro Pedido    Cliente     Direccion         Sector       Saco 5kg    Saco 10kg   Saco 20kg\n"
    salida+="-"*95 + "\n"
    for cliente in pedidos:
        salida+= (f"{cliente['Nro Pedido']:15}{cliente['Cliente']:10} {cliente['Direccion']:10} {cliente['Sector']:10} "
                    f"{cliente['Saco 5kg']:11} {cliente['Saco 10kg']:11} {cliente['Saco 20kg']:5}\n")
    print(salida)


def guardarcsv():
    with open("archivo.csv", mode="w", newline="") as file:
        escritor=csv.writer(file)
        escritor.writerow(["Nro Pedido","Cliente","Direccion","Sector","Saco 5kg","Saco 10kg","Saco 20kg"])
        for cliente in pedidos:
            escritor.writerow([
                cliente["Nro Pedido"],
                cliente["Cliente"],
                cliente["Direccion"],
                cliente["Sector"],
                cliente["Saco 5kg"],
                cliente["Saco 10kg"],
                cliente["Saco 20kg"]
            ])
def cargarcsv():
    if os.path.exists("archivo.csv"):
        with open("archivo.csv",mode="r",newline="") as file:
            lector=csv.DictReader(file)
            for i in lector:
                cargar={
                    "Nro Pedido":i["Nro Pedido"],
                    "Cliente":i["Cliente"],
                    "Direccion":i["Direccion"],
                    "Sector":i["Sector"],
                    "Saco 5kg":i["Saco 5kg"],
                    "Saco 10kg":i["Saco 10kg"],
                    "Saco 20kg":i["Saco 20kg"],
                }
                pedidos.append(cargar)
def hojaruta():
    print("1>San Bernardo")
    print("2>Buin")
    print("3>Santiago")
    try:
        rutasector=int(input("Ingrese la ruta que desea imprimir: "))
    except ValueError:
        print("Ingrese un sector valido")
    if rutasector==1:
        salida="\nNro Pedido    Cliente     Direccion         Sector       Saco 5kg    Saco 10kg   Saco 20kg\n"
        salida+="-"*95 + "\n"
        for cliente in sanbernardo:
            salida+= (f"{cliente['Nro Pedido']:15}{cliente['Cliente']:10} {cliente['Direccion']:10} {cliente['Sector']:10} "
                        f"{cliente['Saco 5kg']:11} {cliente['Saco 10kg']:11} {cliente['Saco 20kg']:5}\n")
        print(salida)
    elif rutasector==2:
        salida="\nNro Pedido    Cliente     Direccion         Sector       Saco 5kg    Saco 10kg   Saco 20kg\n"
        salida+="-"*95 + "\n"
        for cliente in buin:
            salida+= (f"{cliente['Nro Pedido']:15}{cliente['Cliente']:10} {cliente['Direccion']:10} {cliente['Sector']:10} "
                        f"{cliente['Saco 5kg']:11} {cliente['Saco 10kg']:11} {cliente['Saco 20kg']:5}\n")
        print(salida)
    elif rutasector==3:
        salida="\nNro Pedido    Cliente     Direccion         Sector       Saco 5kg    Saco 10kg   Saco 20kg\n"
        salida+="-"*95 + "\n"
        for cliente in santiago:
            salida+= (f"{cliente['Nro Pedido']:15}{cliente['Cliente']:10} {cliente['Direccion']:10} {cliente['Sector']:10} "
                        f"{cliente['Saco 5kg']:11} {cliente['Saco 10kg']:11} {cliente['Saco 20kg']:5}\n")
        print(salida)
        
def MainMenu():
    cargarcsv()
    menu=0
    while menu==0:
        print("Bienvenidos a CatPremium!! (^.^)")
        print("1>Registrar Pedido")
        print("2>Listar todos los pedidos")
        print("3>Imprimir hoja de ruta")
        print("4>Salir del programa")
        respuesta=int(input("Ingrese la accion que desea realizar: "))
        try:
            if respuesta==1:
                limpiar_pantalla()
                ingreso_cliente()
                menu=0
            elif respuesta==2:
                limpiar_pantalla()
                listar()
                menu=0
            elif respuesta==3:
                hojaruta()
                
            elif respuesta==4:
                guardarcsv()
                print("Saliendo del programa...")
                menu=5
                break
        except ValueError:
            print("Ingrese una opcion valida")
MainMenu()