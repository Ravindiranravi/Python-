import os

def file_to_append(file_name,content):
    if not os.path.exists(file_name):
        print(f'File not exists: {file_name}')
    else:
        file = open(file_name,'a')
        file.write(content)
        print()


def main():
    appendfile = input('Enter the File Name:')
    content =input('Enter the content:')
    file_to_append(appendfile,content)


if __name__ == "__main__":
    main()
