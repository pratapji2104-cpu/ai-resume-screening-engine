from pypdf import PdfReader


def extract_text_from_pdf(file):
    try:
        reader = PdfReader(file)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        if not text.strip():
            raise ValueError("Could not extract text from PDF")

        return text.strip()

    except Exception as e:
        raise ValueError(f"PDF processing failed: {str(e)}")