# import re
# from pathlib import Path
# import streamlit as st

# st.set_page_config(page_title="Roshan Jha | Data Science & AI", page_icon="✦", layout="wide")

# ROOT = Path(__file__).parent
# RESUME_PATH = ROOT / "assets" / "Roshan_Jha_Resume.pdf"

# st.markdown("""
# <style>
# @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');
# :root{--bg:#080d18;--panel:#101827;--muted:#a5b2c7;--text:#f4f7fb;--cyan:#6ee7e0;--violet:#a78bfa}
# html{scroll-behavior:smooth}
# .stApp{background:radial-gradient(ellipse at 12% 0%,#182a46 0%,transparent 42%),radial-gradient(ellipse at 95% 18%,#25204b 0%,transparent 32%),var(--bg);color:var(--text);font-family:'DM Sans',sans-serif}
# .block-container{max-width:1160px;padding-top:1rem;padding-bottom:3rem}
# h1,h2,h3{font-family:'Manrope',sans-serif!important;color:var(--text)!important;letter-spacing:-.035em}
# p,li{color:#c4cede;line-height:1.7}
# a{color:var(--cyan)!important;text-decoration:none!important}
# header,#MainMenu,footer{visibility:hidden}
# .hero{padding:3.4rem 2.8rem;border:1px solid rgba(255,255,255,.13);border-radius:28px;background:linear-gradient(125deg,rgba(20,35,58,.97),rgba(25,23,55,.9));box-shadow:0 24px 80px rgba(0,0,0,.28);position:relative;overflow:hidden;animation:rise .8s ease both}
# .hero:after{content:"";position:absolute;width:320px;height:320px;right:-90px;top:-140px;border-radius:50%;background:radial-gradient(circle,rgba(110,231,224,.24),transparent 68%);animation:pulse 5s ease-in-out infinite}
# @keyframes rise{from{opacity:0;transform:translateY(18px)}to{opacity:1;transform:translateY(0)}}
# @keyframes pulse{0%,100%{transform:scale(1);opacity:.7}50%{transform:scale(1.18);opacity:1}}
# .eyebrow,.kicker{color:var(--cyan);text-transform:uppercase;letter-spacing:.17em;font-size:.76rem;font-weight:700}
# .hero h1{font-size:clamp(2.6rem,6vw,4.8rem);line-height:1.04;margin:.7rem 0 1rem}
# .gradient{background:linear-gradient(90deg,var(--cyan),#b7a5ff);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
# .hero-copy{max-width:760px;font-size:1.08rem;color:#c7d3e5}
# .pill{display:inline-block;padding:.4rem .75rem;margin:.24rem .25rem .1rem 0;border:1px solid rgba(110,231,224,.25);background:rgba(110,231,224,.08);color:#c9fffb;border-radius:99px;font-size:.8rem}
# .metric,.card,.arch{border:1px solid rgba(255,255,255,.1);background:linear-gradient(145deg,rgba(18,29,46,.94),rgba(13,21,35,.92));border-radius:18px;box-shadow:0 12px 35px rgba(0,0,0,.12)}
# .metric{padding:1rem 1.1rem}.metric strong{display:block;font-family:'Manrope';font-size:1.55rem;color:#fff}.metric span{color:var(--muted);font-size:.82rem}
# .card{height:100%;padding:1.3rem;margin-bottom:.8rem}.card h3{font-size:1.12rem;margin:.3rem 0 .5rem}.card p{font-size:.93rem}
# .card-top{color:var(--cyan);font-size:.74rem;text-transform:uppercase;letter-spacing:.12em;font-weight:700}
# .section-title{font-size:2rem;margin:.1rem 0 .25rem}.subtle{color:var(--muted)}
# .arch{padding:1rem;text-align:center;margin:.2rem 0}.arch b{color:#eaf9ff}.arch small{color:#9eacc1}
# .arch-arrow{text-align:center;color:var(--cyan);font-size:1.2rem;padding:.1rem}
# .timeline{border-left:1px solid rgba(110,231,224,.35);margin-left:.45rem;padding-left:1.2rem}
# .timeline-item{position:relative;margin-bottom:1.3rem}
# .timeline-item:before{content:"";position:absolute;width:9px;height:9px;border-radius:50%;background:var(--cyan);left:-1.53rem;top:.4rem;box-shadow:0 0 0 4px rgba(110,231,224,.1)}
# .contact{padding:1.6rem;border-radius:20px;border:1px solid rgba(110,231,224,.2);background:linear-gradient(120deg,rgba(24,47,64,.8),rgba(35,29,66,.8))}
# div[data-testid="stTabs"] button{color:#c8d4e6!important}
# .stButton>button,.stDownloadButton>button{border-radius:999px;border:1px solid rgba(110,231,224,.45);background:linear-gradient(90deg,#5bd8d0,#9e8cf4);color:#07111d;font-weight:700;padding:.5rem 1rem}
# .stButton>button:hover,.stDownloadButton>button:hover{border-color:#fff;color:#07111d}
# div[data-testid="stExpander"]{border:1px solid rgba(255,255,255,.12);border-radius:14px}
# @media(max-width:700px){.hero{padding:2rem 1.3rem}.block-container{padding-left:1rem;padding-right:1rem}.hero h1{font-size:2.55rem}}
# </style>
# """, unsafe_allow_html=True)

# def section(kicker, title, intro=None, anchor=None):
#     if anchor:
#         st.markdown(f'<div id="{anchor}"></div>', unsafe_allow_html=True)
#     st.markdown(f'<div class="kicker">{kicker}</div><h2 class="section-title">{title}</h2>', unsafe_allow_html=True)
#     if intro: st.markdown(f'<p class="subtle">{intro}</p>', unsafe_allow_html=True)

# def pills(items):
#     return "".join(f'<span class="pill">{x}</span>' for x in items)

# def architecture(steps):
#     cols = st.columns(len(steps))
#     for i,(title,desc) in enumerate(steps):
#         with cols[i]:
#             st.markdown(f'<div class="arch"><b>{title}</b><br><small>{desc}</small></div>', unsafe_allow_html=True)
#         if i < len(steps)-1:
#             pass

# # Navigation
# nav = st.columns([1.5,1,1,1,1,1])
# with nav[0]: st.markdown("**✦ ROSHAN JHA**")
# for col,label,anchor in zip(nav[1:],["About","Skills","Projects","Experience","Contact"],["about","skills","projects","experience","contact"]):
#     with col: st.markdown(f'<div style="text-align:center;padding-top:.2rem"><a href="#{anchor}">{label}</a></div>',unsafe_allow_html=True)

# st.markdown("""
# <div class="hero">
#  <div class="eyebrow">Data Science · Machine Learning · Generative AI</div>
#  <h1>Turning data into<br><span class="gradient">intelligent solutions.</span></h1>
#  <p class="hero-copy">Hi, I'm Roshan Jha — a Data Science and AI professional with a software development foundation. I build practical machine learning systems, LLM-powered applications, and end-to-end data solutions that connect experimentation with real-world deployment.</p>
#  <div style="margin-top:1.2rem"><span class="pill">Python & SQL</span><span class="pill">Machine Learning</span><span class="pill">Deep Learning</span><span class="pill">GenAI & RAG</span><span class="pill">Model Deployment</span></div>
# </div>
# """,unsafe_allow_html=True)
# st.write("")
# m=st.columns(4)
# for col,v,l in zip(m,["3+","3","2","E2E"],["Years across software & data roles","Featured ML / AI projects","Mentoring experiences","Build · Evaluate · Deploy"]):
#     with col: st.markdown(f'<div class="metric"><strong>{v}</strong><span>{l}</span></div>',unsafe_allow_html=True)

# st.write("")
# section("01 / Profile","A little about me","Engineering discipline, analytical thinking, and a passion for applied AI.","about")
# a,b=st.columns([1.35,1])
# with a:
#     st.markdown("""I work across the lifecycle of data products — from data preparation and exploratory analysis to model development, evaluation, API creation, and deployment.

# My experience spans **software development, data science mentoring, machine learning, NLP, and Generative AI**. I enjoy translating complex problems into usable applications and helping learners build confidence through hands-on projects.

# My approach: understand the problem, build a reliable solution, communicate the outcome, and make it usable.""")
# with b:
#     st.markdown('<div class="card"><div class="card-top">Current focus</div><h3>Applied AI that ships</h3><p>LLM applications, RAG workflows, intelligent assistants, predictive modelling, and production-minded ML deployment.</p><hr><p><b>Based in</b><br>India</p><p><b>Target roles</b><br>Data Scientist · ML Engineer · AI Engineer</p></div>',unsafe_allow_html=True)

# st.write("")
# section("02 / Capabilities","Technical toolkit","Core technologies across analysis, modelling, AI application development, and deployment.","skills")
# groups=[
# ("Programming & Data",["Python","SQL","PySpark","ETL / ELT","Pandas","NumPy","Statistics","EDA"]),
# ("Machine Learning",["Scikit-learn","Predictive Modelling","Feature Engineering","Ensemble Learning","Time Series","A/B Testing"]),
# ("AI & Deep Learning",["TensorFlow","PyTorch","BERT","LLMs","NLP","Generative AI","Agentic AI","Object Localization"]),
# ("LLM Application Stack",["LangChain","RAG","FAISS","Hugging Face","Vector Databases","Gemini API"]),
# ("Deployment & Engineering",["Streamlit","Flask","FastAPI","Docker","GitHub Actions","CI/CD","Render"]),
# ("Cloud & BI",["AWS","Azure ML","Power BI","Tableau","PostgreSQL","GitHub"])]
# sc=st.columns(3)
# for i,(name,items) in enumerate(groups):
#     with sc[i%3]: st.markdown(f'<div class="card"><h3>{name}</h3>{pills(items)}</div>',unsafe_allow_html=True)

# st.write("")
# section("03 / Selected work","Projects with practical impact","Explore project summaries, architecture flows, and lightweight interactive previews.","projects")
# projects=[
# ("01","Personal Advisor Chat System","GenAI · RAG · Streamlit","A multi-domain AI advisor for Education, Finance, Health, and Travel, featuring PDF question-answering and personalized recommendations.",["Gemini API","LangChain","Hugging Face","Streamlit","RAG"],"Designed and deployed a conversational experience for real-time, multi-domain queries.","https://github.com/jroshanjha/personal-advisor-chat-application"),
# ("02","Email Spam Detection Analysis","ML · Deep Learning","A hybrid spam classification approach combining TF-IDF, a StackingClassifier, and a BiLSTM model with Attention.",["Python","TF-IDF","Scikit-learn","BiLSTM","Flask","Docker"],"Applied regularization and callback techniques to help control overfitting; added API deployment and CI/CD.","https://github.com/jroshanjha/Email-spam-detection"), 
# ("03","Employee Loan Prediction","Predictive Analytics · Finance","An employee loan eligibility prediction workflow using ensemble models and a structured evaluation process.",["Python","Pandas","Scikit-learn","Cross-validation","Feature Engineering"],"Applied imbalance handling, hyperparameter tuning, and evaluation visualizations; resume reports a 10% accuracy improvement.","https://github.com/jroshanjha/Loan-approved")]
# ("04","Customer Review Classification","NLP · Sentiment Analysis . Machine Learning . Deep Learning . TFIDF","A sentiment analysis model using TF-IDF and a BiLSTM model with Attention.",["Python","TF-IDF","BiLSTM","Attention","Flask","Docker"],"Applied regularization and callback techniques to help control overfitting; added API deployment and CI/CD.","https://github.com/jroshanjha/Customer-Review-Classification"),
# for num,title,kind,desc,stack,impact,url in projects:
#     with st.container():
#         l,r=st.columns([1.35,1])
#         with l:
#             st.markdown(f'<div class="card"><div class="card-top">PROJECT {num} · {kind}</div><h3>{title}</h3><p>{desc}</p><p><b>Outcome</b><br>{impact}</p>{pills(stack)}<br><br><a href="{url}" target="_blank">↗ GitHub repository placeholder</a><br><small style="color:#9eacc1">Proposed URL — create the repository before publishing this link.</small></div>',unsafe_allow_html=True)
#         with r:
#             with st.expander("View project architecture",expanded=False):
#                 if num=="01":
#                     architecture([("User","Question / PDF"),("Streamlit UI","Chat interface"),("RAG pipeline","Retrieve context"),("Gemini API","Generate answer")])
#                     st.caption("Conceptual architecture based on the resume description.")
#                 elif num=="02":
#                     architecture([("Email data","Labeled samples"),("TF-IDF","Text features"),("ML + BiLSTM","Hybrid classifier"),("Flask API","Serve prediction")])
#                     st.caption("Conceptual architecture based on the resume description.")
#                 else:
#                     architecture([("Loan data","Input records"),("Preprocessing","Clean / encode"),("Ensemble ML","Train / predict"),("Evaluation","Metrics / insights")])
#                     st.caption("Conceptual architecture based on the resume description.")
#             with st.expander("Try an interactive preview",expanded=False):
#                 if num=="01":
#                     st.caption("Illustrative UI preview only. This does not call a live Gemini model or access private PDFs.")
#                     topic=st.selectbox("Choose an advisor topic",["Education","Finance","Health","Travel"],key="advisor_topic")
#                     q=st.text_input("Ask a sample question",placeholder="How can I plan my next steps?",key="advisor_q")
#                     examples={"Education":"Break the goal into milestones, compare learning paths, and track progress with a weekly plan.","Finance":"Start by clarifying your goal, time horizon, cash flow, and risk tolerance. Validate decisions with a qualified financial professional.","Health":"Use trusted clinical sources and discuss personal symptoms or treatment decisions with a licensed healthcare professional.","Travel":"Choose dates and budget first, then compare transport, stay, local travel, and a flexible day-by-day itinerary."}
#                     if st.button("Preview sample response",key="advisor_btn"):
#                         st.info(examples[topic] if not q.strip() else f"Sample {topic.lower()} guidance for “{q.strip()}”: {examples[topic]}")
#                 elif num=="02":
#                     st.caption("Transparent keyword-based demonstration — not the trained TF-IDF / BiLSTM model.")
#                     email=st.text_area("Paste a sample email",placeholder="Congratulations! You have won a prize. Click here now.",key="spam_text")
#                     if st.button("Classify sample",key="spam_btn"):
#                         t=email.lower()
#                         spam_words=["winner","won","prize","claim now","urgent","click here","free gift","cash bonus"]
#                         hits=[w for w in spam_words if w in t]
#                         if not t.strip(): st.warning("Enter some email text first.")
#                         elif hits: st.warning(f"Demo result: suspicious wording detected ({', '.join(hits)}). Review carefully.")
#                         else: st.success("Demo result: no listed trigger phrases found. This does not guarantee the email is safe.")
#                 else:
#                     st.caption("Illustrative rule-based preview — not the trained ensemble model and not a lending decision.")
#                     income=st.number_input("Monthly income (₹)",min_value=0,step=5000,value=50000,key="loan_income")
#                     emi=st.number_input("Existing monthly obligations (₹)",min_value=0,step=1000,value=10000,key="loan_emi")
#                     tenure=st.slider("Employment tenure (years)",0,30,3,key="loan_tenure")
#                     if st.button("View illustrative profile",key="loan_btn"):
#                         ratio=emi/income if income else 1
#                         if income==0: st.warning("Enter a monthly income above zero.")
#                         else:
#                             st.metric("Existing obligation / income",f"{ratio:.0%}")
#                             st.info("Illustrative profile: " + ("Lower existing-obligation ratio" if ratio<.3 else "Higher existing-obligation ratio") + (", with longer employment tenure." if tenure>=3 else ", with shorter employment tenure.") + " This is not a credit score or eligibility result.")

# st.caption("Repository URLs above are proposed placeholders, not verified repositories. Demo panels are educational previews and are not connected to trained project models or production APIs.")

# st.write("")
# section("04 / Career","Experience & impact","Software delivery, data science education, and applied analytics.","experience")
# experience=[
# ("Jan 2026 – Present","Data Science Mentor","Skill Circle","Teaching Python, SQL, Statistics, ML, Deep Learning, and Generative AI; mentoring real-world projects in Data Science, NLP, and AI; conducting hands-on sessions on model building and deployment."),
# ("Jul 2025 – Dec 2025","Data Science Mentor","Git India","Taught Python, SQL, Statistics, ML/DL/NLP, and Generative AI; guided learners on practical Data Science and BI projects."),
# ("Jun 2023 – Oct 2024","Software Developer","Aeologic Technologies / NIC","Developed Samadhan and Pencil portals for labour case management; performed EDA using Pandas, NumPy, and SQL for backend redesign; automated MIS reporting dashboards with Python and PostgreSQL."),
# ("Jan 2022 – Mar 2023","Software Developer (Part-Time)","WebKart Digital Pvt Ltd","Improved UI/UX, developed custom modules for client requirements, and delivered production-ready maintainable code.")]
# st.markdown('<div class="timeline">',unsafe_allow_html=True)
# for date,role,company,desc in experience:
#     st.markdown(f'<div class="timeline-item"><div class="card-top">{date}</div><h3 style="margin:.2rem 0">{role} · {company}</h3><p>{desc}</p></div>',unsafe_allow_html=True)
# st.markdown('</div>',unsafe_allow_html=True)

# st.write("")
# section("05 / Education","Education & certifications")
# e1,e2=st.columns(2)
# with e1:
#     st.markdown('<div class="card"><div class="card-top">Jan 2026 – Dec 2027</div><h3>Master of Computer Applications (MCA)</h3><p>Amity University, Noida</p><hr><div class="card-top">Aug 2018 – Dec 2022</div><h3>Bachelor of Computer Applications (BCA)</h3><p>Maharaja Agrasen Enclave University (IGNOU)</p></div>',unsafe_allow_html=True)
# with e2:
#     st.markdown('<div class="card"><h3>Certifications</h3><p>✦ Data Science and AI/ML Program — Bosscoder Academy</p><p>✦ Advanced Python, ML, DL, GenAI — Udemy</p><p>✦ Python EDA, Statistics, ML — Great Learning</p><p>✦ HackerRank — Python, SQL, Problem Solving</p></div>',unsafe_allow_html=True)

# st.write("")
# section("06 / Let's connect","Have a problem worth solving?","I'm interested in opportunities and conversations around Data Science, Machine Learning, and AI engineering.","contact")
# st.markdown('<div class="contact"><h3>Let’s build something useful.</h3><p class="subtle">Reach out for roles, collaborations, or conversations about applied AI.</p></div>',unsafe_allow_html=True)
# c1,c2,c3=st.columns(3)
# with c1: st.markdown("**Email**  \n[jroshan731@gmail.com](mailto:jroshan731@gmail.com)")
# with c2: st.markdown("**LinkedIn**  \n[roshan-jha-tech](https://www.linkedin.com/in/roshan-jha-tech)")
# with c3: st.markdown("**GitHub profile**  \n[jroshanjha](https://github.com/jroshanjha)")
# if RESUME_PATH.exists():
#     st.download_button("↓  Download my resume",data=RESUME_PATH.read_bytes(),file_name="Roshan_Jha_Resume.pdf",mime="application/pdf")
# st.markdown("---")
# st.markdown('<p style="text-align:center;color:#8290a6;font-size:.82rem">Designed & built with Python + Streamlit · Roshan Jha</p>',unsafe_allow_html=True)

from pathlib import Path
import streamlit as st

st.set_page_config(page_title="Roshan Jha | Data Science & AI", page_icon="✦", layout="wide")
ROOT = Path(__file__).parent
RESUME_PATH = ROOT / "assets" / "Roshan_Jha_Resume.pdf"

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');
:root{--bg:#080d18;--muted:#a5b2c7;--text:#f4f7fb;--cyan:#6ee7e0}
html{scroll-behavior:smooth}
.stApp{background:radial-gradient(ellipse at 12% 0%,#182a46 0%,transparent 42%),radial-gradient(ellipse at 95% 18%,#25204b 0%,transparent 32%),var(--bg);color:var(--text);font-family:'DM Sans',sans-serif}
.block-container{max-width:1160px;padding-top:1rem;padding-bottom:3rem}
h1,h2,h3{font-family:'Manrope',sans-serif!important;color:var(--text)!important;letter-spacing:-.035em}
p,li{color:#c4cede;line-height:1.7} a{color:var(--cyan)!important;text-decoration:none!important}
header,#MainMenu,footer{visibility:hidden}
.hero{padding:3.4rem 2.8rem;border:1px solid rgba(255,255,255,.13);border-radius:28px;background:linear-gradient(125deg,rgba(20,35,58,.97),rgba(25,23,55,.9));box-shadow:0 24px 80px rgba(0,0,0,.28);position:relative;overflow:hidden;animation:rise .8s ease both}
.hero:after{content:"";position:absolute;width:320px;height:320px;right:-90px;top:-140px;border-radius:50%;background:radial-gradient(circle,rgba(110,231,224,.24),transparent 68%);animation:pulse 5s ease-in-out infinite}
@keyframes rise{from{opacity:0;transform:translateY(18px)}to{opacity:1;transform:translateY(0)}}
@keyframes pulse{0%,100%{transform:scale(1);opacity:.7}50%{transform:scale(1.18);opacity:1}}
.eyebrow,.kicker{color:var(--cyan);text-transform:uppercase;letter-spacing:.17em;font-size:.76rem;font-weight:700}
.hero h1{font-size:clamp(2.6rem,6vw,4.8rem);line-height:1.04;margin:.7rem 0 1rem}
.gradient{background:linear-gradient(90deg,var(--cyan),#b7a5ff);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.hero-copy{max-width:760px;font-size:1.08rem;color:#c7d3e5}
.pill{display:inline-block;padding:.4rem .75rem;margin:.24rem .25rem .1rem 0;border:1px solid rgba(110,231,224,.25);background:rgba(110,231,224,.08);color:#c9fffb;border-radius:99px;font-size:.8rem}
.metric,.card,.arch{border:1px solid rgba(255,255,255,.1);background:linear-gradient(145deg,rgba(18,29,46,.94),rgba(13,21,35,.92));border-radius:18px;box-shadow:0 12px 35px rgba(0,0,0,.12)}
.metric{padding:1rem 1.1rem}.metric strong{display:block;font-family:'Manrope';font-size:1.55rem;color:#fff}.metric span{color:var(--muted);font-size:.82rem}
.card{height:100%;padding:1.3rem;margin-bottom:.8rem}.card h3{font-size:1.12rem;margin:.3rem 0 .5rem}.card p{font-size:.93rem}
.card-top{color:var(--cyan);font-size:.74rem;text-transform:uppercase;letter-spacing:.12em;font-weight:700}
.section-title{font-size:2rem;margin:.1rem 0 .25rem}.subtle{color:var(--muted)}
.arch{padding:1rem;text-align:center;margin:.2rem 0}.arch b{color:#eaf9ff}.arch small{color:#9eacc1}
.timeline{border-left:1px solid rgba(110,231,224,.35);margin-left:.45rem;padding-left:1.2rem}
.timeline-item{position:relative;margin-bottom:1.3rem}
.timeline-item:before{content:"";position:absolute;width:9px;height:9px;border-radius:50%;background:var(--cyan);left:-1.53rem;top:.4rem;box-shadow:0 0 0 4px rgba(110,231,224,.1)}
.contact{padding:1.6rem;border-radius:20px;border:1px solid rgba(110,231,224,.2);background:linear-gradient(120deg,rgba(24,47,64,.8),rgba(35,29,66,.8))}
.stButton>button,.stDownloadButton>button{border-radius:999px;border:1px solid rgba(110,231,224,.45);background:linear-gradient(90deg,#5bd8d0,#9e8cf4);color:#07111d;font-weight:700;padding:.5rem 1rem}
div[data-testid="stExpander"]{border:1px solid rgba(255,255,255,.12);border-radius:14px}
@media(max-width:700px){.hero{padding:2rem 1.3rem}.block-container{padding-left:1rem;padding-right:1rem}.hero h1{font-size:2.55rem}}
</style>
""", unsafe_allow_html=True)

def section(kicker, title, intro=None, anchor=None):
    if anchor:
        st.markdown(f'<div id="{anchor}"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="kicker">{kicker}</div><h2 class="section-title">{title}</h2>', unsafe_allow_html=True)
    if intro:
        st.markdown(f'<p class="subtle">{intro}</p>', unsafe_allow_html=True)

def pills(items):
    return "".join(f'<span class="pill">{item}</span>' for item in items)

def architecture(steps):
    cols = st.columns(len(steps))
    for col, (title, desc) in zip(cols, steps):
        with col:
            st.markdown(f'<div class="arch"><b>{title}</b><br><small>{desc}</small></div>', unsafe_allow_html=True)

nav = st.columns([1.5, 1, 1, 1, 1, 1])
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
<div style="margin-top:1.2rem"><span class="pill">Python & SQL</span><span class="pill">Machine Learning</span><span class="pill">Deep Learning</span><span class="pill">GenAI & RAG</span><span class="pill">Model Deployment</span></div>
</div>
""", unsafe_allow_html=True)

st.write("")
metrics = st.columns(4)
for col, value, label in zip(metrics, ["3+", "4", "2", "E2E"], ["Years across software & data roles", "Featured ML / AI projects", "Mentoring experiences", "Build · Evaluate · Deploy"]):
    with col:
        st.markdown(f'<div class="metric"><strong>{value}</strong><span>{label}</span></div>', unsafe_allow_html=True)

st.write("")
section("01 / Profile", "A little about me", "Engineering discipline, analytical thinking, and a passion for applied AI.", "about")
left, right = st.columns([1.35, 1])
with left:
    st.markdown("""I work across the lifecycle of data products — from data preparation and exploratory analysis to model development, evaluation, API creation, and deployment.

My experience spans **software development, data science mentoring, machine learning, NLP, and Generative AI**. I enjoy translating complex problems into usable applications and helping learners build confidence through hands-on projects.

My approach: understand the problem, build a reliable solution, communicate the outcome, and make it usable.""")
with right:
    st.markdown("""<div class="card"><div class="card-top">Current focus</div><h3>Applied AI that ships</h3><p>LLM applications, RAG workflows, intelligent assistants, predictive modelling, and production-minded ML deployment.</p><hr><p><b>Based in</b><br>India</p><p><b>Target roles</b><br>Data Scientist · ML Engineer · AI Engineer</p></div>""", unsafe_allow_html=True)

st.write("")
section("02 / Capabilities", "Technical toolkit", "Core technologies across analysis, modelling, AI application development, and deployment.", "skills")
skill_groups = [
    ("Programming & Data", ["Python", "SQL", "PySpark", "ETL / ELT", "Pandas", "NumPy", "Statistics", "EDA"]),
    ("Machine Learning", ["Scikit-learn", "Predictive Modelling", "Feature Engineering", "Ensemble Learning", "Time Series", "A/B Testing"]),
    ("AI & Deep Learning", ["TensorFlow", "PyTorch", "BERT", "LLMs", "NLP", "Generative AI", "Agentic AI", "Object Localization"]),
    ("LLM Application Stack", ["LangChain", "RAG", "FAISS", "Hugging Face", "Vector Databases", "Gemini API"]),
    ("Deployment & Engineering", ["Streamlit", "Flask", "FastAPI", "Docker", "GitHub Actions", "CI/CD", "Render"]),
    ("Cloud & BI", ["AWS", "Azure ML", "Power BI", "Tableau", "PostgreSQL", "GitHub"]),
]
skill_cols = st.columns(3)
for i, (name, items) in enumerate(skill_groups):
    with skill_cols[i % 3]:
        st.markdown(f'<div class="card"><h3>{name}</h3>{pills(items)}</div>', unsafe_allow_html=True)

st.write("")
section("03 / Selected work", "Projects with practical impact", "Explore project summaries, architecture flows, and lightweight interactive previews.", "projects")
projects = [
    {"num":"01","title":"Personal Advisor Chat System","kind":"GenAI · RAG · Streamlit","desc":"A multi-domain AI advisor for Education, Finance, Health, and Travel, featuring PDF question-answering and personalized recommendations.","stack":["Gemini API","LangChain","Hugging Face","Streamlit","RAG"],"impact":"Designed and deployed a conversational experience for real-time, multi-domain queries.","url":"https://github.com/jroshanjha/personal-advisor-chat-application","steps":[("User","Question / PDF"),("Streamlit UI","Chat interface"),("RAG pipeline","Retrieve context"),("Gemini API","Generate answer")]},
    {"num":"02","title":"Email Spam Detection Analysis","kind":"ML · Deep Learning","desc":"A hybrid spam classification approach combining TF-IDF, a StackingClassifier, and a BiLSTM model with Attention.","stack":["Python","TF-IDF","Scikit-learn","BiLSTM","Flask","Docker"],"impact":"Applied regularization and callback techniques to help control overfitting; added API deployment and CI/CD.","url":"https://github.com/jroshanjha/Email-spam-detection","steps":[("Email data","Labeled samples"),("TF-IDF","Text features"),("ML + BiLSTM","Hybrid classifier"),("Flask API","Serve prediction")]},
    {"num":"03","title":"Employee Loan Prediction","kind":"Predictive Analytics · Finance","desc":"An employee loan eligibility prediction workflow using ensemble models and a structured evaluation process.","stack":["Python","Pandas","Scikit-learn","Cross-validation","Feature Engineering"],"impact":"Applied imbalance handling, hyperparameter tuning, and evaluation visualizations; resume reports a 10% accuracy improvement.","url":"https://github.com/jroshanjha/Loan-approved","steps":[("Loan data","Input records"),("Preprocessing","Clean / encode"),("Ensemble ML","Train / predict"),("Evaluation","Metrics / insights")]},
    {"num":"04","title":"Customer Review Classification","kind":"NLP · Sentiment Analysis · ML / DL","desc":"A sentiment analysis model using TF-IDF and a BiLSTM model with Attention.","stack":["Python","TF-IDF","BiLSTM","Attention","Flask","Docker"],"impact":"Applied regularization and callback techniques to help control overfitting; added API deployment and CI/CD.","url":"https://github.com/jroshanjha/Customer-Review-Classification","steps":[("Reviews","Text samples"),("TF-IDF","Text features"),("BiLSTM + Attention","Sentiment model"),("Output","Class prediction")]},
]
for project in projects:
    with st.container():
        lcol, rcol = st.columns([1.35, 1])
        with lcol:
            st.markdown(f"""<div class="card"><div class="card-top">PROJECT {project['num']} · {project['kind']}</div><h3>{project['title']}</h3><p>{project['desc']}</p><p><b>Outcome</b><br>{project['impact']}</p>{pills(project['stack'])}<br><br><a href="{project['url']}" target="_blank" rel="noopener noreferrer">↗ GitHub repository</a><br><small style="color:#9eacc1">Confirm this repository exists and is public before publishing.</small></div>""", unsafe_allow_html=True)
        with rcol:
            with st.expander("View project architecture"):
                architecture(project["steps"])
                st.caption("Conceptual architecture based on the project description.")
            with st.expander("Try an interactive preview"):
                if project["num"] == "01":
                    st.caption("Illustrative preview only — it does not call Gemini or access private PDFs.")
                    topic = st.selectbox("Advisor topic", ["Education", "Finance", "Health", "Travel"], key="advisor_topic")
                    question = st.text_input("Sample question", placeholder="How can I plan my next steps?", key="advisor_q")
                    examples = {
                        "Education":"Break the goal into milestones, compare learning paths, and track progress with a weekly plan.",
                        "Finance":"Clarify your goal, time horizon, cash flow, and risk tolerance. Validate decisions with a qualified financial professional.",
                        "Health":"Use trusted clinical sources and discuss personal symptoms or treatment decisions with a licensed healthcare professional.",
                        "Travel":"Choose dates and budget first, then compare transport, stay, local travel, and a flexible itinerary.",
                    }
                    if st.button("Preview sample response", key="advisor_btn"):
                        st.info(f"Sample {topic.lower()} guidance: {examples[topic]}" if question.strip() else examples[topic])
                elif project["num"] == "02":
                    st.caption("Keyword-based demonstration — not the trained TF-IDF / BiLSTM model.")
                    email = st.text_area("Paste a sample email", placeholder="Congratulations! You have won a prize. Click here now.", key="spam_text")
                    if st.button("Classify sample", key="spam_btn"):
                        triggers = ["winner", "won", "prize", "claim now", "urgent", "click here", "free gift", "cash bonus"]
                        hits = [word for word in triggers if word in email.lower()]
                        if not email.strip():
                            st.warning("Enter some email text first.")
                        elif hits:
                            st.warning(f"Suspicious wording detected: {', '.join(hits)}. Review carefully.")
                        else:
                            st.success("No listed trigger phrases found. This does not guarantee the email is safe.")
                elif project["num"] == "03":
                    st.caption("Rule-based illustration — not the trained model or a lending decision.")
                    income = st.number_input("Monthly income (₹)", min_value=0, step=5000, value=50000, key="loan_income")
                    emi = st.number_input("Existing monthly obligations (₹)", min_value=0, step=1000, value=10000, key="loan_emi")
                    tenure = st.slider("Employment tenure (years)", 0, 30, 3, key="loan_tenure")
                    if st.button("View illustrative profile", key="loan_btn"):
                        if income <= 0:
                            st.warning("Enter a monthly income above zero.")
                        else:
                            ratio = emi / income
                            st.metric("Existing obligation / income", f"{ratio:.0%}")
                            st.info(("Lower" if ratio < 0.3 else "Higher") + " existing-obligation ratio; " + ("longer" if tenure >= 3 else "shorter") + " employment tenure. This is not a credit score or eligibility result.")
                else:
                    st.caption("Simple illustrative text check — not the trained sentiment model.")
                    review = st.text_area("Customer review", placeholder="The product quality is excellent and delivery was quick.", key="review_text")
                    if st.button("Preview review analysis", key="review_btn"):
                        if not review.strip():
                            st.warning("Enter a review first.")
                        else:
                            positive = ["excellent", "great", "good", "love", "fast", "happy", "useful", "best"]
                            negative = ["bad", "poor", "slow", "hate", "broken", "disappoint", "worst", "late"]
                            pos_hits = sum(term in review.lower() for term in positive)
                            neg_hits = sum(term in review.lower() for term in negative)
                            if pos_hits > neg_hits:
                                st.success("Illustrative result: positive wording detected.")
                            elif neg_hits > pos_hits:
                                st.warning("Illustrative result: negative wording detected.")
                            else:
                                st.info("Illustrative result: mixed or neutral wording.")

st.caption("Project links should be checked against your actual public GitHub repositories. Interactive panels are educational previews, not production models or APIs.")

st.write("")
section("04 / Career", "Experience & impact", "Software delivery, data science education, and applied analytics.", "experience")
experience = [
    ("Jan 2026 – Present", "Data Science Mentor", "Skill Circle", "Teaching Python, SQL, Statistics, ML, Deep Learning, and Generative AI; mentoring real-world projects in Data Science, NLP, and AI; conducting hands-on sessions on model building and deployment."),
    ("Jul 2025 – Dec 2025", "Data Science Mentor", "Git India", "Taught Python, SQL, Statistics, ML/DL/NLP, and Generative AI; guided learners on practical Data Science and BI projects."),
    ("Jun 2023 – Oct 2024", "Software Developer", "Aeologic Technologies / NIC", "Developed Samadhan and Pencil portals for labour case management; performed EDA using Pandas, NumPy, and SQL; automated MIS dashboards with Python and PostgreSQL."),
    ("Jan 2022 – Mar 2023", "Software Developer (Part-Time)", "WebKart Digital Pvt Ltd", "Improved UI/UX, developed custom modules for client requirements, and delivered maintainable production code."),
]
st.markdown('<div class="timeline">', unsafe_allow_html=True)
for date, role, company, desc in experience:
    st.markdown(f'<div class="timeline-item"><div class="card-top">{date}</div><h3 style="margin:.2rem 0">{role} · {company}</h3><p>{desc}</p></div>', unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

st.write("")
section("05 / Education", "Education & certifications")
edu1, edu2 = st.columns(2)
with edu1:
    st.markdown("""<div class="card"><div class="card-top">Jan 2026 – Dec 2027</div><h3>Master of Computer Applications (MCA)</h3><p>Amity University, Noida</p><hr><div class="card-top">Aug 2018 – Dec 2022</div><h3>Bachelor of Computer Applications (BCA)</h3><p>Maharaja Agrasen Enclave University (IGNOU)</p></div>""", unsafe_allow_html=True)
with edu2:
    st.markdown("""<div class="card"><h3>Certifications</h3><p>✦ Data Science and AI/ML Program — Bosscoder Academy</p><p>✦ Advanced Python, ML, DL, GenAI — Udemy</p><p>✦ Python EDA, Statistics, ML — Great Learning</p><p>✦ HackerRank — Python, SQL, Problem Solving</p></div>""", unsafe_allow_html=True)

st.write("")
section("06 / Let's connect", "Have a problem worth solving?", "I'm interested in opportunities and conversations around Data Science, Machine Learning, and AI engineering.", "contact")
st.markdown("""<div class="contact"><h3>Let’s build something useful.</h3><p class="subtle">Reach out for roles, collaborations, or conversations about applied AI.</p></div>""", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("**Email**  \n[jroshan731@gmail.com](mailto:jroshan731@gmail.com)")
with c2:
    st.markdown("**LinkedIn**  \n[roshan-jha-tech](https://www.linkedin.com/in/roshan-jha-tech)")
with c3:
    st.markdown("**GitHub profile**  \n[jroshanjha](https://github.com/jroshanjha)")

if RESUME_PATH.exists():
    st.download_button("↓ Download my resume", data=RESUME_PATH.read_bytes(), file_name="Roshan_Jha_Resume.pdf", mime="application/pdf")
else:
    st.info("Add your resume PDF at assets/Roshan_Jha_Resume.pdf to enable the download button.")

st.markdown("---")
st.markdown('<p style="text-align:center;color:#8290a6;font-size:.82rem">Designed & built with Python + Streamlit · Roshan Jha</p>', unsafe_allow_html=True)

