# Import Libraries
import os
from PIL import Image
from tqdm import tqdm  # A library for progress bars, install with: pip install tqdm

# --- CONFIGURE THIS ---
# The path to the folder containing your 32,000+ images
image_directory = '/space/home/enrique.montes@CNS.local/plankton_imaging/unclassified_dataset/unclassified'
# --------------------

bad_files = []
print(f"Scanning directory: {image_directory}")

# Get a list of all files to iterate over with a progress bar
file_list = os.listdir(image_directory)

for filename in tqdm(file_list, desc="Verifying Images"):
    # Check for common non-image files to skip them quickly
    if filename.lower().startswith(('.ds_store', 'thumbs.db')):
        continue

    filepath = os.path.join(image_directory, filename)

    # Check if it's a directory, skip if so
    if not os.path.isfile(filepath):
        continue

    try:
        with Image.open(filepath) as img:
            img.verify()  # Verify that it is, in fact, an image
    except (IOError, SyntaxError, Image.UnidentifiedImageError) as e:
        print(f"\nFound bad file: {filename} (Reason: {e})")
        bad_files.append(filepath)

print("\n--- Scan Complete ---")
if bad_files:
    print(f"\nFound {len(bad_files)} bad files.")
    print("--- Attempting to delete bad files ---")
    
    deleted_count = 0
    failed_count = 0
    
    for path in bad_files:
        print(f"Processing: {path}")
        try:
            # First, check if the file still exists
            if os.path.exists(path):
                os.remove(path)
                print(f"  -> Successfully deleted.")
                deleted_count += 1
            else:
                print(f"  -> File already gone. Skipping.")
                
        except Exception as e:
            # Catch ANY exception to see what's going on
            print(f"  -> !!! FAILED to delete. Reason: {e}")
            failed_count += 1

    print("\n--- Deletion Summary ---")
    print(f"Successfully deleted: {deleted_count} files")
    print(f"Failed to delete: {failed_count} files")

else:
    print("No bad image files found.")