# 5 question:Write a program to check if a string contains any special character
def specialcharacter(input_string):
   
    special_characters = "!@#$%^&*()-_=+[{]}\\|;:\',<.>/?`~"

    
    for char in input_string:
     
        if char in special_characters:
            return True
    
    return False

def main():
    input_str = input("Enter a string to check for special characters: ")

    if specialcharacter(input_str):
        print(f"The string '{input_str}' contains special characters.")
    else:
        print(f"The string '{input_str}' does not contain any special characters.")

if __name__ == "__main__":
    main()
