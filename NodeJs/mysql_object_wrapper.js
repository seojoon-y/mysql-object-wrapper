// MYSQL
const db_config = {
  host: "XXXXXXXXXXXXXXXXXXXXXXXX",
  user: "XXXXXXXXXXXXXXXXXXXXXXXX",
  password: "XXXXXXXXXXXXXXXXXXXXXXXX",
  database: "XXXXXXXXXXXXXXXXXXXXXXXX",
  multipleStatements: true
}

class Con {
	constructor() {
		this.con = mysql.createConnection(db_config);
		this.con.connect(function(err) {
			if (err) console.log("Connect error",err)
		});
		this.con.on('error', function(err) {
			if(err.code === 'PROTOCOL_CONNECTION_LOST') {
				console.log("Con timeout somewhere.");
			} else {
				throw err;
			}
		});
	}
	end() {
		this.con.end();
	}
	query(sql, callback) {
		this.con.query(sql, function (err, result) {
			if (err) throw err;
			callback(result);
		});
	}
	insert(table, dict, callback) {
		const keys = Object.keys(dict);
		const vals = keys.map(function(key) {
		    return dict[key];
		});
		var sql = "INSERT INTO " + table + " ";  
		sql += "(" + keys.join(", ") + ") ";     
		sql += "VALUES ('" + vals.join("', '") + "')"; 
		this.query(sql, callback);    
	}
	update(table, dict, where, callback) {
		const keys = Object.keys(dict);         
		const vals = keys.map(function(key) {
			return dict[key];
		});
		var sql = "UPDATE " + table + " SET ";  
		var arr = [];  
		for (var i=0;i<keys.length;i++) { 
			arr.push(keys[i] + "= '" + vals[i] + "'");
		}
		sql += arr.join(", ");    
		sql += " WHERE " + where; 
		// console.log(sql);         
		this.query(sql, callback);     
	}
	multi_insert(table, dicts, callback) {
		const L = dicts.length;
		if (L > 0) {
			const keys = Object.keys(dicts[0]);
			var sql = "INSERT INTO " + table + " ";  
			sql += "(" + keys.join(", ") + ") VALUES ";
			for (var i=0;i<L;i++) {
				const dict = dicts[i];
				const vals = keys.map(function(key) {
				    return dict[key];
				});
				sql += "('" + vals.join("', '") + "')";
				if (i == L - 1) {
					sql += ";";
				} else {
					sql += ", ";
				}
			}
			this.query(sql, callback);
		}  else {
			callback();
		}
	}
}

module.exports = Con