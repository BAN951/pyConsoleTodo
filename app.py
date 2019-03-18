import json
import sys


def command(user_input, todos):
    if user_input == 'add':
        add_todo(todos)
    elif user_input == 'remove':
        remove_todo(todos)
    elif user_input == 'list':
        list_todos(todos)
    elif user_input == 'exit':
        print('Closing program.. Bye bye!')
        sys.exit(0)


def add_todo(todos):
    title = input("\t Title: ")
    description = input('\t Description: ')
    todo = dict()
    todo['title'] = title
    todo['description'] = description
    todos.append(todo)
    write_todos(todos)


def remove_todo(todos):
    # manage exceptions for string inputs
    index = int(input('\t To remove a TO-DO you must indicate it\'s index: '))
    del todos[index]


def write_todos(todos):
    f = open('todos.json', 'w')
    json.dump(todos, f)
    f.close()


def load_todos():
    with open('todos.json') as f:
        return json.load(f)
    

def list_todos(todos):
    for index, todo in enumerate(todos):
        print('Index:', index, '--', todo)


def main():
    print("Welcome to the console TO-DO app!")
    print("=" * 80)
    print("To exit the program enter: exit")

    todos = load_todos()
    while True:
        try:
            user_input = input('>>> ')
            command(user_input, todos)
        except KeyboardInterrupt:
            print('Bye Bye!')
            sys.exit(0)


if __name__ == "__main__":
    main()


