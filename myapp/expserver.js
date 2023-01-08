const express = require("express");
const bodyParser = require("body-parser");

const app = express();
const path = require("path");


console.log(path.join(__dirname,"/htmlfolder"));

app.use(bodyParser.urlencoded({extended:true}));

app.get("/", function(req, res){
	console.log(__dirname)
	// res.send("Welcome home page to my channel :)")
	res.sendFile(__dirname+"/index.html")

});
 


app.get("/about", function(req, res){
	res.send("hello this is about");
});

app.get("/hello", function(req, res){
	// console.log(__dirname);
	res.sendFile(__dirname+"/index.html");
});

app.get("/calculator", function(req, res){
	// console.log(__dirname);
	res.sendFile(__dirname+"/calculator.html");
	// res.send("hello php");
});

app.post("/calculator", function(req, res){
	// res.send("thannku for your lovely post");
	console.log(req.body);

	let n1 = req.body.v1;
	let n2 = req.body.v2;

	let T1 = Number(n1);
	let T2 = Number(n2);
	let sum = T1 + T2; 

	res.send(""+sum);


});

// app.get("/profile", function(){
// 	res.sendFile(__dirname+"/hello.html");
// });

app.listen(3000, function(req, res){
	console.log("server is running at port no. 3000");
});