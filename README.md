# Python File Automation Tool

A simple Python automation script that organizes files into folders
based on their file types.

## Features
- Automatically organizes files by extension
- Creates folders if they do not exist
- Reduces manual effort and clutter
- Safe and easy to use

## Technologies Used
- Python 3
- pathlib
- shutil

## How It Works

Before running the script:
downloads/
├── image.PNG
├── report.pdf
├── script.py
├── archive.zip

After running the script:
downloads/
├── Images/
│ └── image.PNG
├── Documents/
│ └── report.pdf
├── Code/
│ └── script.py
├── Archives/
│ └── archive.zip

## How to Run
1. Create a folder named `downloads`
2. Place files inside the folder
3. Run the script:

   
## Limitations
- Only processes files in the top-level directory
- Files with unsupported extensions are ignored

## Author
K.W.R.Nethmini  
AI-Assisted Automation Developer



