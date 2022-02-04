function getType() {
    var x = document.getElementById("mapyear").value;
    var items;
    if (x === "2020") {
        items = ["Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"];
    } else if (x === "2021") {
    items = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"];
    } else {
        items = ["Enero", "Febrero"]
    }
    var str = ""
    for (let i = 0; i <  items.length; i++) {
        str += '<option' + ' value="' + (x === "2020" ? i+3 : i+1) + '">' + items[i] + '</option>';
    }
    document.getElementById("mapmonth").innerHTML = str;
}
document.getElementById("mapyear").addEventListener("click", getType);
getType();