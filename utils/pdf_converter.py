# import subprocess
# import os

# def docx_to_pdf(docx_path: str):
#     output_dir = os.path.dirname(docx_path) or "."

#     subprocess.run(
#         [
#             "libreoffice",
#             "--headless",
#             "--convert-to",
#             "pdf",
#             docx_path,
#             "--outdir",
#             output_dir,
#         ],
#         check=True,
#     )
