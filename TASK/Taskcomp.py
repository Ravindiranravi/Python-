import os
import filecmp

def compare_files(filename1, filename2):
    if not os.path.exists(filename1):
        print(f'Not Exist: {filename1}')
    
    elif not os.path.exists(filename2):
        print(f'Not Exist: {filename2}')
    
    else:
        compare = filecmp.cmp(filename1, filename2)
        if compare:
            print('Success -> The files are the same')
        else:
            print('Failure -> The files are different')

def main():
        print("Compare Files:")
        file1_compare = input('Enter the name of the first file to compare: ')
        file2_compare = input('Enter the name of the second file to compare: ')
        compare_files(file1_compare, file2_compare)

if __name__ == "__main__":
    main()