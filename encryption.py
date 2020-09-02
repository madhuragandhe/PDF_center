from PyPDF2 import PdfFileReader,PdfFileWriter

inputf='pdf_name.pdf'
output='encrypt_'+inputf

# Ask the user for the password
password=input("Enter password")

# Open the input file in read mode
PDFfile=open(inputf,"rb")
PDFinput=PdfFileReader(PDFfile)
PDFoutput=PdfFileWriter()

for page in range(PDFinput.numPages):
    # For each page of the input pdf add the page to the output pdf
    PDFoutput.addPage(PDFinput.getPage(page))

# Encrypt the contents
PDFoutput.encrypt(password)
# Open the output file in write mode
result=open(output,"wb")
# Write the contents with encryption
PDFoutput.write(result)
result.close()
