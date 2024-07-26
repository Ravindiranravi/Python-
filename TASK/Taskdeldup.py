# Write an application which will delete duplicate files
import os
import filecmp

def Delete_file(file1,file2):
    if not os.path.isfile(file1):
        print("1st file not exist")
    elif not os.path.isfile(file2):
        print("2nd file not exist")
    else:
        file_copm = filecmp.cmp(file1,file2)
        if file_copm == True:
            os.remove(file2)
            print('Success -> File is deleted')
        else:
            print('Failure -> Both the Files are different')

def main():
    file_1 = input("Enter the First File: ")
    file_2 = input("Enter the Second file: ")
    
    Delete_file(file_1, file_2)


if __name__ == "__main__":
    main()