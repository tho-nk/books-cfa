from PyPDF2 import PdfReader, PdfWriter

# https://chatgpt.com/share/a9520757-ba06-4c8a-945b-1d3c381eb6dc
# Define your TOC entries and their corresponding page numbers
toc_entries = [
    ("Results from One-Variable Calculus", 1),
    ("1.1 The Real Number System", 1),
    ("1.2 Foundational and Basic Theorems", 4),
    ("1.3 Taylor’s Theorem", 6),
    
    ("Part I Multivariable Differential Calculus", 23),
    
    ("2 Euclidean Space", 23),
    ("2.1 Algebra: Vectors", 23),
    ("2.2 Geometry: Length and Angle", 31),
    ("2.3 Analysis: Continuous Mappings", 41),
    ("2.4 Topology: Compact Sets and Continuity", 49),
    ("2.5 Review of the One-Variable Derivative", 57),
    ("2.6 Summary", 60),
    
    ("3 Linear Mappings and Their Matrices", 61),
    ("3.1 Linear Mappings", 62),
    ("3.2 Operations on Matrices", 73),
    ("3.3 The Inverse of a Linear Mapping", 79),
    ("3.4 Inhomogeneous Linear Equations", 88),
    ("3.5 The Determinant: Characterizing Properties and Their Consequences", 89),
    ("3.6 The Determinant: Uniqueness and Existence", 98),
    ("3.7 An Explicit Formula for the Inverse", 109),
    ("3.8 Geometry of the Determinant: Volume", 111),
    ("3.9 Geometry of the Determinant: Orientation", 120),
    ("3.10 The Cross Product, Lines, and Planes in R3", 123),
    ("3.11 Summary", 130),
    
    ("4 The Derivative", 131),
    ("4.1 Trying to Extend the Symbol-Pattern: Immediate, Irreparable Catastrophe", 132),
    ("4.2 New Environment: the Bachmann–Landau Notation", 132),
    ("4.3 One-Variable Revisionism; the Derivative Redefined", 139),
    ("4.4 Basic Results and the Chain Rule", 145),
    ("4.5 Calculating the Derivative", 152),
    ("4.6 Higher Order Derivatives", 163),
    ("4.7 Extreme Values", 169),
    ("4.8 Directional Derivatives and the Gradient", 179),
    ("4.9 Summary", 188),
    
    ("5 Inverse and Implicit Functions", 189),
    ("5.1 Preliminaries", 191),
    ("5.2 The Inverse Function Theorem", 196),
    ("5.3 The Implicit Function Theorem", 202),
    ("5.4 Lagrange Multipliers: Geometric Motivation and Specific Examples", 217),
    ("5.5 Lagrange Multipliers: Analytic Proof and General Examples", 227),
    ("5.6 Summary", 238),
    
    ("Part II Multivariable Integral Calculus", 241),
    
    ("6 Integration", 241),
    ("6.1 Machinery: Boxes, Partitions, and Sums", 241),
    ("6.2 Definition of the Integral", 251),
    ("6.3 Continuity and Integrability", 257),
    ("6.4 Integration of Functions of One Variable", 264),
    ("6.5 Integration Over Nonboxes", 271),
    ("6.6 Fubini’s Theorem", 280),
    ("6.7 Change of Variable", 293),
    ("6.8 Topological Preliminaries for the Change of Variable Theorem", 308),
    ("6.9 Proof of the Change of Variable Theorem", 316),
    ("6.10 Summary", 328),
    
    ("7 Approximation by Smooth Functions", 329),
    ("7.1 Spaces of Functions", 331),
    ("7.2 Pulse Functions", 336),
    ("7.3 Convolution", 338),
    ("7.4 Test Approximate Identity and Convolution", 344),
    ("7.5 Known-Integrable Functions", 350),
    ("7.6 Summary", 354),
    
    ("8 Parametrized Curves", 355),
    ("8.1 Euclidean Constructions and Two Curves", 355),
    ("8.2 Parametrized Curves", 364),
    ("8.3 Parametrization by Arc Length", 370),
    ("8.4 Plane Curves: Curvature", 373),
    ("8.5 Space Curves: Curvature and Torsion", 378),
    ("8.6 General Frenet Frames and Curvatures", 384),
    ("8.7 Summary", 388),
    
    ("9 Integration of Differential Forms", 389),
    ("9.1 Integration of Functions Over Surfaces", 390),
    ("9.2 Flow and Flux Integrals", 398),
    ("9.3 Differential Forms Syntactically and Operationally", 404),
    ("9.4 Examples: 1-forms", 407),
    ("9.5 Examples: 2-forms on R3", 411),
    ("9.6 Algebra of Forms: Basic Properties", 418),
    ("9.7 Algebra of Forms: Multiplication", 419),
    ("9.8 Algebra of Forms: Differentiation", 422),
    ("9.9 Algebra of Forms: the Pullback", 428),
    ("9.10 Change of Variable for Differential Forms", 439),
    ("9.11 Closed Forms, Exact Forms, and Homotopy", 441),
    ("9.12 Cubes and Chains", 447),
    ("9.13 Geometry of Chains: the Boundary Operator", 450),
    ("9.14 The General Fundamental Theorem of Integral Calculus", 457),
    ("9.15 Classical Change of Variable Revisited", 461),
    ("9.16 The Classical Theorems", 467),
    ("9.17 Divergence and Curl in Polar Coordinates", 473),
    ("9.18 Summary", 481),
    
    ("Index", 483)
]

# Paths to the input and output PDF files
input_pdf_path = "yourfile.pdf"
output_pdf_path = "output_with_toc.pdf"

# Offset to adjust for the page number shift
offset = 12  # Since the first TOC page is 23 in the actual PDF, the offset is 23 - 1

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
