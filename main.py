import json
import os
import shutil

folder = input("Enter folder path to organize: ")

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Code": [".py", ".js", ".html", ".css", ".java"]
}

script_folder = os.path.dirname(os.path.abspath(__file__))
undo_file = os.path.join(script_folder, "undo_log.json")

def get_unique_path(destination, filename):
    name, extension = os.path.splitext(filename)

    new_path = os.path.join(destination, filename)
    counter = 1

    while os.path.exists(new_path):
        new_filename = f"{name}_{counter}{extension}"
        new_path = os.path.join(destination, new_filename)
        counter += 1

    return new_path
def undo_organization():
    if not os.path.exists(undo_file):
        print("No previous organization found.")
        return

    with open(undo_file, "r") as file:
        moves = json.load(file)

    for original_path, new_path in reversed(moves):
        if os.path.exists(new_path):
            if not os.path.exists(original_path):
                shutil.move(new_path, original_path)
                print(f"Restored: {os.path.basename(original_path)}")
            else:
                print(f"Skipped: {os.path.basename(original_path)} already exists.")

    os.remove(undo_file)
    print("\nUndo operation completed!")
print("\n=== AUTOMATIC FILE ORGANIZER ===")
print("1. Preview changes")
print("2. Organize files")
print("3. Undo last organization")

choice = input("\nChoose an option: ")

if choice == "3":
    undo_organization()

elif choice in ["1", "2"]:
    moves = []

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)

        if os.path.isfile(file_path):
            extension = os.path.splitext(filename)[1].lower()

            category = "Others"

            for name, extensions in file_types.items():
                if extension in extensions:
                    category = name
                    break

            destination = os.path.join(folder, category)

            if choice == "1":
                new_path = get_unique_path(destination, filename)

                print(f"{filename} -> {category}/{os.path.basename(new_path)}")

            elif choice == "2":
                os.makedirs(destination, exist_ok=True)

                new_path = get_unique_path(destination, filename)

                shutil.move(file_path, new_path)

                moves.append([file_path, new_path])

                print(f"Moved {filename} to {category}")

    if choice == "1":
        print("\nPreview complete. No files were moved.")

    elif choice == "2":
        with open(undo_file, "w") as file:
            json.dump(moves, file, indent=4)

        print("\nOrganization complete!")

else:
    print("Invalid option!")