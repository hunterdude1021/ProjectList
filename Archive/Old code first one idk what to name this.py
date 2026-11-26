tasks = []

while True:
    print('Your todo list')

    print("1: Add a task")
    print("2: View tasks")
    print("3: Remove a task")

    choice = input('Pick a option')
   
    if choice == "1":
        task = input('Enter a task: ')
        tasks.append(task)
        print('Task added')

    elif choice == "2":
        print('Your tasks:')
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")

    elif choice == "3":
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

        task_number = int(input('Enter the number of the task to remove: '))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f'Task "{removed_task}" removed')
        else:
            print('Invalid')