"""
DATA PROFIL E-CV KELOMPOK
=========================
Semua isi CV ada di file ini. Untuk mengubah isi web, cukup edit file ini
(tidak perlu menyentuh app.py). Simpan, lalu klik Rerun di browser.

Catatan:
- Kosongkan list ([]) kalau datanya belum ada; web akan menampilkan "belum diisi".
- "photo": nama file foto di folder yang sama. Kalau file tidak ada,
  otomatis dipakai avatar inisial nama.
- "icon" pada kontak/proyek: teks pendek 1-2 huruf (mis. "WA", "GH").
"""

# ----------------------------------------------------------------------------
# PROFIL KELOMPOK
# ----------------------------------------------------------------------------
TEAM = {
    "name": "Anggota Dewan",  # TODO: ganti dengan nama kelompok
    "course": "Digital Kreatif",
    "headline": "Information Systems Students & Fullstack Developers",
    "tagline": "Crafting Efficient Code to Solve Real-World Problems",
    "about": (
        "Kami adalah tim mahasiswa Sistem Informasi semester 7 yang berfokus pada "
        "pengembangan solusi digital end-to-end, mulai dari perancangan antarmuka (UI/UX) "
        "hingga arsitektur backend. Dengan mengombinasikan keahlian dalam koding dan analisis "
        "sistem, kami berdedikasi untuk membangun aplikasi yang efisien, aman, dan berdampak "
        "bagi pengguna."
    ),
}

# ----------------------------------------------------------------------------
# ANGGOTA (tambah/kurangi sesuai kebutuhan; "ip" = IP per semester)
# ----------------------------------------------------------------------------
MEMBERS = [
    {
        "name": "Brian Bernard",
        "role": "Information Systems Student & Fullstack Developer",
        "tagline": "Crafting Efficient Code to Solve Real-World Problems",
        "photo": "foto.jpg",
        "tech": ["Python", "Streamlit", "HTML/CSS", "MySQL", "PHP", "Laravel","Adobe","Canva"],
        "ip": [3.78, 4.00, 4.00, 4.00, 4.00, 4.00],
        "contacts": [
            {"icon": "WA", "label": "WhatsApp", "value": "0895331387177", "url": "https://wa.me/62895331387177"},
            {"icon": "EM", "label": "Email", "value": "brianbernardz12@gmail.com", "url": "mailto:brianbernardz12@gmail.com"},
            {"icon": "GH", "label": "GitHub", "value": "github.com/xcompany12", "url": "https://github.com/xcompany12"},
            {"icon": "IG", "label": "Instagram", "value": "@brianbrnard", "url": "https://instagram.com/brianbrnard"},
        ],
    },
    {
        "name": "Roland Kenneth",  # TODO: ganti nama anggota kedua
        "role": "Jungler Level 7",
        "tagline": "Lebih baik ditakuti daripada dicintai, Jika kamu tidak bisa mendapatkan keduanya",
        "photo": "foto2.jpg",
        "tech": ["Python", "Streamlit", "HTML/CSS", "MySQL", "PHP", "Laravel"],
        "ip": [],
        "contacts": [],
    },
]

# ----------------------------------------------------------------------------
# PROYEK
# ----------------------------------------------------------------------------
FEATURED_PROJECT = {
    "title": "E-CV / Portofolio Digital Interaktif",
    "description": (
        "Aplikasi web portofolio digital kelompok yang menampilkan profil, tech stack, "
        "perkembangan akademik, proyek, dan sertifikasi dalam satu halaman. Dibangun dengan "
        "Python dan Streamlit, dengan custom HTML/CSS, grafik interaktif, serta unduhan CV "
        "dalam bentuk PDF."
    ),
    "tech": ["Python", "Streamlit", "Plotly", "HTML/CSS"],
    "url": "https://github.com/xcompany12/ecv-digital-kreatif",
}

# Format: {"icon": "IV", "title": "Sistem Inventaris", "desc": "Deskripsi singkat.", "tech": ["Laravel", "MySQL"]}
OTHER_PROJECTS = []

# ----------------------------------------------------------------------------
# SERTIFIKAT
# ----------------------------------------------------------------------------
# Format: {"title": "Nama sertifikat", "issuer": "Penerbit", "year": "2025", "url": "https://..."}
CERTIFICATES = []
