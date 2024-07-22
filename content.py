from PyPDF2 import PdfReader, PdfWriter

# https://chatgpt.com/share/a9520757-ba06-4c8a-945b-1d3c381eb6dc
# Define your TOC entries and their corresponding page numbers
toc_entries = [
    ("1. General Probability Theory", 1, [
        ("1.1 Infinite Probability Spaces", 1, []),
        ("1.2 Random Variables and Distributions", 7, []),
        ("1.3 Expectations", 13, []),
        ("1.4 Convergence of Integrals", 23, []),
        ("1.5 Computation of Expectations", 27, []),
        ("1.6 Change of Measure", 32, []),
        ("1.7 Summary", 39, []),
        ("1.8 Notes", 41, []),
        ("1.9 Exercises", 41, [])
    ]),
    ("2. Information and Conditioning", 49, [
        ("2.1 Information and u-algebras", 49, []),
        ("2.2 Independence", 53, []),
        ("2.3 General Conditional Expectations", 66, []),
        ("2.4 Summary", 75, []),
        ("2.5 Notes", 77, []),
        ("2.6 Exercises", 77, [])
    ]),
    ("3. Brownian Motion", 83, [
        ("3.1 Introduction", 83, []),
        ("3.2 Scaled Random Walks", 83, [
            ("3.2.1 Symmetric Random Walk", 83, []),
            ("3.2.2 Increments of the Symmetric Random Walk", 84, []),
            ("3.2.3 Martingale Property for the Symmetric Random Walk", 85, []),
            ("3.2.4 Quadratic Variation of the Symmetric Random Walk", 85, []),
            ("3.2.5 Scaled Symmetric Random Walk", 86, []),
            ("3.2.6 Limiting Distribution of the Scaled Random Walk", 88, []),
            ("3.2.7 Log-Normal Distribution as the Limit of the Binomial Model", 91, [])
        ]),
        ("3.3 Brownian Motion", 93, [
            ("3.3.1 Definition of Brownian Motion", 93, []),
            ("3.3.2 Distribution of Brownian Motion", 95, []),
            ("3.3.3 Filtration for Brownian Motion", 97, []),
            ("3.3.4 Martingale Property for Brownian Motion", 98, [])
        ]),
        ("3.4 Quadratic Variation", 99, [
            ("3.4.1 First-Order Variation", 99, []),
            ("3.4.2 Quadratic Variation", 101, []),
            ("3.4.3 Volatility of Geometric Brownian Motion", 106, [])
        ]),
        ("3.5 Markov Property", 107, []),
        ("3.6 First Passage Time Distribution", 108, []),
        ("3.7 Reflection Principle", 111, [
            ("3.7.1 Reflection Equality", 111, []),
            ("3.7.2 First Passage Time Distribution", 112, []),
            ("3.7.3 Distribution of Brownian Motion and Its Maximum", 113, [])
        ]),
        ("3.8 Summary", 115, [])
    ]),
    ("4. Stochastic Calculus", 125, [
        ("4.1 Introduction", 125, []),
        ("4.2 Ito's Integral for Simple Integrands", 126, [
            ("4.2.1 Construction of the Integral", 126, []),
            ("4.2.2 Properties of the Integral", 128, [])
        ]),
        ("4.3 Ito's Integral for General Integrands", 132, []),
        ("4.4 Ito-Doeblin Formula", 137, [
            ("4.4.1 Formula for Brownian Motion", 137, []),
            ("4.4.2 Formula for Ito Processes", 143, []),
            ("4.4.3 Examples", 147, [])
        ]),
        ("4.5 Black-Scholes-Merton Equation", 154, [
            ("4.5.1 Evolution of Portfolio Value", 154, []),
            ("4.5.2 Evolution of Option Value", 155, []),
            ("4.5.3 Equating the Evolutions", 156, []),
            ("4.5.4 Solution to the Black-Scholes-Merton Equation", 158, []),
            ("4.5.5 The Greeks", 159, []),
            ("4.5.6 Put-Call Parity", 162, [])
        ]),
        ("4.6 Multivariable Stochastic Calculus", 164, [
            ("4.6.1 Multiple Brownian Motions", 164, []),
            ("4.6.2 Ito-Doeblin Formula for Multiple Processes", 165, []),
            ("4.6.3 Recognizing a Brownian Motion", 168, [])
        ]),
        ("4.7 Brownian Bridge", 172, [
            ("4.7.1 Gaussian Processes", 172, []),
            ("4.7.2 Brownian Bridge as a Gaussian Process", 175, []),
            ("4.7.3 Brownian Bridge as a Scaled Stochastic Integral", 176, []),
            ("4.7.4 Multidimensional Distribution of the Brownian Bridge", 178, []),
            ("4.7.5 Brownian Bridge as a Conditioned Brownian Motion", 182, [])
        ]),
        ("4.8 Summary", 183, [])
    ]),
    ("5. Risk-Neutral Pricing", 209, [
        ("5.1 Introduction", 209, []),
        ("5.2 Risk-Neutral Measure", 210, [
            ("5.2.1 Girsanov's Theorem for a Single Brownian Motion", 210, []),
            ("5.2.2 Stock Under the Risk-Neutral Measure", 214, []),
            ("5.2.3 Value of Portfolio Process Under the Risk-Neutral Measure", 217, []),
            ("5.2.4 Pricing Under the Risk-Neutral Measure", 218, []),
            ("5.2.5 Deriving the Black-Scholes-Merton Formula", 218, [])
        ]),
        ("5.3 Martingale Representation Theorem", 221, [
            ("5.3.1 Martingale Representation with One Brownian Motion", 221, []),
            ("5.3.2 Hedging with One Stock", 222, [])
        ]),
        ("5.4 Fundamental Theorems of Asset Pricing", 224, [
            ("5.4.1 Girsanov and Martingale Representation Theorems", 224, []),
            ("5.4.2 Multidimensional Market Model", 226, []),
            ("5.4.3 Existence of the Risk-Neutral Measure", 228, []),
            ("5.4.4 Uniqueness of the Risk-Neutral Measure", 231, [])
        ]),
        ("5.5 Dividend-Paying Stocks", 235, [
            ("5.5.1 Continuously Paying Dividend", 235, []),
            ("5.5.2 Continuously Paying Dividend with Constant Coefficients", 237, []),
            ("5.5.3 Lump Payments of Dividends", 238, []),
            ("5.5.4 Lump Payments of Dividends with Constant Coefficients", 239, [])
        ]),
        ("5.6 Forwards and Futures", 240, [
            ("5.6.1 Forward Contracts", 240, []),
            ("5.6.2 Futures Contracts", 241, []),
            ("5.6.3 Forward-Futures Spread", 247, [])
        ]),
        ("5.7 Summary", 248, []),
        ("5.8 Notes", 250, []),
        ("5.9 Exercises", 251, [])
    ]),
    ("6. Connections with Partial Differential Equations", 263, [
        ("6.1 Introduction", 263, []),
        ("6.2 Stochastic Differential Equations", 263, []),
        ("6.3 The Markov Property", 266, []),
        ("6.4 Partial Differential Equations", 268, []),
        ("6.5 Interest Rate Models", 272, []),
        ("6.6 Multidimensional Feynman-Kac Theorems", 277, []),
        ("6.7 Summary", 280, []),
        ("6.8 Notes", 281, []),
        ("6.9 Exercises", 282, [])
    ]),
    ("7. Exotic Options", 295, [
        ("7.1 Introduction", 295, []),
        ("7.2 Maximum of Brownian Motion with Drift", 295, []),
        ("7.3 Knock-Out Barrier Options", 300, [
            ("7.3.1 Up-and-Out Call", 300, []),
            ("7.3.2 Black-Scholes-Merton Equation", 300, []),
            ("7.3.3 Computation of the Price of the Up-and-Out Call", 304, [])
        ]),
        ("7.4 Lookback Options", 308, [
            ("7.4.1 Floating Strike Lookback Option", 308, []),
            ("7.4.2 Black-Scholes-Merton Equation", 309, []),
            ("7.4.3 Reduction of Dimension", 312, []),
            ("7.4.4 Computation of the Price of the Lookback Option", 314, [])
        ]),
        ("7.5 Asian Options", 320, [
            ("7.5.1 Fixed-Strike Asian Call", 320, []),
            ("7.5.2 Augmentation of the State", 321, []),
            ("7.5.3 Change of Numeraire", 323, [])
        ]),
        ("7.6 Summary", 331, []),
        ("7.7 Notes", 331, []),
        ("7.8 Exercises", 332, [])
    ]),
    ("8. American Derivative Securities", 339, [
        ("8.1 Introduction", 339, []),
        ("8.2 Stopping Times", 340, []),
        ("8.3 Perpetual American Put", 345, [
            ("8.3.1 Price Under Arbitrary Exercise", 345, []),
            ("8.3.2 Price Under Optimal Exercise", 349, []),
            ("8.3.3 Analytical Characterization of the Put Price", 351, []),
            ("8.3.4 Probabilistic Characterization of the Put Price", 353, [])
        ]),
        ("8.4 Finite-Expiration American Put", 356, [
            ("8.4.1 Analytical Characterization of the Put Price", 356, []),
            ("8.4.2 Probabilistic Characterization of the Put Price", 359, [])
        ]),
        ("8.5 American Call", 361, [
            ("8.5.1 Underlying Asset Pays No Dividends", 361, []),
            ("8.5.2 Underlying Asset Pays Dividends", 363, [])
        ]),
        ("8.6 Summary", 368, []),
        ("8.7 Notes", 369, []),
        ("8.8 Exercises", 370, [])
    ]),
    ("9. Change of Numeraire", 375, [
        ("9.1 Introduction", 375, []),
        ("9.2 Numeraire", 376, []),
        ("9.3 Foreign and Domestic Risk-Neutral Measures", 381, [
            ("9.3.1 The Basic Processes", 381, []),
            ("9.3.2 Domestic Risk-Neutral Measure", 381, []),
            ("9.3.3 Foreign Risk-Neutral Measure", 383, []),
            ("9.3.4 Siegel's Exchange Rate Paradox", 385, []),
            ("9.3.5 Forward Exchange Rates", 387, []),
            ("9.3.6 Garman-Kohlhagen Formula", 388, []),
            ("9.3.7 Exchange Rate Put-Call Duality", 390, [])
        ]),
        ("9.4 Summary", 392, []),
        ("9.5 Notes", 392, []),
        ("9.6 Exercises", 394, [])
    ]),
    ("10. Term-Structure Models", 403, [
        ("10.1 Introduction", 403, []),
        ("10.2 Affine-Yield Models", 420, [
            ("10.2.1 Two-Factor Vasicek Model", 420, []),
            ("10.2.2 Two-Factor CIR Model", 420, []),
            ("10.2.3 Mixed Model", 422, [])
        ]),
        ("10.3 Heath-Jarrow-Morton Model", 423, [
            ("10.3.1 Forward Rates", 423, []),
            ("10.3.2 Dynamics of Forward Rates and Bond Prices", 425, []),
            ("10.3.3 No-Arbitrage Condition", 426, []),
            ("10.3.4 HJM Under Risk-Neutral Measure", 429, []),
            ("10.3.5 Relation to Affine-Yield Models", 430, []),
            ("10.3.6 Implementation of HJM", 432, [])
        ]),
        ("10.4 Forward LIBOR Model", 435, [
            ("10.4.1 The Problem with Forward Rates", 435, []),
            ("10.4.2 LIBOR and Forward LIBOR", 436, []),
            ("10.4.3 Pricing a Backset LIBOR Contract", 437, []),
            ("10.4.4 Black Caplet Formula", 438, []),
            ("10.4.5 Forward LIBOR and Zero-Coupon Bond Volatilities", 440, []),
            ("10.4.6 A Forward LIBOR Term-Structure Model", 442, [])
        ]),
        ("10.5 Summary", 447, []),
        ("10.6 Notes", 450, []),
        ("10.7 Exercises", 451, [])
    ]),
    ("11. Introduction to Jump Processes", 461, [
        ("11.1 Introduction", 461, []),
        ("11.2 Poisson Process", 462, [
            ("11.2.1 Exponential Random Variables", 462, []),
            ("11.2.2 Construction of a Poisson Process", 463, []),
            ("11.2.3 Distribution of Poisson Process Increments", 463, []),
            ("11.2.4 Mean and Variance of Poisson Increments", 466, []),
            ("11.2.5 Martingale Property", 467, [])
        ]),
        ("11.3 Compound Poisson Process", 468, [
            ("11.3.1 Construction of a Compound Poisson Process", 468, []),
            ("11.3.2 Moment-Generating Function", 470, [])
        ]),
        ("11.4 Jump Processes and Their Integrals", 474, [
            ("11.4.1 Jump Processes", 474, []),
            ("11.4.2 Quadratic Variation", 479, [])
        ]),
        ("11.5 Stochastic Calculus for Jump Processes", 483, [
            ("11.5.1 Ito-Doeblin Formula for One Jump Process", 483, []),
            ("11.5.2 Ito-Doeblin Formula for Multiple Jump Processes", 489, [])
        ]),
        ("11.6 Change of Measure", 492, [
            ("11.6.1 Change of Measure for a Poisson Process", 492, []),
            ("11.6.2 Change of Measure for a Compound Poisson Process", 495, []),
            ("11.6.3 Change of Measure for a Compound Poisson Process and a Brownian Motion", 502, [])
        ]),
        ("11.7 Pricing a European Call in a Jump Model", 505, [
            ("11.7.1 Asset Driven by a Poisson Process", 505, []),
            ("11.7.2 Asset Driven by a Brownian Motion and a Compound Poisson Process", 512, [])
        ]),
        ("11.8 Summary", 523, []),
        ("11.9 Notes", 525, []),
        ("11.10 Exercises", 525, [])
    ]),
    ("A. Advanced Topics in Probability Theory", 527, [
        ("A.1 Countable Additivity", 527, []),
        ("A.2 Generating u-algebras", 530, []),
        ("A.3 Random Variable with Neither Density nor Probability Mass Function", 531, [])
    ]),
    ("B. Existence of Conditional Expectations", 533, []),
    ("C. Completion of the Proof of the Second Fundamental Theorem of Asset Pricing", 535, []),
    ("References", 537, []),
    ("Index", 545, [])
]





# Paths to the input and output PDF files
input_pdf_path = "yourfile.pdf"
output_pdf_path = "output_with_toc.pdf"

# Offset to adjust for the page number shift
offset = 20  # Since the first TOC page is 23 in the actual PDF, the offset is 23 - 1

# Read the input PDF
reader = PdfReader(input_pdf_path)
writer = PdfWriter()

# Copy all pages from the reader to the writer
# Copy all pages from the reader to the writer
for page in reader.pages:
    writer.add_page(page)

# Function to recursively add bookmarks
def add_bookmarks(writer, toc_entries, parent=None):
    for title, page_num, children in toc_entries:
        # Adjust page number for zero-based index
        page_index = page_num - 1 + offset
        # Add the current bookmark
        current = writer.add_outline_item(title, page_index, parent)
        # Add children recursively
        if children:
            add_bookmarks(writer, children, current)

# Add the hierarchical bookmarks
add_bookmarks(writer, toc_entries)

# Write to the output PDF
with open(output_pdf_path, "wb") as f:
    writer.write(f)

print(f"Bookmarks added successfully. Output saved as {output_pdf_path}")