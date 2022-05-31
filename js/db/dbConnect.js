// const mysql = require('mysql');
// const mySqlConfig = require('../../config/jsconfig.js');

// var connection = mysql.createConnection(mySqlConfig);

// var fetchData = function(callback){
//     connection.query("SELECT days.datetime AS datetime, temperatures.temp AS temp FROM days INNER JOIN temperatures ON days.ID = temperatures.ID", (err, result) => {
//         if(err){
//             console.log(err);
//             callback(err, null);
//         }
//         callback(null, result);
//     });
// };

// module.exports.fetchData = fetchData;