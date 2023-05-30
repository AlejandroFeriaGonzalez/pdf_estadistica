import PyPDF2
import re


#* Escribe aqui la direccion del pdf
pdf_reader = PyPDF2.PdfReader('pdf_estadistica\diavositiva.pdf')
#----------------------------------------------------

patron_numDiavositiva = "(\d*)\s/\s(\d*)"
writer = PyPDF2.PdfWriter()

numDiavositas =  re.search(patron_numDiavositiva, pdf_reader.pages[-1].extract_text()[-7:]).group(1)

def numeroPagina(pagina:str):
    return re.search(patron_numDiavositiva, pagina.extract_text()).group(1)

for i, page in enumerate(pdf_reader.pages):
    numPag = numeroPagina(page)

    #Si el indice de la siguiente pagina es diferente al actual, entonces es una diavositiva final
    if (int(numPag) == int(numDiavositas)): break

    if (numeroPagina(pdf_reader.pages[i+1]) != numPag):
        writer.add_page(page)

#añadir ultima pagina
writer.add_page(pdf_reader.pages[-1])

with open("Nueva diavositiva.pdf", "wb") as fp:
    writer.write(fp)
