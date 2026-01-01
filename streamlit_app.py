import streamlit as st
from utils.pdf_loader import extract_resume_text
from chains.generator import generate_enhanced_resume, generate_cover_letter, generate_resume_advice
from utils.resume_writer import save_enhanced_resume, extract_between_markers
from utils.doc_writer import save_cover_letter
from chains.resume_parser import parse_resume
from chains.jd_parser import parse_jd
from chains.matcher import match_resume_to_jd
from docx2pdf import convert
#from utils.pdf_converter import docx_to_pdf

st.title("Resume Enhancer 🚀")


resume_file = st.file_uploader("Upload your resume PDF", type=["pdf"])
if resume_file:
    resume_text = extract_resume_text(resume_file)

   
    jd_text = st.text_area("Paste the full Job Description here")

    if st.button("Generate Enhanced Resume"):
     
        resume_data = parse_resume(resume_text)
        jd_data = parse_jd(jd_text)
        match = match_resume_to_jd(resume_data, jd_data)

       
        st.subheader("Match Results")
        st.write(f"**Skill Match %:** {match.skill_match_percentage}%")
        st.write(f"**Experience Match:** {'Yes' if match.experience_match else 'No'}")
        st.write(f"**Matched Skills:** {', '.join(match.matched_skills)}")
        st.write(f"**Missing Skills:** {', '.join(match.missing_skills)}")

       
        advice = generate_resume_advice(resume_text, jd_text)
        st.subheader("Resume Improvement Suggestions")
        st.text(advice)

        
        enhanced_resume = generate_enhanced_resume(resume_text, jd_text)
        enhanced_resume = extract_between_markers(enhanced_resume)
        save_enhanced_resume(enhanced_resume)
        #convert("enhanced_resume.docx", "enhanced_resume.pdf")
        #docx_to_pdf("enhanced_resume.docx")

        
        cover_letter = generate_cover_letter(resume_text, jd_text)
        save_cover_letter(cover_letter)

        st.success("Enhanced resume and cover letter generated!")

        
        with open("enhanced_resume.docx", "rb") as f:
            st.download_button("Download Resume (DOCX)", f, file_name="enhanced_resume.docx")
        with open("enhanced_resume.pdf", "rb") as f:
            st.download_button("Download Resume (PDF)", f, file_name="enhanced_resume.pdf")
        with open("cover_letter.docx", "rb") as f:
            st.download_button("Download Cover Letter (DOCX)", f, file_name="cover_letter.docx")
