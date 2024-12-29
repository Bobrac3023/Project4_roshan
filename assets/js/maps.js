async function initMap() {
  // Request needed libraries.
  const {
    Map
  } = await google.maps.importLibrary("maps");
  const {
    AdvancedMarkerElement
  } = await google.maps.importLibrary("marker");
  const map = new Map(document.getElementById("map"), {
    center: {
      lat: 24.49416732788086,
      lng: 54.37644577026367
    },
    zoom: 14,
    mapId: "4504f8b37365c3d0",
  });
  const marker = new AdvancedMarkerElement({
    map,
    position: { lat: 24.49416732788086,lng: 54.37644577026367},
  });
  
}
initMap();