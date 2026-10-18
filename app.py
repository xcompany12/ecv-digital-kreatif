"""
E-CV / Portofolio Digital Interaktif
Tugas Kelompok - Digital Kreatif
Dibuat dengan Python + Streamlit

Jalankan:  streamlit run app.py
"""

import base64
import io
from pathlib import Path

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# =============================================================================
# 1. KONFIGURASI HALAMAN
# =============================================================================
st.set_page_config(
    page_title="E-CV | Portofolio Digital",
    page_icon="💠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =============================================================================
# 2. DATA DUMMY  (ganti dengan data asli kelompok/mahasiswa)
# =============================================================================
PROFILE = {
    "name": "Brian Bernard",
    "headline": "Information Systems Student & Fullstack Developer",
    "tagline": "Crafting Efficient Code to Solve Real-World Problems",
    "avatar": "foto.jpg",  # file foto di folder yang sama dengan app.py
    "avatar_fallback": "https://api.dicebear.com/7.x/avataaars/svg?seed=ECV&backgroundColor=1b1740",
    "location": "Jakarta",
    "about": (
        "Kami adalah tim mahasiswa Sistem Informasi semester 7 yang berfokus pada "
        "pengembangan solusi digital end-to-end, mulai dari perancangan antarmuka (UI/UX) "
        "hingga arsitektur backend. Dengan mengombinasikan keahlian dalam koding dan analisis "
        "sistem, kami berdedikasi untuk membangun aplikasi yang efisien, aman, dan berdampak "
        "bagi pengguna."
    ),
}

TECH_STACK = ["Python", "Streamlit", "HTML/CSS", "MySQL", "PHP", "Laravel"]

CONTACTS = [
    {"icon": "💬", "label": "WhatsApp", "value": "0895331387177", "url": "https://wa.me/62895331387177"},
    {"icon": "✉️", "label": "Email", "value": "brianbernardz12@gmail.com", "url": "mailto:brianbernardz12@gmail.com"},
    {"icon": "🐙", "label": "GitHub", "value": "github.com/xcompany12", "url": "https://github.com/xcompany12"},
    {"icon": "📸", "label": "Instagram", "value": "@brianbrnard", "url": "https://instagram.com/brianbrnard"},
]

# Indeks Prestasi (IP) per semester
GPA = pd.DataFrame(
    {
        "Semester": ["Sem 1", "Sem 2", "Sem 3", "Sem 4", "Sem 5", "Sem 6"],
        "IPK": [3.78, 4.00, 4.00, 4.00, 4.00, 4.00],
    }
)

# Transkrip per mata kuliah (opsional). Isi dengan baris: ["Sem 1", "Nama MK", 3, "A"]
TRANSCRIPT = pd.DataFrame(columns=["Semester", "Mata Kuliah", "SKS", "Nilai"])

FEATURED_PROJECT = {
    "title": "E-CV / Portofolio Digital Interaktif",
    "description": (
        "Aplikasi web portofolio digital kelompok yang menampilkan profil, tech stack, "
        "perkembangan akademik, proyek, dan sertifikasi dalam satu halaman. Dibangun dengan "
        "Python dan Streamlit, dengan tema gelap dan tampilan kartu dari custom HTML/CSS, "
        "grafik interaktif, serta unduhan CV dalam bentuk PDF."
    ),
    "tech": ["Python", "Streamlit", "Plotly", "HTML/CSS"],
    "url": "https://github.com/xcompany12",
}

# Tambah proyek baru dengan format:
# {"icon": "📦", "title": "Nama", "desc": "Deskripsi singkat", "tech": ["Laravel", "MySQL"]}
OTHER_PROJECTS = []

# Tambah sertifikat baru dengan format:
# {"title": "Nama", "issuer": "Penerbit", "year": "2025", "url": "https://..."}
CERTIFICATES = []

# =============================================================================
# 3. CUSTOM CSS  (tema gelap, biru/ungu neon, kartu & badge)
# =============================================================================
CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700&family=Inter:wght@400;500&display=swap');

:root {
  --bg: #0b0a1a;
  --panel: #14122b;
  --panel-2: #1b1840;
  --line: #2b2763;
  --text: #e9e8ff;
  --muted: #9b98c9;
  --blue: #4cc9ff;
  --violet: #9b6bff;
  --pink: #d46bff;
}

html, body, [class*="css"], .stApp { font-family: 'Inter', sans-serif; }
.stApp {
  background:
    radial-gradient(900px 500px at 85% -10%, rgba(155,107,255,.22), transparent 60%),
    radial-gradient(700px 400px at -10% 10%, rgba(76,201,255,.14), transparent 60%),
    var(--bg);
  color: var(--text);
}
header[data-testid="stHeader"] { background: transparent; }
.block-container { padding-top: 2rem; max-width: 1100px; }

h1, h2, h3, h4 { font-family: 'Sora', sans-serif !important; color: var(--text) !important; }

/* Sidebar */
section[data-testid="stSidebar"] { background: var(--panel); border-right: 1px solid var(--line); }
.side-name { font-family: 'Sora', sans-serif; font-weight: 700; font-size: 1.1rem; margin: .4rem 0 0; }
.side-sub { color: var(--muted); font-size: .85rem; margin-bottom: 1rem; }
.side-link {
  display: block; padding: .5rem .8rem; margin: .15rem 0; border-radius: 10px;
  color: var(--text) !important; text-decoration: none !important; font-size: .92rem;
  border: 1px solid transparent; transition: all .2s ease;
}
.side-link:hover { background: var(--panel-2); border-color: var(--line); color: var(--blue) !important; }

section[data-testid="stSidebar"] .side-name { color: var(--text); }
section[data-testid="stSidebar"] [data-testid="stMetricLabel"] p { color: var(--muted) !important; }
section[data-testid="stSidebar"] [data-testid="stMetricValue"] { color: var(--text) !important; }
div[role="dialog"] { background: var(--panel); color: var(--text); }

/* Hero */
.hero {
  display: flex; gap: 2rem; align-items: center; flex-wrap: wrap;
  background: linear-gradient(135deg, rgba(76,201,255,.10), rgba(155,107,255,.16));
  border: 1px solid var(--line); border-radius: 22px; padding: 2rem;
  box-shadow: 0 0 40px rgba(155,107,255,.18);
}
.hero img {
  width: 150px; height: 150px; border-radius: 50%; object-fit: cover;
  border: 3px solid var(--violet); box-shadow: 0 0 28px rgba(155,107,255,.6); background: var(--panel-2);
}
.hero-name { font-family: 'Sora', sans-serif; font-size: 2.3rem; font-weight: 700; margin: 0; line-height: 1.15; }
.hero-headline {
  font-family: 'Sora', sans-serif; font-size: 1.05rem; margin: .4rem 0;
  background: linear-gradient(90deg, var(--blue), var(--pink));
  -webkit-background-clip: text; background-clip: text; color: transparent;
}
.hero-quote { color: var(--muted); font-style: italic; margin: .2rem 0 0; }

/* Judul section */
.sec-title { font-size: 1.5rem; font-weight: 700; margin: 2.6rem 0 1rem; padding-left: .8rem; border-left: 4px solid var(--violet); }

/* Kartu */
.card {
  background: var(--panel); border: 1px solid var(--line); border-radius: 16px;
  padding: 1.2rem 1.3rem; height: 100%; transition: border-color .2s ease, box-shadow .2s ease;
}
.card:hover { border-color: var(--violet); box-shadow: 0 0 22px rgba(155,107,255,.28); }
.card h4 { margin: 0 0 .35rem; font-size: 1.05rem; }
.card p { color: var(--muted); margin: 0 0 .7rem; font-size: .93rem; line-height: 1.55; }
.card-icon { font-size: 1.6rem; margin-bottom: .3rem; }
.card-meta { color: var(--muted); font-size: .85rem; margin-bottom: .6rem; }
.featured { border: 1px solid var(--violet); background: linear-gradient(160deg, var(--panel-2), var(--panel)); box-shadow: 0 0 32px rgba(155,107,255,.25); }

/* Badge */
.badge {
  display: inline-block; padding: .25rem .75rem; margin: 0 .35rem .4rem 0; border-radius: 999px;
  font-size: .8rem; color: var(--blue); background: rgba(76,201,255,.08);
  border: 1px solid rgba(76,201,255,.45);
}
.badge.v { color: #c9b0ff; background: rgba(155,107,255,.1); border-color: rgba(155,107,255,.55); }

/* Tombol tautan */
.btn {
  display: inline-block; padding: .45rem 1rem; border-radius: 10px; font-size: .88rem; font-weight: 500;
  color: #fff !important; text-decoration: none !important;
  background: linear-gradient(90deg, #4c7dff, #9b6bff); transition: filter .2s ease;
}
.btn:hover { filter: brightness(1.15); }

/* Tombol bawaan Streamlit */
.stButton > button, .stDownloadButton > button {
  background: linear-gradient(90deg, #4c7dff, #9b6bff); color: #fff; border: none;
  border-radius: 10px; font-weight: 500; padding: .5rem 1.2rem;
}
.stButton > button:hover, .stDownloadButton > button:hover { filter: brightness(1.15); color: #fff; border: none; }

.footer { text-align: center; color: var(--muted); font-size: .85rem; margin: 3rem 0 1rem; }
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)


# =============================================================================
# 4. FUNGSI BANTU
# =============================================================================
@st.cache_data
def get_avatar_src(filename: str, fallback: str) -> str:
    """Pakai foto lokal (diubah ke base64) bila ada; kalau tidak ada, pakai URL cadangan."""
    path = Path(__file__).parent / filename
    if path.is_file():
        mime = "image/png" if path.suffix.lower() == ".png" else "image/jpeg"
        return f"data:{mime};base64,{base64.b64encode(path.read_bytes()).decode()}"
    return fallback


def badges(items, violet=False):
    """Membuat deretan badge teknologi dalam HTML."""
    cls = "badge v" if violet else "badge"
    return "".join(f'<span class="{cls}">{t}</span>' for t in items)


def section_title(text, anchor):
    """Judul section dengan anchor agar bisa dituju dari sidebar."""
    st.markdown(f'<div id="{anchor}" class="sec-title">{text}</div>', unsafe_allow_html=True)


def build_cv_pdf() -> bytes:
    """Membuat CV PDF sederhana dari data di atas (memakai fpdf2)."""
    from fpdf import FPDF

    def clean(text):  # font bawaan hanya mendukung latin-1
        return str(text).encode("latin-1", "replace").decode("latin-1")

    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    def line(text, h=6):
        """Tulis satu paragraf lalu kembali ke margin kiri (aman untuk fpdf2 terbaru)."""
        pdf.set_x(pdf.l_margin)
        pdf.multi_cell(0, h, clean(text), new_x="LMARGIN", new_y="NEXT")

    def heading(text):
        pdf.ln(2)
        pdf.set_font("Helvetica", "B", 13)
        line(text, 9)
        pdf.set_font("Helvetica", "", 10.5)

    pdf.set_font("Helvetica", "B", 20)
    line(PROFILE["name"], 10)
    pdf.set_font("Helvetica", "", 11)
    line(PROFILE["headline"], 7)
    line(PROFILE["location"], 7)

    heading("Tentang Saya")
    line(PROFILE["about"])

    heading("Tech Stack")
    line(", ".join(TECH_STACK))

    heading("Kontak")
    for c in CONTACTS:
        line(f"{c['label']}: {c['value']}")

    heading("IP per Semester")
    for _, row in GPA.iterrows():
        line(f"{row['Semester']}: {row['IPK']:.2f}")

    heading("Proyek")
    line(f"{FEATURED_PROJECT['title']} ({', '.join(FEATURED_PROJECT['tech'])})")
    for p in OTHER_PROJECTS:
        line(f"- {p['title']}: {p['desc']}")

    heading("Lisensi & Sertifikasi")
    if not CERTIFICATES:
        line("Belum ada.")
    for c in CERTIFICATES:
        line(f"- {c['title']} - {c['issuer']} ({c['year']})")

    return bytes(pdf.output())


@st.dialog("Transkrip Nilai", width="large")
def show_transcript():
    """Pop-up transkrip nilai."""
    st.markdown("**IP per semester**")
    st.dataframe(GPA.rename(columns={"IPK": "IP"}), use_container_width=True, hide_index=True)
    if TRANSCRIPT.empty:
        st.caption("Rincian nilai per mata kuliah belum diisi.")
    else:
        st.markdown("**Rincian mata kuliah**")
        st.dataframe(TRANSCRIPT, use_container_width=True, hide_index=True)


# =============================================================================
# 5. SIDEBAR  (navigasi + info singkat)
# =============================================================================
with st.sidebar:
    st.markdown(
        f"""
<div class="side-name">{PROFILE['name']}</div>
<div class="side-sub">📍 {PROFILE['location']}</div>
<a class="side-link" href="#tentang" target="_self">Tentang & Tech Stack</a>
<a class="side-link" href="#kontak" target="_self">Kontak & Sosial Media</a>
<a class="side-link" href="#akademik" target="_self">Perkembangan Akademik</a>
<a class="side-link" href="#proyek" target="_self">Portofolio Proyek</a>
<a class="side-link" href="#sertifikat" target="_self">Lisensi & Sertifikasi</a>
""",
        unsafe_allow_html=True,
    )
    st.divider()
    st.metric("Rata-rata IP", f"{GPA['IPK'].mean():.2f}")
    st.metric("Semester Selesai", len(GPA))


# =============================================================================
# 6. HEADER UTAMA
# =============================================================================
avatar_src = get_avatar_src(PROFILE["avatar"], PROFILE["avatar_fallback"])
st.markdown(
    f"""
<div class="hero">
<img src="{avatar_src}" alt="Foto profil">
<div>
<p class="hero-name">{PROFILE['name']}</p>
<p class="hero-headline">{PROFILE['headline']}</p>
<p class="hero-quote">“{PROFILE['tagline']}”</p>
</div>
</div>
""",
    unsafe_allow_html=True,
)

st.write("")
try:
    st.download_button(
        "Download CV PDF",
        data=build_cv_pdf(),
        file_name="CV_Portofolio.pdf",
        mime="application/pdf",
    )
except ModuleNotFoundError:
    st.warning("Library fpdf2 belum terpasang. Jalankan: pip install fpdf2")

# =============================================================================
# 7. TENTANG SAYA & CORE TECH STACK
# =============================================================================
section_title("Tentang Saya & Core Tech Stack", "tentang")
col_a, col_b = st.columns([3, 2], gap="medium")
with col_a:
    st.markdown(
        f'<div class="card"><h4>Tentang Saya</h4><p>{PROFILE["about"]}</p></div>',
        unsafe_allow_html=True,
    )
with col_b:
    st.markdown(
        f'<div class="card"><h4>Core Tech Stack</h4>{badges(TECH_STACK)}</div>',
        unsafe_allow_html=True,
    )

# =============================================================================
# 8. KONTAK & SOSIAL MEDIA
# =============================================================================
section_title("Kontak & Sosial Media", "kontak")
cols = st.columns(len(CONTACTS), gap="small")
for col, c in zip(cols, CONTACTS):
    with col:
        st.markdown(
            f"""
<div class="card">
<div class="card-icon">{c['icon']}</div>
<h4>{c['label']}</h4>
<p>{c['value']}</p>
<a class="btn" href="{c['url']}" target="_blank">Buka</a>
</div>
""",
            unsafe_allow_html=True,
        )

# =============================================================================
# 9. PERKEMBANGAN AKADEMIK (IPK)
# =============================================================================
section_title("Perkembangan Akademik (IPK)", "akademik")

fig = go.Figure(
    go.Bar(
        x=GPA["Semester"],
        y=GPA["IPK"],
        text=[f"{v:.2f}" for v in GPA["IPK"]],
        textposition="outside",
        marker=dict(
            color=GPA["IPK"],
            colorscale=[[0, "#4cc9ff"], [1, "#9b6bff"]],
            line=dict(color="rgba(255,255,255,.15)", width=1),
        ),
        hovertemplate="%{x}<br>IP %{y:.2f}<extra></extra>",
    )
)
fig.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color="#e9e8ff", family="Inter"),
    yaxis=dict(range=[0, 4.2], gridcolor="#2b2763", title="IP"),
    xaxis=dict(title=None),
    margin=dict(l=10, r=10, t=20, b=10),
    height=360,
)
st.plotly_chart(fig, use_container_width=True)

st.caption("IP = Indeks Prestasi pada masing-masing semester.")
if st.button("Lihat Transkrip Nilai"):
    show_transcript()

# =============================================================================
# 10. PORTOFOLIO PROYEK
# =============================================================================
section_title("Portofolio Proyek", "proyek")

# 10a. Proyek utama
st.markdown(
    f"""
<div class="card featured">
<h4 style="font-size:1.3rem">⭐ {FEATURED_PROJECT['title']}</h4>
<p>{FEATURED_PROJECT['description']}</p>
{badges(FEATURED_PROJECT['tech'], violet=True)}
<div style="margin-top:.6rem"><a class="btn" href="{FEATURED_PROJECT['url']}" target="_blank">Lihat di GitHub</a></div>
</div>
""",
    unsafe_allow_html=True,
)

# 10b. Proyek lainnya (grid 3 kolom)
st.markdown("#### Proyek Lainnya")
if not OTHER_PROJECTS:
    st.markdown(
        '<div class="card"><h4>Segera hadir</h4><p>Proyek lainnya akan ditambahkan di sini.</p></div>',
        unsafe_allow_html=True,
    )
for i in range(0, len(OTHER_PROJECTS), 3):
    row = st.columns(3, gap="small")
    for col, p in zip(row, OTHER_PROJECTS[i : i + 3]):
        with col:
            st.markdown(
                f"""
<div class="card">
<div class="card-icon">{p['icon']}</div>
<h4>{p['title']}</h4>
<p>{p['desc']}</p>
{badges(p['tech'])}
</div>
""",
                unsafe_allow_html=True,
            )
    st.write("")

# =============================================================================
# 11. LISENSI & SERTIFIKASI
# =============================================================================
section_title("Lisensi & Sertifikasi", "sertifikat")
if not CERTIFICATES:
    st.markdown(
        '<div class="card"><h4>Belum ada sertifikat</h4><p>Sertifikat dan pelatihan akan ditambahkan di sini.</p></div>',
        unsafe_allow_html=True,
    )
for i in range(0, len(CERTIFICATES), 2):
    row = st.columns(2, gap="medium")
    for col, c in zip(row, CERTIFICATES[i : i + 2]):
        with col:
            st.markdown(
                f"""
<div class="card">
<h4>🏅 {c['title']}</h4>
<div class="card-meta">{c['issuer']} • {c['year']}</div>
<a class="btn" href="{c['url']}" target="_blank">Lihat Sertifikat</a>
</div>
""",
                unsafe_allow_html=True,
            )
    st.write("")

# =============================================================================
# 12. FOOTER
# =============================================================================
st.markdown(
    '<div class="footer">Dibuat dengan Python & Streamlit untuk tugas Digital Kreatif.</div>',
    unsafe_allow_html=True,
)
