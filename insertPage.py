import fitz

inputp="abc.pdf"
pdf=fitz.open(inputp)

count=len(pdf)
print("Total pages:",count)

print("1. Plain Page.\n2. Written Page.\n ")
n=int(input())

pno = int(input("Page number [-1 for first page] : "))

if n==2:
    text=input("Enter text: \n")
    com=pdf.insertPage(pno,text)

else:
    com=pdf.newPage(pno)

output="Updated_"+inputp
pdf.save(output)