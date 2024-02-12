import os

def create_folder(folder_path, folder):
    """
    This function will be creating a folder in the given . 
    The 
    """

    try:
        os.makedirs(folder_path, exist_ok=True)
        print(f"Folder '{folder}' created successfully.")
    except FileExistsError:
        print(f"Folder '{folder}' already exists.")

def create_file(file_path):
    try:
        with open(file_path, 'w') as file:
            file.write("This is a sample file.")
        print(f"File '{file_path}' created successfully.")
    except Exception as e:
        print(f"Error occurred while creating file '{file_path}': {e}")

def main():
    main_directory = os.getcwd()
    directory = input("Name of the folder you wish to create: ")

    path = os.path.join(main_directory, directory)

    create_folder(path, directory)