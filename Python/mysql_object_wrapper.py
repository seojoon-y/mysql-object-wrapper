# COPYRIGHT SEOJOON YEON, 2020 Feb 13 - 

import urllib.parse
from mysql import connector as conn

credentials = None

def set_credentials(host, user, password, database):
	global credentials
	credentials = {
		'host': host,
		'user': user,
		'passwd': password,
		'database': database
	}

def insert(table, dictionary):
	# Connection
	global conn, credentials
	assert credentials != None, fail_return("Please set the credentials first, by using j.set_credentials()")
	mydb = conn.connect(**credentials)
	mycursor = mydb.cursor()
	# SQL
	columns, values = dictionary.keys(), dictionary.values()
	keys = ", ".join(columns)
	masks = ", ".join(list(["%s"]*len(columns)))
	vals = list(map(str, list(values)))
	sql = f"INSERT INTO {table} ({keys}) VALUES ({masks})"
	# Execution
	mycursor.executemany(sql, [vals])
	mydb.commit()
	mycursor.close()
	mydb.close()

def update(table, dictionary, where):
	# Connection
	global conn, credentials
	assert credentials != None, fail_return("Please set the credentials first, by using j.set_credentials()")
	mydb = conn.connect(**credentials)
	mycursor = mydb.cursor()
	# SQL
	columns, values = dictionary.keys(), dictionary.values()
	pairs = ""
	for col in columns:
		pairs += col+"=%s, "
	if pairs != "":
		pairs = pairs[:-2]
	vals = list(map(str, list(values)))
	sql = f"UPDATE {table} SET {pairs} WHERE {where}"
	# Execution
	mycursor.executemany(sql, [vals])
	mydb.commit()
	mycursor.close()
	mydb.close()

def query(SQL):
	global conn, credentials
	assert credentials != None, fail_return("Please set the credentials first, by using j.set_credentials()")
	mydb = conn.connect(**credentials)
	mycursor = mydb.cursor(buffered=True)
	execution_successful = False
	try:
		mycursor.execute(SQL)
		mydb.commit()
		execution_successful = True
	except Exception as e:
		fail_message("SQL Error: " + str(e))
		pass;

	fetched_data = None
	if execution_successful:
		try:
			fetched_data = mycursor.fetchall()
		except Exception as e:
			pass;

	mycursor.close()
	mydb.close()

	if fetched_data != None and fetched_data != "":
		return fetched_data

def multi_insert(table, dictionaries):
	# Connection
	global conn, credentials
	assert credentials != None, fail_return("Please set the credentials first, by using j.set_credentials()")
	if len(dictionaries) > 0:
		mydb = conn.connect(**credentials)
		mycursor = mydb.cursor()
		# SQL
		columns = dictionaries[0].keys()
		keys = ", ".join(columns)
		masks = ", ".join(list(["%s"]*len(columns)))
		sql = f"INSERT INTO {table} ({keys}) VALUES ({masks})"
		all_vals = []
		for i in range(len(dictionaries)):
			values = dictionaries[i].values()
			vals = list(map(str, list(values)))
			all_vals.append(vals)
		# Execution
		mycursor.executemany(sql, all_vals)
		mydb.commit()
		mycursor.close()
		mydb.close()


# COLORS
class c:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def title(x):
	print(c.WARNING + x + c.ENDC)

def blue(x):
	print(c.OKBLUE + x + c.ENDC)

def fail_message(x):
	print(c.FAIL + x + c.ENDC)

def fail_return(x):
	return c.FAIL + x + c.ENDC
