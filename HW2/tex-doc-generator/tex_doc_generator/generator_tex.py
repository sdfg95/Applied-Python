
def generate_latex_table(data, table_title):
    latex_table = "\\begin{table}[h]\n\\centering\n"
    latex_table += "\\caption{" + table_title + "}\n"
    latex_table += "\\begin{tabular}{|" + "|".join(["c"] * len(data[0])) + "|}\n"
    latex_table += "\\hline\n"
    for row in data:
        latex_table += " & ".join(map(str, row)) + "\\\\ \\hline\n"
    latex_table += "\\end{tabular}\n\\end{table}"
    return latex_table


def generate_latex_image(image_path):
    image_name = image_path.split('/')[-1]
    return "\\includegraphics[width=0.5\\textwidth]{" + image_name + "}"


def generate_latex_preamble():
    return "\\documentclass{article}\n\\usepackage{graphicx}\n\\begin{document}\n"

def generate_latex_end():
    return "\n\\end{document}"

def generate_latex_document(table, image):
    return '\n'.join([generate_latex_preamble(), table, image, generate_latex_end()])

