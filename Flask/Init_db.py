import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO author (authorid,name,priority) VALUES (?,?,?)",
            ('1','Thanh Son','nope')
            )
cur.execute("INSERT INTO author (authorid,name,priority) VALUES (?,?,?)",
            ('2','Anh Son','nope')
            )
cur.execute("INSERT INTO book (bookid, title,authorid) VALUES (?,?,?)",
            ('1', 'Dragonball Z','1')
            )
cur.execute("INSERT INTO book (bookid, title,authorid) VALUES (?,?,?)",
            ('2', 'Dragonball Supper','2')
            )

connection.commit()
connection.close()