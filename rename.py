import os

# Folder where images are stored
image_dir = r"car_dataset\images\val"  # Change to actual folder

# Iterate through all files in the directory
for filename in os.listdir(image_dir):
    if "Maruti_S-Cross" in filename:  # Check if the filename contains "Maruti_S-Cross"
        new_filename = filename.replace("Maruti_S-Cross", "Maruti_S_Cross")  # Rename
        
        # Full paths for renaming
        old_path = os.path.join(image_dir, filename)
        new_path = os.path.join(image_dir, new_filename)

        # Rename the file
        os.rename(old_path, new_path)
        print(f"✅ Renamed: {filename} ➝ {new_filename}")

print("\n🚀 File renaming complete!")
