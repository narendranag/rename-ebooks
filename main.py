import os
import shutil

def contains_target_files(dir_path, extensions):
    """
    Check if the directory contains any of the target file extensions.
    """
    for root, _, files in os.walk(dir_path):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                return True
    return False

def move_folders_without_target_files(root_path, target_extensions):
    """
    Traverse the directory tree and move folders that don't contain target file extensions to a trash folder.
    """
    trash_path = os.path.join(root_path, 'trash')
    if not os.path.exists(trash_path):
        os.makedirs(trash_path)
    
    # We need to start from the deepest folders, so a reverse traversal is ideal
    for root, dirs, _ in os.walk(root_path, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if not contains_target_files(dir_path, target_extensions) and dir_path != trash_path:
                new_path = os.path.join(trash_path, dir_name)
                shutil.move(dir_path, new_path)
                print(f"Moved: {dir_path} to {new_path}")

if __name__ == '__main__':
    root_start_point = input("Enter the root starting point path: ")
    if os.path.exists(root_start_point) and os.path.isdir(root_start_point):
        move_folders_without_target_files(root_start_point, ['.pdf', '.epub', '.mobi'])
    else:
        print("Invalid path! Please ensure the path exists and is a directory.")
