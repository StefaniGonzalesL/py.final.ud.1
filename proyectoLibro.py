import os
import csv
import pathlib


# clase libro
class Libro:
    def __init__(self, id: int, titulo: str, genero: str, ISBN: str, editorial: str, autores: list):
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.ISBN = ISBN
        self.editorial = editorial
        self.autores = autores

    def descripcion_libro(self) -> dict:
        return {'id': self.id, 'titulo': self.titulo, 'genero': self.genero,
                'ISBN': self.ISBN, 'editorial': self.editorial, 'autores': str(self.autores)}


# termina la clase libro

def leer_archivos_disco(file:str)->list:
    lista = []
    os.system("cls")
    with open(file, "r", newline="") as archivo_csv:
        reader = csv.DictReader(archivo_csv)
        for linea in reader:
            lista.append(linea)
        return lista


def listar_libros(lista:list):
    os.system("cls")
    for i in lista:
        print(i)


def agregar_libro(lista: list, libro: Libro):
    lista.append(libro.descripcion_libro())
    print("El libro se agregó a la lista")


def guardar_libro(file, lista):
    campos = ['id', 'titulo', 'genero', 'ISBN', 'editorial', 'autores']
    with open(file, "a", newline='') as archivo_csv:
        writer = csv.DictWriter(archivo_csv, fieldnames=campos)
        writer.writerow(lista[-1])
        print("el libro se guardó correctamente en el disco")

#Elimininar libro

def eliminar_libro(lista,file,id):
    for i in lista:
        if int(i['id'])==id:
            lista.pop(lista.index(i))
    escribe_archivo(file,lista)


def escribe_archivo(file,lista):
    campos=['id','titulo','genero','ISBN','editorial','autores']
    with open(file, "w", newline='') as archivo_csv:
        writer = csv.DictWriter(archivo_csv, fieldnames=campos)
        writer.writeheader()
    with open(file,"a",newline='') as archivo_csv:
        writer=csv.DictWriter(archivo_csv,fieldnames=campos)
        for i in lista:
            writer.writerow(lista[lista.index(i)])

#Buscar libro por ISBN y titulo

def buscar_libro_ISBN(lista,ISBN):
    for i in lista:
        if i ['ISBN']== ISBN:
            print(i)

def buscar_libro_titulo(lista, titulo):
    for i in lista:
        if i ['titulo']== titulo:
            print(i)

#Buscar libro por autor y editorial o género

def busqueda_autores (lista,autor):
    for i in lista:
        string_autores = i["autores"]
        lista_autores=eval(string_autores)
        for j in lista_autores:
            if j==autor:
                print(i)

def busqueda_editorial (lista,editorial):
    for i in lista: 
        if i ['editorial']== editorial:
            print(i)


def busqueda_genero (lista,genero):
    for i in lista:
        if i ['genero']== genero:
            print(i)


#ordenar libro por titulo

def ordenar_por_titulo(lista):
    lista_titulo=[]
    for i in lista:
        lista_titulo.append(i['titulo'])
    lista_titulo.sort()      #ordena la lista

    for i in lista_titulo:
        for j in lista:
            if i==j['titulo']:
                print(j)
                


def main():
    enEjecucion = True
    file = "libros.csv"
    lista_libros = leer_archivos_disco(file)

    while (enEjecucion):
        input("holaaa presione cuaquier tecla para continuar")
        os.system("cls")
        print("Opciones: ")
        print("1: Leer archivo de disco duro")
        print("2: Listar libros")
        print("3: Agregar libro")
        print("4: Eliminar libro")
        print("5: Buscar libro por ISBN o por título. Se debe sugerir las opciones y listar el resultado")
        print("6: Ordenar libros por título")
        print("7: Buscar libros por autor, editorial o género")
        print("8: Buscar libros por número de autores. Se debe ingresar un número por ejemplo 2 (hace referencia a dos autores) y se deben listar todos los libros que contengan 2 autores")
        print("9: Editar o actualizar datos de un libro (título, género, ISBN, editorial y autores)")
        print("10: Guardar libros en archivo de disco duro (.txt o csv)")
        print("11: Salir")
        opcion = int(input("Elige una opción (de 1 a 10): "))
        
        if opcion == 1:
            leer_archivos_disco(file)
            print("lectura correcta")        
        elif opcion == 2:
            listar_libros(lista_libros)
        elif opcion == 3:
            os.system("cls")
            Id = input("Id:")
            titulo = input("Título:")
            genero = input("Género:")
            ISBN = input("ISBN:")
            editorial = input("Editorial:")
            numero_autores=int(input("Cuantos autores hay?: "))
            lista_autores=[]
            for i in range(numero_autores):
                autor = input(f"Autor {i}:")
                lista_autores.append(autor)
            libro = Libro(Id, titulo, genero, ISBN, editorial, lista_autores)
            agregar_libro(lista_libros, libro)

        elif opcion == 4:
            os.system("cls")
            Id = int(input("Ingrese el Id. del libro a eliminar: \n"))
            eliminar_libro(lista_libros,file,Id)
            print(f"Se elimino el libro con el \"id.\" {Id}")
            
            
        elif opcion == 5:
            os.system("cls")
            opciones_busqueda = int(input("Ingresa una opcion: \n Opcion 1 : ISBN \n Opcion 2 : Titulo \n"))

            while opciones_busqueda < 1 or opciones_busqueda > 2:
                opciones_busqueda = int(input("Opcion Incorrecta, ingrese nuevamente una opcion valida"
                "\n Opcion 1 : ISBN \n Opcion 2 : Titulo: \n"))

            if opciones_busqueda == 1:
                ISBN = input("Ingrese el ISBN del libro a buscar: ")
                buscar_libro_ISBN(lista_libros, ISBN)

            if opciones_busqueda == 2:
                titulo = input("Ingrese el Titulo del libro a buscar: ")
                buscar_libro_titulo(lista_libros, titulo)
        

        elif opcion == 6:
            os.system("cls")
            ordenar_por_titulo(lista_libros)
        elif opcion == 7:
            
            os.system("cls")
            opciones_busqueda = int(input("Ingresa una opcion: \n Opcion 1 : Autor \n Opcion 2 : Editorial \n Opcion 3 : Genero \n"))

            while opciones_busqueda < 1 or opciones_busqueda > 3:
                opciones_busqueda = int(input("Opcion Incorrecta, ingrese nuevamente una opcion valida"
                "\n Opcion 1 : Autor \n Opcion 2 : Editorial: \n Opcion 3 : Genero \n"))

            if opciones_busqueda == 1:
                autor = input("Ingrese el Autor(es) del libro a buscar: ")
                busqueda_autores(lista_libros, autor)

            if opciones_busqueda == 2:
                editorial = input("Ingrese la Editorial a buscar: ")
                busqueda_editorial(lista_libros, editorial)
            
            if opciones_busqueda == 3:
                genero = input("Ingrese el Género a buscar: ")
                busqueda_genero(lista_libros, genero)


        elif opcion == 8:
            pass
        elif opcion == 9:
            pass
        elif opcion == 10:
            guardar_libro(file, lista_libros)
        elif opcion == 11:
            os.system("cls")
            enEjecucion = False
        else:
            print("opción no válida, ingrese nuevamente(de 1 a 11)")


if __name__ == "__main__":
    main()