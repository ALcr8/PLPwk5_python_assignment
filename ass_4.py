file_name = input("Enter the name of the file to read: ")

try:
    with open(filename, "r") as f:
        content = f.read()
    modified_content = content.upper()

    new_filename = "modified_" + filename
    with open(new_filename, "w") as f:
        f.write(modified_content)
    print(f"File processed successfully! Modified version saved as '{new_filename}'")

except FileNotFoundError:
    print("Error: The file does not exist. Please check the filename and try again.")
except PermissionError:
    print("Error: You don’t have permission to read this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
