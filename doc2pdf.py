import fitz

input="pdf_name.docx"
out=list(input.split("."))[0]
output=out+".pdf"  

# Open the pdf
con=fitz.open(input)

# Convert to pdf, -1 indicates the start page to end page
pdfbytes=con.convertToPDF(from_page=-1,to_page=-1,rotate=0)

# Open the pdfbytes in the pdf format
pdf=fitz.open("pdf",pdfbytes)

# Save it in desired output file
pdf.save(output)
