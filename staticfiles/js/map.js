// CREDS: Borrow from CI UCD Resume Project

async function initMap() {
    // Request needed libraries.
    const { Map, InfoWindow } = await google.maps.importLibrary("maps");
    const { AdvancedMarkerElement, PinElement } = await google.maps.importLibrary(
      "marker",
    );
    
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 3,
      center: { lat: 46.619261, lng: -33.134766 },
      mapId: "DEMO_MAP_ID",
    });
    
    // Create an array of alphabetical characters used to label the markers.
    const labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    // Add some markers to the map.      
    var markers = locations.map(function(location, i){
      return new google.maps.Marker({
          position: location,
          label: labels[i % labels.length]
      });
    });
  
    // Add a marker clusterer to manage the markers.
    const markerCluster = new markerClusterer.MarkerClusterer({ map, markers });
  }
  
  const locations = [
    { lat: 40.785091, lng: -73.968285 },
    { lat: 41.084045, lng: -73.874245 },
    { lat: 40.754932, lng: -73.984016 }
  ];
  
  initMap();