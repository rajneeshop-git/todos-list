s = ["1", "v", "2", "a", "3", "d", "4", "m", "5", "c", "6" , "e"]    # services list
# function to print list
def show_list():
    for i in range(len(lst)):
        print(str(i+1)+".", lst[i])
print("\nTODOS LIST")
while True:
    import list
    lst = list.ls
    print("\n\n1. View Tasks (v)", "\n2. Add Task (a)", "\n3. Delete Task (d)", "\n4. Modify Task (m)", "\n5. Clear List (c)\n6. Exit (e)")
    choice = input("\nChoose One: ")
    if choice in s:
        if choice == s[0] or choice == s[1]:    # viewing list
            print("\nVIEW TASKS")
            if lst == []:
                print("List is Empty")
            else:
                show_list()
        elif choice == s[2] or choice == s[3]:    # adding task
            print("\nADD TASK")
            task = input("What Task to Add? ")
            lst.append(task)
            print(task, "Added")
        elif choice == s[4] or choice == s[5]:    # removing task
            print("\nDELETE TASK")
            if lst != []:
                show_list()
                while True:
                    task = int(input("\nWhich Task to Delete? "))
                    if lst[task-1]:
                        print(lst[task-1], "Removed")
                        lst.remove(lst[task-1])
                        break
                    elif task == "None":
                        break
                    else:
                        print("Not Available")
            else:
                print("List is Empty")
        elif choice == s[6] or choice == s[7]:    # renaming task
            print("\nMODIFY TASK")
            if lst != []:
                show_list()
                while True:
                    task = int(input("\nWhich Task to Modify? "))
                    if lst[task-1]:
                        lst.remove(lst[task-1])
                        task = input("New Name: ")
                        lst.append(task)
                        print(task, "Renamed")
                        break
                    elif task == "None":
                        break
                    else:
                        print("Not Available")
            else:
                print("List is Empty")
        elif choice == s[8] or choice == s[9]:    # clearing list
            print("\nCLEAR LIST")
            confirm = input("Clear List? (y/n) ")
            if confirm == "y":
                lst.clear()
                print("List Cleared")
            else:
                print("Operation Cancelled")
        # modifys data file & saves list in ROM
        f = open("list.py", "w")
        f.write("ls = " + str(lst))
        f.close()
        if choice == s[10] or choice == s[11]:
            confirm = input("Confirm to Exit? (y/n) ")
            if confirm == "y":
                print("\nGOOD BYE\n")
                break
    else:
        print("Invalid Selection")
    input("\n———————————————Session End————————————————")