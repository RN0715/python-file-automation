import shutil
from pathlib import Path

# UPDATED: Use current working directory instead of hardcoded "downloads"
# This ensures the script organizes the folder you run it from.
SOURCE_DIR = Path.cwd()

FILE_TYPES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Code": [".py", ".js", ".html", ".css", ".json"],
    "Archives": [".zip", ".rar", ".7z"],
    "Other": [] 
}

def get_unique_path(filepath):
    """If file exists, append (1), (2), etc. until a unique name is found."""
    if not filepath.exists():
        return filepath
    
    counter = 1
    stem = filepath.stem
    suffix = filepath.suffix
    parent = filepath.parent
    
    while True:
        new_name = f"{stem} ({counter}){suffix}"
        new_path = parent / new_name
        if not new_path.exists():
            return new_path
        counter += 1

def organize_files():
    if not SOURCE_DIR.exists():
        print(f"Source folder '{SOURCE_DIR}' does not exist.")
        return

    print("-" * 30)
    print(f"Scanning folder: {SOURCE_DIR}")
    print("-" * 30)

    files_moved = 0
    
    for item in SOURCE_DIR.iterdir():
        # Skip the script itself and newly created folders to prevent infinite loops
        if item.name == Path(__file__).name:
            continue
        
        if item.is_file():
            target_folder = None
            found_match = False
            
            for folder, extensions in FILE_TYPES.items():
                if folder == "Other":
                    continue
                
                if item.suffix.lower() in extensions:
                    target_folder = folder
                    found_match = True
                    break
            
            if not found_match:
                target_folder = "Other"

            target_dir = SOURCE_DIR / target_folder
            target_dir.mkdir(exist_ok=True)

            destination = target_dir / item.name
            destination = get_unique_path(destination)

            try:
                shutil.move(str(item), str(destination))
                print(f"[OK] Moved '{item.name}' -> {target_folder}/")
                files_moved += 1
            except Exception as e:
                print(f"[ERROR] Could not move '{item.name}': {e}")
        
        # Optional: Debug info to see why files aren't moving
        # else:
        #     print(f"[SKIP] '{item.name}' is a directory, skipping...")

    print("-" * 30)
    print(f"Operation Complete. {files_moved} files moved.")
    print("-" * 30)

if __name__ == "__main__":
    organize_files()
    
    # This line keeps the command prompt window open after the script finishes
    input("Press Enter to exit...")
