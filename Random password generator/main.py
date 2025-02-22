# collect user preferences
# length
# should contain uppercase
# should contain special
# should contain digits

# get all available characters
# randomly pick characters up to the length
# ensure we have at least one of each character type
# ensure length is valid

import random
import string

def generate_password():
    # Get user input for password preferences
    length = int(input("Enter the desired password length: ").strip()) 
    include_uppercase = input("Include uppercase letters? (yes/no): ").lower().strip()  
    include_special = input("Include special characters? (yes/no): ").lower().strip()  
    include_digits = input("Include digits? (yes/no): ").lower().strip()  

    # Ensure the password length is at least 4
    if length < 4:
        print("Password length should be at least 4.")
        return

    # Define available character sets
    lower = string.ascii_lowercase  
    upper = string.ascii_uppercase  
    special = string.punctuation  
    digits = string.digits  


    all_characters = lower + upper + special + digits

    # Initialize the list to store required characters based on user input
    required_characters = []  
    if include_uppercase == 'yes':
        required_characters.append(random.choice(upper))  
    if include_special == 'yes':
        required_characters.append(random.choice(special))  
    if include_digits == 'yes':
        required_characters.append(random.choice(digits))  

    # Calculate how many more characters are needed
    remaining_length = length - len(required_characters)  
    password = required_characters  

    # Add random characters to fill up the remaining length
    for _ in range(remaining_length):  
        character = random.choice(all_characters)  
        password.append(character)

    random.shuffle(password)  

    str_password = ''.join(password) 

    # Display the generated password
    print("Generated Password:", str_password)  


generate_password()
