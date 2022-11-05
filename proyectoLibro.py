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
                'ISBN': self.ISBN, 'editorial': self.editorial, 'autores': self.autores}


# termina la clase libro

def leer_archivos_disco(file):
    lista = []
    os.system("cls")
    with open(file, "r", newline="") as archivo_csv:
        reader = csv.DictReader(archivo_csv)
        for linea in reader:
            lista.append(linea)
        print("lectura correcta")
        return lista


def listar_libros(lista):
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

def main():
    enEjecucion = True
    file = "libros.csv"
    lista_libros = leer_archivos_disco(file)

    while (enEjecucion):
        input("holaaa presione cuaquier tecla para continuar")
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
        elif opcion == 2:
            listar_libros(lista_libros)
        elif opcion == 3:
            os.system("cls")
            id = input("Id:")
            titulo = input("Título:")
            genero = input("Género:")
            ISBN = input("ISBN:")
            editorial = input("Editorial:")
            autores = input("Autores:")
            libro = Libro(id, titulo, genero, ISBN, editorial, autores)
            agregar_libro(lista_libros, libro)

        elif opcion == 4:
            os.system("cls")
            id = int(input("Ingrese el Id. del libro a eliminar: \n"))
            eliminar_libro(lista_libros,file,id)
            print(f"Se elimino el libro con el \"id.\" {id}")
            
            
        elif opcion == 5:
            pass
        elif opcion == 6:
            pass
        elif opcion == 7:
            pass
        elif opcion == 8:
            pass
        elif opcion == 9:
            pass
        elif opcion == 10:
            guardar_libro(file, lista_libros)
        elif opcion == 11:
            enEjecucion = False
        else:
            print("opción no válida, ingrese nuevamente(de 1 a 11)")


if __name__ == "__main__":
    main()