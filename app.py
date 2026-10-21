"""
E-CV / Portofolio Digital Kelompok - tampilan profesional (tema terang)
Tugas Kelompok - Digital Kreatif | Python + Streamlit

File ini hanya mengatur TAMPILAN. Semua isi CV ada di data_profile.py.
Jalankan:  streamlit run app.py
"""

import base64
from pathlib import Path

import plotly.graph_objects as go
import streamlit as st

from data_profile import CERTIFICATES, FEATURED_PROJECT, MEMBERS, OTHER_PROJECTS, TEAM

st.set_page_config(
    page_title=f"{TEAM['name']} | E-CV",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed",
)

COLORS = ["#4f46e5", "#0ea5e9"]  # warna anggota 1 dan 2

# =============================================================================
# 1. CSS
# =============================================================================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;700;800&family=Inter:wght@400;500&display=swap');
:root{--bg:#f6f7fb;--card:#fff;--line:#e5e7f0;--text:#1b1f3a;--muted:#626a86;--indigo:#4f46e5;--sky:#0ea5e9;--tint:#eef2ff;--tint2:#e0f2fe}
html,body,[class*="css"],.stApp{font-family:'Inter',sans-serif}
.stApp{background:var(--bg);color:var(--text)}
header[data-testid="stHeader"]{background:transparent}
.block-container{padding-top:1rem;max-width:1100px}
h1,h2,h3,h4,h5{font-family:'Plus Jakarta Sans',sans-serif!important;color:var(--text)!important}
@keyframes fadeUp{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}

section[data-testid="stSidebar"]{background:#fff;border-right:1px solid var(--line)}

/* Navbar */
.nav{display:flex;justify-content:space-between;align-items:center;background:#fff;border:1px solid var(--line);border-radius:14px;padding:.6rem 1rem;margin-bottom:2.2rem;flex-wrap:wrap;gap:.4rem}
.brand{display:flex;align-items:center;gap:.6rem;font-family:'Plus Jakarta Sans',sans-serif;font-weight:800;color:var(--text)}
.logo{width:30px;height:30px;border-radius:8px;background:var(--indigo);color:#fff;display:flex;align-items:center;justify-content:center;font-size:.8rem;font-weight:700}
.links a{color:var(--muted)!important;text-decoration:none!important;font-size:.9rem;font-weight:500;padding:.4rem .8rem;border-radius:8px;display:inline-block;transition:all .2s}
.links a:hover{background:var(--tint);color:var(--indigo)!important}

/* Hero */
.kicker{display:inline-block;color:var(--indigo);background:var(--tint);border-radius:8px;padding:.3rem .75rem;font-size:.82rem;font-weight:500;margin-bottom:1rem}
.hero-title{font-family:'Plus Jakarta Sans',sans-serif;font-size:2.8rem;font-weight:800;line-height:1.12;color:var(--text);margin-bottom:.6rem}
.hero-headline{font-size:1.1rem;font-weight:500;color:var(--indigo);margin-bottom:.5rem}
.hero-sub{color:var(--muted);line-height:1.65;margin-bottom:1.3rem;max-width:32rem}
.roster{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:1.2rem 1.3rem;box-shadow:0 10px 30px rgba(27,31,58,.07);animation:fadeUp .7s ease both}
.roster-h{font-family:'Plus Jakarta Sans',sans-serif;font-weight:700;margin-bottom:.8rem}
.r-row{display:flex;align-items:center;gap:.9rem;padding:.7rem 0;border-top:1px solid var(--line)}
.r-av{width:52px;height:52px;border-radius:12px;object-fit:cover;object-position:top;background:var(--tint);flex:none}
.r-name{font-weight:600;font-size:.98rem}
.r-role{color:var(--muted);font-size:.84rem}
.roster-f{display:flex;gap:1.2rem;border-top:1px solid var(--line);padding-top:.9rem;margin-top:.2rem}
.roster-f b{display:block;font-family:'Plus Jakarta Sans',sans-serif;font-size:1.3rem;color:var(--indigo)}
.roster-f span{color:var(--muted);font-size:.8rem}

/* Section */
.sec{margin:3rem 0 1.1rem}
.sec h2{font-size:1.65rem;font-weight:800;margin:0}
.sec p{color:var(--muted);margin:.2rem 0 0;font-size:.95rem}

/* Kartu */
.card{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:1.2rem 1.35rem;height:100%;transition:all .2s;animation:fadeUp .5s ease both}
.card:hover{border-color:#c7d2fe;box-shadow:0 10px 28px rgba(79,70,229,.10)}
.card h4{margin:0 0 .4rem;font-size:1.05rem}
.card p{color:var(--muted);margin:0 0 .8rem;font-size:.93rem;line-height:1.6}
.card-meta{color:var(--muted);font-size:.85rem;margin-bottom:.7rem}
.stat{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:1rem 1.2rem}
.stat b{display:block;font-family:'Plus Jakarta Sans',sans-serif;font-size:1.8rem;font-weight:800;color:var(--indigo)}
.stat span{color:var(--muted);font-size:.85rem}
.cic{width:38px;height:38px;border-radius:10px;background:var(--tint);color:var(--indigo);display:flex;align-items:center;justify-content:center;font-size:.8rem;font-weight:700;flex:none}

/* Anggota */
.pro{display:flex;gap:1.1rem;background:var(--card);border:1px solid var(--line);border-top-width:4px;border-radius:16px;padding:1.2rem 1.3rem;height:100%;transition:all .2s;animation:fadeUp .6s ease both}
.pro:hover{box-shadow:0 10px 28px rgba(79,70,229,.10)}
.pro-av{width:96px;height:96px;border-radius:14px;object-fit:cover;object-position:top;background:var(--tint);flex:none}
.pro-name{font-family:'Plus Jakarta Sans',sans-serif;font-weight:700;font-size:1.2rem}
.pro-role{font-size:.88rem;font-weight:500;margin:.1rem 0 .4rem}
.pro-tag{color:var(--muted);font-style:italic;font-size:.9rem;margin-bottom:.7rem}

/* Daftar kontak */
.clist{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:.4rem}
.crow{display:flex;align-items:center;gap:.8rem;padding:.65rem .7rem;border-radius:10px;text-decoration:none!important;color:var(--text)!important;transition:background .2s}
.crow:hover{background:var(--tint)}
.cl{font-size:.8rem;color:var(--muted);display:block}
.cv{font-weight:500;font-size:.92rem;word-break:break-all}
.ca{margin-left:auto;color:var(--muted)}

/* Badge & tombol */
.badge{display:inline-block;padding:.25rem .75rem;margin:0 .35rem .4rem 0;border-radius:8px;font-size:.8rem;font-weight:500;color:#4338ca;background:var(--tint)}
.badge.s{color:#0369a1;background:var(--tint2)}
.pill{display:inline-block;font-size:.78rem;font-weight:500;color:var(--indigo);background:var(--tint);border-radius:999px;padding:.2rem .7rem;margin-bottom:.6rem}
.btn{display:inline-block;padding:.5rem 1.1rem;border-radius:10px;font-size:.88rem;font-weight:500;color:#fff!important;text-decoration:none!important;background:var(--indigo);transition:background .2s}
.btn:hover{background:#4338ca}
.btn.o{background:#fff;color:var(--indigo)!important;border:1px solid #c7d2fe}
.btn.o:hover{background:var(--tint)}
.stButton>button,.stDownloadButton>button{border-radius:10px;font-weight:500;padding:.55rem 1.3rem;transition:all .2s}
.stButton>button[kind="primary"],.stDownloadButton>button[kind="primary"],button[data-testid="stBaseButton-primary"]{background:var(--indigo);color:#fff;border:1px solid var(--indigo)}
.stButton>button[kind="primary"]:hover,.stDownloadButton>button[kind="primary"]:hover,button[data-testid="stBaseButton-primary"]:hover{background:#4338ca;color:#fff;border-color:#4338ca}
.stButton>button[kind="secondary"],.stDownloadButton>button[kind="secondary"],button[data-testid="stBaseButton-secondary"]{background:#fff;color:var(--indigo);border:1px solid #c7d2fe}
.stButton>button[kind="secondary"]:hover,.stDownloadButton>button[kind="secondary"]:hover,button[data-testid="stBaseButton-secondary"]:hover{background:var(--tint);color:var(--indigo);border-color:var(--indigo)}

/* Kartu anggota yang bisa diklik: tombol transparan menutupi seluruh kartu */
.pro{min-height:270px;align-items:flex-start}
.pro.sel{box-shadow:0 0 0 2px #c7d2fe,0 12px 30px rgba(79,70,229,.15)}
.hint{font-size:.82rem;font-weight:500;margin-top:.3rem}
[class*="st-key-mcard_"]{position:relative}
[class*="st-key-mcard_"] [data-testid="stElementContainer"]:has(button){position:absolute;top:0;left:0;right:0;bottom:0;margin:0;z-index:5}
[class*="st-key-mcard_"] [data-testid="stElementContainer"]:has(button) [data-testid="stButton"],
[class*="st-key-mcard_"] [data-testid="stElementContainer"]:has(button) button{width:100%;height:100%;min-height:0;padding:0;opacity:0!important;cursor:pointer}
[class*="st-key-mcard_"]:hover .pro{transform:translateY(-4px);box-shadow:0 12px 30px rgba(79,70,229,.16);border-color:#c7d2fe}

/* Profil lengkap */
.pf{display:flex;gap:1.4rem;align-items:center;background:var(--card);border:1px solid var(--line);border-top-width:4px;border-radius:16px;padding:1.4rem 1.5rem;animation:fadeUp .5s ease both}
.pf-av{width:132px;height:132px;border-radius:16px;object-fit:cover;object-position:top;background:var(--tint);flex:none}
.muted{color:var(--muted);font-size:.9rem}

/* Transisi antar profil */
html,[data-testid="stMain"],section.main{scroll-behavior:smooth}
@keyframes swapA{from{opacity:0;transform:translateY(22px)}to{opacity:1;transform:none}}
@keyframes swapB{from{opacity:0;transform:translateY(22px)}to{opacity:1;transform:none}}
@keyframes rowIn{from{opacity:0;transform:translateX(-10px)}to{opacity:1;transform:none}}
@keyframes growBar{from{transform:scaleY(0)}to{transform:scaleY(1)}}
.st-key-detail_a{animation:swapA .55s cubic-bezier(.22,.8,.3,1) both}
.st-key-detail_b{animation:swapB .55s cubic-bezier(.22,.8,.3,1) both}
[class*="st-key-detail_"] [data-stale="true"]{opacity:1!important}
.pro{transition:transform .3s cubic-bezier(.22,.8,.3,1),box-shadow .3s ease,border-color .3s ease}
.clist .crow{animation:rowIn .45s cubic-bezier(.22,.8,.3,1) both}
.clist .crow:nth-child(1){animation-delay:.12s}.clist .crow:nth-child(2){animation-delay:.2s}
.clist .crow:nth-child(3){animation-delay:.28s}.clist .crow:nth-child(4){animation-delay:.36s}
.clist .crow:nth-child(5){animation-delay:.44s}.clist .crow:nth-child(6){animation-delay:.52s}
.js-plotly-plot .barlayer .point path{transform-box:fill-box;transform-origin:50% 100%;animation:growBar .7s cubic-bezier(.22,.8,.3,1) both}
.js-plotly-plot .barlayer .point:nth-child(2) path{animation-delay:.05s}.js-plotly-plot .barlayer .point:nth-child(3) path{animation-delay:.1s}
.js-plotly-plot .barlayer .point:nth-child(4) path{animation-delay:.15s}.js-plotly-plot .barlayer .point:nth-child(5) path{animation-delay:.2s}
.js-plotly-plot .barlayer .point:nth-child(6) path{animation-delay:.25s}.js-plotly-plot .barlayer .point:nth-child(7) path{animation-delay:.3s}
.js-plotly-plot .barlayer .point:nth-child(8) path{animation-delay:.35s}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important;scroll-behavior:auto!important}}

.feat{background:var(--card);border:1px solid var(--line);border-left:5px solid var(--indigo);border-radius:16px;padding:1.5rem 1.7rem;box-shadow:0 8px 26px rgba(79,70,229,.08);animation:fadeUp .5s ease both}
.feat h4{font-size:1.35rem;margin:0 0 .5rem}
.feat p{color:var(--muted);line-height:1.65;margin:0 0 .9rem}

@media(max-width:700px){.hero-title{font-size:2rem}.pro,.pf{flex-direction:column}}
div[role="dialog"]{background:#fff;color:var(--text)}
.footer{text-align:center;color:var(--muted);font-size:.85rem;margin:3.5rem 0 1rem}
</style>
""",
    unsafe_allow_html=True,
)


# =============================================================================
# 2. FUNGSI BANTU
# =============================================================================
@st.cache_data
def avatar(photo: str, name: str) -> str:
    """Foto lokal (base64) bila ada; kalau tidak, avatar inisial nama."""
    path = Path(__file__).parent / photo
    if path.is_file():
        mime = "image/png" if path.suffix.lower() == ".png" else "image/jpeg"
        return f"data:{mime};base64,{base64.b64encode(path.read_bytes()).decode()}"
    initials = "".join(w[0] for w in name.split()[:2]).upper() or "?"
    svg = (
        "<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200'>"
        "<rect width='200' height='200' fill='#e0e7ff'/>"
        "<text x='50%' y='54%' font-family='Arial,sans-serif' font-size='76' font-weight='700' "
        f"fill='#4f46e5' text-anchor='middle' dominant-baseline='middle'>{initials}</text></svg>"
    )
    return "data:image/svg+xml;base64," + base64.b64encode(svg.encode()).decode()


def badges(items, sky=False):
    cls = "badge s" if sky else "badge"
    return "".join(f'<span class="{cls}">{t}</span>' for t in items)


def section(title, sub, anchor):
    st.markdown(f'<div id="{anchor}" class="sec"><h2>{title}</h2><p>{sub}</p></div>', unsafe_allow_html=True)


def empty_card(title, text):
    st.markdown(f'<div class="card"><h4>{title}</h4><p>{text}</p></div>', unsafe_allow_html=True)


def ip_chart(members):
    """Grafik batang IP per semester; beberapa anggota = grouped bar."""
    fig = go.Figure()
    shown = 0
    for m, color in zip(MEMBERS, COLORS):
        if m not in members or not m["ip"]:
            continue
        shown += 1
        fig.add_bar(
            name=m["name"],
            x=[f"Sem {i + 1}" for i in range(len(m["ip"]))],
            y=m["ip"],
            marker=dict(color=color, cornerradius=6),
            text=[f"{v:.2f}" for v in m["ip"]],
            textposition="outside",
            hovertemplate="%{x}<br>IP %{y:.2f}<extra>" + m["name"] + "</extra>",
        )
    fig.update_layout(
        barmode="group",
        showlegend=shown > 1,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#1b1f3a", family="Inter"),
        yaxis=dict(range=[0, 4.3], gridcolor="#e5e7f0", title="IP"),
        legend=dict(orientation="h", y=1.12),
        margin=dict(l=10, r=10, t=30, b=10),
        height=340,
    )
    return fig


def build_cv_pdf() -> bytes:
    """CV PDF sederhana untuk seluruh tim (fpdf2)."""
    from fpdf import FPDF

    def clean(t):
        return str(t).encode("latin-1", "replace").decode("latin-1")

    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    def line(t, h=6):
        pdf.set_x(pdf.l_margin)
        pdf.multi_cell(0, h, clean(t), new_x="LMARGIN", new_y="NEXT")

    def heading(t):
        pdf.ln(2)
        pdf.set_font("Helvetica", "B", 13)
        line(t, 9)
        pdf.set_font("Helvetica", "", 10.5)

    pdf.set_font("Helvetica", "B", 20)
    line(TEAM["name"], 10)
    pdf.set_font("Helvetica", "", 11)
    line(TEAM["headline"], 7)
    heading("Tentang Tim")
    line(TEAM["about"])
    for m in MEMBERS:
        heading(m["name"])
        line(m["role"])
        if m["tech"]:
            line("Tech stack: " + ", ".join(m["tech"]))
        for c in m["contacts"]:
            line(f"{c['label']}: {c['value']}")
        if m["ip"]:
            line("IP per semester: " + ", ".join(f"{v:.2f}" for v in m["ip"]))
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
def show_transcript(m):
    st.markdown(f"**{m['name']} - IP per semester**")
    st.dataframe(
        {"Semester": [f"Sem {i + 1}" for i in range(len(m["ip"]))], "IP": m["ip"]},
        use_container_width=True,
        hide_index=True,
    )


all_ip = [v for m in MEMBERS for v in m["ip"]]
all_tech = list(dict.fromkeys(t for m in MEMBERS for t in m["tech"]))
avg_all = f"{sum(all_ip) / len(all_ip):.2f}" if all_ip else "-"
n_sem = max((len(m["ip"]) for m in MEMBERS), default=0)

# =============================================================================
# 3. SIDEBAR (info singkat)
# =============================================================================
with st.sidebar:
    st.markdown(f"**{TEAM['name']}**  \n{TEAM['course']}")
    st.divider()
    for m in MEMBERS:
        st.markdown(f"**{m['name']}**  \n{m['role']}")
    st.divider()
    st.metric("Rata-rata IP tim", avg_all)

# =============================================================================
# 4. NAVBAR + HERO
# =============================================================================
st.markdown(
    f"""
<div class="nav">
<div class="brand"><span class="logo">{TEAM['name'][:1].upper()}</span>{TEAM['name']}</div>
<div class="links">
<a href="#tentang" target="_self">Tentang</a>
<a href="#anggota" target="_self">Anggota</a>
<a href="#proyek" target="_self">Proyek</a>
<a href="#sertifikat" target="_self">Sertifikasi</a>
</div>
</div>
""",
    unsafe_allow_html=True,
)

left, right = st.columns([1.2, 1], gap="large", vertical_alignment="center")
with left:
    st.markdown(
        f"""
<div class="kicker">Portofolio digital • {TEAM['course']}</div>
<div class="hero-title">{TEAM['name']}</div>
<div class="hero-headline">{TEAM['headline']}</div>
<div class="hero-sub">“{TEAM['tagline']}”</div>
""",
        unsafe_allow_html=True,
    )
    try:
        st.download_button("Download CV PDF", data=build_cv_pdf(), file_name="CV_Tim.pdf", mime="application/pdf", type="primary")
    except ModuleNotFoundError:
        st.warning("Library fpdf2 belum terpasang. Jalankan: pip install fpdf2")
with right:
    rows = "".join(
        f'<div class="r-row"><img class="r-av" src="{avatar(m["photo"], m["name"])}" alt="{m["name"]}">'
        f'<div><div class="r-name">{m["name"]}</div><div class="r-role">{m["role"]}</div></div></div>'
        for m in MEMBERS
    )
    st.markdown(
        f"""
<div class="roster">
<div class="roster-h">Anggota tim</div>
{rows}
<div class="roster-f">
<div><b>{avg_all}</b><span>Rata-rata IP</span></div>
<div><b>{n_sem}</b><span>Semester ditempuh</span></div>
<div><b>{1 + len(OTHER_PROJECTS)}</b><span>Proyek</span></div>
</div>
</div>
""",
        unsafe_allow_html=True,
    )

# =============================================================================
# 5. TENTANG & TECH STACK
# =============================================================================
section("Tentang kami", "Siapa kami dan teknologi yang kami pakai.", "tentang")
ca, cb = st.columns([3, 2], gap="medium")
with ca:
    empty_card("Profil tim", TEAM["about"])
with cb:
    st.markdown(
        f'<div class="card"><h4>Core tech stack</h4>{badges(all_tech) if all_tech else "<p>Belum diisi.</p>"}</div>',
        unsafe_allow_html=True,
    )

# =============================================================================
# 6. ANGGOTA + DETAIL INTERAKTIF
# =============================================================================
section("Anggota tim", "Klik kartu anggota untuk melihat profil lengkapnya.", "anggota")

if "view" not in st.session_state:
    st.session_state.view = MEMBERS[0]["name"]


def set_view(name):
    st.session_state.view = name


view = st.session_state.view
if view not in [m["name"] for m in MEMBERS]:
    view = st.session_state.view = MEMBERS[0]["name"]

# --- kartu anggota: klik kartunya untuk membuka profil lengkap ---
for i, (col, m) in enumerate(zip(st.columns(len(MEMBERS), gap="medium"), MEMBERS)):
    color = COLORS[i % 2]
    selected = view == m["name"]
    with col:
        with st.container(key=f"mcard_{i}"):
            st.markdown(
                f"""
<div class="pro{' sel' if selected else ''}" style="border-top-color:{color}">
<img class="pro-av" src="{avatar(m['photo'], m['name'])}" alt="{m['name']}">
<div>
<div class="pro-name">{m['name']}</div>
<div class="pro-role" style="color:{color}">{m['role']}</div>
<div class="pro-tag">“{m['tagline']}”</div>
{badges(m['tech'], sky=i == 1)}
</div>
</div>
""",
                unsafe_allow_html=True,
            )
            st.button(f"Lihat profil {m['name']}", key=f"v{i}", on_click=set_view, args=(m["name"],), use_container_width=True)

# --- profil lengkap anggota terpilih ---
st.write("")
m = next(x for x in MEMBERS if x["name"] == view)
idx = MEMBERS.index(m)
color = COLORS[idx % 2]
detail = st.container(key=f"detail_{'ab'[idx % 2]}")  # key berganti -> animasi masuk berulang
detail.markdown(f"#### Profil lengkap: {m['name']}")
tech = badges(m["tech"], sky=idx == 1) if m["tech"] else '<span class="muted">Tech stack belum diisi.</span>'
detail.markdown(
    f"""
<div class="pf" style="border-top-color:{color}">
<img class="pf-av" src="{avatar(m['photo'], m['name'])}" alt="{m['name']}">
<div>
<div class="pro-name">{m['name']}</div>
<div class="pro-role" style="color:{color}">{m['role']}</div>
<div class="pro-tag">“{m['tagline']}”</div>
{tech}
</div>
</div>
""",
    unsafe_allow_html=True,
)
detail.write("")
left_col, right_col = detail.columns([3, 2], gap="medium")
with left_col:
    st.markdown("##### Perkembangan akademik")
    if m["ip"]:
        s1, s2, s3 = st.columns(3, gap="small")
        s1.markdown(f'<div class="stat"><b>{sum(m["ip"]) / len(m["ip"]):.2f}</b><span>Rata-rata IP</span></div>', unsafe_allow_html=True)
        s2.markdown(f'<div class="stat"><b>{max(m["ip"]):.2f}</b><span>IP tertinggi</span></div>', unsafe_allow_html=True)
        s3.markdown(f'<div class="stat"><b>{len(m["ip"])}</b><span>Semester</span></div>', unsafe_allow_html=True)
        st.plotly_chart(ip_chart([m]), use_container_width=True)
        if st.button("Lihat transkrip nilai", key=f"tr_{m['name']}"):
            show_transcript(m)
    else:
        empty_card("Data IP belum diisi", "Isi daftar ip pada data anggota di data_profile.py.")
with right_col:
    st.markdown("##### Kontak & sosial media")
    if m["contacts"]:
        rows = "".join(
            f'<a class="crow" href="{c["url"]}" target="_blank"><span class="cic">{c["icon"]}</span>'
            f'<span><span class="cl">{c["label"]}</span><span class="cv">{c["value"]}</span></span>'
            f'<span class="ca">↗</span></a>'
            for c in m["contacts"]
        )
        st.markdown(f'<div class="clist">{rows}</div>', unsafe_allow_html=True)
    else:
        empty_card("Kontak belum diisi", "Isi daftar contacts pada data anggota di data_profile.py.")

# =============================================================================
# 7. PROYEK
# =============================================================================
section("Portofolio proyek", "Karya yang sudah kami kerjakan.", "proyek")
st.markdown(
    f"""
<div class="feat">
<span class="pill">Proyek utama</span>
<h4>{FEATURED_PROJECT['title']}</h4>
<p>{FEATURED_PROJECT['description']}</p>
{badges(FEATURED_PROJECT['tech'])}
<div style="margin-top:.5rem"><a class="btn" href="{FEATURED_PROJECT['url']}" target="_blank">Lihat di GitHub</a></div>
</div>
""",
    unsafe_allow_html=True,
)
st.write("")
st.markdown("#### Proyek lainnya")
if not OTHER_PROJECTS:
    empty_card("Segera hadir", "Proyek lainnya akan ditambahkan di sini.")
for i in range(0, len(OTHER_PROJECTS), 3):
    for col, p in zip(st.columns(3, gap="small"), OTHER_PROJECTS[i : i + 3]):
        col.markdown(
            f"""
<div class="card">
<div class="cic" style="margin-bottom:.6rem">{p['icon']}</div>
<h4>{p['title']}</h4>
<p>{p['desc']}</p>
{badges(p['tech'])}
</div>
""",
            unsafe_allow_html=True,
        )
    st.write("")

# =============================================================================
# 8. SERTIFIKASI
# =============================================================================
section("Lisensi & sertifikasi", "Pelatihan dan sertifikat yang pernah diikuti.", "sertifikat")
if not CERTIFICATES:
    empty_card("Belum ada sertifikat", "Sertifikat dan pelatihan akan ditambahkan di sini.")
for i in range(0, len(CERTIFICATES), 2):
    for col, c in zip(st.columns(2, gap="medium"), CERTIFICATES[i : i + 2]):
        col.markdown(
            f"""
<div class="card">
<h4>{c['title']}</h4>
<div class="card-meta">{c['issuer']} • {c['year']}</div>
<a class="btn o" href="{c['url']}" target="_blank">Lihat Sertifikat</a>
</div>
""",
            unsafe_allow_html=True,
        )
    st.write("")

st.markdown(f'<div class="footer">{TEAM["name"]} • {TEAM["course"]} • Dibuat dengan Python & Streamlit</div>', unsafe_allow_html=True)
