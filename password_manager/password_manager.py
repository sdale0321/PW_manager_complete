from cryptography.fernet import Fernet

'''
def write_key():#key + password + text to encrypt = random text 
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key) ''' #changed to 'load_key'

def load_key(): 
    file = open("key.key", "rb") #'rb' opens the file in binary format for reading
    key = file.read() #reads file
    file.close() #closes file 
    return key #whenever a file is opened, it needs to be closed.  If not using a method that will automatically take care
    #of this, you have to explicitly state it 

key = load_key() #.encode is turning the PW into bytes 
fer = Fernet(key) #this is initializing an encryption module 

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|") #splits the data up based on the character put into the parameter
            #when declaring 2 elements equal to the split operator, the 1st element is assigned to the 1st item that was split and so on 
            print("User: ", user, "| Password: ", fer.decrypt(passw.encode()).decode())

def add():
    name = input('Account Name: ')
    pwd = input("Password: ")
    #'with' keyword means that the file will automatically close once the code is performed 
    with open('passwords.txt', 'a') as f: 
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n") 

'''
open requires two parameters, name of the file and the mode to open it in
the main modes are 'w', 'a' and 'r'.  'w' write mode opens a file in write mode meaning it clears the file 
 'r' read mode opens it in read mode which means you can't alter it but only read its data
 'a' append mode allows you to add something to the end of an existing file and if a file doesn't exist it'll create a new one. 
 - 'a' allows you to read and write/ create new file if it doens't exist``'''        

while True:
    mode = input("Would you like to add a new password or view existing ones (add/view), press q to quit? ")

    if mode == "q": 
        break

    if mode == "view": 
        view()
    elif mode == "add":
        add()
    else: 
        print("Invalid mode.")
        continue
