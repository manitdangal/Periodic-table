import os

# Get the directory where the script is located
root_directory = os.path.dirname(os.path.abspath(__file__))

# Iterate through all HTML files in the root directory and subdirectories
for foldername, subfolders, filenames in os.walk(root_directory):
    for filename in filenames:
        if filename.endswith(".html"):  # Process only HTML files
            file_path = os.path.join(foldername, filename)

            # Read file contents
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()

            # Replace occurrences of "Periodictable.html" with "index.html"
            updated_content = content.replace("Periodictable.html", "index.html")

            # Write back the updated content
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(updated_content)

            print(f'Updated: {file_path}')

print("Replacement completed successfully!")
