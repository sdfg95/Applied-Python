from tex_doc_generator import generate_latex_table, generate_latex_image, generate_latex_document
import os

data = [
    ['January', 1],
    ['February', 12],
    ['March', 15],
    ['April', 20],
    ['May', 25],
    ['June', 30],
    ['July', 35],
    ['August', 40],
    ['September', 45],
    ['October', 50],
    ['November', 55],
    ['December', 60]
]

latex_table = generate_latex_table(data, "Bobr population")
latex_image = generate_latex_image('bobr.png')
latex_document = generate_latex_document(latex_table, latex_image)

latex_file_path = '../artifacts/document.tex'
pdf_file_path = '../artifacts/document.pdf'

with open(latex_file_path, 'w') as f:
    f.write(latex_document)

os.system(f"pdflatex -output-directory=../artifacts {latex_file_path}")

if os.path.exists(latex_file_path[:-4] + ".aux"):
    os.remove(latex_file_path[:-4] + ".aux")

if os.path.exists(latex_file_path[:-4] + ".log"):
    os.remove(latex_file_path[:-4] + ".log")
