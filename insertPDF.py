import fitz

# Open both the PDFs
doc1 = fitz.open("pdf1_name.pdf")
doc2 = fitz.open("pdf2_name.pdf")

# Calculate the length of PDF1
pages1 = len(doc1)

# Get the Table of Content for both the PDFs
toc1 = doc1.getToC(False)
toc2 = doc2.getToC(False)

# Insert the PDF2 after PDF1
doc1.insertPDF(doc2)

# When we merge two PDFs, do not forget their Table of Contents
# we need to update the TOC for the new PDF
for t in toc2:
    t[2] += pages1

# new TOC=TOC of pdf1 + TOC of pdf2
doc1.setToC(toc1 + toc2)

# Save the changes in new PDF
output="Updated_.pdf"
doc1.save(output)
