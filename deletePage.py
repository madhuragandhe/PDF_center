import fitz

inputp="pdf_name.pdf"
# open the pdf 
pdf=fitz.open(inputp)

# total number of pages in the pdf
count=len(pdf)
print("Total pages:",count)

# enter the page no. to delete
pno = int(input("Page number: "))

com=pdf.deletePage(pno)

# output is saved in a new file "Updated_pdf_name.pdf"
output="Updated_"+inputp
pdf.save(output)
