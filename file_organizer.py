import shutil
from pathlib import Path

SOURCE_DIR = Path("downloads")

FILE_TYPES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Code": [".py", ".js", ".html", ".css"],
    "Archives": [".zip", ".rar"]
}

def organize_files():
    if not SOURCE_DIR.exists():
        print("Source folder does not exist.")
        return

    for file in SOURCE_DIR.iterdir():
        if file.is_file():
            for folder, extensions in FILE_TYPES.items():
                if file.suffix.lower() in extensions:
                    target_dir = SOURCE_DIR / folder
                    target_dir.mkdir(exist_ok=True)
                    shutil.move(str(file), target_dir / file.name)
                    break

if __name__ == "__main__":
    organize_files()
