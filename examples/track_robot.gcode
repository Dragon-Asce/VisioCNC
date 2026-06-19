; --- ALUR TRACK MINI ---
G0 X0 Y0 Z10
G0 X10 Y10 Z2
G1 X10 Y10 Z-1   ; Mulai motong lintasan
G1 X10 Y60 Z-1   ; Lurus ke atas
G1 X30 Y60 Z-1   ; Belok kanan patah
G1 X30 Y30 Z-1   ; Turun (U-turn tajam)
G1 X50 Y30 Z-1   ; Belok kanan lagi
G1 X50 Y80 Z-1   ; Naik trek panjang
G1 X80 Y80 Z-1   ; Belok kanan atas
G1 X80 Y10 Z-1   ; Trek lurus panjang sampai bawah
G1 X45 Y10 Z-1   ; Belok kiri bawah
G1 X45 Y20 Z-1   ; Zig-zag kecil
G1 X35 Y20 Z-1
G1 X35 Y10 Z-1
G1 X10 Y10 Z-1   ; Balik ke titik start (Loop tertutup)
G0 X10 Y10 Z10   ; Angkat pahat
G0 X0 Y0 Z0
