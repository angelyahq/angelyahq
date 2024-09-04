from sumar import sumar
from resta import restar
from multiplicacion import multiplicar
from dividir import dividir
from suma_avanzada import suma_avanzada

def mostrar_menu():
    print("Calculadora")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Dividir dos números")
    print("5. Sumar N números")
    print("6. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == '1':
            a = float(input("Ingresa el primer número"))
            b = float(input("Ingresa el segundo número:"))
            print(f"Resultado: {sumar(a, b)}")
        elif opcion == '2':
            a = float(input("Ingresa el primer número:"))
            b = float(input("Ingresa el segundo número:"))
            print(f"Resultado: {restar(a, b)}")
        elif opcion == '3':
            a = float(input("Ingresa el primer número:"))
            b = float(input("Ingresa el segundo número:"))
            print(f"Resultado: {multiplicar(a, b)}")
        elif opcion == '4':
            a = float(input("Ingresa el primer número:"))
            b = float(input("Ingresa el segundo número: "))
            print(f"Resultado: {dividir(a, b)}")
        elif opcion == '5':
            nums = list(map(float, input("Ingresa los números separados por espacio: ").split()))
            print(f"Resultado: {suma_avanzada(nums)}")
        elif opcion == '6':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
