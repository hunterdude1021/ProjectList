tasks = []

print('Your todo list')

print("1: Add a task")
print("2: View tasks")
print("3: Remove a task")

choice = input('Pick a option')
   
if choice == "1":
    task = input('Enter a task: ')
    tasks.append(task)
    print('Task added')