
class ToDoList:

    def add(self, task):
        f = open("myfile.txt", "a")
        f.write(f"{task}\n")
        f.close()

    def get_all(self):
        f = open("myfile.txt", "r")
        my_list = [line.strip() for line in f]
        print("\ntask:")
        for item in my_list:
            print(item)
    
    def delete(self, item):
        with open("myfile.txt", "r") as f:
            my_list = [line.strip() for line in f]

        if item in my_list:
            my_list.remove(item)

        with open("myfile.txt", "w") as f:
            for line in my_list:
                f.write(line + "\n")


    @staticmethod
    def show():
        print("1)add task")
        print("2)delete task")
        print("3)print all tasks")
        print("4)exit")