from PyPDF2 import PdfFileWriter,PdfFileReader

pdf1='170950107011_ins.pdf'
pdf2='pymupdf.pdf'

PDFS=[pdf1,pdf2]

writer=PdfFileWriter()

for pdf in PDFS:
    reader=PdfFileReader(open(pdf,"rb"))
    for i in range(reader.getNumPages()):
        page=reader.getPage(i)
        page.compressContentStreams()
        writer.addPage(page)

with open("output_file.pdf","wb") as file:
    writer.write(file)