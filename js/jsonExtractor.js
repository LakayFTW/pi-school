const tempJson = '../json/temperatures.json';
const weatherJson = '../json/testdata.json';

function getDBEntriesFromJson() {
    fetch("./json/temperatures.json")
    .then(response => {
    return response.json();
    })
    .then(jsondata => {
        var tempjson = jsondata;
        // console.log(tempjson);
        pasteResultToHtmlTable(tempjson);
    });
}

function getWeatherFromAPI() {
    fetch("./json/testdata.json")
    .then(response => {
    return response.json();
    })
    .then(jsondata => {
        var json = jsondata;
        pasteWeatherDataToHeader(jsondata);
    });
}

function pasteResultToHtmlTable(json){
    for (let index = 0; index < json.length; index++) {
        var element = json[index][index];
        // console.log(element.temp);
        // console.log(element.date);

        var date = new Date(element.date)
        var newDate = date.toLocaleString("de-DE", {
            day: '2-digit',
            year: 'numeric',
            month: '2-digit',
            hour24: true,
            hour: 'numeric',
            minute: 'numeric',
        })

        // console.log(newDate);

        var table = document.getElementById("table");

        var tr = document.createElement("tr");
        var td0 = document.createElement("td");
        var td1 = document.createElement("td");

        td0.innerText = newDate + " Uhr";
        td1.innerText = element.temp + "°";
        tr.appendChild(td0);
        tr.appendChild(td1);
        table.appendChild(tr)
    }
}

function pasteWeatherDataToHeader(json){
    console.log(json.name);
    console.log(json.weather[0].description);
    console.log(json.main.temp);

    var city = json.name;
    var weather = json.weather[0].description;
    var temp = json.main.temp.toString();

    var newTemp = temp.split(".")[0];

    var w = document.getElementById("weatherdata");

    w.innerText = city + ": " + weather + " " + newTemp + "°";
}