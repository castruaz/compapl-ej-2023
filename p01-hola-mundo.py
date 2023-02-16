# Lee datos y envia un saludo

# Entrada
print('Leyendo datos y enviando un saludo:\n')
nombre = input('Dame tu nombre ? ') # aqui se lee una cadena
edad = int(input('Dame la edad ? '))
peso = float(input('Dame el peso ? '))

# Salida
print(f'{nombre} bienvenido a python, tu edad es {edad}, tu peso es {peso}')
print(type(nombre)) # aqui se muestra el tipo de dato de la variable
print(type(edad))
print(type(peso))

