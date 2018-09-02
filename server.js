const express = require('express');
const app = express();
const mongodb = require('./mongodb.js');
const config = require('./config.js');
const bodyParser = require('body-parser')
var d3 = require('d3')

/** parse application/json **/
app.use(bodyParser.json())

mongodb.connectToServer(function (err) {
  app.listen(config.server.port, function () {
    console.log('Node server listening on ' + config.server.port);
    db = mongodb.getDb();
  })
});


app.use(express.static(__dirname + '/view'));

//main web page
app.get('/', function (req, res) {
  res.send('index.html')

});

// this is to get all data from mongoDB
app.get('/getalldata', function (req, res) {
  db.collection('collection').find().toArray(function (err, results) {
    res.send(results);
  })
  res.set({
    'Cache-Control': 'no-cache'
  });
});


app.get('/countcarbyregion', function (req, res) {
  db.collection('collection').aggregate([{ $group: { _id: "$region", countofcars: { $sum: 1 } } }]).toArray(function (err, results) {
    res.send(JSON.stringify(results));
  })
  res.set({
    'Cache-Control': 'no-cache'
  });
});


app.get('/countcarbytype', function (req, res) {
  db.collection('collection').aggregate([{ $group: { _id: {title:"$title", region:"$region"}, countofcars: { $sum: 1 },imageURL: { $push: "$URL"} } }]).toArray(function (err, results) {
    res.send(results);
  })
  res.set({
    'Cache-Control': 'no-cache'
  });
});

app.get('/countcarbyyear', function (req, res) {
  db.collection('collection').aggregate([{ $group: { _id: {man_year: "$Man_year",region: "$region"}, countofcars: { $sum: 1 } } }]).toArray(function (err, results) {
    res.send(results);
  })
  res.set({
    'Cache-Control': 'no-cache'
  });
});

app.get('/topfivecarsbyprice', function (req, res) {
  db.collection('collection').find().sort({'price':-1}).toArray(function (err, results) {
    res.send(results);
  })
  res.set({
    'Cache-Control': 'no-cache'
  });
});