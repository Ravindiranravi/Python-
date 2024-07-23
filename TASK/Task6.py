# 4 question:Write a program which will count the frequency of letters of the string

def Repetition(string,letter):
    count=0
    for i in string:
        if(i==letter):
            count+=1
    return count

def main():
    string=input('Enter the string: ')
    letter=input('Enter the letter to check the Repetition : ')
    count=Repetition(string,letter)
    print(count)

if __name__=="__main__":
    main()