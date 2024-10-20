import os

def contains_ebook_files(dir_path):
    """
    Check if the directory contains .epub or .mobi files.
    """
    for root, _, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.epub') or file.endswith('.mobi'):
                return True
    return False

def rename_folders_without_ebooks(root_path):
    """
    Traverse the directory tree and rename folders that don't contain .epub or .mobi files.
    """
    # We need to start from the deepest folders, so a reverse traversal is ideal
    for root, dirs, _ in os.walk(root_path, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if not contains_ebook_files(dir_path):
                new_name = dir_name + "_noEbook"
                new_path = os.path.join(root, new_name)
                os.rename(dir_path, new_path)
                print(f"Renamed: {dir_path} to {new_path}")

if __name__ == '__main__':
    root_start_point = input("Enter the root starting point path: ")
    if os.path.exists(root_start_point) and os.path.isdir(root_start_point):
        rename_folders_without_ebooks(root_start_point)
    else:
        print("Invalid path! Please ensure the path exists and is a directory.")

