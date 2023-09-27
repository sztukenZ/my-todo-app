FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """
    Read a textfile and return the list of to-do items
    :param filepath: str
    :return: List
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """
    Write to-do items list in text file
    :param todos_arg: List
    :param filepath: str
    :return: None
    """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)
