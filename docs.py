from PyPDF2 import PdfReader 

def pdf_to_text(pdf_path, txt_path):
    reader = PdfReader(pdf_path)
    
    all_text = ""
    for page_num, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            #all_text += f"\n--- Page {page_num + 1} ---\n"
            all_text += text + "\n"

    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(all_text)

    print(f"Text successfully saved to: {txt_path}")

pdf_to_text("got_book1.pdf", "got1.txt")
pdf_to_text("got_book2.pdf", "got2.txt")
pdf_to_text("got_book3.pdf", "got3.txt")
pdf_to_text("got_book4.pdf", "got4.txt")
pdf_to_text("got_book5.pdf", "got5.txt")

def combine_text_files(file_paths, output_path):
    with open(output_path, 'w', encoding='utf-8') as outfile:
        for file_path in file_paths:
            with open(file_path, 'r', encoding='utf-8') as infile:
                content = infile.read()
                outfile.write(content)
                outfile.write('\n')  # Optional: separate files with a newline

# Example usage
file_paths = [
    'got1.txt',
    'got2.txt',
    'got3.txt',
    'got4.txt',
    'got5.txt'
]

combine_text_files(file_paths, 'got_corpus.txt')
