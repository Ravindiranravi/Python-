#course = ['','python','java',',,','angu:lar','php']
#filter_output=['python','java','php']

# courses = ['', 'python', 'java', ',,', 'angu:lar', 'php']
# def is_valid_course(course):
#     return course.isalnum()
# filtered_output = list(filter(is_valid_course, courses))
# print(filtered_output)

def checkSplletter(checkSplChar):
    special_Char = ['!','@','#','$','%','^','&','*','(',')','-','_','/','?','~',',','<','>','.',':',';','\'','\"','+','=','[',']','{','}']
    for ch in checkSplChar:
        if ch in special_Char:
            return False
        else:
            continue
    return checkSplChar    
      
    

def main():
    # print('Reduce Value ',reduce_list)
    course = ['','Python','java',',,','angul:ar','php']

    filter_list = list(filter(checkSplletter,course))
    print('Filter List : ',filter_list)
if __name__ == '__main__':
    main()