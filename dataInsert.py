import sqlite3

connection = sqlite3.connect("contestants.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE fighters (name TEXT,bg TEXT,fg TEXT,powerlevel INTEGER)")
cursor.execute("INSERT INTO fighters VALUES ('Quicksilver','light blue','white',6)")
cursor.execute("INSERT INTO fighters VALUES ('Black Widow','black','red',2)")
cursor.execute("INSERT INTO fighters VALUES ('Hawkeye','purple','yellow',2)")
cursor.execute("INSERT INTO fighters VALUES ('Hulk','green','yellow',9)")
cursor.execute("INSERT INTO fighters VALUES ('Iron Man','red','yellow',7)")
cursor.execute("INSERT INTO fighters VALUES ('Captain America','blue','white',5)")
cursor.execute("INSERT INTO fighters VALUES ('Thor','gray','yellow',9)")

cursor.execute("INSERT INTO fighters VALUES ('Wonder Man','green','red',9)")
cursor.execute("INSERT INTO fighters VALUES ('Tigra','orange','blue',4)")
cursor.execute("INSERT INTO fighters VALUES ('Ms Marvel','blue','yellow',8)")

connection.commit()
connection.close()

