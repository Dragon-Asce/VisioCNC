import sys
import re
import numpy as np
from vispy import app, scene
import os
os.environ["QT_LOGGING_RULES"] = "*.warning=false"

def parse_gcode_numpy(filename):
    cx, cy, cz = 0.0, 0.0, 0.0
    current_g = None

    pos = []
    colors = []

    print(f"Memproses file {filename} ke dalam memori...")
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
                    pos.append([cx, cy, cz])
                    pos.append([nx, ny, nz])

                    if current_g == 0:
                        c = [1.0, 0.0, 0.0, 0.5]
                    else:
                        c = [0.0, 0.3, 1.0, 1.0]

                    colors.append(c)
                    colors.append(c)

                cx, cy, cz = nx, ny, nz

    return np.array(pos, dtype=np.float32), np.array(colors, dtype=np.float32)

if __name__ == '__main__':
    input_file = '../examples/logo_polman.nc'  # Ganti dengan path ke file G-code Anda
    
    if os.path.exists(input_file):
        print(f"Membaca file: {input_file}...")
        
        pos_data, color_data = parse_gcode_numpy(input_file)
        total_points = len(pos_data)
        print(f"Data siap! Mengirim {total_points} vertex ke GPU OpenGL...")

        canvas = scene.SceneCanvas(keys='interactive', show=True, title='VisPy GPU G-Code Visualizer', size=(1024, 768))
        view = canvas.central_widget.add_view()
        view.camera = scene.cameras.TurntableCamera(elevation=30, azimuth=45, distance=150)
        grid = scene.visuals.GridLines(parent=view.scene)

        line_visual = scene.visuals.Line(pos=np.zeros((1,3)), color=np.zeros((1,4)), 
                                         connect='segments', width=3, antialias=True, parent=view.scene)

        current_idx = 0
        speed_multiplier = 5 # Garis yang digambar per frame (semakin besar semakin cepat)

        def update(ev):
            global current_idx
            current_idx += speed_multiplier
            
            if current_idx > total_points:
                current_idx = total_points
                timer.stop()
                print("Animasi Selesai!")
                
            if current_idx > 0:
                line_visual.set_data(pos=pos_data[:current_idx], color=color_data[:current_idx])

        timer = app.Timer('auto', connect=update, start=True)

        if sys.flags.interactive != 1:
            app.run()
            
    else:
        print(f"Error: File '{input_file}' tidak ditemukan!")
        print("Pastikan nama file sesuai dan berada di dalam folder yang tepat.")
