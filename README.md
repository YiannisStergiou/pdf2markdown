# PDF 2 Markdown (Vision LLM OCR)

A Python CLI utility that converts PDF documents into clean Markdown (`.md`) files using Vision Large Language Models. 

I initially wrote this script to solve a personal problem: I needed a reliable way to extract text from Greek university notes (which are full of complex math/physics equations and weird formatting) and some scanned real estate documents. Standard OCR tools usually mess up the structure, so I decided to use Vision models (like Gemini Flash or local models) to do the heavy lifting and output pure, structured Markdown.

## Features
* **Interactive CLI:** Simple terminal menu with ASCII art to pick files and set DPI.
* **Multi-API Support:** Works out-of-the-box with Google's Gemini API, but also supports local, offline models via [LM Studio](https://lmstudio.ai/).
* **High Accuracy:** Uses a strict system prompt to prevent the model from hallucinating or translating the text (flawlessly handles Greek and complex LaTeX math).
* **Base64 Pipeline:** Converts PDF pages to Grayscale PNGs internally via `PyMuPDF` to save token payload size before sending them to the Vision API.

## 🚀 Quick Start (Windows Only - No Python Required)

If you just want to use the tool without setting up a Python environment or installing dependencies, you can use the standalone executable:

1. Download the `pdf2markdown.exe` file from this repository.
2. Place it in the same folder as the PDF files you want to convert.
3. Double-click the `.exe` to run it!
*(Note: If you choose a Google model, the terminal will ask you to paste your API key the first time).*

---

## 👨‍💻 Developer Setup (Cross-Platform)

### Prerequisites
If you prefer to run the Python script directly, you'll need Python 3.8+ and a few dependencies. 
*(Note: Make sure to install `pymupdf` and not the outdated `fitz` package from pip).*

```bash
pip install pymupdf openai python-dotenv art

```

### Usage

1. Clone the repo and navigate to the folder.
2. **Set up your API Key:** Create a `.env` file in the root directory and add your Google Gemini API key:
```text
Google_API_KEY="your_api_key_here"

```


3. Run the script:
```bash
python pdf2markdown.py

```


4. Follow the terminal prompts to select your API, model, PDF file, and DPI.

## 📂 File Structure

* `pdf2markdown.exe`: The standalone Windows executable (Ready to use).
* `pdf2markdown.py`: The main script containing the conversion logic and CLI.
* `1.pdf` & `1.md`: Example input/output demonstrating the extraction of probability math equations in Greek.
* `.env`: (Ignored in git) Your environment variables file.

## 🚧 Future Improvements / TODOs

Right now, the script is a synchronous blocker—it processes pages one by one in a `for` loop. For a 30-page PDF, this means waiting for 30 sequential API calls. My next goal is to refactor the `ocr_function` using `asyncio` to send multiple pages to the API concurrently, significantly speeding up the conversion time.