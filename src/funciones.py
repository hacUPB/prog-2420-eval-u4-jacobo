import os
import csv
import matplotlib.pyplot as plt

def listar_archivos(ruta):
    archivos = []
    carpetas = []
    try:# el código capturar cualquier error que se produzca para que el programa pueda manejarlo sin detenerse de forma abrupta.
        elementos = os.listdir(ruta) #revisa la totalidad de elemntos de la ruta
        for elemento in elementos: #itera cada elemnto de la lista
            ruta_completa=os.path.join(ruta,elemento) # crea una ruta completa incluyendo el elemento (ruta\primer_elemento)
            verificador_carpeta=os.path.isdir(ruta_completa)#realiza una verificacion de si es una carpeta manda true (os.path.isfile()este revisa si es archivo)
            if verificador_carpeta==True:
                carpetas.append(elemento)
            elif verificador_carpeta==False:
                archivos.append(elemento)
            
        print(f"Carpetas en la ruta '{ruta}':")
        for carpeta in carpetas:
            print(f" - {carpeta}")
            
        print(f"\nArchivos en la ruta '{ruta}':")
        for archivo in archivos:
            print(f" - {archivo}")
    except FileNotFoundError: #excepción en Python que se produce cuando intentas acceder a un archivo o directorio que no existe
            print(f"Error: La ruta '{ruta}' no existe.")
    except PermissionError: #exepcion cuando no se cuenta con los permisos adecuados
            print(f"Error: No tienes permisos para acceder a la ruta '{ruta}'.")

def cont_palabrs (ruta_completa):
    with open(ruta_completa,"r") as file:
        palabras=file.read().split()
        return len(palabras)

def reem_palabra(ruta_archivo, palabra_buscar, palabra_reemplazar):
    with open(ruta_archivo, 'r') as archivo:
        contenido = archivo.read()

    contenido_modificado = contenido.replace(palabra_buscar, palabra_reemplazar)#remplasa la primera palabra con la segunda

    with open(ruta_archivo, 'w') as archivo:
        archivo.write(contenido_modificado)
    print(f"La palabra '{palabra_buscar}' ha sido reemplazada por '{palabra_reemplazar}' en el archivo '{ruta_archivo}'.")

def cont_caracteres_sin(ruta_completa):
    with open(ruta_completa,"r") as file:
        contenido=file.read()
    contenido_mod=contenido.replace(' ','')
    N_caracteres=len(contenido_mod)
    return N_caracteres

def cont_caracteres(ruta_completa):
    with open(ruta_completa,"r") as file:
        contenido=file.read()
    N_caracteres=len(contenido)
    return N_caracteres  

def mostrar_primeras_filas(ruta_archivo):
   with open(ruta_archivo, mode='r') as archivo:
        lector_csv = csv.reader(archivo)
        contador = 0
        for fila in lector_csv:
            print(fila)
            contador += 1 
            if contador == 15:
                break
        

def estadisticas (ruta_archivo, columna):
    with open (ruta_archivo,'r') as archivo:
        leer=csv.DictReader(archivo)
        datos=[]
        for filas in leer:
            datos.append(float(filas[columna]))
    
    num_datos=len(datos)

    prom=sum(datos)/num_datos

    datos_ordenados = sorted(datos) 
    indice=(num_datos//2)
    if num_datos % 2 == 0: 
        mediana = (datos_ordenados[indice-1] + datos_ordenados[indice]) / 2
    else:
        mediana = datos_ordenados[indice]

    maximo = max(datos_ordenados)
    minimo = min(datos_ordenados)

    return num_datos, prom, mediana, maximo, minimo


def graficar_columna(ruta_archivo, columna):
        with open(ruta_archivo, 'r') as archivo:
            lector = csv.DictReader(archivo)
            datos = []
            for fila in lector:
                datos.append(float(fila[columna]))
                
        plt.plot(datos, marker='o')
        plt.xlabel('Índice')
        plt.ylabel(columna)
        plt.title(f'Gráfica de la columna {columna}')
        plt.grid(True)
        plt.show()


