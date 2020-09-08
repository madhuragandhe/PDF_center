import fitz

inputp="pdf_name.pdf"
# Open the pdf 
pdf=fitz.open(inputp)

count=len(pdf)
# Count the total number of pages in the pdf
print("Total pages:",count)

# Two inputs 1--> Page to be moved 2-->In front of which page
pno = int(input("Enter page number(0 - {}): ".format(len(pdf))))
top=int(input("In front of which page: "))

# Move the paf using the movePage function
com=pdf.movePage(pno,top)

# Save the changes in new updated pdf
output="Updated_"+inputp
pdf.save(output)
