import fitz

pdf=fitz.open()
img_list=['img.png','bar.png']

for img in img_list:
    imgdoc=fitz.open(img)
    pdfbytes=imgdoc.convertToPDF()
    imgpdf=fitz.open("pdf",pdfbytes)
    pdf.insertPDF(imgpdf)

pdf.save("ImagesPDF.pdf")