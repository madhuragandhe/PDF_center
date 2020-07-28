import fitz

input_file=''
output_file=input_file+'_barcode'
barcode='barcode.png'

# define the position(upper-right-corner)
image_rectagle= fitz.Rect(450,20,550,120)

# retrive the first page
file_handle = fitz.open(input_file)
first_page = file_handle[0]

# add the image
first_page.insertImage(image_rectagle,fileName=barcode)

file_handle.save(output_file)
