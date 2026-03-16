import os
# os.mkdir('todolist')
# if os.path.exists('todolist'):
#     print('To-Do List directory already exists.')
# f= open('todolist/Monday.txt','x')
# if os.path.exists('todolist/Monday.txt'):
#     print('Monday To-Do List already exists.')
# f= open('todolist/Tuesday.txt', 'x')
# if os.path.exists('todolist/Tuesday.txt'):
#     print('Tuesday To-Do List already exists.')
# f= open('todolist/Wednesday.txt', 'x')
# if os.path.exists('todolist/Wednesday.txt'):
#     print('Wednesday To-Do List already exists.')
# f= open('todolist/Thursday.txt', 'x')
# if os.path.exists('todolist/Thursday.txt'):
#     print('Thursday To-Do List already exists.')
# f= open('todolist/Friday.txt', 'x')
# if os.path.exists('todolist/Friday.txt'):
#     print('Friday To-Do List already exists.')
# f= open('todolist/Saturday.txt', 'x')
# if os.path.exists('todolist/Saturday.txt'):
#     print('Saturday To-Do List already exists.')
# f= open('todolist/Sunday.txt', 'x')
# if os.path.exists('todolist/Sunday.txt'):
#     print('Sunday To-Do List already exists.')






    
def main():
    
 match day:
    case 'monday':
        with open('todolist/Monday.txt', 'w') as f:
            while True:
                task= input('Enter a task for Monday (or type "done" to finish): ')
                if task.lower() == 'done':
                    break
                f.write(task + '\n')
                print('Task added to Monday To-Do List.')
    case 'tuesday':
        with open('todolist/Tuesday.txt', 'w') as f:
            while True:
                task= input('Enter a task for Tuesday (or type "done" to finish): ')
                if task.lower() == 'done':
                    break
                f.write(task + '\n')
                print('Task added to Tuesday To-Do List.')

    case 'wednesday':
        with open('todolist/Wednesday.txt', 'w') as f:
            while True:
                task= input('Enter a task for Wednesday (or type "done" to finish): ')
                if task.lower() == 'done':
                    break
                f.write(task + '\n')
                print('Task added to Wednesday To-Do List.')
    case 'thursday':
        with open('todolist/Thursday.txt', 'w') as f:       
            while True:
                task= input('Enter a task for Thursday (or type "done" to finish): ')
                if task.lower() == 'done':
                    break
                f.write(task + '\n')
                print('Task added to Thursday To-Do List.')
    case 'friday':
        with open('todolist/Friday.txt', 'w') as f:
            while True:
                task= input('Enter a task for Friday (or type "done" to finish): ')
                if task.lower() == 'done':
                    break
                f.write(task + '\n')
                print('Task added to Friday To-Do List.')
    case 'saturday':
        with open('todolist/Saturday.txt', 'w') as f:
            while True:
                task= input('Enter a task for Saturday (or type "done" to finish): ')
                if task.lower() == 'done':
                    break
                f.write(task + '\n')
                print('Task added to Saturday To-Do List.')
    case 'sunday':
        with open('todolist/Sunday.txt', 'w') as f:
            while True:
                task= input('Enter a task for Sunday (or type "done" to finish): ')
                if task.lower() == 'done':
                    break
                f.write(task + '\n')
                print('Task added to Sunday To-Do List.')
    case _:
        print('Invalid day. Please enter a day between Monday and Sunday.')


def view():
    match dway:
        case 'monday':
            with open('todolist/Monday.txt', 'r') as f:
                tasks= f.read()
            print('Monday To-Do List:')
            print(tasks)
        case 'tuesday':
            with open('todolist/Tuesday.txt', 'r') as f:
                 tasks= f.read()
            print('Tuesday To-Do List:')
            print(tasks)
        case 'wednesday':
            with open('todolist/Wednesday.txt', 'r') as f:
                tasks= f.read()
            print('Wednesday To-Do List:')
            print(tasks)
        case 'thursday':
            with open('todolist/Thursday.txt', 'r') as f:
                tasks= f.read()
            print('Thursday To-Do List:')
            print(tasks)
        case 'friday':
            with open('todolist/Friday.txt', 'r') as f:
                 tasks= f.read()
            print('Friday To-Do List:')
            print(tasks)
        case 'saturday':
            with open('todolist/Saturday.txt', 'r') as f:
               tasks= f.read()
            print('Saturday To-Do List:')
            print(tasks)
        case 'sunday':
            with open('todolist/Sunday.txt', 'r') as f:
             tasks= f.read()
            print('Sunday To-Do List:')
            print(tasks)
        case _:
            print('Invalid day. Please enter a day between Monday and Sunday.')


    print('Have you completed all the tasks on your To-Do List? (yes/no) ')
    if input().lower() == 'yes':
            with open(dway + '.txt', "r+") as f:
             f.seek(0)
            f.truncate()
            print('tasks cleared from To-Do List.')
            print('Congratulations on completing your tasks! Keep up the good work!')


    elif input().lower() == 'no':
            print('Keep working on your tasks! You can do it!')
    else:
             print('Invalid choice. Please enter "yes" or "no".')

def inputday():
    valid_days = [
        "monday", "tuesday", "wednesday", "thursday", 
        "friday", "saturday", "sunday"
    ]
    answer=True
    while answer:
   
        user_input = input("Please enter a day of the week: ").strip().lower()
        
        if user_input in valid_days:
            answer=False
            return user_input
        else:
            print(f"'{user_input}' is not a valid day. Please check your spelling.")



print('Welcome to your To-Do List!')
work= True  
while work:
   print('What would you like to do?')
   print('1. Create a new To-Do List')
   print('2. View an existing To-Do List')
   print('3. Edit a To-Do List')
   print('4. Exit')
   choice= input('Enter your choice (1-4): ')
   if choice == '1':
          day= inputday()
          main()
   elif choice == '2':
        dway= inputday()
        view()
   elif choice == '3':
        day= inputday()
        main()
   elif choice == '4':
        print('Goodbye!')
        work= False