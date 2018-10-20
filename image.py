import os
import csv
from shutil import copyfile
dir_lsit =[]
folder_name =[]
curr_dir = os.getcwd()
for root, dirs, files in os.walk(curr_dir):  #a generator with root="abs path of curr dir",dir,file=a list of dir/files in curr dir
    if 'IMD002' in dirs:
        dir_list = [root+os.path.sep+d for d in dirs] #os.path.sep=\ #C:\Users\Wang\Documents\Tongyu_python_ML\My_python\Image + \ +IMDXXX
        folder_name = dirs   # IMDXXX
#print(folder_name)
#print(dir_list)
#read new name
newname = open('C:\\Users\\Wang\\Documents\\Tongyu_python_ML\\My_python\\Image\\rename_pics.csv')
newdata = csv.reader(newname,delimiter=',')  #Return a reader object which will iterate over lines in the given csvfile.
row_count = sum(1 for row in newdata)
newname.seek(0)  #Once you go through it once, you read to the end of the file, so there is no more to read. If you need to go through it again, you can seek to the beginning of the file:
img_folder = '_Dermoscopic_Image'
counter=0
for d, name in zip(dir_list, folder_name):
    image_path = d + os.path.sep +name+ img_folder+os.path.sep+ name+'.bmp' #C:\Users\Wang\Documents\Tongyu_python_ML\My_python\Image\IMD002 + \ +IMD002 + _Dermoscopic_Image + \ + IMDXXX + .bmp
    if os.path.isfile(image_path):
        for i in newdata:
            print(i[0],name)
            if name==i[0]:
                #print("h")
                dst='C:\\Users\\Wang\\Documents\\Tongyu_python_ML\\My_python\\wang\\'+i[1]+'.bmp' # double \\ OW it interprets as sth else
                copyfile(image_path, dst)
                break
            else:
                counter+=1
                continue
                #print("i")
        newname.seek(0)
        if counter==row_count:
            dst='C:\\Users\\Wang\\Documents\\Tongyu_python_ML\\My_python\\wang\\'+name+'.bmp'
            copyfile(image_path,dst)
            couter=0
