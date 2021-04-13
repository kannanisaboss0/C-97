'''
import os
import shutil
path=input("Enter path:")
files=os.listdir(path)

for file in files:
    name,ext=os.path.splitext(file)
    ext=ext[1:]
    if (ext==""):
        continue 
    if(os.path.exists(path+"/"+ext)):
        shutil.move(path+"/"+file,path+"/"+ext+"/"+file)
    else:
        os.makedirs(path+"/"+ext)
        shutil.move(path+"/"+file,path+"/"+ext+"/"+file)
        '''
import os
import shutil
path=input("Enter path:")
source=input("Enter source:")
destination=input("Enter destination:")

allFiles=os.listdir(source)

for file in allFiles:
    shutil.copy(source,destination)
    





