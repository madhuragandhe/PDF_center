from PyPDF2 import PdfFileReader

file="pdf_name.pdf"

# Open the file in read mode
output_reader=PdfFileReader(open(file,"rb"))
# Get the pdf's information/metadata
info=output_reader.getDocumentInfo()

# Print each information 
for key in info:
    print(key[1:]," --> ",info[key])
