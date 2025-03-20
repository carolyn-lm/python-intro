class PersonalAssistant:
  def __init__(self, todos):
    self.contacts = {}
    self.todos = todos

  def add_todo(self, new_item):
    self.todos.append(new_item)

  def remove_todo(self, todo_item):
    if todo_item in self.todos:
      # Get the todo_item index in list
      index = self.todos.index(todo_item)
      # pop the index for todo_item in todos list
      self.todos.pop(index)
      return "Item removed!"
    else:
      return "Todo is not in list!"

  def get_todos(self):
    return self.todos
  
  def get_birthday(self, name): 
    if name == "Samantha":
      return "Birthday is 11/16/1996!"
    elif name == "Ryan":
      return "Birthday is 03/23/1999!"
    elif name == "Cindy":
      return "Birthday is 05/21/1976!"
    else:
      return "Can’t find a birthday for this person"

  
  def get_contact(self, name):
    if name in self.contacts:
      return self.contacts[name]
    else:
      return "No contact with that name"