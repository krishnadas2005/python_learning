# TO-DO list application

lists = []

def add_tasks():
    task = input("enter the task you want to add into the list: ")
    lists.append(task)
    print(f'your task {task} is added to the list ')

def remove_task():
    show_tasks()
    try:
        task_num = int(input("Enter the number of the task you want to remove: "))
        removed_task=lists.pop(task_num - 1)
        print(f'the task {removed_task} is removed sucessfully.')
    except(IndexError, ValueError):
         print("the input you typed is invalid try again!")

        
def show_tasks():
                if not lists:
                    print("your list  is empty. add task")
                else:
                    print("here is your to-do list")
                    for i, task in enumerate(lists, start=1):
                         print(i, task)

def main():
    while True:
        options = int(input(" options: 1.add tasks 2.remove task 3.show task 4 exit \n Enter the option you want "))
        if options == 1:
            add_tasks()
        elif options == 2:
            remove_task()
        elif options == 3:
            show_tasks()
        elif options == 4:
            print("exiting to-do list bye!....")
            break
        else:
            print("entered input is invaild. try again!")

main()