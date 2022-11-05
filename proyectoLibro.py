import os
import csv
import pathlib

#clase libro
class Libro:
    def _init_(self, id: int, titulo: str, genero: str, ISBN: str, editorial: str, autores: list):
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.ISBN = ISBN
        self.editorial = editorial
        self.autores = autores

    def descripcion_libro(self)->dict:
        return {'id':self.id,'titulo':self.titulo,'genero':self.genero,
                         'ISBN':self.ISBN,'editorial':self.editorial,'autores':self.autores}


#termina la clase libro

def leer_archivos_disco(file):
    lista=[]
    os.system("cls")
    with open(file,"r",newline="") as archivo_csv:
        reader=csv.DictReader(archivo_csv)
        for linea in reader:
            lista.append(linea)
        print("lectura correcta")
        return lista



def main():    
    enEjecucion=True
    file="libros.csv"
    lista_libros=leer_archivos_disco(file)

    while(enEjecucion):
        print("Opciones: ")
        print("1: Leer archivo de disco duro")
        print("2: Listar libros")
        print("3: Agregar libro")
        print("4: Eliminar libro")
        print("5: Buscar libro por ISBN o por título")
        print("6: Ordenar libros por título")
        print("7: Buscar libros por autor, editorial o género")
        print("8: Buscar libros por número de autores")
        print("9: Editar o actualizar datos de un libro (título, género, ISBN, editorial y autores)")
        print("10: Guardar libros en archivo de disco duro")
        print("11: Salir")
        opcion=int(input("Elige una opción (de 1 a 10): "))
        if opcion==1:
            leer_archivos_disco(file)       
        elif opcion==2:
            pass
        elif opcion==3:
            pass
        elif opcion==4:
            pass
        elif opcion==5:
            pass
        elif opcion==6:
            pass
        elif opcion==7:
            pass
        elif opcion==8:
            pass
        elif opcion==9:
            pass
        elif opcion==10:
            pass
        elif opcion==11:
            enEjecucion=False
        else:
            print("Opción no válida, ingrese nuevamente(de 1 a 11)")


if __name__=="__main__":
    main()