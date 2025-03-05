from reportlab.pdfgen import canvas
import os


def converter_txt_pdf(caminho,saida):
    with open(caminho,"r",encoding="utf-8") as file:
        linhas = file.readlines()
        print(linhas)

    pdf = canvas.Canvas(f"c:/Users/kaduk/OneDrive/Documentos/conversor-arquivos/output/{saida}.pdf")
    pdf.setFont("Helvetica",12)
    
    y = 800
    for linha in linhas:
        pdf.drawString(100,y,linha.strip())
        y-=20

        if y < 50:
            pdf.showPage()
            pdf.setFont("Helvetica", 12)
            y = 800


    pdf.save()        


converter_txt_pdf("c:/Users/kaduk/OneDrive/Documentos/conversor-arquivos/input/input.txt")