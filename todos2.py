# make list of items
todo_list = []

def show_help():    
    # print instructions on use
    print("todo list:")
    print("""
type DONE to stop & exit
type HELP for this help
type SHOW to see current todos
""")

def show_list():
    # print todos
    print("here's your todos:")

    for item in todo_list:
        print(item)

show_help()
    
# ask for new todos
while True:
    new_todo = input("> ")

    # be able to quit app
    if new_todo == 'DONE':
        break
    elif new_todo == 'HELP':
        show_help()
        continue
    elif new_todo == 'SHOW':
        show_list()
        continue
        
    # add new todos to list
    todo_list.append(new_todo)
    
# print list on quit
show_list()