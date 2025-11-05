import os
import shutil
from pathlib import Path
import pandas as pd
from tqdm import tqdm

def filter_and_copy_png_files():
    """
    Recursively finds PNG files, filters them by a date range derived
    from their filenames, and copies the matches to a destination folder.
    """
    # --- Configuration ---
    # Use os.path.expanduser to correctly handle the '~' for the home directory
    source_directory = Path(os.path.expanduser("~/plankton_imaging/cpics_img/"))
    destination_directory = Path(os.path.expanduser("~/plankton_imaging/unclassified_dataset/unclassified/"))
    
    # Define the date range for filtering (inclusive)
    start_date = pd.Timestamp("2025-01-01 00:00:00", tz="UTC")
    end_date = pd.Timestamp("2025-02-01 00:00:00", tz="UTC")
    # -------------------

    # --- Step 1: Prepare Destination Directory ---
    print(f"Preparing destination directory: {destination_directory}")
    # Create the directory if it doesn't exist
    destination_directory.mkdir(parents=True, exist_ok=True)
    # Empty the directory
    for item in destination_directory.iterdir():
        if item.is_file():
            item.unlink() # More modern equivalent of os.remove()
    print("Destination directory emptied.")

    # --- Step 2: Find all PNG files ---
    print(f"Finding all PNG files in '{source_directory}'...")
    all_files = list(source_directory.rglob("*.png"))

    if not all_files:
        print("Error: No PNG files were found in the source directory. Please check the path.")
        return

    print(f"Found {len(all_files)} total PNG files.")

    # --- Step 3: Create a DataFrame and Filter by Date ---
    files_df = pd.DataFrame({'file_path': all_files})
    
    # Extract datetime from filename (assumes 'YYYYMMDD_hhmmss' format at the start)
    files_df['datetime_str'] = files_df['file_path'].apply(lambda p: p.name[:15])
    files_df['date'] = pd.to_datetime(files_df['datetime_str'], format="%Y%m%d_%H%M%S", errors='coerce', utc=True)

    # Drop any rows where the date could not be parsed
    files_df.dropna(subset=['date'], inplace=True)
    
    print("Filtering files between", start_date.strftime('%Y-%m-%d'), "and", end_date.strftime('%Y-%m-%d'), "...")
    
    filtered_df = files_df[
        (files_df['date'] >= start_date) & (files_df['date'] <= end_date)
    ].copy() # Use .copy() to avoid SettingWithCopyWarning

    # --- Step 4: Copy Filtered Files ---
    if filtered_df.empty:
        print("No files matched the specified date range. No files will be copied.")
    else:
        print(f"Found {len(filtered_df)} files within the date range.")
        print(f"Copying files to '{destination_directory}'...")
        
        # Use tqdm for a user-friendly progress bar
        for file_path in tqdm(filtered_df['file_path'], desc="Copying"):
            shutil.copy(file_path, destination_directory)
            
        print("\n--- All Done! ---")
        print(f"{len(filtered_df)} files have been successfully copied to:")
        print(destination_directory.resolve())

if __name__ == "__main__":
    # To run the script, first install the required libraries in your terminal:
    # pip install pandas tqdm
    filter_and_copy_png_files()