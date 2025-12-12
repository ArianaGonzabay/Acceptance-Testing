# To-Do List Manager (Behave BDD) --- Proyecto de Acceptance Testing

El **To-Do List Manager** es una aplicación de línea de comandos que
permite al usuario gestionar tareas (añadir, listar, completar, eliminar
y limpiar).\
Este proyecto sirve como base para realizar **pruebas de aceptación**
utilizando **BDD con Behave**.

Se implementan los 5 requerimientos principales: 
1. Agregar tareas\
2. Listar tareas\
3. Marcar como completadas\
4. Limpiar la lista\
5. **Eliminar una tarea específica** (feature adicional)

------------------------------------------------------------------------

## Estructura del Proyecto

    todo_list.py          # Lógica principal del To-Do List
    features/
        todo_list.feature # Escenarios BDD (Gherkin)
        steps/
            todo_list_steps.py  # Implementación de steps para Behave
    README.md

------------------------------------------------------------------------

# 🛠 Requisitos

-   Python 3.x\

-   pip\

-   Librerías:

    ``` bash
    pip install behave
    ```

------------------------------------------------------------------------

# ▶️ Ejecutar la Aplicación

Puedes interactuar con la aplicación en modo consola:

``` bash
python todo_list.py
```

------------------------------------------------------------------------

# 🧪 Ejecutar Pruebas de Aceptación (Behave)

Desde la raíz del proyecto:

``` bash
behave
```
