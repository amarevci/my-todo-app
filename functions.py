FILEPATH = "todos.txt"  # in capital letters, a constant variable

def get_todos(filepath= FILEPATH): #'Files/todos.txt'):  ## filepath is parameters, the value of the argument is the 'Files/todos.txt' in our case
    """Reads a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH): #'Files/todos.txt'):
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)

print(__name__)  ## returns __main__ here inside this file, but will return 'functions' if executed in the cli.py file
if __name__ == "__main__":
    print("Hello")
    print(get_todos())
