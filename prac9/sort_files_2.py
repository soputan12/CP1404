import os

file_type_list = {}
os.chdir("FilesToSort")
for filename in os.listdir('.'):
    if os.path.isdir(filename):
        continue

    file_type = filename.split('.')[-1]
    if file_type not in file_type_list:
        category = input(f"What category would you like to sort {file_type} files into? ")
        file_type_list[file_type] = category
        try:
            os.mkdir(category)
        except FileExistsError:
            pass

    os.rename(filename, f"{file_type_list[file_type]}/{filename}")