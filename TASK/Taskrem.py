import os
def file_to_delete(file_name):
    if not os.path.exists(file_name):
        print(f'File not exists: {file_name}')
    else:
         os.remove(file_name)
    print("File removed....")

def main():
    file_name = input('Enter the File Name')
    file_to_delete(file_name)
if __name__ == "__main__":
    main()