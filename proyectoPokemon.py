import requests
import os

url_general="https://pokeapi.co/api/v2/"

def abrir_json(url:str)->dict:
    peticion=requests.get(url)
    return peticion.json()


datos_json=abrir_json(url_general)

url_generacion=datos_json["generation"]
url_forma=datos_json["pokemon-shape"]
url_habilidad=datos_json["ability"]
url_habitat=datos_json["pokemon-habitat"]
url_tipo=datos_json["type"]



#listar pokemones
def listar_pokemones_1(url, numero):
    datos_del_url=abrir_json(url)
    results=datos_del_url["results"]
    url_numero=""
    for i in results:
        if numero==results.index(i)+1:
            url_numero=i["url"]
    datos_numero=abrir_json(url_numero)
    pokemones=datos_numero["pokemon_species"]

    for i in pokemones:
        nombre=i["name"]
        datos_pokemon=abrir_json(i["url"])
        id_pokemon=datos_pokemon["id"]
        pokemon=abrir_json(f"https://pokeapi.co/api/v2/pokemon/{id_pokemon}/")
        habilidad_pokemon=pokemon["abilities"]
        lista_nombre_habilidad=[]
        for n in habilidad_pokemon:
            lista_nombre_habilidad.append(n["ability"]["name"])
        sprites_pokemon=pokemon["sprites"]
        url_imagen=sprites_pokemon["front_default"]

        dic_datos_pokemon={"nombre":nombre,"habilidades":lista_nombre_habilidad,"URL imagen":url_imagen}
        print(dic_datos_pokemon)

def main():
    enEjecucion = True

    while (enEjecucion):
        input("hola, presione cuaquier tecla para continuar")
        os.system("cls")
        print("Opciones: ")
        print("1: Listar pokemons por generación")
        print("2: Listar pokemons por forma")
        print("3: Listar pokemons por habilidad")
        print("4: Listar pokemons por habitat")
        print("5: Listar pokemons por tipo")
        print("6: Salir")

        opcion = int(input("Elige una opción (de 1 a 6): "))
        
        if opcion == 1:
            os.system("cls")
            opciones_busqueda = int(input("Ingresa una generación del 1-8: \n"))

            while opciones_busqueda < 1 or opciones_busqueda > 8:   
                opciones_busqueda = int(input("Opcion Incorrecta, ingrese nuevamente una opcion valida\n"))

            listar_por_generacion(url_generacion,opciones_busqueda)
        
        elif opcion == 2:
           os.system("cls")
           opciones_busqueda = input("Ingresa una forma: \n") #llamar a la lista de formas
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

        elif opcion==6:
            os.system("cls")
            enEjecucion=False
        else:
            os.system("cls")
            print("Opción inválida, ingrese nuevamnete una opcion(del 1 a 6)")


if __name__ == "__main__":
    main()


