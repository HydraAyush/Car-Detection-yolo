import os
import shutil
from sklearn.model_selection import train_test_split

# Define your source and destination directories
source_directory = r"F:\The Ultimate project\datasets\car_dataset\images"
train_dir = r"F:\The Ultimate project\datasets\car_dataset\images\train"
val_dir = r"F:\The Ultimate project\datasets\car_dataset\images\val"
test_dir = r"F:\The Ultimate project\datasets\car_dataset\images\test"

# Check the source directory and subdirectories for images
def get_image_files(source_dir):
    image_files = []
    for root, _, files in os.walk(source_dir):  # Search through all subdirectories
        for file in files:
            if file.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.webp')):
                image_files.append(os.path.join(root, file))
    return image_files

def split_data(source_dir, train_dir, val_dir, test_dir, test_size=0.2, val_size=0.1):
    # Get all image files from subdirectories
    image_files = get_image_files(source_dir)
    
    if not image_files:
        print("No image files found.")
        return

    # Split the data into train, validation, and test sets
    train_val_files, test_files = train_test_split(image_files, test_size=test_size, random_state=42)
    train_files, val_files = train_test_split(train_val_files, test_size=val_size, random_state=42)

    # Move the files to the respective directories
    def move_files(file_list, destination_dir):
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)
        for file in file_list:
            shutil.move(file, os.path.join(destination_dir, os.path.basename(file)))

    move_files(train_files, train_dir)
    move_files(val_files, val_dir)
    move_files(test_files, test_dir)

    print(f"Data split completed. {len(train_files)} images in training, {len(val_files)} images in validation, and {len(test_files)} images in testing.")

# Call the function to split the data
split_data(source_directory, train_dir, val_dir, test_dir)
