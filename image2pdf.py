import fitz

pdf=fitz.open()
img_list=['img.png','bar.png']

for img in img_list:
    # Open each image from the image list
    imgdoc=fitz.open(img)
    # Convert the opened image to PDF
    pdfbytes=imgdoc.convertToPDF()
    imgpdf=fitz.open("pdf",pdfbytes)
    # Insert the converted pdf to the original pdf
    pdf.insertPDF(imgpdf)

# Save the new pdf
pdf.save("ImagesPDF.pdf")
