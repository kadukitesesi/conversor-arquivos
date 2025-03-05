from reportlab.pdfgen import canvas
import os


def converter_txt_pdf(caminho,saida):

    arquivo_txt = f"c:/Users/kaduk/OneDrive/Documentos/conversor-arquivos/input/{caminho}.txt"

    with open(arquivo_txt, "w", encoding="utf-8") as file:
        file.write("Este é o conteúdo que estou escrevendo no arquivo.\n")
        file.write("Adicionar mais conteúdo aqui...\n")

    with open(arquivo_txt, "r", encoding="utf-8") as file:
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


converter_txt_pdf("souls","like")