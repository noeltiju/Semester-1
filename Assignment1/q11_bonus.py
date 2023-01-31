tasks = []
myfile = open("q11_bonus_file.txt","w") #Opens the fils if it does not exist

def correct_int_input():
    #Goal of this function is to always get an integer output
    val = 0
    while True:
        try:

            val = int(input(""))
            break

        except:
            print("Incorrect input")

    return val

def correct_string_input():
    #Goal of this function is to get a str output
    val = ""
    while True:
        try:

            val = input("").strip()
            if val.isalpha():
                break

        except:
            print("Enter correct input")
    return val

def add_task(task):
    #Adds a task to the file
    tasks.append(task.title())
    myfile.write(task.title()+"\n")

#The goal of this program is to do basic functionalities like a todo app

while True:
    print("Type add , show , edit, complete or exit: ")

    while True:
        ans = correct_string_input().lower()
        if ans in ["add" , "show" , "edit" , "complete" , "exit"]:
            break


    if ans == "add":
        #Runs the function which adds a task to the file
        task = correct_string_input()
        add_task(task)

    elif ans == "show":
        #Displays all the todos to do
        if tasks:
            for i in tasks:
                print(i)
        else:
            print("No tasks added yet!")

    elif ans == "exit":
        print("Have a nice Day!")
        myfile.close()
        break
    
    elif ans == "edit":
        #Edits a todo in the file
        if tasks:
            for i in range(1,len(tasks)+1):
                print(f"{i}. {tasks[i-1]}")

            print("Which task to edit?")
            while True:
                ans = correct_int_input()
                if ans in list(range(1,len(tasks)+1)):
                    break
                
            print("New task?")
            new_task = correct_string_input()
            tasks[ans-1] = new_task

    elif ans == "complete":
        #Completes a particular todo
        if tasks:
            for i in range(1,len(tasks)+1):
                print(f"{i}. {tasks[i-1]}")

            print("Which task to complete?")
            ans = -1
            while True:
                ans = correct_int_input()
                if ans in list(range(1,len(tasks)+1)):
                    break

            tasks.pop(ans - 1)


        else:
            print("All tasks are completed")
