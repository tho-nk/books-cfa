from PyPDF2 import PdfReader, PdfWriter

# https://chatgpt.com/share/a9520757-ba06-4c8a-945b-1d3c381eb6dc
# Define your TOC entries and their corresponding page numbers
toc_entries = [
    ("Functions", 1),
    ("1.1 What is a function?", 1),
    ("1.2 The definition of a function", 1),
    ("1.3 Representing a function", 3),
    ("1.3.1 Exponents", 4),
    ("1.3.2 Polynomials", 7),
    ("1.3.3 Trigonometric functions", 13),
    ("Differentiation", 18),
    ("2.1 Rates of change", 18),
    ("2.1.1 What is the slope of a curve at a point?", 19),
    ("2.1.2 Rules for differentiation", 23),
    ("Differentiation of trigonometric functions", 33),
    ("2.2.1 The derivatives of inverse trig functions", 37),
    ("Maxima, minima and second derivatives", 39),
    ("2.3.1 Second derivative", 42),
    ("Real life examples", 47),
    ("Exponentials and Logarithms", 51),
    ("3.1 Exponentials", 51),
    ("3.1.1 Slope of exponentials", 52),
    ("The natural logarithm", 53),
    ("3.2.1 Logarithms base a", 55),
    ("Exponential growth and decay", 56),
    ("3.3.1 Radioactive decay", 56),
    ("3.3.2 Carbon dating", 57),
    ("3.3.3 Population growth", 59),
    ("3.3.4 Interest rate", 59),
    ("Integration", 61),
    ("4.1 The basic idea", 61),
    ("Fundamental Theorem of Calculus", 65),
    ("Indefinite integrals", 68),
    ("4.3.1 Substitution", 71),
    ("4.3.2 Trigonometric substitution", 75),
    ("4.3.3 Partial fractions", 77),
    ("4.3.4 Integration by parts", 78),
    ("Definite integrals", 80),
    ("Numerical integration", 82),
    ("4.5.1 Trapezium method", 82),
    ("Application of the definite integral", 86),
    ("4.6.1 Area bounded by curves", 86),
    ("4.6.2 Finding a distance by the integral of velocity", 89),
    ("Differential Equations", 90),
    ("First order differential equations", 91),
    ("5.1.1 Separation of variables", 91),
    ("5.1.2 Linear first-order differential equations", 94),
    ("Second-order linear differential equations with constant coefficients", 101),
    ("Simple Harmonic Motion (SHM)", 110),
    ("Solving initial-value problems numerically: Euler’s method", 114)
]


# Paths to the input and output PDF files
input_pdf_path = "yourfile.pdf"
output_pdf_path = "output_with_toc.pdf"

# Offset to adjust for the page number shift
offset = 4  # Since the first TOC page is 23 in the actual PDF, the offset is 23 - 1

# Read the input PDF
reader = PdfReader(input_pdf_path)
writer = PdfWriter()

# Copy all pages from the reader to the writer
for page in reader.pages:
    writer.add_page(page)

# Add bookmarks using add_outline_item with the offset
for title, page_num in toc_entries:
    writer.add_outline_item(title, page_num - 1 + offset)

# Write to the output PDF
with open(output_pdf_path, "wb") as f:
    writer.write(f)

print(f"Bookmarks added successfully. Output saved as {output_pdf_path}")
