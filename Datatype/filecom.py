import os
import filecmp
def Comparefile(filename1,filename2):
    if(not os.path.exists(filename1)):
        print('Not Exists',filename1)
    elif(not os.path.exists(filename2)):
        print('Not Exists',filename2)
    else:
        compare = filecmp.cmp(filename1,filename2)
        if compare == True:
            print('Success-> These files are Same')
        else:
            print('Failure-> These files are Different')

def main():
    file_01 = input('Enter the first File Name:')
    file_02 = input('Enter the first File Name:')
    Comparefile(file_01,file_02)





if __name__=="__main__":
    main()