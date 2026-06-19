import re
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

def parse_gcode(filename):
    cx, cy, cz = 0.0, 0.0, 0.0
    current_g = None
    segments = []
    
    with open(filename, 'r') as file:
        for line in file:
            # 1. Bersihkan komentar dan spasi kosong
            line = line.split(';')[0].strip().upper()
            if not line:
                continue
            
            # 2. Cek apakah ada perintah G0 atau G1
            g_match = re.search(r'G(00|01|0|1)\b', line)
            if g_match:
                current_g = int(g_match.group(1))
            
            # 3. Ekstrak koordinat X, Y, Z menggunakan Regex
            x_match = re.search(r'X([-+]?\d*\.\d+|\d+)', line)
            y_match = re.search(r'Y([-+]?\d*\.\d+|\d+)', line)
            z_match = re.search(r'Z([-+]?\d*\.\d+|\d+)', line)
            
            # Jika ada koordinat di baris ini
            if x_match or y_match or z_match:
                nx = float(x_match.group(1)) if x_match else cx
                ny = float(y_match.group(1)) if y_match else cy
                nz = float(z_match.group(1)) if z_match else cz
                
                if current_g in [0, 1]:
                    segments.append({
                        'x': (cx, nx),
                        'y': (cy, ny),
                        'z': (cz, nz),
                        'type': f'G{current_g}'
                    })
                
                cx, cy, cz = nx, ny, nz
                
    return segments

def plot_gcode(segments):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    # Gambar segmen garis satu per satu berdasarkan jenisnya
    for seg in segments:
        if seg['type'] == 'G0':
            # G0: Travel/Gerakan cepat (Merah, Putus-putus)
            ax.plot(seg['x'], seg['y'], seg['z'], color='red', linestyle='--', alpha=0.6)
        elif seg['type'] == 'G1':
            # G1: Cutting/Proses potong (Biru, Tebal)
            ax.plot(seg['x'], seg['y'], seg['z'], color='blue', linewidth=2)
            
    ax.set_xlabel('Sumbu X (mm)')
    ax.set_ylabel('Sumbu Y (mm)')
    ax.set_zlabel('Sumbu Z (mm)')
    ax.set_title('Mini CNC Simulator & G-Code Visualizer')
    
    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], color='red', linestyle='--', label='G0: Rapid/Travel'),
        Line2D([0], [0], color='blue', linewidth=2, label='G1: Linear Cutting')
    ]
    ax.legend(handles=legend_elements)
    
    plt.show()

if __name__ == '__main__':
    input_file = '../examples/logo_polman.nc' # Sesuaikan dengan nama file G-code Anda
    
    if os.path.exists(input_file):
        print(f"Membaca file: {input_file}...")
        jalur_pahat = parse_gcode(input_file)
        print("Memulai visualisasi 3D...")
        print(f"Berhasil memproses {len(jalur_pahat)} gerakan pahat.")
        print("Menampilkan visualisasi 3D...")
        plot_gcode(jalur_pahat) 
        
    else:
        print(f"Error: File '{input_file}' tidak ditemukan!")
        print("Pastikan nama file sesuai dan berada di folder 'examples/'")
