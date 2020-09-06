import fitz
from functools import reduce

inputp="pdf_name.pdf"
# Open the pdf
pdf=fitz.open(inputp)

# Count the number of pages
count=len(pdf)
print(count)

print("1. Page No.\n2. Complete PDF")
n=int(input())

font=[]

if n==1:
    no=int(input("Page number: "))
    # Get the font for the particular page
    page=[page[3] for page in pdf.getPageFontList(no, full=False)]
    font.append(page)

else:
    for i in range(0,count):
        # For each page in the PDF, get the font of the page
        page=[page[3] for page in pdf.getPageFontList(i,full=False)]
        font.append(page)

fonts=reduce(lambda x,y:x+y,font)

for i in set(fonts):
    # Print different fonts in the set 
    print((i.split("+")[1]))
