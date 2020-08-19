import fitz

inputp="abc.pdf"
pdf=fitz.open(inputp)

# count=len(pdf)
# print("Total pages:",count)

pno = int(input("Enter page number(0 - {}): ".format(len(pdf))))
top=int(input("In front of which page: "))

com=pdf.movePage(pno,top)

output="Updated_"+inputp
pdf.save(output)