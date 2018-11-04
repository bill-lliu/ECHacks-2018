var mymap = L.map('mapid').setView([51.505, -0.09], 13);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox.streets',
    accessToken: 'pk.eyJ1IjoiZ3V5bW9yZyIsImEiOiJjam8yd25vbGwwcjRwM3FxaTk5Z3EyZjBnIn0.BoDV84KaHRnA3nl4XTbH9w'
}).addTo(mymap);


function getData(category) {
    var long = 1;
    var lat = 1;
    mymap.eachLayer(function (layer) {
        mymap.removeLayer(layer);
    });
    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        id: 'mapbox.streets',
        accessToken: 'pk.eyJ1IjoiZ3V5bW9yZyIsImEiOiJjam8yd25vbGwwcjRwM3FxaTk5Z3EyZjBnIn0.BoDV84KaHRnA3nl4XTbH9w'
    }).addTo(mymap);
    fetch(`http://localhost:5000/api?long=${long}&lat=${lat}&category=${category}`, {method: 'POST'})
        .then(function (response) {
            return response.json();
        })
        .then(function (json) {
            json.Locations.forEach(function (arrayItem) {
                console.log(arrayItem);

                var marker = L.marker([arrayItem.lat, arrayItem.long]).addTo(mymap);

                marker.bindPopup(`<b>${arrayItem.name}</b><br>${arrayItem.description}`).openPopup();
            });
        })
}