import os, sys, PyPDF2

pdf_file1 = sys.argv[1]
pdf_file2 = sys.argv[2]

def pdf_concat():
    try: 
        concat_pdf = input("Please enter the name to save new merged pdf file: ")
        pdf_merge = []
        for filename in os.listdir('.'):
            if filename.endswith('.pdf'):
                pdf_merge.append(filename)
        pdf_writer = PyPDF2.PdfFileWriter()
        #loop through all pdf files
        for filename in pdf_merge:
            with open(filename, 'rb') as f1:
                pdf_reader = PyPDF2.PdfFileReader(f1)
                for pageNum in range(pdf_reader.numPages):
                    pageObj = pdf_reader.getPage(pageNum)
                    pdf_content = pageObj.extractText()
                    pdf_writer.addPage(pageObj)
            #Save PDF to file, wb for write binary
            pdf_output = open(concat_pdf + '.pdf', 'wb')
            #Outputting the PDF file
            pdf_writer.write(pdf_output)
            #Close PDF Writer
            pdf_output.close()
        print("File created successfully!")
    except:
        print("Please check the file path!")

if __name__ == "__main__":
    pdf_concat()
#     print("The uploaded file path is: " , pdf_file1, " and " , pdf_file2)
