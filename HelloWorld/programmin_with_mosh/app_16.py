from pathlib import Path
import time

# Absolute path
# c:\Program Files/Microsofe
# /usr/local/bin

# Relative path

path = Path("ecommerce")
path1 = Path("ecommerce/shipping.py")
path2 = Path("app_1.py")
print(path.exists())
print(path1.exists())
print(path2.exists())

path = Path("emails")
print(path.mkdir())

time.sleep(2)
print(path.rmdir())

# path = Path("email\data")
# print(path.mkdir())

path = Path()
print(path.glob('*.py'))

for files in path.glob('*.py'):
    print(files)

print('---')
path = Path("C:\\Users\\Dell\\OneDrive - Sudhir Srivastava Innovations Pvt. Ltd\\Abhinay's Workspace\\main x\\GitHub Repo\\Programming_py\\HelloWorld\\programmin_with_mosh")
print(path)
print(path.glob('*.*'))

for files in path.glob('*.*'):
    path_n = Path(files)
    print(files)
    for files_n in path_n.glob('*.*'):
        print('- -',files_n)