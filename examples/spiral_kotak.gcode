; --- SPIRAL KOTAK ---
G0 X0 Y0 Z10
G0 X50 Y50 Z2
G1 X50 Y50 Z-1   ; Nusuk mulai dari ujung kanan atas
G1 X50 Y10 Z-1
G1 X10 Y10 Z-1
G1 X10 Y45 Z-1
G1 X45 Y45 Z-1   ; Masuk ke cincin kedua
G1 X45 Y15 Z-1
G1 X15 Y15 Z-1
G1 X15 Y40 Z-1
G1 X40 Y40 Z-1   ; Masuk ke cincin ketiga
G1 X40 Y20 Z-1
G1 X20 Y20 Z-1
G1 X20 Y35 Z-1
G1 X35 Y35 Z-1   ; Masuk ke cincin keempat
G1 X35 Y25 Z-1
G1 X25 Y25 Z-1
G1 X25 Y30 Z-1
G1 X30 Y30 Z-1   ; Cincin terakhir (titik tengah)
G0 X30 Y30 Z10   ; Angkat pahat, kelar!
G0 X0 Y0 Z0