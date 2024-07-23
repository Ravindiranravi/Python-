# def Addition():
#     print('Inside Addition')#No parameter,argument,return
    
# Addition()


# def Addition(value_01,value_02):
#     print('Inside Addition')
#     print(' Argument:',value_01)
#     print(' Argument:',value_02)
#     print(f'{value_01} and {value_02} addition is:',value_01+value_02)
# Addition(12,13)

def Addition(value_01,value_02):
    print('Inside Addition')
    print(' Argument:',value_01)
    print(' Argument:',value_02)
    Add= value_01+value_02
    Sub= value_01-value_02
    return Add,Sub
Result1,Result2 = Addition(12,13)
print('Addition:',Result1)
print('Subtraction:',Result2)

# def Subtraction(value_01,value_02):
#     print('Inside Addition')
#     print(' Argument:',value_01)
#     print(' Argument:',value_02)
#     Sub= value_01-value_02
#     return Sub
# Result = Subtraction(121,77)
# print('Subtraction:',Result)