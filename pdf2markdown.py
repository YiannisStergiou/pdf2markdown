import fitz
import os
import time
import base64
from openai  import OpenAI
from pathlib import Path
from dotenv  import load_dotenv

#################################################
#############  pdf2base64 function  #############
#################################################

# converts each page of the pdf into base64 string, using utf-8 formating
# Output: base64 string & total pdf pages

def pdf2doc(PDF):
    # Document Mapping
    document        = fitz.open(PDF)
    total_doc_pages = len(document)
    
    return document, total_doc_pages

##################################################
##################  doc2base64  ##################
##################################################

def doc2base64(document, DPI):
    # PDF page converts to PNG
    pic = document.get_pixmap(dpi = DPI, colorspace = fitz.csGRAY)

    # Raw pixels to PNG format
    pic_bytes = pic.tobytes("png")

    #Encode from Binary to Base64
    base64_pic = base64.b64encode(pic_bytes)

    # Decode to UTF-8
    base64_string = base64_pic.decode("utf-8")

    return base64_string

##################################################
###############  save2md function  ###############
##################################################

def save2md(document, filename):

    # Ανοίγουμε το αρχείο και το γράφουμε σε Markdown
    with open(f"{Path(filename).stem}.md", "a", encoding = "utf-8") as final_markdown:
        final_markdown.write(document)

###################################################
#############  ocr_function function  #############
###################################################

# Inputs the base64 string, as long as the total pdf pages and sents them to the API.
# Outputs the pdf as a string

def ocr_function(pdf, dpi, url, api_key, model):

    # Conencting with the API
    client = OpenAI(base_url = url, api_key  = api_key)

    document, page_count = pdf2doc(PDF = pdf)

    # Initializes the markdown file
    with open(f"{Path(pdf).stem}.md", "w", encoding = "utf-8") as final_markdown:
        pass

    # Prints the model that used for OCR on top of the Markdown
    picked_model      = f"<!--  File:  {Path(pdf).stem}.md  -->\n<!--  Model:  {model}  -->\n<!--  DPI:  {dpi}  -->\n\n"
    save2md(document = picked_model, filename = pdf)

    for page in range(page_count):

        # Timer
        start_time = time.time()

        print(f"Page {page + 1}/{page_count} scan in proccess . . .")

        # Base 64 String
        string = doc2base64(document = document[page], DPI = dpi)

        response_OCR = client.chat.completions.create(
            model       = model,
            messages    = [
                # System Promt
                {
                    "role": "system",
                    "content": (
                        "You are an expert document OCR analyst. Your sole mission is to extract the text "
                        "from the provided images with 100% accuracy, faithfully preserving its original structure, "
                        "paragraphs, and formatting.\n\n"
                        "**CRITICAL RULES:**\n"
                        "1. DO NOT translate the text. Extract it exactly in its ORIGINAL language (e.g., Greek).\n"
                        "2. Do not add your own comments, introductions, or explanations. Output ONLY the extracted text.\n"
                        "3. Do not enclose the output in Markdown code blocks (```). Return pure, raw Markdown text.\n"
                        "4. If the image is completely empty or contains no text, output ONLY this exact string: <!-- Page Empty -->\n\n"
                        "5. When encountering mathematical equations, formulas, or symbols, you MUST format them strictly using LaTeX. Use `$` for inline math and `$$` for display/block equations.\n"
                        "6. When encountering URLs or web links, you MUST format them as clickable HTML tags (e.g., `<a href=\"URL\">URL</a>`).\n\n"
                        "**MARKDOWN FORMATTING:**\n"
                        "Use standard Markdown tools (bold, italics, tables, lists, `#` headers) exclusively "
                        "to visually and structurally replicate the original document as closely as possible."
                    )
                },
                # User Input
                {
                    "role": "user",
                    "content": [
                        # User Prompt
                        {
                            "type": "text",
                            "text": "Extract the text from this document image following the system rules."

                        },
                        # User Attached Files
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:image/png;base64,{string}"}
                        }
                    ]
                }
            ],
            # Temperature set to 0.0 for less hallucination
            temperature = 0.0
        )
        # Time
        end_time  = time.time()

        # Totel Seconds for one page OCR
        total_sec = end_time - start_time
  
        print(f"API time: {total_sec:.1f} seconds")

        # API Response stored as text
        markdown_text     = response_OCR.choices[0].message.content

        # Total Prompt & Completion Tokens
        prompt_tokens     = response_OCR.usage.prompt_tokens
        completion_tokens = response_OCR.usage.completion_tokens
        total_tokens      = response_OCR.usage.total_tokens

        print(f"Prompt Tokens:   {prompt_tokens}")
        print(f"Response Tokens: {completion_tokens}")
        print(f"Total Tokens:    {total_tokens}")

        # Header, Footer and page count
        page_num          = f"{page + 1}"
        header            = f"<!--  Page {page_num}  -->"
        footer            = f"<!-- End of {page_num} -->"

        # Full page content construction
        full_page_content = f"{header}\n\n{markdown_text}\n\n{footer}\n\n"

        # Εδώ θα μπει η συνάρτηση save2md
        save2md(document = full_page_content, filename = pdf)
        print(". . . done\n")
    document.close()



##################################################
##################### pdf2md #####################
##################################################

# Final function that containse all of the above

def pdf2md(pdf, dpi, url, api_key, model):
    start_time = time.time() 

    ocr_function(pdf = pdf, dpi = dpi, url = url, api_key = api_key, model = model)

    end_time       = time.time()

    time_2_convert = end_time - start_time
    minutes        = int(time_2_convert // 60) # How many "60"s fit inside time_2_convert
    seconds        = int(time_2_convert % 60)  # Mod(60)

    print(f"Conversion took {minutes}:{seconds}\n")

#################################################
##################  API Picker ##################
#################################################

def api_picker():

    api_list = [
        {
            "name"    : "Local",
            "url"     : "http://127.0.0.1:1234/v1",
            "model"   : "local-model",
            "api_key" : "lm-studio"
        },
        {
            "name"    : "Google",
            "url"     : "https://generativelanguage.googleapis.com/v1beta/openai/",
            "model"   : [
                "gemini-3.5-flash-lite",
                "gemini-3.1-flash-lite",
                "gemma-4-31b-it",
                "gemma-4-26b-a4b-it",
                "gemini-3.6-flash",
                "gemini-3.5-flash",
                "gemini-3-flash-preview",
                "gemini-2.5-flash-lite",
                "gemini-3.1-pro-preview"
                ],
            "api_key" : "empty" # No payment has been set
        }

    ]
    user_error = True
    while (user_error == True):

        ###  Available APIs in this session ###
        print("Available APIs")

        for index, api_name in enumerate(api_list):
            print(f"[ {index + 1} ] {api_name['name']}")

        # User Input for API picking
        user_input_for_api = input("\nPick a number to choose your API\n")

        try:
            user_input_for_api = int(user_input_for_api)

            if user_input_for_api >= 1 and user_input_for_api <= index + 1:
                # Picked API
                picked_api = api_list[user_input_for_api - 1]

                # User picked a ligal number
                user_error = False
            else:
                print(f"You must pick between 1 and {index + 1}\n")

        except ValueError:
            print("Something went wrong. Try again\n")

    ###  Model Picker  ###
    if isinstance(picked_api["model"], list):

        user_error = True
        while (user_error == True):

            print(f"Available Models for {picked_api['name']} API\n")
            models_to_pick = picked_api["model"]

            for index, model_name in enumerate(models_to_pick):
                print(f"[ {index + 1} ] {model_name}")

            # User input for model pick
            user_input_for_model = input("\nPick a number to choose your model\n")

            try:
                user_input_for_model = int(user_input_for_model)

                if user_input_for_model >= 1 and user_input_for_model <= index + 1:
                    picked_api["model"]  =  picked_api["model"][user_input_for_model - 1]

                    user_error = False
                else:
                    print(f"ERROR: You must pick between 1 and {index + 1}")

            except ValueError:
                print("ERROR: Something went wrong. Please try again\n")

    ###  API Key Set  ###
    if picked_api["api_key"] == "empty":
        load_dotenv()
        picked_api_name = picked_api["name"]
        env_api_key     = os.getenv(f"{picked_api_name}_API_KEY")

        if env_api_key:
            picked_api["api_key"] = env_api_key
            print(f"{picked_api_name}API key leaded from enviroment\n")
        else:
            user_input_api_key    = input(f"Please paste you {picked_api['name']} API key\nNOTE: If API key is wrong, the program is going to crash\n")

            user_input_api_key    = str(user_input_api_key)
            picked_api["api_key"] = user_input_api_key

    return picked_api

##################################################################################################
##################################################################################################

from art import text2art

if __name__ == "__main__":

    banner_block = text2art("PDF  2  MD ")
    print(banner_block)
    print("© 2026 Ioannis Stergiou | Licensed under MIT\n")

    # Scans for all pdf in the folder
    pdf_files_list = list(Path(".").glob("*.pdf"))

    # 
    if not pdf_files_list:
        print("ERROR: No PDFs in this folder")
    else:
        user_error = True
        while user_error == True:

            print("Available PDFs in this Folder:")

            # Prints the name of every pdf in the current folder
            for index, pdf in enumerate(pdf_files_list):
                print(f"[ {index + 1} ] {pdf.name}")

            # User input here
            raw_user_input = input("\nPick a pdf to convert into Markdown.\n-1: Convert All\n 0: No Conversion\n")

            # Check if User Intput for PDF pick was wrong
            try:
                user_input = int(raw_user_input)

                # If User sets an illigal value, user_input resets to 0
                if (user_input < -1 or user_input > len(pdf_files_list)):
                    print(f"\n*** ERROR: You have to pick between 1 and {len(pdf_files_list)}.\n{user_input} is wrong! ***\n")
                    user_error = True
                else:
                    user_error = False
            except ValueError:
                # If user_intput is not integer, user_input will set to 0, and the program will end
                print(f"\n*** ERROR: Bro said '{raw_user_input}' LOL\nTry again. ***\n")
                user_error = True

        if (user_input == 0):
            print("\nHave Fun")
        else:
            # We call the function that gives the API info
            picked_api = api_picker()
            
            raw_user_input_dpi = input("Default DPI = 100\nYou can change this now\n")
            
            # If User presses Enter, DPI resets to 100
            if (raw_user_input_dpi.strip() == ""):
                user_input_dpi = 100
            else:
                try:
                    user_input_dpi = int(raw_user_input_dpi)

                    # DPI must be between 1 to 500.
                    # If not DPI resets to 100
                    if (user_input_dpi <= 0 or user_input_dpi > 500):
                        print("ERROR: DPI was Wrong. Accepted range: 1 to 500.\nDPI resets to 100")
                        user_input_dpi = 100
                # If user input was wrong, like string or float, DPI resets to 100
                except ValueError:
                    print("ERROR: DPI Must Be Integer.\nDPI resets to 100")
                    user_input_dpi = 100

            print("#" * 100 + "\n")

            # In case User wants to Convert every PDF into Markdown in the folder
            if (user_input == -1):
    
                for index, pdf in enumerate(pdf_files_list):
                    print(f"[ {index + 1} ] {pdf.name} is now converting using {picked_api["model"]} . . .")
                    pdf2md(
                        url     = picked_api["url"],
                        api_key = picked_api["api_key"],
                        model   = picked_api["model"],
                        pdf     = pdf.name,
                        dpi     = user_input_dpi
                    )
                

    
            # In case User wants to Convers a specific PDF into Markdown in the folder
            else:
                print(f"[ {user_input} ] {pdf_files_list[user_input - 1].name} is now converting using {picked_api["model"]} . . .")
                pdf2md(
                    url     = picked_api["url"],
                    api_key = picked_api["api_key"],
                    model   = picked_api["model"],
                    pdf     = pdf_files_list[user_input - 1],
                    dpi     = user_input_dpi
                )

    input("\nPress 'ENTER' to end the task ...")