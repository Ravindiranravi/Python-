#using for loop create a list of square numbers 
def numbers(): 
    n = int(input("Enter number:"))
    ans = [] 
    for i in range(1, n + 1): 
        ans.append(i * 2) 
    print(ans) 

if __name__ == "__main__": 
    numbers()