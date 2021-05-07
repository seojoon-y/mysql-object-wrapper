# mysql-object-wrapper
Isn't it annoying to have to structure queries every time you use MySQL?
I've had the same problem, so I built a simple wrapper to easily convert objects into MySQL statements.

## examples
For example, you can write this:
```
info = {
	"id": "1", 
	"name": "Jason"
}
j.insert("main", info)
```
Rather than this:
```
mydb = conn.connect(**credentials)
mycursor = mydb.cursor()
sql = "INSERT INTO main (id, name) VALUES (%s, %s)"
vals = ["1", "Jason"]
mycursor.executemany(sql, [vals])
mydb.commit()
mycursor.close()
mydb.close()
```
