Feature: To Do List Manager

  @add_task 
  Scenario: Add a task to the to-do list
    Given the to-do list is empty
    When the user adds a task "Buy groceries"
    Then the to-do list should contain "Buy groceries"

  @clear_all_tasks
  Scenario: Clear the entire to-do list
    Given the to-do list contains tasks:
      | Task |
      | Buy groceries |
      | Pay bills |
    When the user clears the to-do list
    Then the to-do list should be empty

  @list_tasks
  Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks:
      | Task |
      | Buy groceries |
      | Pay bills |
    When the user lists all tasks
    Then the output should contain:
      """
      Tasks:
       - Buy groceries
       - Pay bills
      """
  @delete_task
  Scenario: Delete a task from the to-do list
    Given the to-do list contains tasks:
      | Task |
      | Buy groceries |
      | Pay bills |
    When the user deletes the task "Pay bills"
    Then the to-do list should not contain "Pay bills"

  @mark_task
  Scenario: Mark a task as completed
    Given the to-do list contains tasks:
      | Task |
      | Buy groceries |
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show task "Buy groceries" as completed
