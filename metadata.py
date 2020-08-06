from PyPDF2 import PdfFileReader

file="170950107011_ins.pdf"

output_reader=PdfFileReader(open(file,"rb"))
info=output_reader.getDocumentInfo()

for key in info:
    print(key[1:]," --> ",info[key])