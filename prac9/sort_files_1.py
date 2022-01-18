import os

os.chdir("FilesToSort")
for filename in os.listdir('.'):
    if os.path.isdir(filename):
        continue

    extension = filename.split('.')[-1]
    try:
        os.mkdir(extension)
    except FileExistsError:
        pass
    print(f"{extension}/{filename}")
    os.rename(filename, f"{extension}/{filename}")
