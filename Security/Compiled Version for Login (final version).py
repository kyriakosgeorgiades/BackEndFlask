import csv, pandas, numpy, string

# letters
letters = 'abcdefghijklmnopqrstuvwxyz@.'

# defines user input
def userInput():
    global username
    username = input("Please Input Username: ")
    global password
    password = input("Please Input Password: ")
    global email
    email = input("Please Input E-Mail: ")
userInput()

# retrieves database information
data_list = []
with open('Sensitive Database.csv', 'r', newline='') as SensitiveDatabase:
    reader = csv.reader(SensitiveDatabase)
    for row in reader:
        data_list.append(row)
    retrieve = data_list[1]

# defines & combines salt with password & e-mail
combineSalt_password = [retrieve[1], password]
joinCombine1 = ''.join(combineSalt_password)

# defines hash function & hashes password
keyString = retrieve[2]
def hashPassword(joinCombine1, keyString, letters):
    hash_password = [letters.index(char.lower()) for char in joinCombine1]
    return ''.join(keyString[alpha] for alpha in hash_password)
hashedPasswordOutput = hashPassword(joinCombine1, keyString, letters)

# compares user inputted password & email to database for login
database_password = retrieve[3]
database_email = retrieve[4]
def checkLogin(database_password, database_email, hashedPasswordOutput, email):
    if database_password == hashedPasswordOutput:
        if database_email == email:
            print('Login Sucessful')
    if database_password != hashedPasswordOutput:
        print('Login Unsucessful')
        print('Password Incorrect')
    if database_email != email:
        print('Login Unsucessful')
        print('E-Mail Incorrect')
    if database_password != hashedPasswordOutput:
        if database_email != email:
            print('Login Unsucessful - Both Password & E-Mail Incorrect')
checkLogin(database_password, database_email, hashedPasswordOutput, email)
