from os import listdir
from os.path import isfile

directory = './screenshots/'
files = [i for i in listdir(directory) if isfile(directory + i) and i.endswith(".png")]
print(files)

#Read
README_file = open('./README.md', 'r')

CONTENT = README_file.read()
print(CONTENT)


#Write
#template: [Cobblestone](materials/cobblestone.blend)<BR>![cobblestone](screenshots/cobblestone.png)