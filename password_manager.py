
## userlogin  and signup
## create a directory for the user  
## encrypting and storing passwords and usernames for a particular username in text file
## decrypting passoword and username of the user

import os

CONST = 2



def main():
    
    get_paths = import_path()
    print("Welcome to the password manager!. This app is useful in storing your passwords in a encrypted way.")
    user_input = input("Enter signup if you are new to the password manager or Login to see or update your passwords. ").lower()
    match user_input:
        case "login":
            log, file_name = login(get_paths)
            print(log)
            if (log == "Login Successful"):
                print("Do you want to see your previously saved passwords or you want to add new passwords to your account? ")
                user_choice = input("Enter 1 to update your account . 2 to read your saved passwords ")
                match user_choice:
                    case  "1":
                        update_user_account(get_paths, file_name)
                    case "2":
                        show_saved_passwords(get_paths, file_name)
                    case _:
                        print("Invalid Input")
        case "signup":
            print(signup(get_paths))

        case _:
            print("Invalid Input")    
        

## user signup
def signup(path):
    
    set_user_name = get_username()
    set_password = get_password()
    name = ["User_Details", "Database"]
    
    for x in range(CONST):
        os.chdir(path[name[x]])
        file_name = set_user_name + ".txt"
        if (file_name) in os.listdir():
            return (f"User {set_user_name} already exists. Log in")
            
        file4 = open(file_name, "a")
    store_user_name = cipher(set_user_name, 22, "encode")
    store_password = cipher(set_password, 22, "encode")
    data_to_store = [store_user_name, store_password]
    
    with open(file_name, "a") as file2:
        for x in range(CONST):
            file2.write(data_to_store[x])
            

    return ("Sign up successful")    
    
    
# userlogin 
def login(path):
    user_name = get_username()
    password = get_password()
    os.chdir(path["Database"])
    
    file_name = user_name + ".txt"

    entered_cred = user_name + password
    if file_name not in os.listdir():
        return (f"""Sorry we couldn't find the user with the username {user_name}.
Kindly Sign up if you have not already or try logging in with a different user name"""), f"{user_name}"
    else:
        with open(file_name) as file3:
            correct_cred = file3.read()
            correct_cred = cipher(correct_cred, 22, "decode")
            if (correct_cred != entered_cred):
                return ("Invalid Password"),  f"{user_name}"
            else:
                return ("Login Successful"), file_name    
            
def cipher(text, shift, direction):
    if (direction == "decode"):
        shift *= -1 
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    Alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']        
        
    text = list(text) # converts the text to list as string is immutable (values can't be updated for a string)
    ## replacing the text with encryption    
    for i in range(0, len(text)):
        if (text[i] in alphabet):           
            for j in range(0, len(alphabet)):# iterates through the list and replaces the letter with encrypted letter
            
                if (text[i] == alphabet[j]):
                    count = shift + j
                    while (count >= 26):
                        count -= 26
                        
                    while (count < 0):
                        count += 26
                    
                    
                    text[i] = alphabet[count]
                    break
        elif (text[i] in Alphabet):
            for j in range(0, len(alphabet)):# iterates through the list and replaces the letter with encrypted letter
            
                if (text[i] == Alphabet[j]):
                    count = shift + j
                    while (count >= 26):
                        count -= 26
                        
                    while (count < 0):
                        count += 26
                    
                    
                    text[i] = Alphabet[count]
                    break
            
    cipher_text = "".join(text)
    return cipher_text
        
def update_user_account(paths, file_name):
    os.chdir(paths["User_Details"])
    with open(file_name, "a+") as file10:
        updates = input("Enter the username and password you want to store in the file with a gap of a space\n").strip()
        
        updates = cipher(updates, 22, "encode")
        
        file10.write(updates)
        file10.write("\n")

def show_saved_passwords(paths, file_name):
    os.chdir(paths["User_Details"])
    with open(file_name) as file100:
        
        encrypted_data = file100.read()
        data = cipher(encrypted_data, 22, "decode")
        print(data)

def import_path():
    ## this is the file that contains the location of the files where location of the file  
    os.chdir(r"C:\Users\panka\OneDrive\Desktop\KIDS\Aryan\code_wars")
    paths = {"User_Details": "", "Database": ""}
    name = ["User_Details", "Database"]
    with open("paths.txt") as file1:
        
        for x in range(CONST):
            txt = file1.readline()
            txt = txt.replace("\n", "")
            txt = txt.split(" ")
            path = txt[1]
            paths[name[x]] = path
    return paths



                
def get_username():
    username = input("Username: ").strip()
    return username

def get_password():
    password = input("Password: ").strip()
    return password




    
    

if __name__ == "__main__":
    main()
