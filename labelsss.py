import os

# Define car classes with actual file names and their corresponding class IDs
car_classes = {
    "Maruti_Suzuki_Swift": 0, "Hyundai_Creta": 1, "Tata_Nexon": 2, "Mahindra_Scorpio": 3, "Kia_Seltos": 4,
    "Toyota_Fortuner": 5, "BMW_X5": 6, "Audi_Q7": 7, "Kia_Sonet": 8, "Maruti_S_Cross": 9, 
    "Maruti_Grand_Vitara": 10, "Maruti_Baleno": 11, "Maruti_WagonR": 12, "Tata_Nano": 13, 
    "Tata_Punch": 14, "Hyundai_i20": 15, "Hyundai_Verna": 16
}

# Paths to images and labels directories
image_dir = r"car_dataset\images\val"  # Change to 'val' for validation set
label_dir = r"car_dataset\labels\val"

# Create labels directory if it doesn't exist
os.makedirs(label_dir, exist_ok=True)

# Track unmatched files
unmatched_files = []

# Process each image file
for image_file in os.listdir(image_dir):
    if image_file.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.webp')):  # Check if it's an image file
        label_filename = os.path.splitext(image_file)[0] + ".txt"  # Replace image extension with .txt
        label_filepath = os.path.join(label_dir, label_filename)

        # Assign class label based on filename
        class_label = None
        for car_name, class_id in car_classes.items():
            if car_name.lower().replace("-", "_") in image_file.lower():  # Case-insensitive match with underscores
                class_label = class_id
                break  # Stop once a match is found

        # If a match is found, create the annotation file
        if class_label is not None:
            with open(label_filepath, "w") as label_file:
                # YOLO format: class_id x_center y_center width height (normalized)
                label_file.write(f"{class_label} 0.5 0.5 1.0 1.0\n")  # Default bounding box covering full image

            print(f"✅ Created label: {label_filename} (Class {class_label} - {car_name})")
        else:
            unmatched_files.append(image_file)  # Store unmatched filenames

# Print unmatched files at the end
if unmatched_files:
    print("\n⚠️ The following files were not matched with any class:")
    for file in unmatched_files:
        print(f"❌ {file}")
else:
    print("\n✅ All files matched successfully!")

print("🚀 Label generation complete!")
