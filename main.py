'''
Firstly import 2 packages which are: -
-> pyttsx3 = used to make the program speak     # write 'pip install pyttsx3' in the terminal
-> PyPDF3 = used to make the program able to perform on a .pdf type of files     # write 'pip install PyPDF3' in the terminal 

'''

import pyttsx3 # to make it speak
import PyPDF3

speaker = pyttsx3.init()

#open pdf file
book = open('oops.pdf','rb') # here we enter the file name
pdfReader = PyPDF3.PdfFileReader(book)

#view nu. of pages
pages = pdfReader.numPages # Here it stores the total number of pages of a file
print("Total Number of Pages:- ", pages)

#reading a particular page
# page = pdfReader.getPage(7)
# text = page.extractText()

#reading from the starting & by chaning the 0, it can read from any particular page
for i in range(6,pages):
    page = pdfReader.getPage(i)
    text = page.extractText() # it extracts text from the page and stores in variable 'text'
    speaker.say(text) # It reads out the complete data saved in variable 'text'
    speaker.runAndWait() # it speaks and wait for a response

#speaking function

speaker.say("Thank You for Listening")
speaker.runAndWait()