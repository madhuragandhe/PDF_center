from PyPDF2 import PdfFileReader,PdfFileWriter

inputf='170950107011_ins.pdf'
output=inputf+'_encrypt.pdf'

password=input("Enter password")

PDFfile=open(inputf,"rb")
PDFinput=PdfFileReader(PDFfile)
PDFoutput=PdfFileWriter()

for page in range(PDFinput.numPages):
    PDFoutput.addPage(PDFinput.getPage(page))

PDFoutput.encrypt(password)
result=open(output,"wb")
PDFoutput.write(result)
result.close()
