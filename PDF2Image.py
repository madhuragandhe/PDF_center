import fitz

pdf_name='pdf_name.pdf'

pdf=fitz.open(pdf_name)

for page in pdf:
    pix=page.getPixmap(alpha=True)
    pix.writePNG("page-%i.png" %page.number)
    
