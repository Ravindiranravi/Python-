# def sum_all(*args):
#     count = 0
#     for i in args:
#         count+=i
#     return count
# output = sum_all(1,2,3,4,5)
# print('Addition:',output)




# def main(*args):
#      for name in args:
#       for i in name:
#           print(i)

# if __name__ == '__main__':
#     main(['Raghul','Vijay','Manoj','Deva'])


def StaffDetails(**kwarg):
    for key,value in kwarg.items():
        print(f'{key} is {value}')
#StaffDetails(Name='Ravi',Age=21,MobileNum=1123445)
def main():
    changepond = {'Name':'Suresh',
                  'Age':21,
                  'MobileNum':1123445}
    StaffDetails(**changepond)
    

if __name__ == '__main__':
     main()