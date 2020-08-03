import img2pdf
from PIL import Image
from PyPDF2 import PdfFileWriter, PdfFileReader
# from reportlab.pdfgen import canvas

input='170950107011_ins.pdf'
watermark='C:/Users/Admin/PycharmProjects/PDF center/watermark.pdf'
output=input+'_watermark.pdf'

img='C:/Users/Admin/PycharmProjects/PDF center/images.jpg'

image=Image.open(img)

pdf_bytes=img2pdf.convert(image.filename)
file=open(watermark,"wb")
file.write(pdf_bytes)

image.close()
file.close()

'''
c=canvas.Canvas("watermark.pdf")

c.drawImage('img.jpg',300,450)

c.drawString(300,450,'Hello World')
c.save()
'''


watermark_file=PdfFileReader(open(watermark,"rb"))

output_file= PdfFileWriter()
input_file=PdfFileReader(open(input,"rb"))

page_count=input_file.getNumPages()

for page in range(page_count):
    # print(" Watermarking page {} of {}".format(page,page_count))

    input_page=input_file.getPage(page)
    input_page.mergePage(watermark_file.getPage(0))

    output_file.addPage(input_page)

with open(output,"wb") as outputStream:
    output_file.write(outputStream)
