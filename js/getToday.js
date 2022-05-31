function getToday(){
    let currentDate = new Date();
    let cDay = currentDate.getDate().toString();
    let cMonth = currentDate.getMonth();
    let realMonth = (cMonth +1).toString();
    let cYear = currentDate.getFullYear().toString();

    document.getElementById('currentDate').innerHTML = cDay + '.' + realMonth + '.' + cYear;
}