# make list of items
todo_list = []

# print instructions on use
print("todo list:")
print("type DONE to stop & exit")

# ask for new todos
while True:
    new_todo = input("> ")

    # be able to quit app
    if new_todo == 'DONE':
        break
    
    # add new todos to list
    todo_list.append(new_todo)
    
# print list on quit
print("here's todos:")

for item in todo_list:
    print(item)