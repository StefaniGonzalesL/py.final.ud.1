import requests

url="https://pokeapi.co/api/v2/"
peticion=requests.get(url)
datos_json=peticion.json()
for k,v in datos_json.items():
    print(f"{k}: {v}")

def main():
    enEjecucion = True
    file = lista_pokemon
    lista_pokemon = leer_archivos(file)

    while (enEjecucion):
        input("hola, presione cuaquier tecla para continuar")
        os.system("cls")
        print("Opciones: ")
        print("1: Listar pokemons por generación")
        print("2: Listar pokemons por forma")
        print("3: Listar pokemons por habilidad")
        print("4: Listar pokemons por habitat")
        print("5: Listar pokemons por tipo")

        opcion = int(input("Elige una opción (de 1 a 5): "))
        
        if opcion == 1:
            os.system("cls")
            opciones_busqueda = int(input("Ingresa una generación del 1-8: \n"))

            while opciones_busqueda < 1 or opciones_busqueda > 8:   
                opciones_busqueda = int(input("Opcion Incorrecta, ingrese nuevamente una opcion valida"
                "\n)
        
        elif opcion == 2:
            os.system("cls")
            opciones_busqueda = int(input("Ingresa una forma: \n")) #llamar a la lista de formas
            print(opciones_busqueda)

        
        elif opcion ==3:
             os.system("cls")
             opciones_busqueda = int(input("Ingresa una habilidad: \n"))
            print(opciones_busqueda)

        elif opcion ==4:
             os.system("cls")
             opciones_busqueda = int(input("Ingresa una habitat: \n"))
            print(opciones_busqueda)

         elif opcion ==5:
             os.system("cls")
             opciones_busqueda = int(input("Ingresa un tipo: \n"))
            print(opciones_busqueda)