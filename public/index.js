function set_gpio(device, state) {
    fetch('/api/device', {
        method: 'POST',
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, *same-origin, omit
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            device: device,
            state: state
        })
    }).then(
        response => response.json() // if the response is a JSON object
    ).then(
        response => console.log(response)
    ).catch(
        error => console.log(error) // Handle the error response object
    );
}

function get_devices(callback) {
    fetch('/api/devices')
    .then(response => response.json())
    .then(json => callback(json), callback)
}

get_devices(function(devices) {
    console.log(devices);

    devices.forEach(function(device) {
        console.log(device)

        let table = document.getElementById("devices");
        let row = table.insertRow();
        let cell0 = row.insertCell(0);
        let cell1 = row.insertCell(1);
        let cell2 = row.insertCell(2);

        cell0.innerHTML = device.name;
        cell1.innerHTML = "<button onclick=\"set_gpio('" + device.name + "',1)\">On</button>";
        cell2.innerHTML = "<button onclick=\"set_gpio('" + device.name + "',0)\">Off</button>";
    });


});


