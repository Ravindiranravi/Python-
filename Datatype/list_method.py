menu_card=['panner','Dal','rice']
print('avaliable items',menu_card)
#append()--> adds an element at the end of the list 
menu_card.append('kofta')
print('after append method avaliable items',menu_card)

#extend() --> add the elements of the list to the end of the list
menu_card.extend(['dal tadaka','biriyani'])
#menu_card.extend('Biriyani')
print("using extend method",menu_card)

#insert --> Adds an element at the specified position
menu_card.remove('rice')
print('Using Insert method:',menu_card)

#remove --> removes a specified values
menu_card.insert(1,'dal tadaka')
print('Using Remove method:',menu_card)

#pop() --> removes an element at the specified position
menu_card.pop(2)
print('Using pop method:',menu_card)
menu_card = ['Panner','Biriyani','Dosa','Panner']

#Index method

Index_method = menu_card.index('Dosa')
print('It will give the position : ',Index_method)

Index_method = menu_card.index('Panner')
print('It will give the position : ',Index_method)


#Sort method
menu_card.sort()
print('Using Sort Method : ',menu_card)

