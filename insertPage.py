import fitz

inputp="pdf_name.pdf"
# Open the pdf
pdf=fitz.open(inputp)

# Count the number of pages
count=len(pdf)
print("Total pages:",count)

print("1. Plain Page.\n2. Written Page.\n ")
n=int(input())

pno = int(input("Page number [-1 for first page] : "))


if n==2:
    # Ask th euser to enter the text
    text=input("Enter text: \n")
    # Insert a new page on the mentioned pageNo with user entered text written
    com=pdf.insertPage(pno,text)

else:
    # Insert a new page on the user entered pageNo
    com=pdf.newPage(pno)

# Save the updated changes in new output file    
output="Updated_"+inputp
pdf.save(output)
