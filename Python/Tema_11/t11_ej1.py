import sqlite3

db_connection = sqlite3.connect('OpenBootcamp.db')
db_cursor = db_connection.cursor()

db_cursor.execute("CREATE TABLE Alumnos(Id INT, Nombre TEXT, Apellido TEXT)")

db_cursor.execute("INSERT INTO Alumnos VALUES(1,'Guillermo', 'Dulce')")
db_cursor.execute("INSERT INTO Alumnos VALUES(2,'Alberto', 'Einstein')")
db_cursor.execute("INSERT INTO Alumnos VALUES(3,'Nicolas', 'Tesla')")
db_cursor.execute("INSERT INTO Alumnos VALUES(4,'Benjamin', 'Franklin')")
db_cursor.execute("INSERT INTO Alumnos VALUES(5,'Isaac', 'Newton')")
db_cursor.execute("INSERT INTO Alumnos VALUES(6,'Esteban', 'Hawkings')")
db_cursor.execute("INSERT INTO Alumnos VALUES(7,'Claudio', 'Ptolomeo')")
db_cursor.execute("INSERT INTO Alumnos VALUES(8,'Ada', 'Lovelace')")
db_cursor.execute("INSERT INTO Alumnos VALUES(9,'Guido', 'Van Rossum')")
db_cursor.execute("INSERT INTO Alumnos VALUES(10,'Alan', 'Turing')")
db_cursor.execute("INSERT INTO Alumnos VALUES(11,'Ricardo', 'Feinman')")

db_connection.commit()

db_cursor.execute("SELECT * FROM Alumnos WHERE Nombre = 'Guillermo'")

filas = db_cursor.fetchall()

print(filas)

db_connection.close()