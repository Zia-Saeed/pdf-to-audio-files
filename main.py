import PyPDF2
from gtts import gTTS


def text_to_speech(text, output_file, language):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(output_file)


def read_pdf_line_by_line():
    pdf_file = input("Enter a file path with extension of pdf:like(C:/file.pdf): ").strip()
    language = input("Enter language like hi for hindi accent and en for english accent: ").strip()
    try:
        with open(pdf_file, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            out_files = [f"page{file + 1}.mp3" for file in range(len(pdf_reader.pages))]

            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                text_to_speech(text=text, output_file=out_files[page_num - 1], language=language)

    except FileNotFoundError:
        print("Invalid path for File")
        read_pdf_line_by_line()


if __name__ == "__main__":
    read_pdf_line_by_line()
