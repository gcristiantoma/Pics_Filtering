# ****************************************************** With this application we are:*******************************************************************
# 1) For each folder and subloder given a certain path we are checking the modification(or creation) date and create folderers named as: Year-month (ex: 2020-02)
# 2)Looping trough each folder and subolder and take modification(or creation) date and move those files in the mathcing folder when it was modified(or created)
import os.path
import time
import os
import shutil
from datetime import datetime
#from where it takes the files to be filter, so this is source
source = r"C:\Users\gcris\Documents\MEGA\MEGAsync\Programming"
dest="c:\\test\\"

def make_dirs(source,dest):
    for root, dirs, files in os.walk(source): # loop trough each folder and subfolder
        for file_ in files:
            s=str(os.path.join(root, file_)) #for each file name we are joing the full path
            if 0 < len(s) < 250: #check if the full path string is not 0
                x=time.ctime(os.path.getmtime(s)) # get the mofication date as a string
                check_time=time.strptime(x) #creates a datetime object from the given string as a list
                print(s)
                print(check_time[0],check_time[1])
                dirName=dest+str(check_time[0])+"-"+str(check_time[1]) #dirName + Year+month
                try:
                    os.makedirs(dirName) #creating the directory ex: path../Year-month
                    print("Directory ", dirName, " Created ")
                    #shutil.move(s, dirName)

                except FileExistsError:
                    print("Directory ", dirName, " already exists")
                    #shutil.move(s, dirName)
                    #print(s,"moved to: "+dirName)

            else:# if path is not valid then go to the next file
                continue


def pywalker(source,dest):
    for root, dirs, files in os.walk(source):
        for file_ in files:
            s=str(os.path.join(root, file_))
            if len(s)>0<250:
                x=time.ctime(os.path.getmtime(s))
                check_time=time.strptime(x)
                nome_file=os.path.basename(s)
                time_stamp=str(int(time.time()*1000))
                print(s)
                print(check_time[0],check_time[1])
                #to be moved to this destion in folders that are named "2020-02" for ex
                dirName=dest+str(check_time[0])+"-"+str(check_time[1])+"\\"+time_stamp+nome_file
                try:
                    shutil.move(s, dirName)
                    print(os.path.basename(s),"  nome file")
                    print(s, "moved to: ", dirName)
                except FileExistsError:
                    print(s, "cannot be moved to: ", dirName)
            else:
                continue

#to be called first in order to create the directories
make_dirs(source,dest)
#moves the files in the folder indicared as "dest"
# pywalker(source,dest)

