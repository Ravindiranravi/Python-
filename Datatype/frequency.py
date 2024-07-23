#dynamic input
def count_num(list,number):
    count = 0
    for i in list:
        if(i==number):
            count+=1
    return count




def main():
    #1
    print('Enter the size :')
    size = int(input())
    data_input=[]
    print('Enter the values:')
    for i in range(size):
        value = int(input())
        data_input.append(value)
    print('User List:',data_input)
    #2
    SearchNum= int(input('Enter the element to be checked:'))
    print(SearchNum ,"is repeated",count_num(data_input,SearchNum),"times")

if __name__ =="__main__":
    main()