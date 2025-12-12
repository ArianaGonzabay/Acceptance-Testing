from behave import given, when, then
from todo_list import TodoList

@given('the to-do list is empty')
def step_impl(context):
    context.todo_list = TodoList()
    context.todo_list.clear()

@given('the to-do list contains tasks:')
def step_impl(context):
    context.todo_list = TodoList()
    context.todo_list.clear()
    for row in context.table:
        title = row.get("Task") or row.get("task")
        if title:
            context.todo_list.add_task(title)

@when('the user adds a task "{task_name}"')
def step_impl(context, task_name):
    context.todo_list.add_task(task_name)

@then('the to-do list should contain "{task_name}"')
def step_impl(context, task_name):
    names = [t.description for t in context.todo_list.get_all_tasks()]
    assert task_name in names, f"Expected '{task_name}' but found {names}"

@when('the user clears the to-do list')
def step_impl(context):
    context.todo_list.clear()

@then('the to-do list should be empty')
def step_impl(context):
    assert len(context.todo_list.get_all_tasks()) == 0, "List is not empty"

@when('the user lists all tasks')
def step_impl(context):
    tasks = context.todo_list.get_all_tasks()
    output = "Tasks:\n"
    for t in tasks:
        output += f" - {t.description}\n"
    context.last_output = output.strip()

@then('the output should contain:')
def step_impl(context):
    expected = context.text.strip()
    actual = context.last_output or ""
    assert expected in actual, f"Expected:\n{expected}\nActual:\n{actual}"

@when('the user deletes the task "{task_name}"')
def step_impl(context, task_name):
    deleted = context.todo_list.delete_task(task_name)
    assert deleted, f"Task '{task_name}' could not be deleted"

@then('the to-do list should not contain "{task_name}"')
def step_impl(context, task_name):
    names = [t.description for t in context.todo_list.get_all_tasks()]
    assert task_name not in names, f"Task '{task_name}' still present: {names}"

# -----------------------
# New steps for "mark as completed"
# -----------------------

@when('the user marks task "{task_name}" as completed')
def step_impl(context, task_name):
    """
    Mark task by name: find the task and set its status to 'Completed'.
    (We modify the in-memory object directly so tests remain independent of CLI input formats.)
    """
    tasks = context.todo_list.get_all_tasks()
    for t in tasks:
        if t.description == task_name:
            t.status = "Completed"
            break
    else:
        # If not found, fail the step
        assert False, f"Task '{task_name}' not found to mark as completed"

@then('the to-do list should show task "{task_name}" as completed')
def step_impl(context, task_name):
    tasks = context.todo_list.get_all_tasks()
    for t in tasks:
        if t.description == task_name:
            assert t.status == "Completed", f"Task '{task_name}' status is '{t.status}', expected 'Completed'"
            return
    assert False, f"Task '{task_name}' not found in the list"
