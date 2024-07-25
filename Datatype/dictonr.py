# watch_details = {
#     'Titan':8000,
#     'Fastrack':5000,
#     'Omega':9000
# }

# print('Length :',len(watch_details))
# print('Type :',type(watch_details))
# print('using key :',watch_details['Titan'])
# print()


# watch_details = {
#     'Titan':8000,
#     'Fastrack':5000,
#     'Omega':9000,
#     'Cartier':8000
# }
# print('Length :',len(watch_details))
# print('Type :',type(watch_details))b      
# print('using key :',watch_details['Titan'])
# print('using key :',watch_details['Cartier'])
# print(watch_details)
# watch_details['Omega'] = 4000
# print('After modifying :',watch_details)
# watch_details['IWC'] = 5000
# print('After new watch :',watch_details)


#Create a dictionary of fooditems and price (add and modify) 

# fooditems = {
#     'Dosa':80,
#     'idly':50,
#     'chapathi':30,
#     'poori':40}
# print(fooditems)
# fooditems['idly'] = 40
# print('After modifying fooditems :',fooditems)
# fooditems['Pongal'] = 50
# print('After new fooditems added :',fooditems)

#Nested Dictionary
user = {
    'Ravibag' : {
        'firstname' :'Ravi',
        'lastname' : 'Kumar',
        'location' : 'Pondy'
    },
     'Kumarbag' : {
        'firstname' :'kumar',
        'lastname' : 'A',
        'location' : 'Gundy'
    },
    'Moorthybag' : {
        'firstname' :'Moorthy',
        'lastname' : 'A',
        'location' : 'Saithapet'
    }
}

# for id, details in user.items():
#     print(f"User ID: {id}")
#     print(f"First Name: {details['firstname']}")
#     print(f"Last Name: {details['lastname']}")
#     print(f"Location: {details['location']}")
#     print()

fname = user['Ravibag']
print(fname['firstname'])
print(fname['lastname'])
print(fname['location'])


list('hello')
print(list)