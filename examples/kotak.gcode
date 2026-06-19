G0 X0 Y0 Z5    ; G0 = Gerakan cepat tanpa motong (pahat diangkat ke Z=5)
G0 X10 Y10 Z5  ; Bergerak cepat ke titik awal (10,10)
G1 X10 Y10 Z-1 ; G1 = Mulai memotong turun ke kedalaman Z=-1
G1 X50 Y10 Z-1 ; Potong ke kanan (X=50)
G1 X50 Y50 Z-1 ; Potong ke atas (Y=50)
G1 X10 Y50 Z-1 ; Potong ke kiri (X=10)
G1 X10 Y10 Z-1 ; Potong kembali ke awal kotak
G0 X10 Y10 Z5  ; Angkat pahat kembali ke atas aman (Z=5)
G0 X0 Y0 Z0    ; Pulang ke titik awal (Home)