from chains.resume_parser import parse_resume
from chains.jd_parser import parse_jd
from chains.matcher import match_resume_to_jd
from chains.generator import generate_resume_advice, generate_cover_letter, generate_enhanced_resume
from utils.doc_writer import save_cover_letter
from utils.pdf_loader import extract_resume_text
from utils.jd_loader import fetch_jd_from_url
from utils.resume_writer import add_markdown_bold_paragraph, extract_between_markers, save_enhanced_resume
#from docx2pdf import convert
from utils.pdf_converter import docx_to_pdf

resume_path = input("Enter path to your resume PDF: ")
resume_text = extract_resume_text(resume_path)


choice = input("Job description input: 1) Paste text 2) Enter URL\n> ")

if choice.strip() == "1":
    print("Paste job description (end with empty line):")
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    jd_text = "\n".join(lines)

elif choice.strip() == "2":
    url = input("Enter job description URL: ")
    jd_text = fetch_jd_from_url(url)
    if jd_text is None:
        print("⚠️ Could not fetch JD from URL. Please paste manually:")
        lines = []
        while True:
            line = input()
            if line.strip() == "":
                break
            lines.append(line)
        jd_text = "\n".join(lines)
else:
    print("Invalid choice. Defaulting to manual paste.")
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    jd_text = "\n".join(lines)


resume = parse_resume(resume_text)
jd = parse_jd(jd_text)

match = match_resume_to_jd(resume, jd)


advice = generate_resume_advice(resume_text, jd_text)

enhanced_resume = generate_enhanced_resume(resume_text, jd_text)
enhanced_resume = extract_between_markers(enhanced_resume)
save_enhanced_resume(enhanced_resume)
#convert("enhanced_resume.docx", "enhanced_resume.pdf")  
docx_to_pdf("enhanced_resume.docx")

cover_letter = generate_cover_letter(resume_text, jd_text)
save_cover_letter(cover_letter)


print("\n=== MATCH RESULT ===")
print(match)

print("\n=== RESUME IMPROVEMENT SUGGESTIONS ===")
print(advice)

print("\nEnhanced resume saved as 'enhanced_resume.docx' and 'enhanced_resume.pdf'")
print("Cover letter saved as 'cover_letter.docx'")
