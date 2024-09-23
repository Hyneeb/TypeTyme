import sqlite3
from password_hash import hash_password, verify_password

def create_database():
    connection = sqlite3.connect('typetyme.db')
    cursor = connection.cursor()
    cursor.execute(
        ''' CREATE table sample(
        username VARCHAR(50) UNIQUE,
        email VARCHAR(50) UNIQUE,
        password VARCHAR(50),
        wins INTEGER,
        WPM INTEGER)''')
    connection.close()
    
def add_user(data):
    username = data['username']
    email = data['email']
    password = hash_password(data['password'])
    if not(username and password and email):
        return False
    connection = sqlite3.connect("typetyme.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO sample VALUES (?, ?, ?, ?, ?)", (username, email, password, 0, 0))
    connection.commit()
    connection.close()
    return True

def read_data():
    connection = sqlite3.connect('typetyme.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM sample")
    fetched = cursor.fetchall()
    connection.close()
    return fetched

def delete_user(name):
    connection = sqlite3.connect('typetyme.db')
    cursor = connection.cursor()
    cursor.execute('''DELETE FROM sample WHERE username = ?;''', (name,))
    connection.commit()
    connection.close()

def check_info(data):
    email = data['email']
    connection = sqlite3.connect('typetyme.db')
    cursor = connection.cursor()
    cursor.execute(''' SELECT * FROM sample WHERE email = ?;''', (email,))
    fetched = cursor.fetchall()
    connection.close()
    if not fetched:
        return (1,)
    fetched = fetched[0]
    if not verify_password(fetched[2], data['password']):
        return (2,)
    else:
        return (3, fetched[0])
    
def find_user(email):
    connection = sqlite3.connect('typetyme.db')
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM sample where email = ?;''', (email,))
    fetched = cursor.fetchall()
    connection.close()
    if fetched:
        return fetched[0][0]
    else:
        return

def find_stats(name):
    connection = sqlite3.connect('typetyme.db')
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM sample where username = ?;''', (name,))
    fetched = cursor.fetchall()
    connection.close()
    if fetched:
        return fetched[0][3:]
    else:
        return

def update_stats(data):
    name = data['name']
    wins = data['wins']
    wpm = data['wpm']
    connection = sqlite3.connect('typetyme.db')
    cursor = connection.cursor()
    cursor.execute('''
            UPDATE sample 
            SET wins = ?, wpm = ? 
            WHERE username = ?;
        ''', (wins, wpm, name))
    connection.commit()
    connection.close()


## ________________________##
## personal commands 
## ________________________##
# # create_database()
# data = {'username':'jim', 'email':'2m@gmail.com', 'password': '124'}
# data2 = {'username':'hyneeb', 'email':'mhyder@gmail.com', 'password': '123'}
# print(check_info(data))
# # for i in check_info(data):
# #     print(i)
# add_user(data)
# update_stats({'wins': 2, 'name': 'hyneeb'})
# for i in read_data():
#     print(i)
# print(find_user('m@gmail.com'))
# print(find_stats('jim'))
# print(read_data())
# print(find_stats('hyneeb'))