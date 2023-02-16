# Calcular el area de un triángulo

print('Calcular el area de un triángulo:\n')
print('Dame la base y la altura separados por Enter:')
base, altura = int(input()), int(input()) # aqui se leen dos datos en una sola linea, hay que dar enter entre cada uno

area = ( base * altura ) / 2

print(f'El triángulo de base {base} y altura {altura} tiene un area de {area}')
