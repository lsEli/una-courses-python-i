# **Lección 2: Elementos básicos del lenguaje Python**

---

## **Objetivos de aprendizaje**

Al finalizar esta lección, el estudiante será capaz de:

* Aplicar la sintaxis fundamental del lenguaje Python con indentación y estructura correcta.
* Escribir código limpio siguiendo las convenciones de estilo definidas en PEP 8.
* Documentar código mediante comentarios útiles y consistentes.
* Declarar y utilizar variables y constantes eficientemente.
* Utilizar y manipular datos compuestos.
* Evaluar y construir expresiones utilizando operadores adecuados.
* Invocar funciones de biblioteca estándar.
* Realizar operaciones básicas con texto y métodos asociados.
* Utilizar colecciones como listas, tuplas, conjuntos y diccionarios con fines prácticos.

---

## **2.1 Sintaxis del lenguaje Python**

Python posee una sintaxis limpia, estructurada y minimalista. A diferencia de otros lenguajes, **la indentación no es opcional**: define bloques de código.

```python
def saludar(nombre):
    if nombre:
        print(f"Hola, {nombre}")
```

**Errores comunes:**

* Usar espacios y tabulaciones mezcladas.
* Omitir la indentación después de estructuras como `if`, `for`, `while`, `def`, etc.

---

## **2.2 Convenciones de escritura**

Python promueve el uso del **estándar PEP 8**, que define las buenas prácticas para:

* Nombres de variables y funciones: `snake_case`
* Constantes: `MAYUSCULAS_CON_GUIONES`
* Clases: `CamelCase`
* Longitud máxima de línea: 79 caracteres
* Uso de espacios, saltos de línea, etc.

```python
PI = 3.14159  # Constante
radio_circulo = 10  # Variable
```

---

## **2.3 Comentarios**

Los comentarios son esenciales para mejorar la mantenibilidad:

* Comentarios en línea:

  ```python
  resultado = x * y  # Multiplicación de enteros
  ```

* Comentarios en bloque:

  ```python
  # Esta función calcula el área de un círculo
  # usando la fórmula: área = π * r^2
  ```

* Docstrings (documentación de funciones):

  ```python
  def saludar(nombre):
      """Imprime un saludo personalizado."""
      print(f"Hola, {nombre}")
  ```

---

## **2.4 Variables**

En Python no se declara el tipo de la variable:

```python
mensaje = "Hola mundo"   # str
edad = 30                # int
pi = 3.14                # float
activo = True            # bool
```

> Python es de **tipado dinámico** y **fuerte**.

---

## **2.5 Constantes**

Python no tiene una palabra clave `const`, pero por convención, las constantes se escriben en mayúsculas:

```python
VELOCIDAD_LUZ = 299_792_458  # m/s
```

> Aunque se pueden modificar, **debe evitarse**.

---

## **2.6 Datos compuestos**

Python incluye estructuras integradas para modelar múltiples datos:

* **str**: cadenas de texto.
* **list**: listas mutables.
* **tuple**: secuencias inmutables.
* **set**: colecciones no ordenadas y sin duplicados.
* **dict**: mapeos clave-valor.

---

## **2.7 Expresiones**

Una **expresión** es cualquier combinación de variables, operadores y llamadas a funciones que produce un valor:

```python
expresion = (a + b) * c - d ** 2
```

---

## **2.8 Operadores**

| Tipo        | Operadores                          |
| ----------- | ----------------------------------- |
| Aritméticos | `+`, `-`, `*`, `/`, `//`, `%`, `**` |
| Comparación | `==`, `!=`, `>`, `<`, `>=`, `<=`    |
| Lógicos     | `and`, `or`, `not`                  |
| Asignación  | `=`, `+=`, `-=`, `*=`, `/=`, etc.   |
| Pertenencia | `in`, `not in`                      |
| Identidad   | `is`, `is not`                      |

---

## **2.9 Funciones de biblioteca**

Python incluye funciones nativas (built-in):

```python
print(len("Python"))       # 6
max([10, 20, 5])            # 20
type(3.14)                  # <class 'float'>
round(3.14159, 2)           # 3.14
```

> Referencia completa en: [https://docs.python.org/3/library/functions.html](https://docs.python.org/3/library/functions.html)

---

## **2.10 Manejo de texto**

Las cadenas de texto (`str`) son objetos con múltiples métodos útiles:

```python
texto = "Python es poderoso"
print(texto.upper())        # "PYTHON ES PODEROSO"
print(texto.split())        # ["Python", "es", "poderoso"]
print(texto.replace("es", "no es"))  # "Python no es poderoso"
```

---

## **2.11 Invocación de métodos**

Los métodos se invocan sobre objetos usando la notación de punto:

```python
lista = [1, 2, 3]
lista.append(4)
print(lista)  # [1, 2, 3, 4]
```

> A diferencia de las funciones, los métodos dependen de un objeto.

---

## **2.12 Listas, tuplas, conjuntos y diccionarios**

### **Listas** (mutable y ordenada)

```python
numeros = [1, 2, 3]
numeros.append(4)
```

### **Tuplas** (inmutable)

```python
coordenadas = (10.5, 20.3)
```

### **Conjuntos** (sin orden, sin duplicados)

```python
colores = {"rojo", "verde", "rojo"}  # {"rojo", "verde"}
```

### **Diccionarios** (clave-valor)

```python
persona = {"nombre": "Luis", "edad": 30}
```
