import PyPDF2


def merge_pdfs(pdf_list, output_filename):
    # Create a PDF writer object
    pdf_writer = PyPDF2.PdfWriter()

    # Iterate through the list of PDF filenames
    for pdf in pdf_list:
        try:
            # Create a PDF reader object for each input PDF
            pdf_reader = PyPDF2.PdfReader(pdf)

            # Add each page of the current PDF to the writer object
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                pdf_writer.add_page(page)
        except Exception as e:
            print(f"Error reading {pdf}: {e}")
            continue

    try:
        # Write the collected pages to the output PDF file
        with open(output_filename, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)
        print(f"PDF files {pdf_list} merged into {output_filename}")
    except Exception as e:
        print(f"Error writing {output_filename}: {e}")


# Example usage
pdf_files = [r"C:\Users\User\Downloads\ERM-Lecture 1.pdf", r"C:\Users\User\Downloads\ERM-Lecture 2.pdf",
             r"C:\Users\User\Downloads\ERM-Lecture 3.pdf", r"C:\Users\User\Downloads\ERM-Lecture 4.pdf",
             r"C:\Users\User\Downloads\ERM-Lecture 5.pdf", r"C:\Users\User\Downloads\ERM-Lecture 6.pdf",
             r"C:\Users\User\Downloads\ERM-Lecture 7.pdf", r"C:\Users\User\Downloads\ERM-Lecture 8.pdf",
             r"C:\Users\User\Downloads\ERM-Lecture 9.pdf", r"C:\Users\User\Downloads\ERM-Lecture 10-5.pdf"
             ]
output_file = r'C:\Users\User\Downloads\ERM-LECTURES.pdf'
merge_pdfs(pdf_files, output_file)
