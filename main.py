"""
¿Qué es una variable en Python?
R/ Una variable es un "contenedor" que almacena datos o valores.
"""
# ¿Cómo manipular la precisión de una variable float al utilizar la función print en Python?
mi_variable = 3.14159265358979323846  # Definición de una variable float
print(f"Con 2 decimales: {mi_variable:.1f}")  # Imprimir con 2 decimales

"""
¿Qué son constantes en Python?
R/ Las constantes son "variables" cuyo valor no debe cambiar durante la ejecución del programa.
"""
# ¿Cómo definir constantes en Python?
PI = 3.14159  # Definición de una constante
GRAVEDAD = 9.81  # Definición de otra constante
print(f"Valor de PI: {PI}")
print(f"Valor de la gravedad: {GRAVEDAD}")

"""
¿Qué es una cadena de texto en Python?
R/ Una cadena de texto es una secuencia de caracteres encerrada entre comillas simples (' ') o dobles (" ").
"""

# ¿Cómo definir una cadena de texto en Python?
mi_cadena = "Hola, mundo!" # Definición de una cadena de texto
print(mi_cadena)

# ¿Cómo definir una cadena de texto multilínea en Python?
mi_cadena_multilinea = """Esta es una cadena
de texto que abarca
múltiples líneas.""" # Definición de una cadena de texto multilínea
print(mi_cadena_multilinea)

"""
¿Qué es una lista mutable en Python?
R/ Una lista mutable es una colección ordenada de elementos que pueden ser modificados (agregados, eliminados o cambiados)
después de su creación.
"""

# ¿Cómo definir listas mutables en Python?
mi_lista = [1, 2, 3, 4, 5]  # Definición de una lista mutable
print(mi_lista)

# ¿Cómo visualizar listas mutables en Python?
print("Lista completa:", mi_lista)

# ¿Cómo acceder a elementos específicos de una lista en Python?
print("Primer elemento:", mi_lista[0])  # Acceder al primer elemento
print("Último elemento:", mi_lista[-1])  # Acceder al último elemento
print("Elementos del índice 1 al 3:", mi_lista[1:4])  # Acceder a un rango de elementos
print("Elementos desde el índice 2 hasta el final:", mi_lista[2:])  # Acceder desde un índice hasta el final
print("Elementos desde el inicio hasta el índice 3:", mi_lista[:4]) # Acceder desde el inicio hasta un índice
print("Elementos con paso/salto de 2:", mi_lista[::2])  # Acceder a elementos con un paso/saltp específico

# ¿Cómo modificar elementos específicos de una lista en Python?
mi_lista[0] = 10  # Modificar el primer elemento
mi_lista[-1] = 50  # Modificar el último elemento
print("Lista modificada:", mi_lista)

# ¿Cómo agregar elementos a una lista en Python?
mi_lista.append(6)  # Agregar un elemento al final
mi_lista.insert(2, 15)  # Insertar un elemento en el índice
print("Lista después de agregar elementos:", mi_lista)

# ¿Cómo eliminar elementos de una lista en Python?
mi_lista.remove(15)  # Eliminar un elemento por valor
del mi_lista[0]  # Eliminar un elemento por índice
print("Lista después de eliminar elementos:", mi_lista)

# ¿Cómo ordenar una lista en Python?
mi_lista.sort()  # Ordenar la lista en orden ascendente
print("Lista ordenada:", mi_lista)

# ¿Cómo invertir el orden de una lista en Python?
mi_lista.reverse()  # Invertir el orden de la lista
print("Lista invertida:", mi_lista)

# ¿Cómo obtener la longitud de una lista en Python?
longitud_lista = len(mi_lista)  # Obtener la longitud de la lista
print("Longitud de la lista:", longitud_lista)

# ¿Cómo verificar si un elemento está en una lista en Python?
elemento = 3  # Elemento a verificar
if elemento in mi_lista:
    print(f"El elemento {elemento} está en la lista.")
else:
    print(f"El elemento {elemento} no está en la lista.")

# ¿Cómo contar cuántas veces aparece un elemento en una lista en Python?
contador = mi_lista.count(3)  # Contar cuántas veces aparece el elemento
print(f"El elemento {elemento} aparece {contador} veces en la lista.")

# ¿Cómo obtener el índice de un elemento en una lista en Python?
indice = mi_lista.index(3)  # Obtener el índice del primer elemento encontrado
print(f"El elemento {elemento} se encuentra en el índice {indice} de la lista.")

# ¿Cómo concatenar dos listas en Python?
otra_lista = [7, 8, 9]
lista_concatenada = mi_lista + otra_lista  # Concatenar dos listas
print("Lista concatenada:", lista_concatenada)

# ¿Cómo repetir una lista en Python?
lista_repetida = mi_lista * 2  # Repetir la lista dos veces
print("Lista repetida:", lista_repetida)

# ¿Cómo convertir una cadena de texto en una lista en Python?
cadena_a_lista = list(mi_cadena)  # Convertir una cadena de texto en una lista de caracteres
print("Cadena convertida a lista:", cadena_a_lista)

# ¿Cómo convertir una lista en una cadena de texto en Python?
mi_lista = ['H', 'o', 'l', 'a']  # Definir una lista de caracteres
lista_a_cadena = ''.join(mi_lista)  # Convertir una lista de caracteres en una cadena de texto
print("Lista convertida a cadena:", lista_a_cadena)

# ¿Cómo copiar una lista en Python?
copia_lista = mi_lista.copy()  # Copiar una lista
print("Copia de la lista:", copia_lista)

# ¿Cómo limpiar una lista en Python?
mi_lista.clear()  # Limpiar todos los elementos de la lista
print("Lista después de limpiar:", mi_lista)

# ¿Cómo verificar si una lista está vacía en Python?
if not mi_lista:
    print("La lista está vacía.")
else:
    print("La lista no está vacía.")

# ¿Cómo crear una lista de listas en Python?
lista_de_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Crear una lista de listas
print("Lista de listas:", lista_de_listas)

# ¿Cómo acceder a elementos de una lista de listas en Python?
print("Primer elemento de la primera lista:", lista_de_listas[0][0])
print("Segundo elemento de la segunda lista:", lista_de_listas[1][1])

# ¿Cómo desempaquetar una lista en Python?
a, b, c, d, e = lista_concatenada[:5]  # Desempaquetar una lista en variables
print("Elementos desempaquetados:", a, b, c, d, e)

# ¿Cómo desempaquetar una lista de listas en Python?
primera_lista, segunda_lista, tercera_lista = lista_de_listas  # Desempaquetar una lista de listas
print("Listas desempaquetadas:", primera_lista, segunda_lista, tercera_lista)

# ¿Cómo desempaquetar con el operador * en Python?
primero, *resto = lista_concatenada  # Desempaquetar con el operador *
print("Primer elemento:", primero)
print("Resto de elementos:", resto)

"""
¿Qué es una tupla en Python?
R/ Una tupla es una colección ordenada de elementos que no pueden ser modificados (inmutables) después de su creación.
"""

# ¿Cómo definir tuplas en Python?
mi_tupla = (1, 2, 3, 4, 5)
print("Tupla:", mi_tupla)

# ¿Cómo acceder a elementos específicos de una tupla en Python?
print("Primer elemento de la tupla:", mi_tupla[0])  # Acceder al primer elemento
print("Último elemento de la tupla:", mi_tupla[-1])  # Acceder al último elemento
print("Elementos del índice 1 al 3:", mi_tupla[1:4])  # Acceder a un rango de elementos
print("Elementos desde el índice 2 hasta el final:", mi_tupla[2:])  # Acceder desde un índice hasta el final
print("Elementos desde el inicio hasta el índice 3:", mi_tupla[:4])  # Acceder desde el inicio hasta un índice
print("Elementos con paso/salto de 2:", mi_tupla[::2])  # Acceder a elementos con un paso/salto específico

# ¿Cómo contar cuántas veces aparece un elemento en una tupla en Python?
contador_tupla = mi_tupla.count(3)  # Contar cuántas veces aparece el elemento
print(f"El elemento 3 aparece {contador_tupla} veces en la tupla.")

# ¿Cómo obtener el índice de un elemento en una tupla en Python?
indice_tupla = mi_tupla.index(3)  # Obtener el índice del primer elemento encontrado
print(f"El elemento 3 se encuentra en el índice {indice_tupla} de la tupla.")

# ¿Cómo convertir una tupla en una lista en Python?
tupla_a_lista = list(mi_tupla)  # Convertir una tupla en una lista
print("Tupla convertida a lista:", tupla_a_lista)

# ¿Cómo convertir una lista en una tupla en Python?
lista_a_tupla = tuple(tupla_a_lista)  # Convertir una lista en una tupla
print("Lista convertida a tupla:", lista_a_tupla)

# ¿Cómo verificar si un elemento está en una tupla en Python?
elemento_tupla = 3  # Elemento a verificar
if elemento_tupla in mi_tupla:
    print(f"El elemento {elemento_tupla} está en la tupla.")
else:
    print(f"El elemento {elemento_tupla} no está en la tupla.")

# ¿Cómo obtener la longitud de una tupla en Python?
longitud_tupla = len(mi_tupla)  # Obtener la longitud de la tupla
print("Longitud de la tupla:", longitud_tupla)

# ¿Cómo concatenar dos tuplas en Python?
otra_tupla = (6, 7, 8)  # Definir otra tupla
tupla_concatenada = mi_tupla + otra_tupla  # Concatenar dos tuplas
print("Tupla concatenada:", tupla_concatenada)

# ¿Cómo repetir una tupla en Python?
tupla_repetida = mi_tupla * 2  # Repetir la tupla dos veces
print("Tupla repetida:", tupla_repetida)

# ¿Cómo verificar si una tupla está vacía en Python?
if not mi_tupla:
    print("La tupla está vacía.")
else:
    print("La tupla no está vacía.")

# ¿Cómo limpiar una tupla en Python?
# Las tuplas son inmutables, por lo que no se pueden limpiar.
# Sin embargo, se puede crear una tupla vacía.
tupla_vacia = ()  # Crear una tupla vacía
print("Tupla vacía:", tupla_vacia)

# ¿Cómo crear una tupla de un solo elemento en Python?
tupla_un_elemento = (42,)  # Crear una tupla de un solo elemento
print("Tupla de un solo elemento:", tupla_un_elemento)

# ¿Cómo crear una tupla de tuplas en Python?
tupla_de_tuplas = ((1, 2), (3, 4),
                    (5, 6))  # Crear una tupla de tuplas
print("Tupla de tuplas:", tupla_de_tuplas)

# ¿Cómo acceder a elementos de una tupla de tuplas en Python?
print("Primer elemento de la primera tupla:", tupla_de_tuplas[0][0])
print("Segundo elemento de la segunda tupla:", tupla_de_tuplas[1][1])

# ¿Cómo desempaquetar una tupla en Python?
a, b, c, d, e = mi_tupla  # Desempaquetar una tupla en variables
print("Elementos desempaquetados:", a, b, c, d, e)

# ¿Cómo desempaquetar una tupla de tuplas en Python?
(tupla1, tupla2, tupla3) = tupla_de_tuplas  # Desempaquetar una tupla de tuplas
print("Tuplas desempaquetadas:", tupla1, tupla2, tupla3)

# ¿Cómo desempaquetar con el operador * en Python?
primero_tupla, *resto_tupla = tupla_concatenada  # Desempaquetar con el operador *
print("Primer elemento de la tupla:", primero_tupla)
print("Resto de elementos de la tupla:", resto_tupla)

"""
¿Qué es un conjunto en Python?
R/ Un conjunto es una colección no ordenada de elementos únicos (sin duplicados).
"""

# ¿Cómo definir conjuntos en Python?
mi_conjunto = {1, 2, 3, 4, 5}
print("Conjunto:", mi_conjunto)

# ¿Cómo definir un conjunto vacío en Python?
conjunto_vacio = set()  # Crear un conjunto vacío
print("Conjunto vacío:", conjunto_vacio)

# ¿Cómo definir un conjunto a partir de una lista en Python?
lista_para_conjunto = [1, 2, 2, 3, 4, 4, 5]  # Lista con duplicados
conjunto_desde_lista = set(lista_para_conjunto)  # Crear un conjunto a partir de una lista
print("Conjunto desde lista:", conjunto_desde_lista)

# ¿Cómo definir un conjunto a partir de una cadena de texto en Python?
cadena_para_conjunto = "hello"  # Cadena de texto
conjunto_desde_cadena = set(cadena_para_conjunto)  # Crear un conjunto
print("Conjunto desde cadena:", conjunto_desde_cadena)

# ¿Cómo agregar elementos a un conjunto en Python?
mi_conjunto.add(6)  # Agregar un elemento al conjunto
mi_conjunto.update([7, 8, 9])  # Agregar múltiples elementos
print("Conjunto después de agregar elementos:", mi_conjunto)

# ¿Cómo eliminar elementos de un conjunto en Python?
mi_conjunto.remove(3)  # Eliminar un elemento (genera error si no existe)
mi_conjunto.discard(10)  # Eliminar un elemento (no genera error si no existe)
eliminado = mi_conjunto.pop()  # Eliminar y devolver un elemento aleatorio
print(f"Elemento eliminado: {eliminado}")
print("Conjunto después de eliminar elementos:", mi_conjunto)

# ¿Cómo limpiar un conjunto en Python?
mi_conjunto.clear()  # Limpiar todos los elementos del conjunto
print("Conjunto después de limpiar:", mi_conjunto)

# ¿Cómo verificar si un elemento está en un conjunto en Python?
mi_conjunto = {1, 2, 3, 4, 5}  # Definir un conjunto
elemento_conjunto = 3  # Elemento a verificar
if elemento_conjunto in mi_conjunto:
    print(f"El elemento {elemento_conjunto} está en el conjunto.")
else:
    print(f"El elemento {elemento_conjunto} no está en el conjunto.")

# ¿Cómo obtener la longitud de un conjunto en Python?
longitud_conjunto = len(mi_conjunto)  # Obtener la longitud del conjunto
print("Longitud del conjunto:", longitud_conjunto)

# ¿Cómo realizar operaciones de conjuntos en Python?
conjunto_a = {1, 2, 3, 4, 5}  # Definir un conjunto
conjunto_b = {4, 5, 6, 7, 8}  # Definir otro conjunto

# Unión
union = conjunto_a | conjunto_b  # Unión de dos conjuntos
print("Unión:", union)

# Intersección
interseccion = conjunto_a & conjunto_b  # Intersección de dos conjuntos
print("Intersección:", interseccion)

# Diferencia
diferencia = conjunto_a - conjunto_b  # Diferencia de dos conjuntos
print("Diferencia (A - B):", diferencia)

# Diferencia simétrica
diferencia_simetrica = conjunto_a ^ conjunto_b  # Diferencia simétrica de dos conjuntos
print("Diferencia simétrica:", diferencia_simetrica)

# ¿Cómo verificar si un conjunto es subconjunto o superconjunto de otro en Python?
subconjunto = {1, 2}  # Definir un subconjunto
superconjunto = {1, 2, 3, 4, 5}  # Definir un superconjunto
print("¿subconjunto es subconjunto de conjunto_a?", subconjunto.issubset(conjunto_a))
print("¿conjunto_a es superconjunto de subconjunto?", conjunto_a.issuperset(subconjunto))

# ¿Cómo copiar un conjunto en Python?
copia_conjunto = mi_conjunto.copy()  # Copiar un conjunto
print("Copia del conjunto:", copia_conjunto)

# ¿Cómo convertir una lista en un conjunto en Python?
lista_para_conjunto2 = [1, 2, 2, 3, 4, 4, 5]  # Lista con duplicados
conjunto_desde_lista2 = set(lista_para_conjunto2)  # Convertir una lista en un conjunto
print("Conjunto desde lista 2:", conjunto_desde_lista2)

# ¿Cómo convertir una cadena de texto en un conjunto en Python?
cadena_para_conjunto2 = "banana"
conjunto_desde_cadena2 = set(cadena_para_conjunto2)  # Convert
print("Conjunto desde cadena 2:", conjunto_desde_cadena2)

# ¿Cómo convertir un conjunto en una lista en Python?
conjunto_a_lista = list(mi_conjunto)  # Convertir un conjunto en una lista
print("Conjunto convertido a lista:", conjunto_a_lista)

# ¿Cómo convertir un conjunto en una cadena de texto en Python?
conjunto_a_cadena = ''.join(map(str, mi_conjunto))  # Convertir
print("Conjunto convertido a cadena:", conjunto_a_cadena)

# ¿Cómo crear un conjunto inmutable en Python?
conjunto_inmutable = frozenset([1, 2, 3, 4, 5])  # Crear un conjunto inmutable
print("Conjunto inmutable:", conjunto_inmutable)

# ¿Cómo verificar si un conjunto inmutable es subconjunto o superconjunto de otro en
print("¿conjunto_inmutable es subconjunto de conjunto_a?", conjunto_inmutable.issubset(conjunto_a))
print("¿conjunto_a es superconjunto de conjunto_inmutable?", conjunto_a.issuperset(conjunto_inmutable))

# ¿Cómo realizar operaciones de conjuntos con conjuntos inmutables en Python?
# Unión
union_inmutable = conjunto_inmutable | conjunto_a  # Unión con conjunto inmutable
print("Unión con conjunto inmutable:", union_inmutable)

# Intersección
interseccion_inmutable = conjunto_inmutable & conjunto_a  # Intersección con conjunto inmutable
print("Intersección con conjunto inmutable:", interseccion_inmutable)

# Diferencia
diferencia_inmutable = conjunto_inmutable - conjunto_a  # Diferencia con conjunto inmutable
print("Diferencia (inmutable - A):", diferencia_inmutable)

# Diferencia simétrica
diferencia_simetrica_inmutable = conjunto_inmutable ^ conjunto_a  # Diferencia simétrica con conjunto inmutable
print("Diferencia simétrica con conjunto inmutable:", diferencia_simetrica_inmutable)

"""
¿Qué es un diccionario en Python?
R/ Un diccionario es una colección no ordenada de pares clave-valor, donde cada
clave es única y se utiliza para acceder a su valor asociado.
"""

# ¿Cómo definir diccionarios en Python?
mi_diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}  # Definición de un diccionario
print("Diccionario:", mi_diccionario)

# ¿Cómo acceder a valores específicos de un diccionario en Python?
print("Nombre:", mi_diccionario["nombre"])  # Acceder al valor de la clave
print("Edad:", mi_diccionario["edad"])  # Acceder al valor de otra clave
print("Ciudad:", mi_diccionario["ciudad"])  # Acceder al valor de otra

# clave
# ¿Cómo agregar o modificar valores en un diccionario en Python?
mi_diccionario["edad"] = 31  # Modificar el valor de una clave existente
mi_diccionario["pais"] = "España"  # Agregar una nueva clave-valor
print("Diccionario después de agregar/modificar:", mi_diccionario)

# ¿Cómo eliminar claves y valores de un diccionario en Python?
del mi_diccionario["ciudad"]  # Eliminar una clave y su valor asociado
mi_diccionario.pop("pais")  # Eliminar una clave y su valor asociado (genera error si no existe)
print("Diccionario después de eliminar claves:", mi_diccionario)

# ¿Cómo limpiar un diccionario en Python?
mi_diccionario.clear()  # Limpiar todos los pares clave-valor del diccionario
print("Diccionario después de limpiar:", mi_diccionario)

# ¿Cómo verificar si una clave está en un diccionario en Python?
mi_diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}  # Definir un diccionario
clave = "edad"  # Clave a verificar

if clave in mi_diccionario:
    print(f"La clave '{clave}' está en el diccionario.")
else:
    print(f"La clave '{clave}' no está en el diccionario.")

# ¿Cómo obtener la longitud de un diccionario en Python?
longitud_diccionario = len(mi_diccionario)  # Obtener la longitud del diccionario
print("Longitud del diccionario:", longitud_diccionario)

# ¿Cómo obtener todas las claves de un diccionario en Python?
claves = mi_diccionario.keys()  # Obtener todas las claves del diccionario
print("Claves del diccionario:", claves)

# ¿Cómo obtener todos los valores de un diccionario en Python?
valores = mi_diccionario.values()  # Obtener todos los valores del diccionario
print("Valores del diccionario:", valores)

# ¿Cómo obtener todos los pares clave-valor de un diccionario en Python?
pares_clave_valor = mi_diccionario.items()  # Obtener todos los pares clave-valor del diccionario
print("Pares clave-valor del diccionario:", pares_clave_valor)

# ¿Cómo copiar un diccionario en Python?
copia_diccionario = mi_diccionario.copy()  # Copiar un diccionario
print("Copia del diccionario:", copia_diccionario)
# ¿Cómo convertir una lista de tuplas en un diccionario en Python?

lista_de_tuplas = [("nombre", "Ana"), ("edad", 25), ("ciudad", "Barcelona")]  # Lista de tuplas
diccionario_desde_lista = dict(lista_de_tuplas)  # Convertir una lista de tuplas en un diccionario
print("Diccionario desde lista de tuplas:", diccionario_desde_lista)

# ¿Cómo convertir dos listas en un diccionario en Python?
claves_lista = ["nombre", "edad", "ciudad"]  # Lista de claves
valores_lista = ["Luis", 28, "Valencia"]  # Lista de valores
diccionario_desde_listas = dict(zip(claves_lista, valores_lista))  # Convertir dos listas en un diccionario
print("Diccionario desde dos listas:", diccionario_desde_listas)
