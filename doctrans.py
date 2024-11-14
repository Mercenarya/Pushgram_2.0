import os
import pymupdf
import deep_translator
from deep_translator import GoogleTranslator
import requests

def resquest_doc(link):
    trans = GoogleTranslator(target='vietnamese')
    response = requests.get(link)
    try:
        if response.status_code == 200:
            # print("Translating...")
            # result = trans.translate(response.text)
            # print(result)
            with open("tranfile.pdf","wb") as file:
                print("insert...")
                file.write(response.content)
        else:
            return response.status_code
    except Exception as error:
        return error
    
def translate(docx):
    doc = pymupdf.open(docx)
    trans = GoogleTranslator(target="vietnamese")
    xref = doc.add_ocg("vietnamese")
    for page in doc.pages:
        target = doc.pages


if __name__ == "__main__":
    print(resquest_doc("https://education.github.com/git-cheat-sheet-education.pdf"))