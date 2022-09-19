function check() {   
    var a1 = document.getElementById("newat").value;
    var b1 = document.getElementById("newbt").value;
    if (isNaN(parseInt(a1)) && isNaN(parseInt(b1))) {
        window.alert("Please enter valid inputs");
        return false ;
    }
    if (isNaN(parseInt(a1))) {
        window.alert("Please enter numeric value of arrival time");
        return false;
    }
    if (isNaN(parseInt(b1))) {
        window.alert("Please enter numeric value of burst time");
        return false;
    }
    if (parseInt(a1)<0 && parseInt(b1)<=0) {
        window.alert("Invalid inputs");
        return false;
    }
    if (parseInt(a1)<0) {
        window.alert("Please enter valid value of arrival time");
        return false;
    }
    if (parseInt(b1)<=0) {
        window.alert("Please enter positive value of burst time");
        return false;
    }
}