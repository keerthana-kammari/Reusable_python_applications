import sys, getopt, re
from docx import Document

#Defining regex pattern for all file formats
csv_pattern = re.compile(r'.*.csv')
pdf_pattern = re.compile(r'.*.pdf')
txt_pattern = re.compile(r'.*.txt')
doc_pattern = re.compile(r'.*.docx')

#Extract function for .txt files
def check_text(input_file):
    try:
        data = open(input_file, 'r')
        text = data.read()
        #extract emails
        match_mail = re.findall(r'[\w\.-]+@[\w\.-]+', text)
        #extract mobile numbers 
        match_mob = re.findall(r'(\(\d{3}\)\d{3}-\d{4})', text)
        print("List of emails in the uploaded doc: ", match_mail)
        print("List of mobile numbers from the uploaded file: ", match_mob)
    except FileNotFoundError:
        print("No file exists in the provided path!!")
        data.close()
      
#Extract function for .csv files     
def check_csv(input_file):
    try:
    #Opening csv file in read mode
        with open(input_file, 'r') as csv_file:
            lines_csv = csv_file.read()         
            #extract emails
            match_mail = re.findall(r'[\w\.-]+@[\w\.-]+', lines_csv)
            print(match_mail)
            #extract mobile numbers
            match_mob = re.findall(r'(\(\d{3}\)\d{3}-\d{4})', lines_csv)
            print(match_mob)
    except FileNotFoundError:
        print("No file exists in the provided path!!")
        csv_file.close()
        
#Extract function for .docx files
def check_doc(input_file):
    try:
        #Opening .doc file
        doc = Document(input_file)
        for paragraph in doc.paragraphs:
            word_text = paragraph.text
            #extract emails
            match_mail = re.findall(r'[\w\.-]+@[\w\.-]+', word_text)
            for mails in match_mail:
                print(mails)
            #extract mobile numbers
            match_mob = re.findall(r'(\(\d{3}\)\d{3}-\d{4})', word_text)
            for mob in match_mob:
                print(mob)
    except:
        print("No file exists in the provided path!!")
        doc.close()

if __name__ == "__main__":
    if bool(csv_pattern.match(sys.argv[1])) == True:
        print("The uploaded file path is: ", sys.argv[1])
        print("This is a CSV File")
        check_csv(sys.argv[1])
    elif bool(txt_pattern.match(sys.argv[1])) == True:
        print("The uploaded file path is: ", sys.argv[1])
        print("This is a text File")
        check_text(sys.argv[1])
    elif bool(doc_pattern.match(sys.argv[1])) == True:
        print("The uploaded file path is: ", sys.argv[1])
        print("This is a Word File")
        check_doc(sys.argv[1])
    else:
        print("Unsupported File format")
