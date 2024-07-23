#Create a tuple
#Hemogenus
student_id = (123,456,357,123)
ice_cream = ('Vanilla','Choco-chips','Blueberry')

#Heterognus
mixed_type = (123,'hello',False,56.78)
#len()
print("length of student id ",len(student_id))
#using index ==> Blueberry(Positive index)
print("length of student id ",ice_cream[2])
#using index ==> False(Negative index)
print("length of student id ",mixed_type[-2])
#using slicing ==> 'Hello',False
print("length of student id ",mixed_type[1:3])

ce_creame = ('Vanilla')        # str
print(ice_cream,type(ice_cream))
ice_creame = ('Vanilla',)       # comma (tuple)
print(ice_cream,type(ice_cream))

"""# immutable
mixed_type[0] = True
print("False ",mixed_type)"""

ice_cream = ('Vanilla','Choco-chips','Blueberry','Vanilla')
countmethod = ice_cream.count('Vanilla')
print('Count Method:',countmethod)
print()
indexmethod = ice_cream.index('Vanilla')
print('Index Method:',indexmethod)