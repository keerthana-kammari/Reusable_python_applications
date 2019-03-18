import sys, getopt, re, time
import docx

file_type = input("What kind of file do you want to use? \n a.txt \n b.docx \n c.PDF \n d.CSV \n")
file_path = sys.argv[1] #File path provided along the command line
existing_word = input("Please enter word/number to replace: ")
replace_word = input("Please enter the new word to be replaced with existing word: ")

#Replace function for .txt files
def check_text(param):
    start_time = time.time()
    try:
        data = open(file_path, 'r')
        text = data.read()
        search_word = re.sub(existing_word, replace_word, text, flags = re.IGNORECASE)
        data_out = open(file_path, 'w')  #Open a file in write mode      
        data_out.write(search_word) #Words replaced will be written and saved to file
    except FileNotFoundError:
        print("No file exists in the provided path!!")
        data.close()
    end_time = time.time()
    print("Your file has been modified with a new word, total time taken: {:.2f} sec".format(end_time-start_time))

#Replace function for .docx files
def check_doc(param):
    start_time = time.time()
    doc = docx.Document(file_path)
    try:
        for paragraph in doc.paragraphs:
            paragraph.text = re.sub(existing_word, replace_word, paragraph.text, flags= re.IGNORECASE)
            print(paragraph.text)
        doc.save('modified_doc.docx')
    except:
        print("No file exists in the provided path!!")
    end_time = time.time()
    print("Your file has been modified with a new word, total time taken {:.2f} ".format(end_time-start_time))

if __name__ == "__main__":
    if file_type == 'txt' and file_path.endswith('.txt'):
        print("The uploaded file path is: ", file_path)
        check_text(file_path)
    elif file_type == 'docx' and file_path.endswith('.docx'):
        print("The uploaded file path is: ", file_path)
        check_doc(file_path)
    else:
        print("Please provide the appropraite file path as chosen")
