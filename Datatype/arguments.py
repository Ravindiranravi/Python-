# def Addition(value_01,value_02):
#     print('Inside Addition')
#     print(' Argument:',value_01)
#     print(' Argument:',value_02)
#     Add = value_01+value_02
#     return Add
# def main():
#     output = Addition(12,13)
#     print('Addition',output)
# if __name__=="__main__":
#     main()   

#Area of a Circle
def Area(Radius,PI=3.14):
    print('PI Value',PI)
    print('Radius',Radius)
    Result = PI*Radius*Radius
    return Result

def main():
# Positional Argumentt
     #Output_1=Area(10,12)
     #print('Area of a circle:',Output_1)

# first argument is positional and second is default
       #Output_1=Area(10)
       #print('Area of a circle:',Output_1)


#keyword argument
    # Output_2 = Area(PI=3.14,Radius=12)
    # print('Area of a circle',Output_2)

#keyword argument and second is default
    Output_2 = Area(Radius=12)
    print('Area of a circle',Output_2)





if __name__ =="__main__":
    main()