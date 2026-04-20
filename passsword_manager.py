MASTER_PASSWORD = "1234"
def authenticate():
    attempts = 3
    while attempts > 0:
        entered = input("Enter master password == ")
        if entered == MASTER_PASSWORD:
            print("Access granted.\n")
            return True
        else:
            attempts -= 1
            print(f"Wrong Password(Attempts left:{attempts})\n")
    print("Too many failed attempts.Exiting.")
    return False

def add_password():
    website = input("Enter website== ") 
    username = input("Enter username== ")
    password = input("Enter password== ") 

    with open("passwords.txt", "a") as file: 
        file.write(f"{website} | {username} | {password}\n")
        print("password saved successfully.\n")  
    
def view_passwords():  
    try:
        with open("passwords.txt", "r") as  file:
           printed_any = False 
           for line in file:
               print(line.strip())     
               printed_any = True 

        if not printed_any:
               print("No password ssved yet.\n")

    except FileNotFoundError: 
        print("No passwords file found yet.\n") 

def search_password():
        search_site = input("Enter site to search == ")
        try:
            with open("passwords.txt", "r") as file: 
                for line in file: 
                    if search_site.lower() in line.lower(): 
                        print("Found:", line.strip())
                        return 
                    print("No match found.\n")
        except FileNotFoundError:
            print("No passwords saved yrt.\n")
    
def main():
        while True: 
            print("PASSWORD MANAGER")
            print("1. Add Password")
            print("2. View Passwords")
            print("3. Search Password")
            print("4. Exit")

            choice = input("Choose an option:")
            if choice == "1":
                add_password()
            
            elif choice == "2":
                view_passwords()

            elif choice == "3":
                search_password()

            elif choice == "4":
                print("Goodbye") 
                break 
            else:
                print("Invalid option.\n")
if authenticate():
 main() 