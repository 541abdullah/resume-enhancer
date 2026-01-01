
from docx import Document

def save_cover_letter(content: str, filename="cover_letter.docx"):
    doc = Document()
    for line in content.split("\n"):
        doc.add_paragraph(line)
    doc.save(filename)
