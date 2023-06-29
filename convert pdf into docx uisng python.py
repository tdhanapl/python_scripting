#conevrt pdf into docx 
# Install the moudle uisng "pip install pdf2docx "
from pdf2docx import converter
pdf_file = 'resume.pdf'
docx_file = 'resume.pdf'
cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()