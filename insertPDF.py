import fitz

doc1 = fitz.open("pdf1_name.pdf")
doc2 = fitz.open("pdf2_name.pdf")

pages1 = len(doc1)
toc1 = doc1.getToC(False)
toc2 = doc2.getToC(False)
doc1.insertPDF(doc2)
for t in toc2:
    t[2] += pages1

doc1.setToC(toc1 + toc2)

output="Updated_.pdf"
doc1.save(output)
