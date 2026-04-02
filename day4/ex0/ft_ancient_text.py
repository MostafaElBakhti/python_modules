import sys

if len(sys.argv) != 2:
    print("Usage: ft_ancient_text.py <file>")
else:
    filename = sys.argv[1]
    print(filename)
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
    except Exception as error:
        print(f"Error opening file '{filename}': {error}")
