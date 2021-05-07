var Con = require("./mysql_object_wrapper.js");


// insert
con = new Con();
con.insert("main_table", {
	id: "1",
	name: "Jason"
});
con.end();

// and so forth.
con = new Con();
con.update("main_table", {
	id: "2",
	name: "Jason"
}, "id='1' ");
con.end();
