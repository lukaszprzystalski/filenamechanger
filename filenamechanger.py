import os

f_path = os.chdir(r'C:\Users\lukasz.przystalski\Dokumenty\programowanie\python\small_projects\filenamechange\files')

for index, f in enumerate(os.listdir()):
    #print(os.path.splitext(f))
    #f_ext = os.path.splitext(f)[1]
    #f_name = os.path.splitext(f)[0]
    f_name, f_ext = os.path.splitext(f)
    oldName = str(f_name) + str(f_ext)
    newName = str(0000) + str(index) + str(f_ext)
    print(oldName)
    print(newName)
    # print(f_name)
    # print(f_ext)
    os.rename(oldName, newName)
    


