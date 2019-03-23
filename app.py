import json
import sys
import datetime


def command(user_input, todos):
    """
    Command classifier function.
    Depending on the input redirects a user to one
    or to another functionality.
    """
    if user_input == 'add':
        add_todo(todos)
    elif user_input == 'remove':
        remove_todo(todos)
    elif user_input == 'done':
        mark_done(todos)
    elif user_input == 'list':
        list_todos(todos)
    elif user_input == 'exit':
        print('Closing program.. Bye bye!')
        sys.exit(0)


def add_todo(todos):
    """ Adds a To-do to the registry. """
    title = input("\t Title: ")
    description = input('\t Description: ')
    todo = dict()
    todo['title'] = title
    todo['description'] = description
    todo['done'] = False
    todos.append(todo)
    write_todos(todos)


def remove_todo(todos):
    # manage exceptions for string inputs
    index = int(input('\t To remove a TO-DO you must indicate it\'s index: '))
    del todos[index]
    write_todos(todos)


def mark_done(todos):
    index = int(input('\t To update a TO-DO you must indicate it\'s index: '))
    todo = todos[index]
    if todo['done'] != True:
        todo['done'] = True
        write_todos(todos)
    else:
        print(' -- ', 'This TO-DO is already done', ' -- ')


def write_todos(todos):
    f = open('todos.json', 'w')
    json.dump(todos, f)
    f.close()


def load_todos():
    with open('todos.json') as f:
        return json.load(f)

def print_format_todo(index, todo):
    """
    Takes in the index and an array a To-do
    and returns the formatted string to print it.
    """
    print('\t::INDEX::', index)
    print('\t::TITLE::', todo['title'])
    print('\t::DESCRIPTION::\n\t\t', todo['description'])
    if todo['done'] is False:
        print('\t::STATUS:: - Not Finished')
    else:
        print('\t::STATUS:: - Finished') 
    print('  ','-'*56)


def list_todos(todos):
    """ Lists all the To-dos registered """
    for index, todo in enumerate(todos):
        print_format_todo(index, todo)


def main():
    """
    Main entry point of the program.
    """
    print("\nWelcome to the console TO-DO app!")
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


