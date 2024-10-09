pacientes = []


def mostrar_menu():
    """
    Muestra las opciones del menu para que el usuario elija.
    """
    print(
        """
#################menu#################
    1-cargar pacientes
    2-mostrar todos los pacientes
    3-buscar paciente por historia clinica
    4-ordenar pacientes por numero de historia clinica
    5-mostrar paciente con mas dias de internacion
    6-mostrar paciente con menos dias de internacion
    7-mostrar pacientes con mas de 5 dias de internacion
    8-promedio de dias de internacion
    9-salir
    """
    )
    opcion = int(input("elige una opcion: "))
    return opcion


def cargar_paciente():
    """
    Permite agregar pacientes con sus datos como nombre, edad, etc.
    """
    numero_de_pacientes = int(input("cuantos pacientes deseas agregar: "))
    for _ in range(numero_de_pacientes):
        historia_clinica = int(input("historia clinica: "))
        nombre = input("nombre del paciente: ")
        edad = int(input("edad del paciente: "))
        diagnostico = input("diagnostico: ")
        dias_de_internacion = int(input("dias de internacion: "))
        pacientes.append(
            [historia_clinica, nombre, edad, diagnostico, dias_de_internacion]
        )
    return


def mostrar_pacientes():
    """
    Muestra la lista de pacientes guardados.
    """
    if pacientes == []:
        print("no hay pacientes")
        return
    for i in pacientes:
        print(
            f"historia clinica: {i[0]} nombre: {i[1]} edad: {i[2]} diagnostico: {i[3]} dias de internacion: {i[4]}"
        )
    return


def buscar_paciente():
    """
    Busca un paciente por el numero de historia clinica.
    """
    if pacientes == []:
        print("no hay pacientes")
        return
    historia_clinica = int(input("introducir el numero de historia clinica: "))
    for i in pacientes:
        if i[0] == historia_clinica:
            print(
                f"historia clinica: {i[0]}, nombre: {i[1]}, edad: {i[2]}, diagnostico: {i[3]}, dias de internacion: {i[4]}"
            )
            return
    print("paciente no encontrado")
    return


def ordenar_pacientes():
    """
    Ordena la lista de pacientes por el numero de historia clinica.
    """
    if pacientes == []:
        print("no hay pacientes")
        return
    n = len(pacientes)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if pacientes[j][0] > pacientes[j + 1][0]:
                pacientes[j], pacientes[j + 1] = pacientes[j + 1], pacientes[j]
    return


def mostrar_mas_dias():
    """
    Muestra el paciente con mas dias de internacion..
    """
    if pacientes == []:
        print("no hay pacientes")
        return
    max_dias = float("-inf")
    min_dias = float("inf")
    paciente_mas_dias = ""
    paciente_menos_dias = ""
    for paciente in pacientes:
        if paciente[4] > max_dias:
            max_dias = paciente[4]
            paciente_mas_dias = paciente[1]
        if paciente[4] < min_dias:
            min_dias = paciente[4]
            paciente_menos_dias = paciente[1]
    print(
        f"paciente con mas dias de internacion es: {paciente_mas_dias} dias: {max_dias}"
    )
    return


def mostrar_menos_dias():
    """
    Muestra el paciente con menos dias de internacion.
    """
    if pacientes == []:
        print("no hay pacientes")
        return
    max_dias = float("-inf")
    min_dias = float("inf")
    paciente_mas_dias = ""
    paciente_menos_dias = ""
    for paciente in pacientes:
        if paciente[4] > max_dias:
            max_dias = paciente[4]
            paciente_mas_dias = paciente[1]
        if paciente[4] < min_dias:
            min_dias = paciente[4]
            paciente_menos_dias = paciente[1]
    print(
        f"paciente con menos dias de internacion es: {paciente_menos_dias} dias: {min_dias}"
    )
    return


def pacientes_mas_5_dias():
    """
    Muestra los pacientes que tienen mas de 5 dias de internacion.
    """
    if pacientes == []:
        print("no hay pacientes")
        return
    print("pacientes con mas de 5 dias internado:")
    for i in pacientes:
        if i[4] > 5:
            print(f"nombre: {i[1]} dias: {i[4]}")
    return


def promedio_dias_internacion():
    """
    Calcula el promedio de dias de internacion de todos los pacientes.
    """
    if pacientes == []:
        print("no hay pacientes")
        return
    total_dias = 0
    for i in pacientes:
        total_dias += i[4]
    promedio = total_dias / len(pacientes)
    print(f"promedio de dias internados es de: {promedio:.2f}")
    return


def menu():
    """
    Muestra el menu y deja elegir opciones hasta que el usuario decida salir.
    """
    continuar = True
    while continuar:
        opcion = mostrar_menu()
        if opcion == 1:
            cargar_paciente()
        elif opcion == 2:
            mostrar_pacientes()
        elif opcion == 3:
            buscar_paciente()
        elif opcion == 4:
            ordenar_pacientes()
        elif opcion == 5:
            mostrar_mas_dias()
        elif opcion == 6:
            mostrar_menos_dias()
        elif opcion == 7:
            pacientes_mas_5_dias()
        elif opcion == 8:
            promedio_dias_internacion()
        elif opcion == 9:
            print("saliendo del sistema")
            continuar = False
        else:
            print("error elige otra opcion")


menu()