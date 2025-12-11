from behave import given, when, then
from todo_list import TodoList

@given('the to-do list is empty')
def step_impl(context):
    context.todo_list = TodoList()
    context.todo_list.clear()

@when('the user adds a task "{task_name}"')
def step_impl(context, task_name):
    context.todo_list.add_task(task_name)

@then('the to-do list should contain "{task_name}"')
def step_impl(context, task_name):
    tasks = context.todo_list.get_all_tasks()
    task_names = [task.description for task in tasks]
    assert task_name in task_names
