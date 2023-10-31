from pathlib import Path

import streamlit as st
from PIL import Image
import json


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"
job_file = current_dir / "assets" / "job.json"
project_file = current_dir / "assets" / "projects.json"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Subhasree Kurusamy"
PAGE_ICON = "💻"
NAME = "Subhasree Kurusamy"
DESCRIPTION = """
Passionate and self driven Software Engineer who enjoys exploring new technologies and diverse working culture..
"""
EMAIL = "sk2745@njit.edu"
LinkedIn = "https://www.linkedin.com/in/subhasreekurusamy/"


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON,)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic, "r")


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📨", EMAIL , "\t|",f"[LinkedIn]({LinkedIn})" )


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader('Experience & Qualifications')
st.write("---")
st.write(
"""
- ✔️ Working Professional with experience in large scale application. 
- ✔️ Have experience in working with different technologies like Python, Java, MEAN along with automated testing framework like Karate, Gatling.
- ✔️ Experience in working with AWS resources like S3, SQS, AWS Glue
- ✔️ Hands on experience with troubleshooting production issue with the help of Splunk and Datadog and to make sure to identify the root cause of the issue.
"""
)

# --- SKILLS ---

st.write('\n')
st.subheader("Area of Expertise")
st.write("---")
st.write(
'''
- • **Programming:** C, C++, Python, Java, Groovy
- • **Frameworks:** Angular.js, Node.js, Java Script, Spring Boot
- • **Web Technologies:** HTML5, CSS3, Bootstrap, XML, JSP, jQuery, Ajax
- • **Databases:** Postgres, MongoDB, MySQL
- • **Cloud Technologies:** Kubernetes, Docker
- • **Analytics and Monitoring Tools:** Splunk, Elastic Search, Datadog
- • **Testing Frameworks:** Karate, Gatling
'''
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1

with open(job_file, 'r') as jf:
    jobs = json.loads(jf.read())
    for i in jobs.keys():
        st.write("📂",f"**{jobs[i]['title']}**")
        col4, col5 = st.columns([3, 1])
        with col5:
            st.write(f'**{jobs[i]["year"]}**')
        job_description = (jobs[i]["desctiption"]).split("\n")
        for points in job_description:
            st.write("- - ‣", points)


#--- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
with open(project_file, 'r') as jf:
    projects = json.loads(jf.read())
    for key, val in projects.items():
        st.write(f'**{key}**\n')
        st.write("- ",val)
