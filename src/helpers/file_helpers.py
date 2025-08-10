

def write_file(file_path: str, content: str) -> None:
    """
    Writes content to a file at the specified path.

    Args:
        file_path (str): The path to the file where content will be written.
        content (str): The content to write to the file.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def read_file(file_path: str) -> str:
    """
    Reads content from a file at the specified path.

    Args:
        file_path (str): The path to the file to read.

    Returns:
        str: The content of the file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()