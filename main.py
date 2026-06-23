from utils.todo import ToDoList
import subprocess
import os

def clear_console():
    subprocess.run(
        "cls" if os.name == "nt" else "clear",
        shell=True
    )

my_todo = ToDoList()

if __name__ == "__main__":
    while True:
        clear_console()
        ToDoList.show()
        value = input()

        match value:
            case "1":
                my_todo.add(input("\nenter a task : "))
            case "2":
                my_todo.delete(input("\nenter the task : "))
            case "3":
                my_todo.get_all()
            case "4":
                break
            case _:
                print("Try Again !!!")
        
        input("\nPress Enter to continue...")
