from PyPDF2 import PdfReader
import textwrap

file_path = input('Enter Path')
reader = PdfReader(f'{file_path}') #read the pdf
number_of_pages = len(reader.pages) 
page_text = [page.extract_text() for page in reader.pages] #extract text from each page as a list item

text=''
for t in page_text: #combine all the text
  text+=t

def wrap_text_preserve_newlines(text, width=110):
    # Split the input text into lines based on newline characters
    lines = text.split('\n')

    # Wrap each line individually
    wrapped_lines = [textwrap.fill(line, width=width) for line in lines]

    # Join the wrapped lines back together using newline characters
    wrapped_text = '\n'.join(wrapped_lines)

    return wrapped_text

final_text = wrap_text_preserve_newlines(text)

prompt = f'''The data about the CV of a job-seeking engineering candidate has been provided within ''' ''', following this prompt. Your job is to generate a number of zeros and ones based on the following rules - 
8 job profiles are provided numbered 1 through 8. The digit at that position is 1 if the candidate is eligible for the given job profile and is zero if the candidate is not.
1. Software related roles
2. Data Related roles
3. Finance related roles
4. Management related roles
5. Consulting related roles
6. Core engineering related roles
7. Product related roles
8. Design related roles

Here core engineering related roles refer to the profile related to the engineering branch the candidate is in, about which data is provided. The details of the CV are:{final_text}'''

print(prompt)