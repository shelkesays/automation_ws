import os
from pathlib import Path


def create_file():
    # path = Path(__file__).parent.joinpath("hello.txt")
    path = Path("hello_1.txt")
    # with open(path, "w") as file:
    with path.open("w") as file:
        file.write("Hello, world!")
    
    with path.open("r") as file:
        print(file.read())

    print(f"File created at: {path}")


def remove_file():
    path = Path("hello_1.txt")
    path.unlink()
    print(f"File removed at: {path}")

def os_remove_file():
    path = Path(__file__).parent.joinpath("hello.txt")
    os.remove(path)
    

def get_file_size(file_path):
    file_size = os.path.getsize(file_path)
    return file_size

def get_file_metadata(file_path):
    file_metadata = os.stat(file_path)
    return file_metadata

def get_file_permissions(file_path):
    file_permissions = os.stat(file_path).st_mode
    return file_permissions

def get_file_owner(file_path):
    file_owner = os.stat(file_path).st_uid
    return file_owner

def get_file_group(file_path):
    file_group = os.stat(file_path).st_gid
    return file_group

def get_file_access_time(file_path):
    file_access_time = os.stat(file_path).st_atime
    return file_access_time

def get_file_modification_time(file_path):
    file_modification_time = os.stat(file_path).st_mtime
    return file_modification_time

def get_file_change_time(file_path):
    file_change_time = os.stat(file_path).st_ctime
    return file_change_time

def set_file_permissions(file_path, permissions):
    os.chmod(file_path, permissions)

def set_file_owner(file_path, owner):
    os.chown(file_path, owner, -1)
    
def set_file_group(file_path, group):
    os.chown(file_path, -1, group)    

if __name__ == "__main__":
    # create_file()
    # remove_file()
    os_remove_file()
