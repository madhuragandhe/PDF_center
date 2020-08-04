import fitz

pdf_name='170950107011_ins.pdf'

pdf=fitz.open(pdf_name)

for page in pdf:
    pix=page.getPixmap(alpha=True)
    pix.writePNG("page-%i.png" %page.number)
    