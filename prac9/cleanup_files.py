import shutil
import os


def main():
    print("Starting directory is: {}".format(os.getcwd()))
    os.chdir('Lyrics')
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))
    for directory, subdirectory, files in os.walk('.'):
        for filename in files:
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))
            full_name = os.path.join(directory, filename)
            new_name = os.path.join(directory, new_name)
            os.rename(full_name, new_name)

def get_fixed_filename(filename):
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


main()
