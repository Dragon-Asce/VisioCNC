# 🔩 VisioCNC — Multi-Engine 3D G-Code Toolpath Visualizer

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Rendering-OpenGL%20%7C%20Matplotlib-00BFFF?style=for-the-badge&logo=opengl&logoColor=white" alt="OpenGL"/>
  <img src="https://img.shields.io/badge/GPU-VisPy%20%2B%20NumPy-76B900?style=for-the-badge&logo=nvidia&logoColor=white" alt="GPU Accelerated"/>
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge" alt="Status"/>
</p>

<p align="center">
  <a href="README.md"><b>🇬🇧 English</b></a> &nbsp;|&nbsp;
  <a href="README.id.md">🇮🇩 Bahasa Indonesia</a>
</p>

> **Translate raw CNC and 3D printing instructions into interactive 3D simulations — before a single axis moves.**

---

## 📖 About The Project

VisioCNC is a Python-based, multi-engine toolpath visualizer designed to help **manufacturing engineering students**, **CAM software developers**, and **industrial automation engineers** perform safe, cost-free **"dry-run" simulations** of their G-Code and NC programs.

CNC machine crashes are expensive — both in time and in material. A collision caused by a malformed toolpath, an incorrect G0 rapid move, or a miscalculated Z-depth can destroy a workpiece, snap an endmill, or in severe cases, damage the machine spindle. VisioCNC solves this by rendering the complete 3D toolpath on screen with full visual fidelity, allowing engineers to audit every movement **before** the program is ever loaded onto a physical controller.

The project ships with **three distinct rendering engines**, each engineered for a different use case — from quick visual sanity-checks of simple programs to high-performance, GPU-accelerated visualization of large-scale industrial files.

---

## ✨ Key Features

### 🖼️ Three Rendering Engines — One Project

| Engine | Script | Backend | Best For | Performance |
|---|---|---|---|---|
| **Static Viewer** | `visio_static.py` | Matplotlib 3D | Quick sanity checks, simple programs | ⚡ Fast startup |
| **Animated Simulator** | `visio_animate.py` | Matplotlib Animation | Step-by-step tool head simulation, education | 🎞️ CPU-bound |
| **OpenGL Accelerated** | `visio_opengl.py` | VisPy + NumPy + OpenGL | Industrial-scale files, smooth 60 FPS | 🚀 GPU-powered |

### 🔑 Feature Highlights

- **Universal G-Code Parsing** — Handles `G0` (Rapid/Travel) and `G1` (Linear Cut) commands with full modal state tracking. Coordinates not specified in a line are correctly inherited from the previous position.
- **Color-Coded Toolpaths** — Red dashed lines for `G0` rapid moves; solid blue lines for `G1` cutting passes, making it visually instant to distinguish travel from cutting.
- **Live Tool Head Tracking** — The animated engine renders a live marker representing the tool head (mata pahat) that follows the programmed path in real-time.
- **Hardware-Accelerated Rendering** — `visio_opengl.py` bypasses the Python render loop by packaging all vertex and color data into NumPy arrays and uploading them directly to VRAM via VisPy's OpenGL bindings. This allows smooth, interactive rendering of files with **thousands of toolpath segments**.
- **Interactive 3D Viewport** — Rotate, zoom, and pan all visualizations in real-time using mouse controls.
- **Comment-Safe Parser** — The G-Code parser strips inline comments (`;` delimiters) before processing, ensuring compatibility with annotated files.

---

## 🗂️ Project Structure

```
VisioCNC/
│
├── 📁 src/                         # Core rendering engine scripts
│   ├── visio_static.py             # Engine 1: Static Matplotlib 3D plot
│   ├── visio_animate.py            # Engine 2: Animated Matplotlib simulation
│   └── visio_opengl.py             # Engine 3: GPU-accelerated VisPy/OpenGL renderer
│
├── 📁 examples/                    # Example G-Code programs for testing
│   ├── kotak.gcode                 # Simple square perimeter toolpath
│   ├── piramida.gcode              # Multi-layer stepped pyramid (Z-stacking)
│   ├── spiral_kotak.gcode          # Inward concentric square spiral
│   ├── track_robot.gcode           # Complex robot track / racetrack profile
│   └── logo_polman.nc # Authentic NC file generated via Autodesk Fusion (4,574 lines) 
│
├── requirements.txt                # Python package dependencies
├── README.id.md                    # Documentation in Indonesian
└── README.md                       # You are here
```

---

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed on your system before proceeding:

- **Python 3.10 or higher** — [Download from python.org](https://www.python.org/downloads/)
- **pip** (bundled with Python 3.10+)
- **Git** — [Download from git-scm.com](https://git-scm.com/)
- A dedicated GPU is **recommended** (but not required) for `visio_opengl.py`.

---

### Step 1 — Clone the Repository

```bash
git clone https://github.com/Dragon-Asce/VisioCNC.git
cd VisioCNC
```

---

### Step 2 — Create a Virtual Environment

It is strongly recommended to install dependencies inside an isolated virtual environment to avoid conflicts with your system-wide Python packages.

**On macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows (Command Prompt):**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

**On Windows (PowerShell):**
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

You should see `(venv)` appear at the beginning of your terminal prompt, confirming the environment is active.

---

### Step 3 — Install Dependencies

With your virtual environment active, install all required packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

This will install the following packages:

| Package | Version | Purpose |
|---|---|---|
| `matplotlib` | ≥ 3.7.0 | Static plots and CPU-based animation |
| `numpy` | ≥ 1.24.0 | High-performance array operations for GPU upload |
| `vispy` | ≥ 0.14.0 | OpenGL-based rendering pipeline |
| `PyQt6` | ≥ 6.5.0 | GUI windowing backend for VisPy |

---

## 🖥️ Usage

All three scripts are located in the `src/` folder. Before running, ensure your terminal's **working directory is `src/`**, as the scripts reference example files using relative paths pointing to `../examples/`.

```bash
cd src
```

Inside each script, there is a variable near the bottom called `input_file`. Change this path to point to the G-Code file you want to visualize.

```python
# Example — change this line in any of the three scripts
input_file = '../examples/piramida.gcode'
```

---

### Engine 1 — Static Viewer

**Best for:** Quick, full-path visualization. Renders the entire toolpath instantly as a static 3D plot. Ideal for a fast sanity check of any G-Code program.

```bash
python visio_static.py
```

The entire toolpath is rendered at once. Use the mouse to rotate the 3D view, scroll to zoom, and middle-click to pan.

---

### Engine 2 — Animated Simulator

**Best for:** Education, presentations, and step-by-step debugging. Simulates the tool head moving through the path sequentially, line by line.

```bash
python visio_animate.py
```

The animation speed is controlled by the `interval` parameter inside the `FuncAnimation` call (in milliseconds). A smaller value produces a faster simulation:

```python
# In visio_animate.py — adjust this value to control playback speed
ani = animation.FuncAnimation(
    fig,
    update,
    frames=len(segments),
    interval=50,   # ← Lower = faster (default: 300ms per step)
    ...
)
```

---

### Engine 3 — OpenGL Accelerated Renderer

**Best for:** Large, complex industrial G-Code files with hundreds or thousands of segments. This is the flagship engine — it sends vertex data directly to VRAM and renders at up to 60 FPS with a fully interactive 3D viewport.

```bash
python visio_opengl.py
```

The rendering speed is controlled by `speed_multiplier` — the number of line-segment vertices drawn per frame:

```python
# In visio_opengl.py — increase this to animate faster
speed_multiplier = 50  # ← Default is 5; increase for large files
```

**Viewport Controls (VisPy TurntableCamera):**

| Action | Control |
|---|---|
| Rotate | Left-click + drag |
| Zoom | Scroll wheel |
| Pan | Right-click + drag |
| Reset view | `Spacebar` or `R` |

---

## 🔧 Troubleshooting & Pro Tips

### ⚠️ Windows: Force Dedicated NVIDIA GPU for `visio_opengl.py`

On laptops with both an integrated Intel GPU and a dedicated NVIDIA GPU, Windows may run `visio_opengl.py` on the weaker integrated graphics by default. This causes noticeably poor performance and may even result in rendering artifacts. To fix this:

**Via Windows Settings**

1. Open **Windows Settings** → **System** → **Display** → **Graphics settings** (or search for "Graphics settings" directly).
2. Click **Browse** and navigate to your Python executable inside the virtual environment (e.g., `C:\...\VisioCNC\venv\Scripts\python.exe`).
3. Once added, click **Options** and select **High performance** (your NVIDIA GPU).
4. Restart the script.

Alternatively, you can force it via the **NVIDIA Control Panel**:

1. Open **NVIDIA Control Panel** → **Manage 3D settings** → **Program Settings**.
2. Click **Add** and select the Python executable from your `venv`.
3. Set "Preferred graphics processor" to **High-performance NVIDIA processor**.
4. Apply and relaunch.

---

### 🔕 Suppressing PyQt6 High-DPI Warnings

When running the OpenGL engine, you may see Qt warnings in the console related to DPI scaling, such as:

```
qt.qpa.window: ...
QWindowsWindow::setGeometry: Unable to set geometry...
```

These warnings are cosmetic and **do not affect functionality**. They are already suppressed in `visio_opengl.py` via:

```python
import os
os.environ["QT_LOGGING_RULES"] = "*.warning=false"
```

If warnings persist, you can additionally set this environment variable in your terminal before running the script:

**macOS / Linux:**
```bash
export QT_LOGGING_RULES="*.warning=false"
python visio_opengl.py
```

**Windows (PowerShell):**
```powershell
$env:QT_LOGGING_RULES="*.warning=false"
python visio_opengl.py
```

---

### 🐍 `ModuleNotFoundError` After Installing Requirements

If you receive a `ModuleNotFoundError` for any package, it most likely means your virtual environment is **not activated** in the current terminal session. Run the activation command again:

```bash
# macOS / Linux
source venv/bin/activate

# Windows CMD
venv\Scripts\activate.bat
```

Then retry running the script.

---

### 🪟 `visio_opengl.py` Window Appears Black / Empty

This usually happens when the G-Code file path is incorrect and no data was loaded. Verify:

1. Your terminal's working directory is `src/` when you run the script.
2. The `input_file` variable inside the script points to a valid `.gcode` or `.nc` file.
3. Try using an **absolute path** as a temporary test: `input_file = 'C:/path/to/VisioCNC/examples/piramida.gcode'`

---

## 🗺️ Included Example Files

| File | Description | Complexity |
|---|---|---|
| `kotak.gcode` | A simple square perimeter — the "Hello, World!" of CNC | ⭐ Basic |
| `piramida.gcode` | A multi-layer stepped pyramid built by stacking shrinking squares at increasing Z heights | ⭐⭐ Intermediate |
| `spiral_kotak.gcode` | An inward-spiraling concentric square path, simulating a pocket-milling operation | ⭐⭐ Intermediate |
| `track_robot.gcode` | A complex, closed-loop robot track / racetrack profile with sharp directional changes | ⭐⭐⭐ Advanced |
| `logo_polman.nc` | A real-world 4,574-line NC file exported from Autodesk Fusion — traces the full Polman Bandung logo contour using G2/G3 arcs and multi-pass depth cutting. The ultimate stress-test for the OpenGL engine. | ⭐⭐⭐⭐ Expert |

---

## 🗺️ Roadmap

- [ ] Support for `G2` / `G3` arc and circular interpolation commands
- [ ] Support for `G28` homing and `G92` coordinate offset commands
- [ ] GUI file picker (tkinter/PyQt6) to load G-Code files without editing source
- [ ] Export rendered toolpath as a static `.png` or animated `.gif`
- [ ] Feed rate (`F`) visualization via color gradient (slow = warm, fast = cool)
- [ ] Multi-file layer comparison mode

---

## 👨‍💻 Author

**Farhan Maulana**
Student — Politeknik Manufaktur Bandung (Polman Bandung)

VisioCNC was conceived and built as an independent engineering initiative during an academic recess — a deliberate effort to apply classroom knowledge in G-Code programming, machine kinematics, and software architecture to a tangible, open-source tool. The goal was straightforward: produce something genuinely useful for fellow students and practitioners, not just an academic exercise. If VisioCNC has helped you verify a toolpath and avoid a costly machine crash, it has done exactly what it was designed to do.

---

## 📄 License

This project is free to use as an **educational reference**. You are welcome to study the source code, adapt it for your own learning, or build upon it in academic and personal projects — with attribution.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome. If you'd like to contribute:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/arc-support`
3. Commit your changes: `git commit -m 'Add G2/G3 arc interpolation support'`
4. Push to your branch: `git push origin feature/arc-support`
5. Open a Pull Request.

---

<p align="center">Built with 🔩 and Python · Politeknik Manufaktur Bandung</p>