def get_user_input():
    try:
        num1 = float(input("Ingrese un numero: "))
        num2 = float(input("Ingrese otro numero: "))
        operation = input("Elija una operacion (+, -, *, /) o escriba 'exit' para salir: ")
        return num1, num2, operation
    except ValueError:
        print("Input invalido. Por favor ingrese numeros.")
        return get_user_input()

def ejecutar_operacion(user_input, callback):
    num1, num2, operation = user_input
    if operation == '+':
        result = callback(num1,num2)
    elif operation == '-':
        result = callback(num1,num2)
    elif operation == '*':
        result = callback(num1,num2)
    elif operation == '/':
        result = callback(num1,num2)
    else:
        result = "Operacion invalida"
    
    print("Resultado:", result)

def operations():
    lambda num1, num2: num1 + num2

def main():
    while True:
        user_input = get_user_input()

        operations = {"+": lambda num1, num2: num1 + num2,"-": lambda num1, num2: num1 - num2,"*": lambda num1, num2: num1 * num2, "/": lambda num1, num2: num1 / num2}

        if user_input[2].lower() == 'exit':
            print("Salir.")
            break

        print("\nCalculando...")

        if user_input[2] in operations:
            ejecutar_operacion(user_input, operations[user_input[2]])
        else:
            print("Operacion invalida. Seleccione (+, -, *, /) o  escriba 'exit' para salir.")

if __name__ == "__main__":
    main()

