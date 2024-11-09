[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/gzRFP7VK)
# Unidad 
---
## Documentación del proyecto
Nombre:  jacobo restrepo chavez
ID:  000418676
---
A continuación, te muestro un diagrama de flujo que describe el proceso y estructura del código que has compartido. Este diagrama ayudará a visualizar el flujo del programa y entender los diferentes caminos que puede tomar el usuario.

### Diagrama de Flujo para el Código

```plaintext
Inicio
   |
   |-- Mostrar menú principal:
   |     1. Listar archivos
   |     2. Procesar archivo de texto (.txt)
   |     3. Procesar archivo CSV (.csv)
   |     4. Salir
   |
   |-- Entrada: Selección del usuario
       |
       |--- Si selección es "1" (Listar archivos):
       |         |
       |         |-- Submenú:
       |         |       1. Listar archivos en ruta actual
       |         |       2. Ingresar una ruta personalizada
       |         |
       |         |-- Entrada: Selección del usuario
       |                |
       |                |--- Si selección es "1": Ejecutar función listar_archivos() en la ruta actual.
       |                |
       |                |--- Si selección es "2": Solicitar ruta, luego ejecutar listar_archivos(ruta).
       |
       |--- Si selección es "2" (Procesar archivo de texto):
       |         |
       |         |-- Entrada: Ruta del archivo (opcional: usar ruta actual con "*")
       |         |-- Entrada: Nombre del archivo
       |         |
       |         |-- Verificar si archivo existe:
       |               |
       |               |--- Si existe, mostrar submenú de opciones:
       |                       1. Contar palabras
       |                       2. Reemplazar palabras
       |                       3. Contar caracteres
       |               |
       |               |--- Entrada: Selección del usuario
       |                     |
       |                     |--- Si selección es "1": Llamar cont_palabrs()
       |                     |--- Si selección es "2": Llamar reem_palabra()
       |                     |--- Si selección es "3": Llamar cont_caracteres() y cont_caracteres_sin()
       |
       |--- Si selección es "3" (Procesar archivo CSV):
       |         |
       |         |-- Entrada: Ruta del archivo (opcional: usar ruta actual con "*")
       |         |-- Entrada: Nombre del archivo
       |         |
       |         |-- Verificar si archivo existe:
       |               |
       |               |--- Si existe, mostrar submenú de opciones:
       |                       1. Mostrar primeras 15 filas
       |                       2. Calcular estadísticas de una columna
       |                       3. Graficar columna completa
       |               |
       |               |--- Entrada: Selección del usuario
       |                     |
       |                     |--- Si selección es "1": Llamar mostrar_primeras_filas()
       |                     |--- Si selección es "2": Llamar estadisticas()
       |                     |--- Si selección es "3": Llamar graficar_columna()
       |
       |--- Si selección es "4" (Salir): Finalizar el programa.
   Fin
```

### Explicación

- **Nodos de Decisión**: Cada punto donde el programa solicita una entrada del usuario se representa con opciones numéricas, y el flujo continúa en función de la selección.
- **Llamadas de Función**: Cada opción lleva a una llamada de función específica que corresponde a la tarea seleccionada (listar archivos, contar palabras, mostrar filas, etc.).
- **Control de Errores**: En el código, hay controles de excepciones (`FileNotFoundError` y `PermissionError`) para manejar situaciones donde el archivo no existe o el usuario no tiene permisos.

Este flujo simplificado muestra cómo el programa guía al usuario paso a paso y facilita visualizar cómo cada selección afecta el proceso del programa.