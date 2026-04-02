import sys

if len(sys.argv) != 2:
    print("Usage: ft_ancient_text.py <file>")
else:
    filename = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")
    try:
        file = open(filename, "r")
        print("---")
        content = file.read()
        print(content, end="")
        print("---")
        file.close()
        print(f"File {filename} closed")

        lines = content.splitlines()
        new_content = ""

        for line in lines:
            new_content += line + "#\n"

        print("Transform data:")
        print("---")
        print(new_content, end="")
        print("---")
        new_filename = input("Enter new file name (or empty): ").strip()

        if new_filename == "":
            print("Not saving data.")
        else:
            print(f"Saving data to '{new_filename}'")
            new_file = open(new_filename, "w")
            new_file.write(new_content)
            new_file.close()
            print(f"Data saved in file '{new_filename}'.")
    except Exception as error:
        print(f"Error opening file '{filename}': {error}")
