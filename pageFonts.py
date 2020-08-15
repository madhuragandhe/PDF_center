import fitz
from functools import reduce

inputp="abc.pdf"
pdf=fitz.open(inputp)

count=len(pdf)
print(count)

print("1. Page No.\n2. Complete PDF")
n=int(input())

font=[]

if n==1:
    no=int(input("Page number: "))
    page=[page[3] for page in pdf.getPageFontList(no, full=False)]
    font.append(page)

else:
    for i in range(0,count):
        page=[page[3] for page in pdf.getPageFontList(i,full=False)]
        font.append(page)

fonts=reduce(lambda x,y:x+y,font)

for i in set(fonts):
    print((i.split("+")[1]))
