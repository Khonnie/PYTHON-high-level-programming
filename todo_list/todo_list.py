todo_list = []
def Add_Task():
  Task = input('what tasks do you plan to do?')
  todo_list.append(Task)
  print('Task Added')
def View_Task():
    if not todo_list: #if todo_list = []
      print('The list is empty')
    else:
      print('Your Tasks')
      for Task in todo_list:
        print(f'{Task}')
while True:
  print('1. Add Task')
  print('2. View Task')
  print('3. Exit')
  user_choice = input ('what do you want to do? :')
  if user_choice == '1':
    Add_Task()
  elif user_choice == '2':
    View_Task()
  elif user_choice == '3':
    print('Good Bye!')
    break
  else:
    print('Invalid Choice')
