import random, csv, pandas, numpy, string

# letters
letters = 'abcdefghijklmnopqrstuvwxyz@.'

# dummy data for 'dataretrival' function
user_input_email = 'user@gmail.com'
user_input_password = 'passwd'

# retrieve login information from frontend
def dataretrival(user_input_email, user_input_password):
    global email
    email = user_input_email
    global password
    password = user_input_password
dataretrival(user_input_email, user_input_password)

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

# generates random salt
def randomSalt():
    character_list = []
    for i in range(0, 16):
        randomiser = random.choice(letters)
        character_list.append(randomiser)
    global salt
    salt = ''.join(character_list)
randomSalt()

# defines & combines salt with password & e-mail
combineSalt_password = [salt, password]
joinCombine1 = ''.join(combineSalt_password)

# defines hash function & hashes password
def hashPassword(joinCombine1, keyString, letters):
    hash_password = [letters.index(char.lower()) for char in joinCombine1]
    return ''.join(keyString[alpha] for alpha in hash_password)
DB_hashed_password = hashPassword(joinCombine1, keyString, letters)

DB_hash_key = keyString
DB_salt = salt
DB_email = email

def returnDB(email, DB_salt, DB_hash_key, DB_hashed_password):
    print("This is email used: ", email)
    print("This is salt used: ", DB_salt)
    print("This is hash key used: ", DB_hash_key)
    print("This is hashed password: ", DB_hashed_password)
    return email
    return DB_salt
    return DB_hash_key
    return DB_hashed_password
returnDB(email, DB_salt, DB_hash_key, DB_hashed_password)


''' --- Code Below This Line Is For Debugging Purposes --- '''
# user information for database
transfer_titles_to_DB = ['email', 'unique_salt', 'unique_hash_key', 'hashed_password']
transfer_data_to_DB = [email, DB_salt, DB_hash_key, DB_hashed_password]              
with open('Sensitive Database.csv', 'w', newline='') as SensitiveDatabase:
    transfer = csv.writer(SensitiveDatabase)
    transfer.writerow(transfer_titles_to_DB)
    transfer.writerow(transfer_data_to_DB)

# print user information from DB
SensitiveDatabase = pandas.read_csv('Sensitive Database.csv')
print("\n", "Stored Information in DB")
print(SensitiveDatabase)
