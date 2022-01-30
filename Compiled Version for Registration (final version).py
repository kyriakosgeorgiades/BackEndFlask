'''Hashing System using Artificial Intelligence for Registration Page'''
# NEEDS FRONTEND & BACKEND IMPLEMENTATION / CONNECTIONS
import random, csv
import sys, pandas, numpy, csv, tensorflow, keras, os, string
from pandas import read_csv
from numpy import loadtxt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# https://codebeautify.org/random-alphanumeric-generator

# letters
letters = 'abcdefghijklmnopqrstuvwxyz@.'

# random key generation
key = []

def AI_Key_Gen():
    dataset = read_csv('Hash_Key_Database.csv')

    targetVar = ['User']
    predVar = ['Hash_1', 'Hash_2', 'Hash_3']
    Y = dataset[targetVar].values
    X = dataset[predVar].values

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.01)
    
    model = LinearRegression()
    model.fit(X_train, Y_train)

    predict_NK = model.predict(X_test)
    retrieve = predict_NK[0]
    retrieve2 = retrieve[0]

    change_type = str(retrieve2)
    remove_char = change_type.replace('.', '')
    key.append(remove_char)


for i in range(0,2):
    AI_Key_Gen()
    
hash_key = key[0] + key[1]

keyString = hash_key

# defines user input
def userInput():
    global username
    username = input("Please Input Username: ")
    global password
    password = input("Please Input Password: ")
    global email
    email = input("Please Input E-Mail: ")

# defines & generates random salt
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
SensitiveDatabase = read_csv('Sensitive Database.csv')
print(SensitiveDatabase)

'''Breakpoint to Keep Program Active at the End'''
input("\n Tap 'Enter' to Exit Program: ")
