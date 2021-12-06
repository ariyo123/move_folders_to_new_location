import glob
import os
import shutil
import time
#get the unique variable to defferentiate date
date=input("enter date: yyyymmdd: ")    
path1 = "C:/python_work/Billingsample/Billingsample/"
#path2="_040219"

#pad the full source path where the original file exist
src_folder=f"{path1}{date}"
dst_folder = f'C:/python_work/sample/3line Card management Limited_{date}_155959/ '
print(src_folder)

#make a list of the content of the source path 
file_names = os.listdir(src_folder)
print(file_names)
#loop through the list to move files with a unique pattern (src_folder + "/3*") to the destination path (3line)
for file_name in file_names[:]:
    pattern = src_folder + "/3*"
    for file in glob.iglob(pattern, recursive=True):
    # extract file name form file path
            file_name = os.path.basename(file)
            shutil.move(file, dst_folder + file_name)
            print('move:', file)

#repeat the flow above

path1 = "C:/python_work/Billingsample/Billingsample/"
#path2="_040219"
src_folder=f"{path1}{date}"
dst_folder = f'C:/python_work/sample/9 Payment Service Bank_{date}_155959/ '
print(src_folder)   
file_names = os.listdir(src_folder)
print(file_names)
#loop through the list to move files with a unique pattern (src_folder + "/3*") to the destination path (9 mobile)
for file_name in file_names[:]:
    pattern = src_folder + "/9*"
    for file in glob.iglob(pattern, recursive=True):
    # extract file name form file path
            file_name = os.path.basename(file)
            shutil.move(file, dst_folder + file_name)
            print('move:', file)


path1 = "C:/python_work/Billingsample/Billingsample/"
#path2="_040219"
src_folder=f"{path1}{date}"
dst_folder = f'C:/python_work/sample/AB Microfinance bank_{date}_155959/ '
print(src_folder)   
file_names = os.listdir(src_folder)
print(file_names)

#loop through the list to move files with a unique pattern (src_folder + "/3*") to the destination path (3line)
for file_name in file_names[:]:
    pattern = src_folder + "/AB*"
    for file in glob.iglob(pattern, recursive=True):
    # extract file name form file path
            file_name = os.path.basename(file)
            shutil.move(file, dst_folder + file_name)
            print('move:', file)