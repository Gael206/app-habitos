#app habitos 

habitos = []

#funcion para el modulo 2
def eliminarhabito(e):
            for i, hab in enumerate(habitos):
                if hab["nombre"] == e:
                    habitos.pop(i)
                    print(f"el habito a eliminado es {e}")
                    break
            else:
                print("el habito no existe")
while True:
    try:
         respuesta = int((input("elige una opcion, 1-agregar habito, 2-ELIMINAR 3-mostrar, 4-marcar ,5-salir ")))
    except ValueError:
        print("dato invalido, ingresa un numero entre 1 y 5")
        continue

    if respuesta<1 or respuesta > 5:
        print("fuera del rango, ingrese numeros del 1 al 5")
        continue

    if respuesta == 1:
        habito = input("agrega el habito: ").lower().strip()

        if not habito:
                     print("dato invalido, ingrese un habito")
                     continue
        
        habitos.append({"nombre": habito, "Realizado": False})
    
    #el siguiente cuadro compara con y con una fucnion elimina el item
    
    if respuesta == 2:
        for i in habitos:
             print("habitos a eliminar: ", i["nombre"])
        eliminarhabitos = input("ingresa el habito a eliminar: ").lower()
        eliminarhabito(eliminarhabitos)

    #muestra los habitos que hay 
    if respuesta == 3:
        for i in habitos:
            if i["Realizado"] == False:
                print(i["nombre"], "- pendiente")
            if i["Realizado"] == True:
                print(i["nombre"], "- hecho")

    if respuesta == 4:
        for i in habitos:
                            print("los habitos a marcar", i["nombre"])
        habito_mc = input("ingresa el habito a marcar: ").lower()
        encontrado = False

        for i in habitos:
            if i["nombre"] == habito_mc:
                i["Realizado"] = True
                print(i["nombre"], "- hecho")
                encontrado = True
        if encontrado == False:
            print("HABITO INEXISTENTE")

    #este es para salir del programa
    if respuesta == 5:
            print("fin del programa")
            break