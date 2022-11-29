#pip install PyPDF2 

#importa a dependencia requerida
from PyPDF2 import PdfFileReader

#define pdf a ser lido
pdf_file_name = 'arquivo.pdf'

#abre o arquivo em binário para leitura
with open(pdf_file_name, 'rb') as arquivo_pdf:
    
    #lê arquivo pdf
    pdf_reader = PdfFileReader(arquivo_pdf)
    
    #retorna o número de páginas no pdf
    page_nums = pdf_reader.numPages
    
    #itera sobre os numeros de páginas
    for page_num in range(page_nums):
        
        #lê a página fornecido do PDF
        page = pdf_reader.getPage(page_num)
        
        #extrai o texto da página fornecida
        text = page.extractText()
        
        #retorna o texto
        print(text)
