tareas_completadas=0
tareas_incompletas=0
tareas=0

def mostrar_tareas_incompletas():
    print(f"¿Cuantas tareas tienes?")

    print(f"Tienes un total de tareas: {tareas}, de las cuales realizaste {tareas_completadas}, asi que tienes que hacer {tareas_incompletas}")

tareas=int(input("Ingrese la cantidad de tareas que tiene: "))
tareas_completadas = int(input("Ingrese la cantidad de las que ya realizo: "))

def completar_tareas():
    global tareas_completadas
    global tareas_incompletas
    tareas_incompletas = tareas - tareas_completadas

completar_tareas()
mostrar_tareas_incompletas()    