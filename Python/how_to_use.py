import J_DB_LIB as j

# Set your credentials
j.set_credentials(host="localhost", user="root", password="", database="__YOUR_DB_NAME__")

# Make new table
j.execute("CREATE TABLE main (id INT, name VARCHAR(200))")

# Display list of tables
print(j.execute("SHOW TABLES;"))

# Select info
result = j.execute("SELECT * from main;")
print(result)

# Insert info
info = {
	"id": "1", 
	"name": "Jason"
}
j.insert("main", info)

# Update info
new_info = {
	"id": "10", 
	"name": "Ken"
}
j.update("main", new_info, where="id=1")

# Delete info
j.execute("DELETE from main WHERE id='10'")

# Select info
result = j.execute("SELECT * from main;")
print(result)
