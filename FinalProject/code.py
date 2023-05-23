import PyPDF2
import pyttsx3

# Open the PDF file in read-binary mode
with open('FinalProject/example.pdf', 'rb') as pdf_file:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    engine = pyttsx3.init()

    # Get the number of pages in the PDF file
    num_pages = len(pdf_reader.pages)

    # Get a list of available voices
    voices = engine.getProperty('voices')

    # Set the voice to the first available voice
    engine.setProperty('voice', voices[1].id)

    # Loop through all pages and extract text
    for page_num in range(num_pages):
        # Get the current page object
        page_obj = pdf_reader.pages[page_num]

        # Extract the text from the page object
        page_text = page_obj.extract_text()

        engine.say(page_text)

        # Wait for the speech to finish before moving on to the next page
        engine.runAndWait()

        # Print the text
        print(f"Page {page_num+1}:")
        print(page_text)

