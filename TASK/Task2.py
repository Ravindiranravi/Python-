#Create a menu card list
#1)Dispaly Menu card
#2)Add Starter in the Menu card
#3)Update Starter in the Menu card
#4)Remove Starter in the Menu card
# veg_starter=['paneer 65','chilly','veg crispy']
# for i  in veg_starter:
#   print('The Menu Items are:',i)
def display(Veg_starter):
    print("Menu Card")
    for i in Veg_starter:
        print(i)
        
def add(Veg_starter):
    starter = input("Enter the starter to be Added : ")
    Veg_starter.append(starter)
    print("Item Added")
    return Veg_starter
 
def update(Veg_starter):
    select = input(" Enter starter name to Updated ")
    if select in Veg_starter:
        ind = Veg_starter.index(select)
        updated=input("Enter New Name to be Updated : ")
        Veg_starter[ind]=updated
        print(" Item Updated")
        return Veg_starter
    print("entered is not in menu")
    return Veg_starter
   
def remove(Veg_starter):
    select = input(" Enter starter name")
    if select in Veg_starter:
        Veg_starter.remove(select)
        print("Item removed")
        return Veg_starter
    print("Entered is not in menu")
    return Veg_starter
def main():
    Veg_starter = ['paneer 65','chilly paneer','veg crispy']
    while True:
        print("1. Menu Card Display")
        print("2.Add")
        print("3.Update")
        print("4.Remove")
        print("5.Exit")
        choice = int(input("Enter the choice:"))
        if choice==1:
            display(Veg_starter)
        elif choice==2:
            Veg_starter = add(Veg_starter)
        elif choice==3:
            Veg_starter= update(Veg_starter)      
        elif choice==4:
            remove(Veg_starter)    
        elif choice==5:
            break
       
 
if __name__ == "__main__":
    main()