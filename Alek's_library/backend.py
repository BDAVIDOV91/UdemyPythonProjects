import sqlite3

# Creating the database for the librbary for each button
def connect():
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, runr text)')
    conn.commit()
    conn.close()
    
def insert(title, author, year, runr):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO book VALUES (NULL, ?, ?, ?, ?)', (title, author, year, runr))
    conn.commit()
    conn.close()
    
def view():
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM book')
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title = '', author = '', year = '', runr = ''):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR runr = ?', (title, author, year, runr))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM book WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    
def update(id, title, author, year, runr):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute('UPDATE book SET title = ?, author = ?, year = ?, runr = ? WHERE id = ?', (title, author, year, runr, id))
    conn.commit()
    conn.close()


connect()
#insert()
#delete(5)
#update(1, 'Astrophysics for People in a Hurry', ' Neil deGrasse Tyson ', 2017, 'Yes')
#print(view())
#print(search())