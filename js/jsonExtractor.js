const tempJson = '../json/temperatures.json';
const weatherJson = '../json/testdata.json';

function getDBEntriesFromJson() {
    fetch("./json/temperatures.json")
    .then(response => {
    return response.json();
    })
    .then(jsondata => {
        var tempjson = jsondata;
        console.log(tempjson);
    });
}

function getWeatherFromAPI() {
    fetch("./json/testdata.json")
    .then(response => {
    return response.json();
    })
    .then(jsondata => {
        var json = jsondata;
        pasteResultToHtml(json);
    });
}

function pasteResultToHtml(json){
    
}