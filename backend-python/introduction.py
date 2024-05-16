# import mysql.connector

# db = mysql.connector.connect(
#     host = 'localhost',
#     user = 'root',
#     password = '',
#     database = 'NyobaBackendPy'
# )



# # #Membuat database baru
# cursor = db.cursor()
# cursor.execute("CREATE DATABASE NyobaBackendPy")

# # Membuat table baru
# cursor = db.cursor()
# cursor.execute(
#     """
#     CREATE TABLE users(
#     idUser INT AUTO_INCREMENT PRIMARY KEY,
#     username VARCHAR(100) NOT NULL,
#     password VARCHAR(100) NOT NULL,
#     namaDepan VARCHAR(100) NOT NULL,
#     namaBelakang VARCHAR(100) NOT NULL
#     )
#     """               
# )

# # # Memasukan data ke database
# cursor = db.cursor()
# query = "INSERT INTO users(username, password, namaDepan, namaBelakang) VALUES (%s, %s, %s, %s)"
# data = ("anbiya", "12345", "nusa", "putraku")

# cursor.execute(query, data)
# db.commit()
# print("table berhasil dibuat") 

# # Menampilkan dan Menghapus data pada Database
# cursor = db.cursor()
# showData = "SELECT * FROM users"
# cursor.execute(showData)

# # Menampilkan data dengan method fetchall
# result = cursor.fetchall()
# for i in result:
#     print(i)

# # Menampilkan data dengan method fetchone
# result = cursor.fetchone()
# print(result)

# # print("perbedaannya")

# while result is not None:
#     print(result)
#     result = cursor.fetchone()
    
# # Menghapus data
# cursor = db.cursor()
# deleteData = "DELETE FROM users WHERE idUser =%s"
# val = (2023004028, )
# cursor.execute(deleteData, val)


# print("data berhasil di hapus")
# db.commit()
    