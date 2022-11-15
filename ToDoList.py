# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
objFile = None


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here

while(True):
    print("\n[R]ead to load and display current 'ToDoList.txt' file or [E]xit to return to main menu.")
    strChoice = input("\nChoose to [R]ead or [E]xit: ")
    # Process the data
    if (strChoice.lower() == 'e'): break
    elif (strChoice.lower() == 'r'):
        # File to List
        objFile = open(strFile, "r")
        for row in objFile:
            lstRow = row.split(",") # Returns a list!
            dicRow = {'Activity': lstRow[0], "Priority": lstRow[1].strip()}
            lstTable.append(dicRow)
            print(dicRow)
        objFile.close()
    else:
        print('Please choose either R or E!')
    continue

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
   +------------------------------+ 
   |       Menu of Options:       | 
   |------------------------------|
   | 1) Show Current Data         |
   | 2) Add a New Item.           |
   | 3) Remove an existing item.  |
   | 4) Save Data to File.        |
   | 5) Exit Program.             |
   +------------------------------+
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
        objFile = open(strFile, "r")
        print('Your current data is: ')
        for row in objFile:
            lstRow = row.split(",")  # Returns a list!
            dicRow = {'Activity': lstRow[0], "Priority": lstRow[1].strip()}
            print(dicRow)
        objFile.close()
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        activity = str(input(" Please enter the Activity: "))
        priority = str(input(" Please enter the Priority: "))
        dicRow = {'Activity': activity, "Priority": priority}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        if lstTable:
            # Get TODO item to be removed
            strRemove = input('Enter the Activity to be removed: ')
            # Remove the indicated dictionary from list
            for row in lstTable:
                if row['Activity'] == strRemove:
                    lstTable.remove(row)
        else:
            input('There are nothing to remove.\nPress Enter to continue.')
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        objFile = open(strFile, "w")  # make a file to a designated directory
        for row in lstTable:
            objFile.write(row['Activity'] + ',' + row['Priority'] + '\n')  # display the data in text file
        objFile.close()  # close the file
        print("The data has been saved.")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        input("Press Enter to exit the program...")
        break  # and Exit the program