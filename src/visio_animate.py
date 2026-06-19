import re
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.lines import Line2D
import os

def parse_gcode(filename):
    cx, cy, cz = 0.0, 0.0, 0.0
    current_g = None
    segments = []
    
    with open(filename, 'r') as file:
        for line in file:
            line = line.split(';')[0].strip().upper()
            if not line:
                continue
            
            g_match = re.search(r'G(00|01|0|1)\b', line)
            if g_match:
                current_g = int(g_match.group(1))
            
            x_match = re.search(r'X([-+]?\d*\.\d+|\d+)', line)
            y_match = re.search(r'Y([-+]?\d*\.\d+|\d+)', line)
            z_match = re.search(r'Z([-+]?\d*\.\d+|\d+)', line)
            
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

def plot_gcode_animated(segments):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    # 1. Batas maksimum & minimum koordinat
    all_x = [p for seg in segments for p in seg['x']]
    all_y = [p for seg in segments for p in seg['y']]
    all_z = [p for seg in segments for p in seg['z']]
    
    ax.set_xlim(min(all_x) - 5, max(all_x) + 5)
    ax.set_ylim(min(all_y) - 5, max(all_y) + 5)
    ax.set_zlim(min(all_z) - 5, max(all_z) + 5)
    
    # Labeling
    ax.set_xlabel('Sumbu X (mm)')
    ax.set_ylabel('Sumbu Y (mm)')
    ax.set_zlabel('Sumbu Z (mm)')
    ax.set_title('CNC G-Code Live Animation')
    
    # Buat objek untuk Mata Pahat (Tool Head)
    tool_head, = ax.plot([], [], [], 'ko', markersize=8, zorder=10)
    
    # Legenda kustom
    legend_elements = [
        Line2D([0], [0], color='red', linestyle='--', label='G0: Rapid/Travel'),
        Line2D([0], [0], color='blue', linewidth=2, label='G1: Linear Cutting'),
        Line2D([0], [0], color='black', marker='o', linestyle='', label='Tool Head (Mata Pahat)')
    ]
    ax.legend(handles=legend_elements)
    ax.grid(True)

    # 2. Fungsi update Matplotlib
    def update(frame_num):
        if frame_num >= len(segments):
            return tool_head,
            
        seg = segments[frame_num]
        
        # Gambar garis baru
        if seg['type'] == 'G0':
            ax.plot(seg['x'], seg['y'], seg['z'], color='red', linestyle='--', alpha=0.6)
        elif seg['type'] == 'G1':
            ax.plot(seg['x'], seg['y'], seg['z'], color='blue', linewidth=2)
            
        # Pindahkan posisi mata pahat
        tool_head.set_data([seg['x'][1]], [seg['y'][1]])
        tool_head.set_3d_properties([seg['z'][1]])
        
        return tool_head,

    # 3. Jalankan Animasi
    ani = animation.FuncAnimation(
        fig, 
        update, 
        frames=len(segments), 
        interval=300, #bisa diubah untuk mempercepat atau memperlambat animasi (sesuai kebutuhan)
        repeat=False, 
        blit=False
    )
    
    plt.show()

if __name__ == '__main__':
    input_file = '../examples/logo_polman.nc' # Sesuaikan dengan nama file G-code Anda
    
    if os.path.exists(input_file):
        print(f"Membaca file: {input_file}...")
        jalur_pahat = parse_gcode(input_file)
        print("Memulai animasi 3D...")
        plot_gcode_animated(jalur_pahat) 
        
    else:
        print(f"Error: File '{input_file}' tidak ditemukan!")
        print("Pastikan nama file sesuai dan berada di folder 'examples/'")
