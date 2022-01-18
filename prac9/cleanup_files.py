import shutil
import os


def main():
    print(f"Starting directory is: {os.getcwd()}")
    os.chdir('Lyrics')
    print(f"Files in {os.getcwd()}:\n{os.listdir('.')}\n")
    for directory, subdirectory, files in os.walk('.'):
        for filename in files:
            new_name = get_fixed_filename(filename)
            print(f"Renaming {filename} to {new_name}")
            full_name = os.path.join(directory, filename)
            new_name = os.path.join(directory, new_name)
            os.rename(full_name, new_name)

def get_fixed_filename(filename):
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt") #INCOMPLETE REQUIRES LOWER TO UPPER, SEPARATE IF UPPER
    return new_name


main()
