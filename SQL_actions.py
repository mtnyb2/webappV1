import sqlite3
conn = sqlite3.connect('Manual Database.db') 
cursor = conn.cursor()

table = """CREATE TABLE TinyWorker (id CHARACTER(10) PRIMARY KEY,
                 name VARCHAR(255),
                        fname VARCHAR(255));
"""

#cursor.execute('''DROP TABLE TinyWorker''')

cursor.execute(table)

def insert_new_worker (id, name, fname):
    print (type(name) , type(fname))
    if type(name)!=str or type(fname)!=str:
        print(f"{name} or {fname} is invalid")
        return
    else: 
        print 
        name = f'\"{name}\"'
        fname = f'\"{fname}\"'
        cursor.execute('''INSERT INTO TinyWorker VALUES (?, ?, ?)''', (id, name, fname))

insert_new_worker(5727,Paz, Saportas)

print("Data Inserted in the table: ") 
data=cursor.execute('''SELECT * FROM TinyWorker''') 
for row in data:
    print(row)

conn.close()