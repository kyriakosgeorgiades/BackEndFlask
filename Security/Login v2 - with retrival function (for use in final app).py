import csv, pandas, numpy, string

# dummy data for 'dataretrival' function
user_input_email = 'user@gmail.com'
user_input_password = 'passwd'
DB_email = 'user@gmail.com'
DB_hashed_password = '3zKuLZuXYNPzlbiKvfPPy3'
DB_hash_key = 'fZz3LmEbWusjuSlvryPuXNyYiIVKc154'
DB_salt = 'dc.tebtuxvscohy.'

# retrieve login information from backend & frontend
def dataretrival(user_input_email, user_input_password, DB_email, DB_hashed_password, DB_hash_key, DB_salt):
    global email
    email =  user_input_email
    global password
    password =  user_input_password
    global database_email
    database_email = DB_email
    global database_hashed_password
    database_hashed_password = DB_hashed_password
    global database_hash_key
    database_hash_key = DB_hash_key
    global database_salt
    database_salt = DB_salt
dataretrival(user_input_email, user_input_password, DB_email, DB_hashed_password, DB_hash_key, DB_salt)

# defines & combines salt with password & e-mail
combineSalt_password = [database_salt, password]
joinCombine1 = ''.join(combineSalt_password)

# defines hash function & hashes password
keyString = database_hash_key
letters = 'abcdefghijklmnopqrstuvwxyz@.'
def hashPassword(joinCombine1, keyString, letters):
    hash_password = [letters.index(char.lower()) for char in joinCombine1]
    return ''.join(keyString[alpha] for alpha in hash_password)
user_hashed_password = hashPassword(joinCombine1, keyString, letters)

# compares user inputted password & email to database for login
def returnLoginStatus(user_hashed_password, database_hashed_password):
    if user_hashed_password == database_hashed_password:
        print("Login Successful", "\n")
        return "Login Accepted"
    if user_hashed_password != database_hashed_password:
        print("Login Unsuccessful", "\n")
        return "Login Failure"
returnLoginStatus(user_hashed_password, database_hashed_password)

''' --- Code Below This Line Is For Debugging Purposes --- '''
# retrieves database information
data_list = []
with open('Sensitive Database.csv', 'r', newline='') as SensitiveDatabase:
    reader = csv.reader(SensitiveDatabase)
    for row in reader:
        data_list.append(row)
    retrieve = data_list[0]
    retrieve2 = data_list[1]
print("Stored Information in DB")
print(retrieve)
print(retrieve2)
