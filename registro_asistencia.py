"""
REGISTRO DE ASISTENCIA
Contexto: Crear un sistema que registre y lea la asistencia de una clase. El sistema trabajará con un archivo.txt.

Instrucciones:
    • Crear un archivo asistencia.txt y registrar nombres de estudiantes que asistieron.
    • Leer el archivo y mostrar la lista de estudiantes en consola.
    • Agregar funcionalidad para eliminar el archivo de asistencia al final del día.
"""

# Escribir en el archivo
with open('asistencia.txt', 'w') as archivo:
    while True:
        nombre = input('Ingresa el nombre del estudiante que ha asistido a clase (o escribe "Fin" para terminar): ').capitalize()
        if nombre == 'Fin':
            break
        archivo.write(f'{nombre}\n')
        
# Leer el archivo
print(f'\nLista de asistencia: ')
with open('asistencia.txt', 'r') as archivo:
    for linea in archivo:
        print(f'{linea.strip()}')
        
# Eliminar el archivo
respuesta = input('\n¿Deseas eliminar el archivo? [S/N]: ').capitalize()
if respuesta == 'S':
    import os
    os.remove('asistencia.txt')
    print('¡EL archivo ha sido eliminado exitosamente!')
else:
    print('Archivo guardado.')