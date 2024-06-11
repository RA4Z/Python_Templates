import os
from docx import Document
import PyPDF2

def extrair_procedimento(filename:str):
    try:
        doc = Document(filename)
        texto = "\n".join([paragraph.text for paragraph in doc.paragraphs])
    except:
        texto = ''
        pass

    return texto

def extrair_pdf(filename:str):
    pdf_file_obj = open(filename, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
    all_text = ""
    for page_num in range(len(pdf_reader.pages)):
        page_obj = pdf_reader.pages[page_num]
        text = page_obj.extract_text()
        all_text += text

    pdf_file_obj.close()
    return all_text

def buscarDados():
    pasta = "\\\\intranet.weg.net@SSL\\DavWWWRoot\\br\\energia-wm\\pcp\\Central de Arquivos"

    # Loop pelos arquivos na pasta
    for arquivo in os.listdir(pasta):
        if arquivo.endswith('.docx'):
            print(extrair_procedimento(f'{pasta}\\{arquivo}'))
        if arquivo.endswith('.pdf'):
            print(extrair_pdf(f'{pasta}\\{arquivo}'))

if __name__ == "__main__":
    buscarDados()