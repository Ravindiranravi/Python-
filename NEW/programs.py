import datetime
today = datetime.date.today()
year = today.year
print(year)

# try:
    # num_1 = int(input('Enter the the num 1:'))
    # num_2 = int(input('Enter the the num 2:'))
    # result = num_1/num_2
    # print(result)
    # items =['Bread','Butter','Jam','Cheese']
    ## items[len(items)]='Spread' 
    # num1 = int (input('Enter the num 1:'))
    # assert num1%2==0
 

# except ZeroDivisionError:
#     print('Error :Denominator cannot be Zero') 

# except ValueError:
#     print('Only Numbers are allowed')

# except IndexError:
#     print('Kindlly use insert or append method')

# except AssertionError:
#     print('Enterred valuse not matching the Condition')
# # else:
# #     print(num1,'is even')
# finally:
#     print('Program is Over')

yob = int(input('Enter your yaer of birth:'))
age = year - yob
if(age<18):
    raise Exception(f'The Age should be greater than 18 and the age is {age}')
print(age)
