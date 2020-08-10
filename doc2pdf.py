import fitz

input="abc.docx"
out=list(input.split("."))[0]
output=out+".pdf"

con=fitz.open(input)

pdfbytes=con.convertToPDF(from_page=-1,to_page=-1,rotate=0)

pdf=fitz.open("pdf",pdfbytes)
pdf.save(output)
