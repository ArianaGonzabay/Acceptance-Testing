from behave import given, when, then
from todo_list import TodoList

# Nuevo paso: Define el estado inicial (lista vacía)
@given('the to-do list is empty')
def step_impl(context):
    # Inicializa o limpia la lista para un estado inicial vacío
    if not hasattr(context, 'todo_list'):
        context.todo_list = TodoList()
    context.todo_list.clear()

# Paso existente: Ahora es la única definición de este 'Given'
@given('the to-do list contains tasks:')
def step_impl(context):
    # 1. Asegura que el objeto de la lista exista
    if not hasattr(context, 'todo_list'):
        context.todo_list = TodoList()

    # 2. Limpia la lista para empezar de nuevo
    context.todo_list.clear() 

    # 3. Procesa los datos de la tabla
    for row in context.table:
        # Obtiene el título de la tarea
        title = row.get("Task") or row.get("task")
        
        # Opcionalmente, puedes manejar el estado si lo implementas
        # status = row.get("Status") or row.get("status")

        if title:
            context.todo_list.add_task(title) 
            # if status and status.lower() in ("completed", "complete"):
            #     context.todo_list.mark_completed(title)


@when('the user adds a task "{task_name}"')
def step_impl(context, task_name):
    # Asegúrate de que la lista exista antes de usarla
    if not hasattr(context, 'todo_list'):
        context.todo_list = TodoList()
        
    context.todo_list.add_task(task_name)

@then('the to-do list should contain "{task_name}"')
def step_impl(context, task_name):
    tasks = context.todo_list.get_all_tasks()
    task_names = [task.description for task in tasks]
    assert task_name in task_names, f"Task '{task_name}' not found in the list."


@when('the user clears the to-do list')
def step_impl(context):
    """
    Llama al método de tu aplicación para limpiar toda la lista.
    """
    context.todo_list.clear()

@then('the to-do list should be empty')
def step_impl(context):
    """
    Verifica que la lista de tareas en tu aplicación no contenga elementos.
    """
    tasks = context.todo_list.get_all_tasks()
    assert len(tasks) == 0, f"Expected 0 tasks, but found {len(tasks)}"


# Paso corregido: Usando context.todo_list en lugar de context.todo
@when('the user lists all tasks')
def step_impl(context):
    # CORRECCIÓN: Usar context.todo_list
    tasks = context.todo_list.get_all_tasks() 
    
    # Formato como se espera en el archivo feature:
    output = "Tasks:\n"
    for task in tasks:
        # Asume que task.description es el nombre de la tarea
        output += f" - {task.description}\n"
        
    context.last_output = output.strip()
    
@then('the output should contain:')
def step_impl(context):
    expected = context.text.strip()
    actual = context.last_output or ""
    assert expected in actual, f"Expected block not in output.\nExpected:\n{expected}\n\nActual:\n{actual}"