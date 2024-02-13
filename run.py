import os

def welcomeMessage():

    """
    This function is to welcome and give instructions for the user 
    to understand what it is that they need to do.
    """

    print("Welcome to the Project File Management System!")
    print("Please follow the instructions below:")
    print("1. Enter the name of the project directory you wish to create.")
    print("2. The system will generate the project structure with nested folders and generic files.")
    print("3. Navigate into the project directory to access or modify files.")
    print("4. Enjoy organizing your project efficiently!")

def create_project_structure(root_directory):

    """
    This function creates the structure of how the project should be.
    It does so by calling all the other functions that are creating the needed folders and files
    """

    create_root_directory(root_directory)
    create_nested_folders(root_directory)
    create_generic_files(root_directory)

def create_root_directory(root_directory):

    """
    
    """

    os.makedirs(root_directory)

def create_project_directory(root_directory):
    os.mkdir(root_directory)

def create_folder(folder_path):
    os.makedirs(folder_path)

def create_nested_folders(root_directory):
    folders = {
        'documents': ['csvFiles', 'presentations'],
        'source-code': ['backend', 'frontend', 'utils'],
        'assets': ['images', 'videos', 'fonts']
    }

    for folder, subfolders in folders.items():
        folder_path = os.path.join(root_directory, folder)
        create_folder(folder_path)
        for subfolder in subfolders:
            subfolder_path = os.path.join(folder_path, subfolder)
            create_folder(subfolder_path)

def create_file(file_path):
    with open(file_path, 'w') as f:
        f.write('This is a generic file.')

def create_generic_files(root_directory):
    generic_files = ['README.md', 'LICENSE.txt', 'requirements.txt']

    for file in generic_files:
        file_path = os.path.join(root_directory, file)
        create_file(file_path)

def main():
    """
    This function will be used to call all the functions and put together how the project works.
    """

    welcomeMessage()
    project_name = input("Enter the name of your project directory: ")
    create_project_structure(project_name)
    print(f"Project structure created successfully at '{project_name}'.")

if __name__ == "__main__":
    main()