import fitz

inputp="pdf_name.pdf"
pdf=fitz.open(inputp)

count=len(pdf)
print("Total pages:",count)

pno = int(input("Page number: "))

com=pdf.deletePage(pno)

output="Updated_"+inputp
pdf.save(output)
