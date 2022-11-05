import os
import csv
import pathlib


class Libro:
    def __init__(self, id: int, titulo: str, genero: str, ISBN: str, editorial: str, autores: list):
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.ISBN = ISBN
        self.editorial = editorial
        self.autores = autores

    def descripcion_libro(self)->dict:
        return {'id':self.id,'titulo':self.titulo,'genero':self.genero,
                         'ISBN':self.ISBN,'editorial':self.editorial,'autores':self.autores}


enEjecucion=True
print("Opciones: ")
print("1: Leer archivo de disco duro (.txt o csv) que cargue 3 libros")
print("2: Listar libros")
print("3: Agregar libro")
print("4: Eliminar libro")
print("5: Buscar libro por ISBN o por título. Se debe sugerir las opciones y listar el resultado")
print("6: Ordenar libros por título")
print("7: Buscar libros por autor, editorial o género. Se deben sugerir las opciones y listar los resultados")
print("8: Buscar libros por número de autores. Se debe ingresar un número por ejemplo 2 (hace referencia a dos autores) y se deben listar todos los libros que contengan 2 autores")
print("9: Editar o actualizar datos de un libro (título, género, ISBN, editorial y autores)")
print("10: Guardar libros en archivo de disco duro (.txt o csv)")
1
print("11: Salir")
while(enEjecucion):

    opcion=int(input("Elige una opción (de 1 a 10): "))

    if opcion==1:
        
        def registrar_libros(nombre_archivo):
            cantidad=int(input("¿Cuantos libros desea registrar?"))
            campos=['Id',"Título",'Género','ISBN','Editorial','Autores']

            if not pathlib.Path(nombre_archivo).exists():
                with open(nombre_archivo,"w", newline='') as archivo_csv:
                    writer = csv.DictWriter(archivo_csv,fieldnames=campos)
                    writer.writeheader()

            with open(nombre_archivo,"a",newline="") as archivo_csv:
                writer=csv.DictWriter(archivo_csv,fieldnames=campos)
                for i in range (cantidad):
                    os.system("cls")
                    Id=input("Id:")
                    Título=input("Título:")
                    Género=input("Género:")
                    ISBN=input("ISBN:")
                    Editorial=input("Editorial:")
                    Autores=input("Autores:")
                    writer.writerow({"Id":Id,"Título":Título,"Género":Género,"ISBN":ISBN,"Editorial":Editorial,"Autores":Autores})

        def recuperar_libros(nombre_archivo):
            os.system("cls")
            print("Libros registrados")
            with open(nombre_archivo,"r",newline="") as archivo_csv:
                reader=csv.DictReader(archivo_csv)
                for linea in reader:
                    for campo,valor in linea.items():
                        print(f"{campo}:{valor}")
                    print("~"*50)

        def main():
            archivo="libros_encabezado.csv"
            registrar_libros(archivo)
            recuperar_libros(archivo)

        if __name__=="__main__":
            main()
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
        print("opción no válida, ingrese nuevamente(de 1 a 11)")

