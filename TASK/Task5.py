# 3 Question:Create a simple calculator which will take two input number from the
# user and give following option
# 1)Addition
# 2) Subtraction
# 3)Multiplication
# 4)Division
# (you can solve above question using normal function )
# (also try to solve using dictionary)


def Add(value_1,value_2):
    Ans = value_1+value_2
    return Ans

def Sub(value_1,value_2):
    Ans = value_1-value_2
    return Ans

def Mul(value_1,value_2):
    Ans = value_1*value_2
    return Ans

def Div(value_1,value_2):
    Ans = value_1/value_2
    return Ans


print('Choose operation')
print('1.Addition\n2.Subtration\n3.Multiplication\n4.Division')
select = int(input('Select 1/2/3/4:'))

def main():
    num01 = int(input('Enter 1st num'))
    num02 = int(input('Enter 2st num'))

    if(select == 1):
        Ans = Add(num01,num02)
        print(f'Addition {num01} and {num02}:',Ans)
    elif(select == 2):
        Ans = Sub(num01,num02)
        print(f'Subtration {num01} and {num02}:',Ans)
    elif(select == 3):
        Ans = Mul(num01,num02)
        print(f'Mutiplication {num01} and {num02}:',Ans)
    elif(select == 4):
        Ans = Div(num01,num02)
        print(f'Division {num01} and {num02}:',Ans)    
    else:
        print('choose 1/2/3/4')

if __name__=="__main__":
    main()