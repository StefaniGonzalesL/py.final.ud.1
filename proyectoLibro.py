class Libro:
    pass




def leer_archivo_disco():
    pass



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
        leer_archivo_disco()
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

