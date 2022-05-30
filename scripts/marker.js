// Node
// R - Restaurant
// M - Market
// B - Bank
// H - Hotel
// S - SPBU

L.marker([-6.88643, 107.58069]).addTo(map); // Universitas Kristen Maranatha
L.marker([-6.886967, 107.581161]).addTo(map); // Terazza (R)
L.marker([-6.887382, 107.581094]).addTo(map); // Permata Surya Sumantri (B)
L.marker([-6.887572, 107.581089]).addTo(map); // Wibisana (R)
L.marker([-6.887588, 107.581528]).addTo(map); // Indomaret (M)
L.marker([-6.88738, 107.581681]).addTo(map); // Inti Laut (R)
L.marker([-6.888509, 107.581671]).addTo(map); // Circle K (M)
L.marker([-6.885594, 107.581622]).addTo(map); // Indomaret (M)
L.marker([-6.885344, 107.581067]).addTo(map); // BNP (B)
L.marker([-6.88521, 107.581217]).addTo(map); // BCA (B)
L.marker([-6.885197, 107.581537]).addTo(map); // Take Ichi Japanese Cafe (R)
L.marker([-6.885178, 107.581099]).addTo(map); // Tujuh Sebelas (M)
L.marker([-6.883174, 107.581011]).addTo(map); // The Majesty Hotel (H)
L.marker([-6.883589, 107.58248]).addTo(map); // Martabak Bolu Golden Bell (R)
L.marker([-6.88261, 107.581364]).addTo(map); // SPBU (S)
L.marker([-6.885022, 107.583322]).addTo(map); // SM Residence Pasteur (H)
L.marker([-6.885516, 107.583295]).addTo(map); // FullMar House (H)
L.marker([-6.889073, 107.581652]).addTo(map); // SPBU (S)
L.marker([-6.889166, 107.582127]).addTo(map); // Verona Palace (H)
L.marker([-6.889154, 107.582271]).addTo(map); // Sugar Rush (R)

// Code For Making a Line or Polygon
// Marnat - Terazza
L.polygon([
  [-6.88643, 107.58069],
  [-6.886967, 107.581161],
]).addTo(map);

// Terazza - Permata Surya Sumantri
L.polygon([
  [-6.886967, 107.581161],
  [-6.887382, 107.581094],
]).addTo(map);

// Terazza - INti Laut
L.polygon([
  [-6.886967, 107.581161],
  [-6.88738, 107.581681],
]).addTo(map);

// Permata Surya Sumantri - Wibisana
L.polygon([
  [-6.887382, 107.581094],
  [-6.887572, 107.581089],
]).addTo(map);

// Permata Surya Sumantri - Indomaret
L.polygon([
  [-6.887382, 107.581094],
  [-6.887588, 107.581528],
]).addTo(map);

// Inti Laut - Indomaret
L.polygon([
  [-6.88738, 107.581681],
  [-6.887588, 107.581528],
]).addTo(map);

// Indomaret - Circle K
L.polygon([
  [-6.887588, 107.581528],
  [-6.888509, 107.581671],
]).addTo(map);

// Wibisanat - Circle K
L.polygon([
  [-6.887572, 107.581089],
  [-6.888509, 107.581671],
]).addTo(map);

// Circle K - SPBU
L.polygon([
  [-6.888509, 107.581671],
  [-6.889073, 107.581652],
]).addTo(map);

// Circle K - Sugar Rush
L.polygon([
  [-6.888509, 107.581671],
  [-6.889154, 107.582271],
]).addTo(map);

// Sugar Rush - Verona Palace
L.polygon([
  [-6.889154, 107.582271],
  [-6.889166, 107.582127],
]).addTo(map);

// Maranatha - BNP
L.polygon([
  [-6.88643, 107.58069],
  [-6.885344, 107.581067],
]).addTo(map);

// Maranatha - Indomaret
L.polygon([
  [-6.88643, 107.58069],
  [-6.885594, 107.581622],
]).addTo(map);

// BNP - Tujuh Sebelas
L.polygon([
  [-6.885344, 107.581067],
  [-6.885178, 107.581099],
]).addTo(map);

// BNP - BCA
L.polygon([
  [-6.885344, 107.581067],
  [-6.88521, 107.581217],
]).addTo(map);

// Tujuh Sebelas - BCA
L.polygon([
  [-6.885178, 107.581099],
  [-6.88521, 107.581217],
]).addTo(map);

// BCA - Take Ichi
L.polygon([
  [-6.88521, 107.581217],
  [-6.885197, 107.581537],
]).addTo(map);

// Indomaret - Take Ichi
L.polygon([
  [-6.885594, 107.581622],
  [-6.885197, 107.581537],
]).addTo(map);

// Indomaret - Fullmar
L.polygon([
  [-6.885594, 107.581622],
  [-6.885516, 107.583295],
]).addTo(map);

// Fullmar - SM Residence
L.polygon([
  [-6.885516, 107.583295],
  [-6.885022, 107.583322],
]).addTo(map);

// SM Residence - Martabak
L.polygon([
  [-6.885022, 107.583322],
  [-6.883589, 107.58248],
]).addTo(map);

// Take Ichi - Martabak
L.polygon([
  [-6.885197, 107.581537],
  [-6.883589, 107.58248],
]).addTo(map);

// Take Ichi - Majesty
L.polygon([
  [-6.885197, 107.581537],
  [-6.883174, 107.581011],
]).addTo(map);

// Martabak - Majesty
L.polygon([
  [-6.883589, 107.58248],
  [-6.883174, 107.581011],
]).addTo(map);

// Martabak - SPBU
L.polygon([
  [-6.883589, 107.58248],
  [-6.88261, 107.581364],
]).addTo(map);

// Majesty - SPBU
L.polygon([
  [-6.883174, 107.581011],
  [-6.88261, 107.581364],
]).addTo(map);
