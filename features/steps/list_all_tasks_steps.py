# features/steps/todo_list_steps.py
from behave import given, when, then
from todo_list import TodoList

@given('the to-do list contains tasks:')
def step_impl(context):
    # Context table may be: | Task | or | Task | Status |
    context.todo = TodoList()
    for row in context.table:
        # row is a behave.model.TableRow, accessible by column names
        title = row.get("Task") or row.get("task") or None
        status = row.get("Status") or row.get("status") or None
        if not title:
            continue
        # If status present and is Completed, we add then mark completed
        context.todo.add_task(title)
        if status and status.lower() in ("completed", "complete"):
            context.todo.mark_completed(title)

@when('the user lists all tasks')
def step_impl(context):
    # capture the "output" as multiline string similar to feature expectation
    tasks = context.todo.get_all_tasks()
    # format as in the feature:
    output = "Tasks:\n"
    for task in tasks:
        output += f" - {task.description}\n"
    context.last_output = output.strip()
    
@then('the output should contain:')
def step_impl(context):
    expected = context.text.strip()
    actual = context.last_output or ""
    assert expected in actual, f"Expected block not in output.\nExpected:\n{expected}\n\nActual:\n{actual}"
