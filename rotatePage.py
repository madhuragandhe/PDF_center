import fitz

inputp='abc.pdf'
pdf=fitz.open(inputp)

for page in pdf:
    page.setRotation(90)

output="Rotated_"+inputp
pdf.save(output)