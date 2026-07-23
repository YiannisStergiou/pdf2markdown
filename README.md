# PDF 2 Markdown (Vision LLM OCR)

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![LLM Supported](https://img.shields.io/badge/LLM-Gemini%20%7C%20Local%20Models-orange)

A powerful, interactive Python CLI utility that converts complex PDF documents into clean, structured Markdown (`.md`) files using Vision Large Language Models.

Unlike standard OCR tools that destroy formatting, **PDF 2 Markdown** uses Vision AI to extract pure text while flawlessly preserving its original structure, making it the perfect first step for **Retrieval-Augmented Generation (RAG)** systems.

*(Insert a GIF or a side-by-side screenshot here showing a complex PDF page and the generated Markdown)*

## Why this tool?
I initially built this script to solve a strict data-extraction problem: reliably parsing Greek university notes packed with complex physics/math equations, and scanning structured real estate documents. 

*   **RAG-Ready Output:** The system prompt is heavily fine-tuned to return pure, raw Markdown without AI hallucinations, conversational filler, or Markdown code blocks (` ``` `).
*   **LaTeX Math Support:** Automatically detects formulas and formats them strictly using LaTeX (`$` for inline, `$$` for blocks).
*   **Local & Cloud AI:** Works out-of-the-box with Google's Gemini API (Flash/Pro), but seamlessly integrates with local, offline models via [LM Studio](https://lmstudio.ai/).
*   **Optimized Pipeline:** Uses `PyMuPDF` to convert pages to Grayscale PNGs and Base64 strings internally, drastically reducing token payload size.

## 🚀 Quick Start (No Python Required)
For Windows users who want a plug-and-play experience without installing dependencies:

1. Head over to the [Releases](../../releases) page and download `pdf2markdown.exe`.
2. Place the executable in the same folder as your `.pdf` files.
3. Double-click to run! 
*(Note: If using Google models, you will be prompted to paste your API key on the first run).*

## Developer Setup

### Prerequisites
Make sure you have Python 3.8+ installed.

```bash
# Clone the repository
git clone https://github.com/yiannisstergiou/pdf-2-markdown.git
cd pdf-2-markdown

# Install the required dependencies
pip install pymupdf openai python-dotenv art

```

### Configuration & Usage

1. **Set up your API Key:** Create a `.env` file in the root directory and add your Google Gemini API key:

```text
Google_API_KEY="your_api_key_here"

```

2. **Run the script:**

```bash
python pdf2markdown.py

```

3. Follow the interactive ASCII terminal prompts to select your API (Local or Google), choose a model, pick your PDF, and define the extraction DPI.

## File Structure

* `pdf2markdown.py`: The main conversion engine and CLI logic.
* `1.pdf` & `1.md`: Example inputs/outputs showcasing mathematical extraction.
* `.env`: Your environment variables (ignored in git).

## Roadmap / Future Improvements

* [ ] **Asynchronous Processing:** Currently, pages are processed sequentially. The next major update will utilize `asyncio` to send multiple pages concurrently to the API, drastically speeding up conversion times for large documents.
* [ ] GUI implementation for non-terminal users.

## License

This project is licensed under the MIT License - see the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.
