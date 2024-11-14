import os
import PyPDF2
import deep_translator
from deep_translator import GoogleTranslator
import requests


target = os.path.dirname(os.path.abspath(__file__))

def change_directory(path):
    pass

def resquest_doc(link):
    
    response = requests.get(link)
    try:
        if response.status_code == 200:

            with open("tranfile.pdf","wb") as file:
                print("insert...")
                file.write(response.content)
        else:
            return response.status_code
    except Exception as error:
        return error
    
def read_pdf():
    with open(f"{target}/tranfile.pdf","rb") as file:
        read_pdf = PyPDF2.PdfReader(file)
        text = ""
        for page in range(len(read_pdf.pages)):
            text += read_pdf.pages[page].extract_text()
        return text
    
        


if __name__ == "__main__":
    # print(resquest_doc("https://education.github.com/git-cheat-sheet-education.pdf"))
    print(read_pdf())