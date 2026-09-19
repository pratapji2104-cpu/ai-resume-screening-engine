from src.tools.pdf_parser import extract_text_from_pdf


pdf_path = input("Enter PDF path: ").strip()

with open(pdf_path, "rb") as file:
    text = extract_text_from_pdf(file)

print("\n===== EXTRACTED RESUME TEXT =====\n")
print(text[:3000])