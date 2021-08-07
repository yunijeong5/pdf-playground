import PyPDF2
import sys




# template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
# watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
# output = PyPDF2.PdfFileWriter()

# for i in range(template.getNumPages()):
#     page = template.getPage(i)
#     page.mergePage(watermark.getPage(0))
#     output.addPage(page)
    
#     with open('watermarked_output.pdf', 'wb') as file:
#         output.write(file)


def watermarker(template_name, watermark_name, output_name):
    template = PyPDF2.PdfFileReader(open(template_name, 'rb'))
    watermark = PyPDF2.PdfFileReader(open(watermark_name, 'rb'))
    output = PyPDF2.PdfFileWriter()

    for i in range(template.getNumPages()):
        page = template.getPage(i)
        page.mergePage(watermark.getPage(0))
        output.addPage(page)
        
    with open(output_name, 'wb') as file:
        output.write(file)


watermarker('super.pdf', 'wtr.pdf', 'watermarked.pdf')

