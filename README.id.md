# 🔩 VisioCNC — Visualisator Jalur Pahat G-Code 3D Multi-Engine

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Rendering-OpenGL%20%7C%20Matplotlib-00BFFF?style=for-the-badge&logo=opengl&logoColor=white" alt="OpenGL"/>
  <img src="https://img.shields.io/badge/GPU-VisPy%20%2B%20NumPy-76B900?style=for-the-badge&logo=nvidia&logoColor=white" alt="GPU Accelerated"/>
  <img src="https://img.shields.io/badge/Lisensi-MIT-green?style=for-the-badge" alt="MIT License"/>
  <img src="https://img.shields.io/badge/Status-Aktif-brightgreen?style=for-the-badge" alt="Status"/>
</p>

<p align="center">
  <a href="README.md">🇬🇧 English</a> &nbsp;|&nbsp;
  <a href="README.id.md"><b>🇮🇩 Bahasa Indonesia</b></a>
</p>

> **Ubah instruksi mentah CNC dan printer 3D menjadi simulasi 3D interaktif — sebelum satu pun sumbu bergerak.**

---

## 📖 Tentang Proyek Ini

VisioCNC adalah visualisator jalur pahat berbasis Python dengan arsitektur multi-engine, dirancang untuk membantu **mahasiswa teknik manufaktur**, **pengembang perangkat lunak CAM**, dan **insinyur otomasi industri** dalam melakukan **simulasi "dry-run"** yang aman dan tanpa biaya dari program G-Code dan NC mereka.

Tabrakan mesin CNC itu mahal — baik dari segi waktu maupun material. Benturan yang disebabkan oleh jalur pahat yang salah, gerakan rapid G0 yang keliru, atau kedalaman Z yang tidak tepat dapat menghancurkan benda kerja, mematahkan endmill, atau dalam kasus yang parah, merusak spindle mesin. VisioCNC mengatasi hal ini dengan merender jalur pahat 3D secara lengkap di layar dengan fidelitas visual penuh, memungkinkan insinyur untuk mengaudit setiap gerakan **sebelum** program dimuat ke kontroler mesin yang sesungguhnya.

Proyek ini hadir dengan **tiga engine rendering yang berbeda**, masing-masing direkayasa untuk kebutuhan yang berbeda — mulai dari pengecekan cepat program sederhana hingga visualisasi file industri berskala besar yang diakselerasi oleh GPU.

---

## ✨ Fitur Unggulan

### 🖼️ Tiga Engine Rendering — Satu Proyek

| Engine | Skrip | Backend | Terbaik Untuk | Performa |
|---|---|---|---|---|
| **Penampil Statis** | `visio_static.py` | Matplotlib 3D | Pengecekan cepat, program sederhana | ⚡ Startup instan |
| **Simulator Animasi** | `visio_animate.py` | Matplotlib Animation | Simulasi langkah demi langkah, pembelajaran | 🎞️ Berbasis CPU |
| **Akselerasi OpenGL** | `visio_opengl.py` | VisPy + NumPy + OpenGL | File industri besar, 60 FPS mulus | 🚀 Bertenaga GPU |

### 🔑 Ringkasan Fitur

- **Parser G-Code Universal** — Menangani perintah `G0` (Rapid/Travel) dan `G1` (Pemotongan Linear) dengan pelacakan status modal penuh. Koordinat yang tidak disebutkan dalam satu baris secara otomatis mewarisi nilai dari posisi sebelumnya.
- **Jalur Pahat Berkode Warna** — Garis putus-putus merah untuk gerakan rapid `G0`; garis biru tebal untuk jalur pemotongan `G1`, sehingga perbedaan antara gerakan transit dan pemotongan dapat dikenali secara instan.
- **Pelacakan Mata Pahat Langsung** — Engine animasi merender penanda hidup yang merepresentasikan mata pahat, mengikuti jalur yang terprogram secara real-time.
- **Rendering Berakselerasi Hardware** — `visio_opengl.py` melewati loop render Python dengan mengemas semua data vertex dan warna ke dalam array NumPy, lalu mengunggahnya langsung ke VRAM melalui binding OpenGL milik VisPy. Ini memungkinkan rendering interaktif yang mulus untuk file dengan **ribuan segmen jalur pahat**.
- **Viewport 3D Interaktif** — Rotasi, zoom, dan geser semua visualisasi secara real-time menggunakan kontrol mouse.
- **Parser Aman Komentar** — Parser G-Code menghapus komentar inline (pemisah `;`) sebelum diproses, memastikan kompatibilitas dengan file yang dianotasi.

---

## 🗂️ Struktur Proyek

```
VisioCNC/
│
├── 📁 src/                         # Skrip engine rendering utama
│   ├── visio_static.py             # Engine 1: Plot 3D Matplotlib statis
│   ├── visio_animate.py            # Engine 2: Simulasi animasi Matplotlib
│   └── visio_opengl.py             # Engine 3: Renderer VisPy/OpenGL berakselerasi GPU
│
├── 📁 examples/                    # Contoh program G-Code untuk pengujian
│   ├── kotak.gcode                 # Jalur pahat kotak sederhana
│   ├── piramida.gcode              # Piramida berlapis (penumpukan Z)
│   ├── spiral_kotak.gcode          # Spiral kotak konsentris ke dalam
│   ├── track_robot.gcode           # Profil lintasan robot yang kompleks
│   └── logo_polman.nc              # File NC nyata dari Autodesk Fusion (4.574 baris)
│
├── requirements.txt                # Dependensi paket Python
├── README.id.md                    # Anda berada di sini
└── README.md                       # Dokumentasi dalam Bahasa Inggris
```

---

## 🚀 Memulai

### Prasyarat

Pastikan hal-hal berikut sudah terpasang di sistem Anda sebelum melanjutkan:

- **Python 3.10 atau lebih tinggi** — [Unduh dari python.org](https://www.python.org/downloads/)
- **pip** (sudah terbundel dengan Python 3.10+)
- **Git** — [Unduh dari git-scm.com](https://git-scm.com/)
- GPU dedicated **disarankan** (namun tidak wajib) untuk menjalankan `visio_opengl.py`.

---

### Langkah 1 — Clone Repositori

```bash
git clone https://github.com/Dragon-Asce/VisioCNC.git
cd VisioCNC
```

---

### Langkah 2 — Buat Virtual Environment

Sangat disarankan untuk menginstal dependensi di dalam virtual environment yang terisolasi, guna menghindari konflik dengan paket Python yang terinstal di sistem Anda.

**Di macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Di Windows (Command Prompt):**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

**Di Windows (PowerShell):**
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

Tanda `(venv)` akan muncul di awal baris terminal Anda, menandakan environment telah aktif.

---

### Langkah 3 — Instal Dependensi

Dengan virtual environment aktif, instal semua paket yang dibutuhkan dari `requirements.txt`:

```bash
pip install -r requirements.txt
```

Perintah ini akan menginstal paket-paket berikut:

| Paket | Versi | Fungsi |
|---|---|---|
| `matplotlib` | ≥ 3.7.0 | Plot statis dan animasi berbasis CPU |
| `numpy` | ≥ 1.24.0 | Operasi array berperforma tinggi untuk upload ke GPU |
| `vispy` | ≥ 0.14.0 | Pipeline rendering berbasis OpenGL |
| `PyQt6` | ≥ 6.5.0 | Backend windowing GUI untuk VisPy |

---

## 🖥️ Cara Penggunaan

Ketiga skrip berada di dalam folder `src/`. Sebelum menjalankan, pastikan **direktori kerja terminal Anda berada di `src/`**, karena skrip mereferensikan file contoh menggunakan path relatif yang mengarah ke `../examples/`.

```bash
cd src
```

Di dalam setiap skrip, terdapat variabel bernama `input_file` di bagian bawah. Ubah path ini untuk mengarahkan ke file G-Code yang ingin Anda visualisasikan.

```python
# Contoh — ubah baris ini di salah satu dari ketiga skrip
input_file = '../examples/piramida.gcode'
```

---

### Engine 1 — Penampil Statis

**Terbaik untuk:** Visualisasi jalur penuh secara cepat. Merender seluruh jalur pahat sekaligus sebagai plot 3D statis. Ideal untuk pengecekan cepat terhadap program G-Code apa pun.

```bash
python visio_static.py
```

Seluruh jalur pahat dirender sekaligus. Gunakan mouse untuk merotasi tampilan 3D, scroll untuk zoom, dan klik tengah untuk menggeser pandangan.

---

### Engine 2 — Simulator Animasi

**Terbaik untuk:** Pembelajaran, presentasi, dan debugging langkah demi langkah. Mensimulasikan pergerakan mata pahat melalui jalur secara berurutan, baris per baris.

```bash
python visio_animate.py
```

Kecepatan animasi dikendalikan oleh parameter `interval` di dalam pemanggilan `FuncAnimation` (dalam milidetik). Nilai yang lebih kecil menghasilkan simulasi yang lebih cepat:

```python
# Di visio_animate.py — sesuaikan nilai ini untuk mengatur kecepatan animasi
ani = animation.FuncAnimation(
    fig,
    update,
    frames=len(segments),
    interval=50,   # ← Lebih kecil = lebih cepat (default: 300ms per langkah)
    ...
)
```

---

### Engine 3 — Renderer Berakselerasi OpenGL

**Terbaik untuk:** File G-Code industri yang besar dan kompleks dengan ratusan hingga ribuan segmen. Ini adalah engine unggulan — mengirim data vertex langsung ke VRAM dan merender hingga 60 FPS dengan viewport 3D yang sepenuhnya interaktif.

```bash
python visio_opengl.py
```

Kecepatan rendering dikontrol oleh `speed_multiplier` — jumlah vertex segmen garis yang digambar per frame:

```python
# Di visio_opengl.py — naikkan nilai ini untuk animasi yang lebih cepat
speed_multiplier = 50  # ← Default adalah 5; naikkan untuk file besar
```

**Kontrol Viewport (VisPy TurntableCamera):**

| Aksi | Kontrol |
|---|---|
| Rotasi | Klik kiri + seret |
| Zoom | Scroll mouse |
| Geser pandangan | Klik kanan + seret |
| Reset tampilan | `Spacebar` atau `R` |

---

## 🔧 Pemecahan Masalah & Tips Pro

### ⚠️ Windows: Paksa GPU NVIDIA Dedicated untuk `visio_opengl.py`

Pada laptop dengan GPU Intel terintegrasi dan GPU NVIDIA dedicated, Windows mungkin menjalankan `visio_opengl.py` pada grafis terintegrasi yang lebih lemah secara default. Hal ini menyebabkan performa yang jauh di bawah standar dan bahkan dapat menimbulkan artefak rendering. Untuk memperbaikinya:

**Melalui Pengaturan Windows:**

1. Buka **Pengaturan Windows** → **Sistem** → **Layar** → **Pengaturan grafis** (atau cari "Pengaturan grafis" langsung).
2. Klik **Telusuri** dan arahkan ke executable Python di dalam virtual environment Anda (misalnya, `C:\...\VisioCNC\venv\Scripts\python.exe`).
3. Setelah ditambahkan, klik **Opsi** dan pilih **Performa tinggi** (GPU NVIDIA Anda).
4. Jalankan ulang skrip.

**Melalui NVIDIA Control Panel:**

1. Buka **NVIDIA Control Panel** → **Manage 3D settings** → **Program Settings**.
2. Klik **Add** dan pilih executable Python dari `venv` Anda.
3. Atur "Preferred graphics processor" ke **High-performance NVIDIA processor**.
4. Klik Apply dan jalankan ulang skrip.

---

### 🔕 Menekan Peringatan High-DPI PyQt6

Saat menjalankan engine OpenGL, Anda mungkin melihat peringatan Qt di konsol terkait penskalaan DPI, seperti:

```
qt.qpa.window: ...
QWindowsWindow::setGeometry: Unable to set geometry...
```

Peringatan ini bersifat kosmetik dan **tidak memengaruhi fungsionalitas** sama sekali. Peringatan ini sudah ditekan di dalam `visio_opengl.py` melalui:

```python
import os
os.environ["QT_LOGGING_RULES"] = "*.warning=false"
```

Jika peringatan masih muncul, Anda dapat menetapkan environment variable ini secara manual di terminal sebelum menjalankan skrip:

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

### 🐍 `ModuleNotFoundError` Setelah Menginstal Requirements

Jika Anda mendapat error `ModuleNotFoundError` untuk salah satu paket, kemungkinan besar virtual environment Anda **belum diaktifkan** di sesi terminal saat ini. Jalankan kembali perintah aktivasi:

```bash
# macOS / Linux
source venv/bin/activate

# Windows CMD
venv\Scripts\activate.bat
```

Kemudian coba jalankan skripnya kembali.

---

### 🪟 Jendela `visio_opengl.py` Tampil Hitam / Kosong

Ini biasanya terjadi ketika path file G-Code salah dan tidak ada data yang berhasil dimuat. Periksa hal berikut:

1. Direktori kerja terminal Anda adalah `src/` saat menjalankan skrip.
2. Variabel `input_file` di dalam skrip mengarah ke file `.gcode` atau `.nc` yang valid.
3. Coba gunakan **path absolut** sebagai uji coba sementara: `input_file = 'C:/path/ke/VisioCNC/examples/piramida.gcode'`

---

## 🗺️ File Contoh yang Tersedia

| File | Deskripsi | Kompleksitas |
|---|---|---|
| `kotak.gcode` | Perimeter kotak sederhana — "Hello, World!"-nya dunia CNC | ⭐ Dasar |
| `piramida.gcode` | Piramida bertingkat multi-lapis yang dibangun dengan menumpuk kotak yang mengecil pada ketinggian Z yang meningkat | ⭐⭐ Menengah |
| `spiral_kotak.gcode` | Jalur kotak konsentris yang berputar ke dalam, mensimulasikan operasi pocket-milling | ⭐⭐ Menengah |
| `track_robot.gcode` | Profil lintasan robot tertutup yang kompleks dengan perubahan arah tajam | ⭐⭐⭐ Lanjutan |
| `logo_polman.nc` | File NC nyata sebanyak 4.574 baris yang diekspor dari Autodesk Fusion — menelusuri kontur penuh logo Polman Bandung menggunakan arc G2/G3 dan pemotongan multi-kedalaman. Uji beban terbaik untuk engine OpenGL. | ⭐⭐⭐⭐ Mahir |

---

## 🗺️ Rencana Pengembangan

- [ ] Dukungan perintah arc dan interpolasi melingkar `G2` / `G3`
- [ ] Dukungan perintah homing `G28` dan offset koordinat `G92`
- [ ] GUI file picker (tkinter/PyQt6) untuk memuat file G-Code tanpa mengubah kode sumber
- [ ] Ekspor jalur pahat yang dirender sebagai gambar `.png` statis atau animasi `.gif`
- [ ] Visualisasi feed rate (`F`) melalui gradien warna (lambat = hangat, cepat = dingin)
- [ ] Mode perbandingan lapisan multi-file

---

## 👨‍💻 Penulis

**Farhan Maulana**
Mahasiswa — Politeknik Manufaktur Bandung (Polman Bandung)

VisioCNC dirancang dan dibangun sebagai inisiatif rekayasa mandiri selama masa jeda akademik — sebuah upaya terencana untuk mengaplikasikan pengetahuan perkuliahan di bidang pemrograman G-Code, kinematika mesin, dan arsitektur perangkat lunak ke dalam sebuah karya nyata yang bersifat open-source. Tujuannya sederhana namun konkret: menghasilkan sesuatu yang benar-benar bermanfaat bagi sesama mahasiswa dan praktisi, bukan sekadar latihan akademis. Jika VisioCNC telah membantu Anda memverifikasi jalur pahat dan mencegah kerusakan mesin yang merugikan, maka proyek ini telah memenuhi tujuannya.

---

## 📄 Lisensi

Proyek ini **bebas digunakan sebagai referensi edukasi**. Anda dipersilakan untuk mempelajari kode sumbernya, mengadaptasinya untuk keperluan belajar, atau mengembangkannya lebih lanjut dalam proyek akademis maupun pribadi — dengan tetap mencantumkan atribusi kepada penulis asli.

---

## 🤝 Berkontribusi

Kontribusi, laporan isu, dan permintaan fitur sangat disambut. Jika Anda ingin berkontribusi:

1. Fork repositori ini.
2. Buat branch fitur baru: `git checkout -b fitur/dukungan-arc`
3. Commit perubahan Anda: `git commit -m 'Tambah dukungan interpolasi arc G2/G3'`
4. Push ke branch Anda: `git push origin fitur/dukungan-arc`
5. Buka Pull Request.

---

<p align="center">Dibangun dengan 🔩 dan Python · Politeknik Manufaktur Bandung</p>