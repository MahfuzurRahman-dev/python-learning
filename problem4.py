import os
import sys

def print_dir_contents(path='/venv'):
    try:
        entries = os.listdir(path)
    except FileNotFoundError:
        print(f"Error: the directory '{path}' does not exist.")
        return
    except PermissionError:
        print(f"Error: permission denied for directory '{path}'.")
        return
    except OSError as e:
        print(f"OS error occurred: {e}")
        return

    print(f"Contents of directory: {path}")
    for name in entries:
        full_path = os.path.join(path, name)
        if os.path.isdir(full_path):
            print(f"[DIR ] {name}")
        elif os.path.isfile(full_path):
            print(f"[FILE] {name}")
        else:
            # e.g. symbolic link, special file
            print(f"[OTHER] {name}")

if __name__ == "__main__":
    # If a path is supplied via command line, use it
    if len(sys.argv) > 1:
        dir_path = sys.argv[1]
    else:
        dir_path = '.'
    print_dir_contents(dir_path)
