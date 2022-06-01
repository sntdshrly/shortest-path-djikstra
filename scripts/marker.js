// Node
// R - Restaurant
// M - Market
// B - Bank
// H - Hotel
// S - SPBU

// Koordinat di map
nodes = [
  [-6.88643, 107.58069],    // Universitas Kristen Maranatha
  [-6.886967, 107.581161],  // Terazza (R)
  [-6.887382, 107.581094],  // Permata Surya Sumantri (B)
  [-6.887572, 107.581089],  // Wibisana (R)
  [-6.887588, 107.581528],  // Indomaret (M)
  [-6.88738, 107.581681],   // Inti Laut (R)
  [-6.888509, 107.581671],  // Circle K (M)
  [-6.885594, 107.581622],  // Indomaret (M)
  [-6.885344, 107.581067],  // BNP (B)
  [-6.88521, 107.581217],   // BCA (B)
  [-6.885197, 107.581537],  // Take Ichi Japanese Cafe (R)
  [-6.885178, 107.581099],  // Tujuh Sebelas (M)
  [-6.883174, 107.581011],  // The Majesty Hotel (H)
  [-6.883589, 107.58248],   // Martabak Bolu Golden Bell (R)
  [-6.88261, 107.581364],   // SPBU (S)
  [-6.885022, 107.583322],  // SM Residence Pasteur (H)
  [-6.885516, 107.583295],  // FullMar House (H)
  [-6.889073, 107.581652],  // SPBU (S)
  [-6.889166, 107.582127],  // Verona Palace (H)
  [-6.889154, 107.582271]   // Sugar Rush (R)
];


function addAllMarkers() {
  deleteAllMarker();
  $.each(nodes, function(index, value) {
    L.marker(value).addTo(markers);
  });
  addAllPath();
}

function addAllPath() {
  
  // Meminta data get dari server.py
  $.get("http://127.0.0.1:8000/list", function (data) {
    $.each(data, function (i, value) {
      $.each(value, function (j, node) {
        if (node != 0) {
          L.polygon([nodes[i],nodes[j]]).addTo(markers);
        }
      });
    })
  });
  
}

function deleteAllMarker() {
  markers.clearLayers()
}

function addMarker() {
  deleteAllMarker();

  let start = $("#start").val();
  let end = $("#end").val();

  // Meminta data get dari server.py
  $.get(`http://127.0.0.1:8000/path?start=${start}&end=${end}`, function (data) {
    $.each(data.path, function (i, value) {
      L.marker(nodes[value]).addTo(markers);
    });
  });
}

function calculateDistance(start, finish) {
  var finalPoint = L.latLng(start[0], start[1]);
  var startPoint = L.latLng(finish[0], finish[1]);
  dist = finalPoint.distanceTo(startPoint);
  return dist;
}