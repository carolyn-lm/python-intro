#imports PersonalAssistant.py file
import json
from PersonalAssistant import PersonalAssistant

#read data from files and pass to PersonalAssistant
with open("todo.json", "r") as todos, open("birthdays.json", "r") as birthdays:
  todo_list = json.load(todos)
  birthday_list = json.load(birthdays)

  assistant = PersonalAssistant(todo_list, birthday_list)

done = False

while not done:
    user_command = input(
        """
How can I help you?

    **** To-dos *****
    1: Add a to-do
    2: Remove a to-do
    3: Get to-do list
    *** Birthdays ***
    4: Get Birthday
    5: Add Birthday
    6: Remove Birthday

    Select a number or type 'Exit' to quit: 
    
    """
    )
    # Add Todo
    if user_command == "1":
        user_input = input("Item to add to to-do list: ")
        assistant.add_todo(user_input)
    # Remove Todo
    elif user_command == "2":
        print(f"Your current todos: {assistant.get_todos()}")
        user_input = input("Item to remove from to-do list: ")
        print(f"\n {assistant.remove_todo(user_input)}")
    # Get Todos
    elif user_command == "3":
        print("\nYour to-do list")
        print(f"\n {assistant.get_todos()}")
    # Get birthday
    elif user_command == "4":
        print("\nBirthdays available:")
        for name in ssistant.get_birthdays():
            print(name)
        user_input = input("Enter name for birthday needed: ")
        print(f"\n {assistant.get_birthday(user_input)}")
    # Add birthday
    elif user_command == "5":
        name = input("Name of the person: ")
        date = input("Their birthday (ex: mm/dd/yyyy): ")
        print(f"\n{assistant.add_birthday(name, date)}")
    # Remove birthday
    elif user_command == "6":
        print("\nCurrent Birthdays:")
        for name in assistant.get_birthdays():
            print(name)
        user_input = input("Enter name to remove: ")
        print(f"\n{assistant.remove_birthday(name)}")
    # Exit
    elif user_command == "exit" or user_command == "Exit" or user_command == "EXIT":
        done = True
        print("\nGoodbye, see you soon!")
    else:
        print("\nNot a valid command.")

# save data
with open("todo.json", "w") as write_todos, open("birthdays.json", "w") as write_birthdays:
    json.dump(assistant.get_todos(), write_todos)
    json.dump(assistant.get_birthdays(), write_birthdays)