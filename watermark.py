from PyPDF2 import PdfFileWriter, PdfFileReader

input='company.pdf'
watermark='watermark.pdf'
output=input+'_watermark.pdf'


watermark_file=PdfFileReader(open(watermark,"rb"))

output_file= PdfFileWriter()
input_file=PdfFileReader(open(input,"rb"))

page_count=input_file.getNumPages()

for page in range(page_count):
    print(" Watermarking page {} of {}".format(page,page_count))

    input_page=input_file.getPage(page)
    input_page.mergePage(watermark_file.getPage(0))

    output_file.addPage(input_page)

with open(output,"wb") as outputStream:
    output_file.write(outputStream)
