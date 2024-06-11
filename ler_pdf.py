import PyPDF2

# Abre o arquivo PDF
pdf_file_obj = open('PCR.pdf', 'rb')

# Cria um objeto PDF Reader
pdf_reader = PyPDF2.PdfReader(pdf_file_obj)

# Imprime o número de páginas
print(len(pdf_reader.pages))

# Extrai o texto da primeira página
page_obj = pdf_reader.pages[0]
text = page_obj.extract_text()
print(text)

# Fecha o arquivo
pdf_file_obj.close()