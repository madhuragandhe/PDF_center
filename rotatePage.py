import fitz

inputp='pdf_name.pdf'
# Open the pdf 
pdf=fitz.open(inputp)

for page in pdf:
    # For each page in the PDF rotate the page by 90 degree to the right
    page.setRotation(90)

# Save the updated pdf in the output file 
output="Rotated_"+inputp
pdf.save(output)
