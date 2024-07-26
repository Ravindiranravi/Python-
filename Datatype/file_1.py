#open  function _. filename,mode(r,w,a....)

# file_read = open('frequency.py','r')
# print(file_read.read())

import os
def Createfile(filename):
    if(os.path.exists(filename)):
        print('File is already Exists')
    else:
        file_create=open(filename,'w')

def main():
    print('Enter filename you want to create:')
    file_name=input()

    Createfile(file_name)

if __name__=="__main__":
    main()