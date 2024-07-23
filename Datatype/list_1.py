#Creating a list
#Creating a same datatype
course = ['Python','Java','PHP']#string
rollno = [123,456,789]#integer


#Creating Mixed Type
mixed_type = ['Ravi',123,True,67.68]
print('Heterogenous',mixed_type)
print('length',len(mixed_type))
#Positive Index
print('Access value of 1',mixed_type[0])
print('Access value of 2',mixed_type[1])
print('Access value of 3',mixed_type[2])
print('Access value of 4',mixed_type[3])
#Negative Index
print('Access value of 1',mixed_type[-4])
print('Access value of 2',mixed_type[-3])
print('Access value of 3',mixed_type[-2])
print('Access value of 4',mixed_type[-1])
#Slicing: [start:stop(excluded)]
print('Slicing',mixed_type[0:3]) 
print('Slicing',mixed_type[-4:-1]) 


#Mutable (can,change,add and delete)
fruits =['Mango','Banana','Grapes','Watermelon']
fruits[1] = 'Kiwi'
print(fruits)
print('Slicing',fruits[-4:-1])
fruits[1:3]=['apple','banana']
print(fruits)