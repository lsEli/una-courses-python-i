# Ejemplo 1: Captura de texto
name = input("Ingrese su nombre: ")
print("Hola", name)

# Ejemplo 2: Captura de número entero
age = int(input("Ingrese su edad: "))
print("Tu edad al cuadrado es:", age ** 2)

# Ejemplo 3: Captura de número decimal
salary = float(input("Ingrese su salario: "))
print("Salario mensual:", salary)

# Ejemplo 4: Captura de múltiples valores
x, y = input("Ingrese dos números separados por espacio: ").split()
print("Primer número:", x, "Segundo número:", y)

# Ejemplo 5: Validación simple de entrada
answer = input("¿Te gusta Python? (sí/no): ").strip().lower()
if answer == "sí":
    print("Excelente elección")
else:
    print("Deberías intentarlo más")
