function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 8,
        center: {lat: -54.2815, lng: -36.5085},
        disableDefaultUI: true,
        streetViewControl: false,
        rotateControl: false,
        fullscreenControl: false,
        mapTypeControl: false,
        zoomControl: true
    })

    var marker = new google.maps.Marker({
        position: new google.maps.LatLng(-54.2815, -36.5085),
        icon: "https://i.ibb.co/HNYVYjM/map-cursor.png",
        map: map,
        title: "Applied Bayesian Capital",
        optimized: false
    })

    var overlay = new google.maps.OverlayView()   
}

google.maps.event.addDomListener(window, 'load', initMap)