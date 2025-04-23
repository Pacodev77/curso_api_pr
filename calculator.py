# calculadora Usando Python

def sumar(a,b):
    return a + b
def restar(a,b):
    return a - b
def multiplicar(a,b):
    return a * b
def dividir(a,b):
    return a / b if b != 0 else 'Error. No se puede dividir por cero.'

def calculadora():
    print('\n*** Calculadora ***\n')
    print('1. Sumar.')
    print('2. Restar.')
    print('3. Multiplicar')
    print('4. Dividir.')
calculadora()
while True:
    try:
        opcion = int(input('Ingrese una opción: '))
        if opcion == 0:
            print('Salir del programa')
            break
        if opcion < 1 or opcion > 4:
            print('Seleccione una opción válida.')
            continue

        num_1 = float(input('Ingrese un número: '))
        num_2 = float(input('Ingrese otro número: '))

        if opcion == 1:
            resultado = sumar(num_1,num_2)
            print(f'Resultado: {resultado}')
        elif opcion == 2:
            resultado = restar(num_1,num_2)
            print(f'Resultado: {resultado}')
        elif opcion == 3:
            resultado = multiplicar(num_1,num_2)  # Corregido
            print(f'Resultado: {resultado}')
        elif opcion == 4:
            resultado = dividir(num_1,num_2)  # Corregido
            print(f'Resultado: {resultado}')
    except ValueError:
        print('Ocurrió un error inesperado')

