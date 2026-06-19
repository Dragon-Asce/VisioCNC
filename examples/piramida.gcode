; --- PIRAMIDA NAIK DENGAN PUNCAK TITIK ---
G90                 ; Mode absolut

; --- Layer 1 (Z = 0, Kotak 40x40) ---
G0 X10 Y10 Z0       ; Start di pojok kiri bawah, Z0
G1 X50 Y10 F200
G1 X50 Y50
G1 X10 Y50
G1 X10 Y10

; --- Layer 2 (Z = 5, Kotak 30x30) ---
G0 X15 Y15 Z5       ; Geser ke dalam, langsung naik ke Z5
G1 X45 Y15 F200
G1 X45 Y45
G1 X15 Y45
G1 X15 Y15

; --- Layer 3 (Z = 10, Kotak 20x20) ---
G0 X20 Y20 Z10      ; Geser ke dalam, langsung naik ke Z10
G1 X40 Y20 F200
G1 X40 Y40
G1 X20 Y40
G1 X20 Y20

; --- Layer 4 (Z = 15, Kotak 10x10) ---
G0 X25 Y25 Z15      ; Geser ke dalam, langsung naik ke Z15
G1 X35 Y25 F200
G1 X35 Y35
G1 X25 Y35
G1 X25 Y25

; --- Layer 5 (Z = 20, Titik Puncak) ---
G0 X30 Y30 Z20      ; Pindah ke pusat puncak
G4 P1000            ; Dwell (diam) selama 1000ms (1 detik) agar terbaca titik
G1 Z20.001          ; Sedikit gerakan vertikal agar titik ter-render sempurna

; --- Selesai ---
G0 Z25              ; Angkat menjauh biar aman
G0 X0 Y0            ; Balik ke titik nol
G0 Z0