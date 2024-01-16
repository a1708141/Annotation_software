import os
import shutil

def copy_class_directories(source_dir, destination_dir):
    # Create destination directories if they don't exist
    test_destination = os.path.join(destination_dir, "test")
    train_destination = os.path.join(destination_dir, "train")
    valid_destination = os.path.join(destination_dir, "valid")

    os.makedirs(test_destination, exist_ok=True)
    os.makedirs(train_destination, exist_ok=True)
    os.makedirs(valid_destination, exist_ok=True)

    # Function to find 'test', 'train', 'valid' subdirectories recursively
    def find_subdirectories(directory, target_subdir):
        subdirs = []
        for root, dirs, files in os.walk(directory):
            if target_subdir in dirs:
                subdirs.append(os.path.join(root, target_subdir))
        return subdirs

    # Function to copy files to the destination
    def copy_files(subdir, dest_dir):
        for root, dirs, files in os.walk(subdir):
            for file in files:
                file_path = os.path.join(root, file)
                dest_subdir = os.path.join(dest_dir, os.path.basename(os.path.dirname(file_path)))
                os.makedirs(dest_subdir, exist_ok=True)
                shutil.copy(file_path, dest_subdir)

    # Find and copy 'test', 'train', 'valid' subdirectories for each class
    for subdir in find_subdirectories(source_dir, "test"):
        copy_files(subdir, test_destination)

    for subdir in find_subdirectories(source_dir, "train"):
        copy_files(subdir, train_destination)

    for subdir in find_subdirectories(source_dir, "valid"):
        copy_files(subdir, valid_destination)

if __name__ == "__main__":
    #EDIT THIS 
    source_directory = "PATH TO SOURCE DIRECTORY REPLACE"
    destination_directory = "PATH TO DESTINATION DIR REPLACE + NAME OF NEW OF NEW DATABASE"

    copy_class_directories(source_directory, destination_directory)