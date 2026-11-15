# Automatic File Organizer

A Python automation tool that organizes files into categories based on their file extensions.

## Features

- **File Categorization:** Automatically sorts files into Images, Documents, Videos, Audio, Code and Others.
- **Preview Mode:** Displays the proposed file movements without changing anything.
- **Duplicate Protection:** Prevents files from being overwritten by generating unique filenames.
- **Undo Functionality:** Restores files to their original locations after organization.

## Technologies Used

- Python
- OS module
- Shutil module
- JSON module

## How to Use

1. Install Python 3 if you haven't already.
2. Clone or download this repository.
3. Open the project folder in your terminal.
4. Run the program:

   ```bash
   python main.py
   ```

5. Enter the folder path you want to organize.
6. Select an option:
   - `1` – Preview changes
   - `2` – Organize files
   - `3` – Undo last organization

## Project Structure

```text
Automatic-File-Organizer/
│
├── main.py
├── README.md
└── undo_log.json  (created automatically)
```

## Purpose

This project was built to practise Python programming and explore file handling, automation, JSON storage and directory management.

## Author

Developed as a Python learning project.