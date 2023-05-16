from fpdf import FPDF
import glob
from pathlib import Path


filepaths = glob.glob("text_file/*")
print(filepaths)

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

for path in filepaths:

    pdf.add_page()

    with open(path, 'r') as file:
        text = file.readline()
        print(text)

    filename=Path(path).stem
    name_file = filename.split(".")[0]


    pdf.set_font(family="Times", size=20, style="B")
    pdf.cell(w=50, h=8, txt=f"{name_file}", ln=1)
    pdf.set_font(family="Times", size=14, style="I")
    pdf.multi_cell(w=180, h=8, txt=f"{text}")

pdf.output(r"PDFs\WIKI.pdf")



