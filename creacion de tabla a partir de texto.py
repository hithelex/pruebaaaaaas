from tabulate import tabulate
import pandas as pd

num_datos = int(input("cantidad de datos a ingresar?"))

datos = []
for i in range(num_datos):
    dato = input(f"ingrese el dato, {i+1}: ")
    datos.append(dato)
#print(datos)
arc_salida = "B_test_usuario.txt"
cant_columnas = int(input("cantidad de comlumnas: "))
grupos = [datos[i:i+cant_columnas]for i in range(0,len(datos), cant_columnas)]
columna = [f'columna {i+1}' for i in range(cant_columnas)]
fila = [f'fila {i+1}' for i in range(len(grupos))]
df = pd.DataFrame(grupos, columns=columna, index=fila)
tabla_final = tabulate(df, headers='keys', tablefmt='pretty',showindex=True)

with open(arc_salida,"w",encoding='utf-8') as file:
    file.write(tabla_final + '\n')

