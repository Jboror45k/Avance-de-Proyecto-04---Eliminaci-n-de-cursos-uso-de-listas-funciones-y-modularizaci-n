# Lista de cursos disponiblcursos = []

mi_lista_cursos = [
    "Contabilidad 2", "Precalculo", "Algoritmos", "Algebra lineal",
    "Matematica discreta", "Programacion 1", "Programacion 2",
    "Fisica 1", "Fisica 2", "Calculo 1", "Calculo 2"
]
cursos = []  # <-- Agregar esto al inicio

#aqui se registra las notas que ya se han guardado y nos devuelve en la pantalla
#todas las cantidades guardadaes
def registrar_curso_y_nota():
    while True:
        usar_lista = input("¿Quieres verificar si un curso esta disponible en la lista UMG? (S/N): ").strip().lower()
        
        if usar_lista == "s":
            print("\nAcontinuacion la lista de Cursos Disponilbes:")
            for i, elem in enumerate(mi_lista_cursos, start=1):
                   print(i, ".", elem)

            try:
                indice = int(input("Selecciona el número del curso: "))
                if 1 <= indice <= len(mi_lista_cursos):
                    curso = mi_lista_cursos[indice-1]
                else:
                    print("Número fuera de lo establecido.\n")
                    continue
            except ValueError:
                print("Debes ingresar un número válido.\n")
                continue
        else:
            curso = input("Ingrese el curso: ").strip()
            if not curso:
                print("El curso no puede estar vacío.\n")
                continue

        try:
            nota = float(input("Ingrese la nota del curso (0 a 100): "))
            if 0 <= nota <= 100:
                cursos.append({"curso": curso, "nota": nota})
                print("Nombre del Curso", curso, "registrado con la nota de ", nota, "\n")

            else:
                print("Error: la nota debe estar entre 0 y 100.\n")
                continue
        except ValueError:
            print("Error: debes ingresar un número válido.\n")
            continue

        opcion = input("¿Registrar otro curso? (S/N): ").strip().lower()
        if opcion != "s":
            break
#aqui en esta funcion nos va a mostrar todas las notas guardadas y las mostrara en la consola
#muestra las notas registradas en la unidad guardada
def mostrar_todas_las_notas():
    if cursos:
        print("\nRegistro de notas por curso:")
        for i, c in enumerate(cursos, start=1):
            print(f"{i}. {c['curso']}: {c['nota']}")
        print()
    else:
        print("No se han registrado cursos.\n")

#aqui vamos a calcular el promedio por medio de una funcion que suma todas las notas y las divide
#dentro de las canctidades de notas y nos regresa el promedio
def calcular_promedio_general():
    if cursos:
        promedio = sum(c["nota"] for c in cursos) / len(cursos)
        print(" El promedio general es: \n", promedio)
    else:
        print("No fue posible calcular el promedio (no hay cursos registrados).\n")

# esta es la funcion que nos sirve para buscar una nota que este guardada en el sistema
# esta funcion nos motrara la nota registrada
def buscar_nota_por_curso():
    if not cursos:
        print("No has registrado cursos.\n")
        return
    curso_buscar = input("Ingrese el curso a buscar: ")
    for c in cursos:
        if c["curso"].lower() == curso_buscar.lower():
            print(f"Registro encontrado: {c['curso']}, Nota: {c['nota']}\n")
            return
    print("Curso no encontrado.\n")

# esta es la funcion que nos sirve para eliminar el curso que estemos usando o el curso que 
# queramos quitar del programa
def eliminar_curso():
    if not cursos:
        print("No hay cursos para eliminar.\n")
        return
    eliminar = input("Nombre del curso a eliminar: ")
    for i in range(len(cursos)):
        if cursos[i]["curso"].lower() == eliminar.lower():
            cursos.pop(i)
            print("Curso", eliminar, " eliminando.\n")
            return
    print("No se encontró ese curso.\n")


# aqui tenesmo el menu principal del proyecto de la unidad
while True:
    print("        MENÚ PRINCIPAL      ")
    print("1. Registrar curso nuevo y nota")
    print("2. Mostrar todas las notas")
    print("3. Calcular promedio general")
    print("4. Buscar nota por curso")
    print("5. Eliminacion de curso")
    print("6. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        registrar_curso_y_nota()
    elif opcion == "2":
        mostrar_todas_las_notas()
    elif opcion == "3":
        calcular_promedio_general()
    elif opcion == "4":
        buscar_nota_por_curso()
    elif opcion == "5":
        eliminar_curso()
    elif opcion == "6":
        print("Saliendo...")
        break
    else:
        print("Opción no válida.\n")
