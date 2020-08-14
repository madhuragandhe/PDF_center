import fitz

print("1. Page No.\n2. Complete PDF")
n=int(input())

inputp="pymupdf.pdf"
pdf=fitz.open(inputp)

if n==1:
    no=int(input("Page number: "))
    page=no

for page in pdf.getPageFontList(0,full=False):
    print(page[3])

