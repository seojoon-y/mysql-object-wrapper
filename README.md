# mysql-object-wrapper
Isn't it annoying to have to structure queries every time you use MySQL?
I've had the same problem, so I built a simple wrapper to easily convert objects into MySQL statements.
It's available for **Python** and **Node.Js** programming languages.

## Examples
For example, you can write this:
```
info = {
	"id": "1", 
	"name": "Jason"
}
j.insert("main", info)
```
Rather than this madness:
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
## How to Use
- Make sure to install the actual `mysql` library.
- Click on the folder `Python` or `NodeJs` on this Github repo to choose your coding language.
- Copy the `mysql_object_wrapper.*` code into your project folder.
- Import the file and ues the functions in your code.
- Examples are provided in the folder.

