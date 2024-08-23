import os

# Path to the Desktop
desktop_path = os.path.expanduser("~/Desktop")

# Path to the folder containing the PDFs
pdf_folder = os.path.join(desktop_path, "new_folder")

# Path to the 5.txt file
txt_file_path = os.path.join(desktop_path, "5.txt")

# Read the txt file and create a list of numbers (3rd column)
with open(txt_file_path, "r") as file:
    lines = file.readlines()

# Extract the 3rd column values (numbers)
numbers = [line.split(',')[2].strip() for line in lines if len(line.split(',')) > 2]
numbers.reverse()

# Get a list of PDF files in the folder
pdf_files = sorted([f for f in os.listdir(pdf_folder) if f.endswith(".pdf")])

# Check if the number of PDF files matches the number of lines in the txt file
if len(pdf_files) != len(numbers):
    print(
        f"Warning: Number of PDF files ({len(pdf_files)}) does not match the number of numbers in the txt file ({len(numbers)}).")

# Rename the PDFs based on the extracted numbers
for number, pdf_file in zip(numbers, pdf_files):
    # Full path for the current and new PDF names
    current_pdf_path = os.path.join(pdf_folder, pdf_file)
    new_pdf_name = f"{number}.pdf"
    new_pdf_path = os.path.join(pdf_folder, new_pdf_name)

    # Rename the PDF file
    os.rename(current_pdf_path, new_pdf_path)
    print(f"Renamed: {pdf_file} to {new_pdf_name}")
