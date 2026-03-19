const net = require('net');


// Mitgaisim.idf
document.addEventListener("submit", (event) => {
    var values = document.querySelectorAll("input");
    console.log(values);
    for (i = 0; i < values.length; i++)
    {
        if (values[i].type == "number" || values[i].type == "password")
            alert(values[i].value);
    }
});

/*
Function to check if there is a login pattern
*/