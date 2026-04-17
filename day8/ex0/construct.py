import sys
import os
import site


def is_venv():
    return sys.prefix != sys.base_prefix


def main():
    print()

    if is_venv():
        print("MATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {sys.executable}")

        venv_name = os.path.basename(sys.prefix)
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {sys.prefix}\n")

        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.\n")

        print("Package installation path:")
        for path in site.getsitepackages():
            print(path)

    else:
        print("MATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected\n")

        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")

        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows\n")
        print("Then run this program again.")


if __name__ == "__main__":
    main()
