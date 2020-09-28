function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 5,
        center: {lat: 53.9628, lng: 2.0163}, //the location coordinates
        disableDefaultUI: true,
        streetViewControl: false,
        rotateControl: false,
        fullscreenControl: false,
        mapTypeControl: false,
        zoomControl: true
    })

    var marker = new google.maps.Marker({
        position: new google.maps.LatLng(53.9628, 2.0163), //the location coordinates
        icon: "https://i.ibb.co/HNYVYjM/map-cursor.png",
        map: map,
        title: "Applied Bayesian Capital",
        optimized: false
    })

    var overlay = new google.maps.OverlayView()   
}
