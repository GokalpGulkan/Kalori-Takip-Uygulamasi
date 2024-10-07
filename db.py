# Veritabanını ve tablomuzu ayrı bir python dosyasında oluşturalım.

import mysql.connector as mysql 

# Veritabanı oluşturalım.
db = mysql.connect(host="localhost", user="root", passwd="root", port=3306)

mycursor = db.cursor()
mycursor.execute("CREATE DATABASE kalori_sayaci")
# Tablo oluşturalım
db = mysql.connect(host="localhost", user="root", passwd="root", database="kalori_sayaci", port=3306)
mycursor = db.cursor()
mycursor.execute("CREATE TABLE log_db (Fullname VARCHAR(50), Username VARCHAR(50), Password VARCHAR(50), Tall INT UNSIGNED, Weight INT UNSIGNED, Age SMALLINT UNSIGNED, Physical VARCHAR(50), Goal VARCHAR(50), Gender VARCHAR(50), personID INT PRIMARY KEY AUTO_INCREMENT, Kcal DOUBLE, Carb DOUBLE, Protein DOUBLE, Fat DOUBLE)")