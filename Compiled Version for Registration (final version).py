import random, csv, pandas, numpy, string

# letters
letters = 'abcdefghijklmnopqrstuvwxyz@.'

# random key generation
upperLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowerLetters = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'

character_bank = [upperLetters, lowerLetters, numbers]
alphanumeric = ''.join(character_bank)

generated = []
for i in range(0, 32):
    randomiser = random.choice(alphanumeric)
    generated.append(randomiser)
join = ''.join(generated)
keyString = join

# defines user input
def userInput():
    global username
    username = input("Please Input Username: ")
    global password
    password = input("Please Input Password: ")
    global email
    email = input("Please Input E-Mail: ")

# generates random salt
def randomSalt():
    character_list = []
    for i in range(0, 16):
        randomiser = random.choice(letters)
        character_list.append(randomiser)
    global salt
    salt = ''.join(character_list)

# calls  user input & random salt functions
userInput()
randomSalt()

# defines & combines salt with password & e-mail
combineSalt_password = [salt, password]
joinCombine1 = ''.join(combineSalt_password)

# defines hash function & hashes password
def hashPassword(joinCombine1, keyString, letters):
    hash_password = [letters.index(char.lower()) for char in joinCombine1]
    return ''.join(keyString[alpha] for alpha in hash_password)
hashedPasswordOutput = hashPassword(joinCombine1, keyString, letters)

# user information for database
transfer_titles_to_DB = ['username', 'salt', 'key', 'hashed pass', 'email']
transfer_data_to_DB = [username, salt, keyString, hashedPasswordOutput, email]              
with open('Sensitive Database.csv', 'w', newline='') as SensitiveDatabase:
    transfer = csv.writer(SensitiveDatabase)
    transfer.writerow(transfer_titles_to_DB) # appends everytime, need to fix so only appears once / append user info only
    transfer.writerow(transfer_data_to_DB)

# print user information from DB
SensitiveDatabase = pandas.read_csv('Sensitive Database.csv')
print(SensitiveDatabase)
