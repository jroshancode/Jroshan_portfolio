import base64
from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="Roshan Jha | Data Science & AI",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

ROOT = Path(__file__).parent
RESUME_PATH = ROOT / "assets" / "Roshan_Jha_Resume.pdf"

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');
:root { --bg:#080d18; --panel:#101827; --muted:#a5b2c7; --text:#f4f7fb; --cyan:#6ee7e0; --violet:#a78bfa; }
html { scroll-behavior:smooth; }
.stApp { background: radial-gradient(ellipse at 15% 0%, #182a46 0%, transparent 42%), radial-gradient(ellipse at 95% 18%, #25204b 0%, transparent 32%), var(--bg); color:var(--text); font-family:'DM Sans',sans-serif; }
.block-container { max-width:1120px; padding-top:1.2rem; padding-bottom:3rem; }
h1,h2,h3 { font-family:'Manrope',sans-serif !important; color:var(--text) !important; letter-spacing:-.035em; }
p,li { color:#c4cede; }
a { color:var(--cyan) !important; text-decoration:none !important; }
div[data-testid="stMarkdownContainer"] p { line-height:1.7; }
.hero { padding:3.2rem 2.8rem; border:1px solid rgba(255,255,255,.12); border-radius:28px; background:linear-gradient(125deg,rgba(20,35,58,.96),rgba(25,23,55,.88)); box-shadow:0 24px 80px rgba(0,0,0,.28); position:relative; overflow:hidden; }
.hero:after { content:""; position:absolute; width:300px;height:300px;right:-90px;top:-130px;border-radius:50%;background:radial-gradient(circle,rgba(110,231,224,.22),transparent 68%); }
.eyebrow { color:var(--cyan); text-transform:uppercase; letter-spacing:.18em; font-size:.75rem; font-weight:700; }
.hero h1 { font-size:clamp(2.6rem,6vw,4.8rem); line-height:1.04; margin:.7rem 0 1rem; }
.gradient { background:linear-gradient(90deg,var(--cyan),#b7a5ff); -webkit-background-clip:text; -webkit-text-fill-color:transparent; }
.hero-copy { max-width:720px; font-size:1.08rem; color:#c7d3e5; }
.pill { display:inline-block; padding:.42rem .78rem; margin:.25rem .3rem .1rem 0; border:1px solid rgba(110,231,224,.25); background:rgba(110,231,224,.08); color:#c9fffb; border-radius:99px; font-size:.82rem; }
.section-kicker { color:var(--cyan); font-size:.76rem; text-transform:uppercase; letter-spacing:.17em; font-weight:700; margin-bottom:.3rem; }
.section-title { font-size:2rem; margin-top:0; margin-bottom:.3rem; }
.subtle { color:var(--muted); }
.card { height:100%; padding:1.35rem; border:1px solid rgba(255,255,255,.10); border-radius:18px; background:linear-gradient(145deg,rgba(18,29,46,.94),rgba(13,21,35,.92)); box-shadow:0 12px 35px rgba(0,0,0,.12); }
.card h3 { font-size:1.12rem; margin:.25rem 0 .5rem; }
.card p { font-size:.94rem; }
.card-top { color:var(--cyan); font-size:.75rem; text-transform:uppercase; letter-spacing:.12em; font-weight:700; }
.metric { padding:1rem 1.1rem; border:1px solid rgba(255,255,255,.1); border-radius:16px; background:rgba(255,255,255,.035); }
.metric strong { display:block; font-family:'Manrope'; font-size:1.55rem; color:#fff; }
.metric span { color:var(--muted); font-size:.82rem; }
.timeline { border-left:1px solid rgba(110,231,224,.35); margin-left:.45rem; padding-left:1.2rem; }
.timeline-item { position:relative; margin-bottom:1.3rem; }
.timeline-item:before { content:""; position:absolute; width:9px;height:9px;border-radius:50%;background:var(--cyan);left:-1.53rem;top:.4rem;box-shadow:0 0 0 4px rgba(110,231,224,.10); }
hr { border-color:rgba(255,255,255,.1) !important; }
.stButton>button, .stDownloadButton>button { border-radius:999px; border:1px solid rgba(110,231,224,.45); background:linear-gradient(90deg,#5bd8d0,#9e8cf4); color:#07111d; font-weight:700; padding:.55rem 1.2rem; }
.stButton>button:hover, .stDownloadButton>button:hover { border-color:#fff; color:#07111d; transform:translateY(-1px); }
footer { visibility:hidden; }
#MainMenu {visibility:hidden;}
header {visibility:hidden;}
.contact-box { padding:1.6rem; border-radius:20px; border:1px solid rgba(110,231,224,.2); background:linear-gradient(120deg,rgba(24,47,64,.8),rgba(35,29,66,.8)); }
</style>
""", unsafe_allow_html=True)

def section(kicker, title, intro=None):
    st.markdown(f'<div class="section-kicker">{kicker}</div><h2 class="section-title">{title}</h2>', unsafe_allow_html=True)
    if intro:
        st.markdown(f'<p class="subtle">{intro}</p>', unsafe_allow_html=True)

# Navigation
nav = st.columns([1.4, 1, 1, 1, 1, 1])
with nav[0]:
    st.markdown("**✦ ROSHAN JHA**")
for col, label, anchor in zip(nav[1:], ["About", "Skills", "Projects", "Experience", "Contact"], ["about", "skills", "projects", "experience", "contact"]):
    with col:
        st.markdown(f'<div style="text-align:center;padding-top:.2rem"><a href="#{anchor}">{label}</a></div>', unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <div class="eyebrow">Data Science · Machine Learning · Generative AI</div>
  <h1>Turning data into<br><span class="gradient">intelligent solutions.</span></h1>
  <p class="hero-copy">Hi, I'm Roshan Jha — a Data Science and AI professional with a software development foundation. I build practical machine learning systems, LLM-powered applications, and end-to-end data solutions that connect experimentation with real-world deployment.</p>
  <div style="margin-top:1.2rem">
    <span class="pill">Python & SQL</span><span class="pill">Machine Learning</span><span class="pill">Deep Learning</span><span class="pill">GenAI & RAG</span><span class="pill">Model Deployment</span>
  </div>
</div>
""", unsafe_allow_html=True)

st.write("")
c1,c2,c3,c4 = st.columns(4)
for col, val, label in [(c1,"3+","Years in software & data roles"),(c2,"3","Featured ML / AI projects"),(c3,"2","Mentoring experiences"),(c4,"E2E","Build · Evaluate · Deploy")]:
    with col:
        st.markdown(f'<div class="metric"><strong>{val}</strong><span>{label}</span></div>', unsafe_allow_html=True)

st.write("")
section("01 / Profile", "A little about me", "A blend of engineering discipline, analytical thinking, and a passion for applied AI.")
st.markdown('<div id="about"></div>', unsafe_allow_html=True)
left,right = st.columns([1.35,1])
with left:
    st.markdown("""
    I work across the lifecycle of data products — from data preparation and exploratory analysis to model development, evaluation, API creation, and deployment.

    My experience spans **software development, data science mentoring, machine learning, NLP, and Generative AI**. I enjoy translating complex problems into usable applications and helping learners build confidence through hands-on projects.

    I bring a practical mindset to every project: understand the problem, build a reliable solution, communicate the outcome, and make it usable.
    """)
with right:
    st.markdown("""
    <div class="card">
      <div class="card-top">Currently focused on</div>
      <h3>Applied AI that ships</h3>
      <p>LLM applications, RAG workflows, intelligent assistants, predictive modelling, and production-minded ML deployment.</p>
      <hr>
      <p><b>Based in</b><br>India</p>
      <p><b>Open to</b><br>Data Science · ML Engineer · AI Engineer opportunities</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.markdown('<div id="skills"></div>', unsafe_allow_html=True)
section("02 / Capabilities", "Technical toolkit", "A practical stack for data analysis, model building, AI applications, and deployment.")
skill_groups = [
    ("Programming & Data", ["Python","SQL","PySpark","ETL / ELT","Pandas","NumPy","Statistics","EDA"]),
    ("Machine Learning", ["Scikit-learn","Predictive Modelling","Feature Engineering","Ensemble Learning","Time Series","A/B Testing"]),
    ("AI & Deep Learning", ["TensorFlow","PyTorch","BERT","LLMs","NLP","Generative AI","Agentic AI","Object Localization"]),
    ("LLM Application Stack", ["LangChain","RAG","FAISS","Hugging Face","Vector Databases","Gemini API"]),
    ("Deployment & Engineering", ["Streamlit","Flask","FastAPI","Docker","GitHub Actions","CI/CD","Render"]),
    ("Cloud & BI", ["AWS","Azure ML","Power BI","Tableau","PostgreSQL","GitHub"]),
]
skill_cols = st.columns(3)
for i,(name,skills) in enumerate(skill_groups):
    with skill_cols[i%3]:
        pills = "".join(f'<span class="pill">{s}</span>' for s in skills)
        st.markdown(f'<div class="card" style="margin-bottom:1rem"><h3>{name}</h3>{pills}</div>', unsafe_allow_html=True)

st.write("")
st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
section("03 / Selected work", "Projects that solve real problems", "A selection of applied AI and machine learning work from my portfolio.")
projects = [
    {
        "num":"01","title":"Personal Advisor Chat System","type":"GenAI · RAG · Streamlit",
        "desc":"A multi-domain AI advisor for Education, Finance, Health, and Travel. Built PDF question-answering with retrieval-augmented generation and personalized recommendations.",
        "stack":["Gemini API","LangChain","Hugging Face","Streamlit","RAG"],
        "impact":"Designed and deployed a conversational experience for real-time, multi-domain queries."
    },
    {
        "num":"02","title":"Email Spam Detection Analysis","type":"Machine Learning · Deep Learning",
        "desc":"A hybrid spam classification solution combining TF-IDF, a StackingClassifier, and a BiLSTM model with Attention.",
        "stack":["Python","TF-IDF","Scikit-learn","BiLSTM","Flask","Docker"],
        "impact":"Used Dropout, EarlyStopping, and ReduceLROnPlateau to help control overfitting; added API deployment and CI/CD."
    },
    {
        "num":"03","title":"Employee Loan Prediction","type":"Predictive Analytics · Finance",
        "desc":"An employee loan eligibility prediction workflow using ensemble machine learning models and a structured model evaluation process.",
        "stack":["Python","Pandas","Scikit-learn","Feature Engineering","Cross-validation"],
        "impact":"Applied imbalance handling, hyperparameter tuning, and evaluation visualizations; reported a 10% accuracy improvement."
    },
]
pcols = st.columns(3)
for col, p in zip(pcols, projects):
    with col:
        pills = "".join(f'<span class="pill">{s}</span>' for s in p["stack"])
        st.markdown(f"""
        <div class="card">
          <div class="card-top">PROJECT {p['num']} · {p['type']}</div>
          <h3>{p['title']}</h3>
          <p>{p['desc']}</p>
          <p><b>Outcome</b><br>{p['impact']}</p>
          <div>{pills}</div>
        </div>
        """, unsafe_allow_html=True)
st.caption("Project descriptions are based on the supplied resume. Add individual repository URLs to make each project card directly clickable.")

st.write("")
st.markdown('<div id="experience"></div>', unsafe_allow_html=True)
section("04 / Career", "Experience & impact", "Experience across software delivery, data science education, and applied analytics.")
experience = [
    ("Jan 2026 – Present","Data Science Mentor","Skill Circle","Teaching Python, SQL, Statistics, ML, Deep Learning, and Generative AI; mentoring real-world projects in Data Science, NLP, and AI; conducting hands-on sessions on model building and deployment."),
    ("Jul 2025 – Dec 2025","Data Science Mentor","Git India","Taught Python, SQL, Statistics, ML/DL/NLP, and Generative AI; guided learners on practical Data Science and BI projects."),
    ("Jun 2023 – Oct 2024","Software Developer","Aeologic Technologies / NIC","Developed Samadhan and Pencil portals for labour case management; performed EDA using Pandas, NumPy, and SQL for backend redesign; automated MIS reporting dashboards with Python and PostgreSQL."),
    ("Jan 2022 – Mar 2023","Software Developer (Part-Time)","WebKart Digital Pvt Ltd","Improved UI/UX, developed custom modules for client requirements, and delivered production-ready maintainable code."),
]
st.markdown('<div class="timeline">', unsafe_allow_html=True)
for date,role,company,desc in experience:
    st.markdown(f'<div class="timeline-item"><div class="card-top">{date}</div><h3 style="margin:.2rem 0">{role} · {company}</h3><p>{desc}</p></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.write("")
section("05 / Education", "Education & certifications")
edu1,edu2 = st.columns(2)
with edu1:
    st.markdown("""
    <div class="card">
      <div class="card-top">Jan 2026 – Dec 2027</div>
      <h3>Master of Computer Applications (MCA)</h3>
      <p>Amity University, Noida</p>
      <hr>
      <div class="card-top">Aug 2018 – Dec 2022</div>
      <h3>Bachelor of Computer Applications (BCA)</h3>
      <p>Maharaja Agrasen Enclave University (IGNOU)</p>
    </div>
    """, unsafe_allow_html=True)
with edu2:
    st.markdown("""
    <div class="card">
      <h3>Certifications</h3>
      <p>✦ Data Science and AI/ML Program — Bosscoder Academy</p>
      <p>✦ Advanced Python, ML, DL, GenAI — Udemy</p>
      <p>✦ Python EDA, Statistics, ML — Great Learning</p>
      <p>✦ HackerRank — Python, SQL, Problem Solving</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="contact-box">
  <div class="section-kicker">06 / Let's connect</div>
  <h2 class="section-title">Have a problem worth solving?</h2>
  <p class="subtle">I'm interested in opportunities and conversations around Data Science, Machine Learning, and AI engineering.</p>
</div>
""", unsafe_allow_html=True)
a,b,c = st.columns(3)
with a: st.markdown("**Email**  \n[jroshan731@gmail.com](mailto:jroshan731@gmail.com)")
with b: st.markdown("**LinkedIn**  \n[roshan-jha-tech](https://www.linkedin.com/in/roshan-jha-tech)")
with c: st.markdown("**GitHub**  \n[jroshanjha](https://github.com/jroshanjha)")

if RESUME_PATH.exists():
    st.download_button(
        "↓  Download my resume",
        data=RESUME_PATH.read_bytes(),
        file_name="Roshan_Jha_Resume.pdf",
        mime="application/pdf",
    )

st.markdown("---")
st.markdown('<p style="text-align:center;color:#8290a6;font-size:.82rem">Designed & built with Python + Streamlit · Roshan Jha</p>', unsafe_allow_html=True)
