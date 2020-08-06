from PyPDF2 import PdfFileMerger,PdfFileReader
from os import listdir
from os.path import isfile, join
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
pdf_files = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]
merger = PdfFileMerger()

for pdf in pdf_files:
    print(pdf.title())
    if ".Pdf" in pdf.title():
        print('true')
        merger.append(open(pdf, 'rb'))

merger.write("Combined.pdf")
