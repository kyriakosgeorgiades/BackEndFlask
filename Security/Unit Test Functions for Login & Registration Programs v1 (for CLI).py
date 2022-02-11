''' Program to Unit Test in Unittest Framework for Functions in Login & Registration Programs'''

# Imports All Functions/Modules used in Registration & Login for the Purpose of Unit Testing
import unittest, csv, pandas, numpy, string, random

# Username Function - In both Login & Registration Programs
def UserName(username):
    username = input("Please Input Username: ")
    print("This is the username: ", username, "\n")
    return {"username": "username"}

# User Password Function - In both Login & Registration Programs
def UserPassword(password):
    password = input("Please Input Password: ")
    print("This is the password: ", password, "\n")
    return {"password": "passwd"}

# User Email Function - In both Login & Registration Programs
def UserEmail(email):
    email = input("Please Input E-Mail: ")
    print("This is the email: ", email, "\n")
    return {"email": "email@gmail.com"}

# Random Salt Generation Function - In Registration Program Only
def RandomSalt(randomsalt):
    letters = 'abcdefghijklmnopqrstuvwxyz@.'
    character_list = []
    for i in range(0, 16):
        randomiser = random.choice(letters)
        character_list.append(randomiser)
    salt = ''.join(character_list)
    print("This is the random salt: ", salt, "\n")
    return {"randomsalt": "successful random salt"}

# Random Key Generation Function - In Registration Program Only
def RandomHashKey(randomhashkey):
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
    print("This is the random hash key: ", keyString, "\n")
    return {"randomhashkey": "successful random hash key"}

# Combine Salt & Password Function - In both Login & Registration Programs
def CombineSaltPassword(saltedpassword):
    salt = "mimic_random_gen"
    password = "passwd"
    combineSalt_Password = [salt, password]
    joinCombine1 = ''.join(combineSalt_Password)
    print("This is the combined salt and password: ", joinCombine1, "\n")
    return {"saltedpassword": "successful salted password"}

# Hashing Password Function - In both Login & Registration Programs
def HashPassword(hashpassword):
    letters = 'abcdefghijklmnopqrstuvwxyz@.'
    joinCombine1 = 'saltedpassword'
    keyString = 'kAyMLzpB4YLaYkpLQed2oVM4ddH9g020'
    hash_password = [letters.index(char.lower()) for char in joinCombine1]
    hash_password2 = ''.join(keyString[alpha] for alpha in hash_password)
    print("This is the hashed password: ", hash_password2, "\n")
    return {"hashpassword": "successful hashed password"}

# Sending Data to Sensitive Database & Printing It Function - In Registration Program Only
def TransferToDB(SensitiveDatabaseTransferal):
    transfer_titles_to_DB = ['username', 'salt', 'key', 'hashed pass', 'email']
    username = 'user'
    salt = 'salt'
    keyString = 'keyString'
    hashedPasswordOutput = 'hashed pass'
    email= 'email@gmail.com'
    transfer_data_to_DB = [username, salt, keyString, hashedPasswordOutput, email]              
    with open('Sensitive Database.csv', 'w', newline='') as SensitiveDatabase:
        transfer = csv.writer(SensitiveDatabase)
        transfer.writerow(transfer_titles_to_DB)
        transfer.writerow(transfer_data_to_DB)
    SensitiveDatabase = pandas.read_csv('Sensitive Database.csv')
    print("This is the Sensitive Database that was Sent to File")
    print(SensitiveDatabase, "\n")
    return {"SensitiveDatabase": "successful transfer & print DB"}

# Retrival of Sensitive Database Information Function - In Login Program Only
def RetrivalOfDB(SensitiveDatabaseRetrival):
    data_list = []
    with open('Sensitive Database.csv', 'r', newline='') as SensitiveDatabase:
        reader = csv.reader(SensitiveDatabase)
        for row in reader:
            data_list.append(row)
        retrieve = data_list[1]
    print("This is the Sensitive Database thaat was Retrieved from File")
    print(data_list, "\n")
    return {"SensitiveDatabaseRetrival": "successful retrieve DB"}

# Comaprison of DB to User Input Function (part 1) - In Login Program Only
def checkPass_and_Email(Pass_and_Email):
    database_password = 'password'
    hashedPasswordOutput = 'password'
    database_email = 'email@gmail.com'
    email = 'email@gmail.com'
    if database_password == hashedPasswordOutput:
        if database_email == email:
            print('Login Sucessful', "\n")
            return {"Pass_and_Email": "Login Sucessful"}
            
# Comaprison of DB to User Input Function (part 2) - In Login Program Only
def checkPass(Pass):
    database_password = 'password'
    hashedPasswordOutput = 'incorrectpassword'
    if database_password != hashedPasswordOutput:
        print('Login Unsucessful')
        print('Password Incorrect', "\n")
        return {"Pass": "Login Unsucessful"}
        
# Comaprison of DB to User Input Function (part 3) - In Login Program Only
def checkEmail(email):
    database_email = 'email@gmail.com'
    email = 'incorrectemail@gmail.com'
    if database_email != email:
        print('Login Unsucessful')
        print('E-Mail Incorrect', "\n")
        return {"email": "Login Unsucessful"}
        
# Comaprison of DB to User Input Function (part 4) - In Login Program Only
def checkPass_and_Email2(Pass_and_Email2):
    database_password = 'password'
    hashedPasswordOutput = 'incorrectpassword'
    database_email = 'email@gmail.com'
    email = 'incorrectemail@gmail.com'
    if database_password != hashedPasswordOutput:
        if database_email != email:
            print('Login Unsucessful - Both Password & E-Mail Incorrect', "\n")
            return {"Pass_and_Email2": "Login Unsucessful - Both Password & E-Mail Incorrect"}
            
# Class Function to Complete All Unit Tests
class testingFunctions(unittest.TestCase):
    # Username Test
    def testUserName(self):
        actual = UserName(username=[""])
        expected = {"username": "username"}
        self.assertEqual(actual, expected)
        
    # User Password Test
    def testUserPassword(self):
        actual = UserPassword(password=[""])
        expected = {"password": "passwd"}
        self.assertEqual(actual, expected)
        
    # User Email Test
    def testUserEmail(self):
        actual = UserEmail(email=[""])
        expected = {"email": "email@gmail.com"}
        self.assertEqual(actual, expected)
        
    # Random Salt Generation Test
    def testRandomSalt(self):
        actual = RandomSalt(randomsalt=[""])
        expected = {"randomsalt": "successful random salt"}
        self.assertEqual(actual, expected)
        
    # Random Hash Key Generation Test
    def testRandomHashKey(self):
        actual = RandomHashKey(randomhashkey=[""])
        expected = {"randomhashkey": "successful random hash key"}
        self.assertEqual(actual, expected)
        
    # Combine Salt Password Test
    def testSaltPassword(self):
        actual = CombineSaltPassword(saltedpassword=[""])
        expected = {"saltedpassword": "successful salted password"}
        self.assertEqual(actual, expected)
        
    # Hashing the Password Test
    def testHashPassword(self):
        actual = HashPassword(hashpassword=[""])
        expected = {"hashpassword": "successful hashed password"}
        self.assertEqual(actual, expected)
        
    # Sending Data To & Printing Sensitive Database Test
    def testTransferToDB(self):
        actual = TransferToDB(SensitiveDatabaseTransferal=[""])
        expected = {"SensitiveDatabase": "successful transfer & print DB"}
        self.assertEqual(actual, expected)
        
    # Retrieve Data from Sensitive Database Test
    def testRetriveDB(self):
        actual = RetrivalOfDB(SensitiveDatabaseRetrival=[""])
        expected = {"SensitiveDatabaseRetrival": "successful retrieve DB"}
        self.assertEqual(actual, expected)
        
    # Comaprison of DB to User Input Function (part 1) - Test
    def testComparison1(self):
        actual = checkPass_and_Email(Pass_and_Email=[""])
        expected = {"Pass_and_Email": "Login Sucessful"}
        self.assertEqual(actual, expected)
        
    # Comaprison of DB to User Input Function (part 2) - Test
    def testComparison2(self):
        actual = checkPass(Pass=[""])
        expected = {"Pass": "Login Unsucessful"}
        self.assertEqual(actual, expected)
        
    # Comaprison of DB to User Input Function (part 3) - Test
    def testComparison3(self):
        actual = checkEmail(email=[""])
        expected = {"email": "Login Unsucessful"}
        self.assertEqual(actual, expected)
        
    # Comaprison of DB to User Input Function (part 4) - Test
    def testComparison4(self):
        actual = checkPass_and_Email2(Pass_and_Email2=[""])
        expected = {"Pass_and_Email2": "Login Unsucessful - Both Password & E-Mail Incorrect"}
        self.assertEqual(actual, expected)
        
# Main Function to Complete & Run Unit Test
if __name__ == '__main__':
    unittest.main()
