from fpdf import FPDF
import pandas as pd
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")
for index, item in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=item["Topic"], align="L", ln=1, border=0)
    pdf.line(10,21,200,21)

    pdf.ln(265)
    pdf.set_font(family="times", style="I", size=8)
    pdf.cell(w=0,h=10,txt=item["Topic"], align="R")

    for x in range(item['Pages']-1):
        pdf.add_page()
        pdf.ln(277)
        pdf.set_font(family="times", style="I", size=8)
        pdf.cell(w=0, h=10, txt=item["Topic"], align="R")

pdf.output("output.pdf")
