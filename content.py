from PyPDF2 import PdfReader, PdfWriter

# https://chatgpt.com/share/a9520757-ba06-4c8a-945b-1d3c381eb6dc
# Define your TOC entries and their corresponding page numbers
toc_entries = [
    ("1 Introduction to Probability Theory", 11, [
        ("1.1 The Binomial Asset Pricing Model", 11, []),
        ("1.2 Finite Probability Spaces", 16, []),
        ("1.3 Lebesgue Measure and the Lebesgue Integral", 22, []),
        ("1.4 General Probability Spaces", 30, []),
        ("1.5 Independence", 40, [
            ("1.5.1 Independence of sets", 40, []),
            ("1.5.2 Independence of σ-algebras", 41, []),
            ("1.5.3 Independence of random variables", 42, []),
            ("1.5.4 Correlation and independence", 44, []),
            ("1.5.5 Independence and conditional expectation", 45, []),
            ("1.5.6 Law of Large Numbers", 46, []),
            ("1.5.7 Central Limit Theorem", 47, []),
        ]),
    ]),
    ("2 Conditional Expectation", 49, [
        ("2.1 A Binomial Model for Stock Price Dynamics", 49, []),
        ("2.2 Information", 50, []),
        ("2.3 Conditional Expectation", 52, [
            ("2.3.1 An example", 52, []),
            ("2.3.2 Definition of Conditional Expectation", 53, []),
            ("2.3.3 Further discussion of Partial Averaging", 54, []),
            ("2.3.4 Properties of Conditional Expectation", 55, []),
            ("2.3.5 Examples from the Binomial Model", 57, []),
        ]),
        ("2.4 Martingales", 58, []),
    ]),
    ("3 Arbitrage Pricing", 59, [
        ("3.1 Binomial Pricing", 59, []),
        ("3.2 General one-step APT", 60, []),
        ("3.3 Risk-Neutral Probability Measure", 61, [
            ("3.3.1 Portfolio Process", 62, []),
            ("3.3.2 Self-financing Value of a Portfolio Process", 62, []),
        ]),
        ("3.4 Simple European Derivative Securities", 63, []),
        ("3.5 The Binomial Model is Complete", 64, []),
    ]),
    ("4 The Markov Property", 67, [
        ("4.1 Binomial Model Pricing and Hedging", 67, []),
        ("4.2 Computational Issues", 69, []),
        ("4.3 Markov Processes", 70, [
            ("4.3.1 Different ways to write the Markov property", 70, []),
        ]),
        ("4.4 Showing that a process is Markov", 73, []),
        ("4.5 Application to Exotic Options", 74, []),
    ]),
    ("5 Stopping Times and American Options", 77, [
        ("5.1 American Pricing", 77, []),
        ("5.2 Value of Portfolio Hedging an American Option", 79, []),
        ("5.3 Information up to a Stopping Time", 81, []),
    ]),
    ("6 Properties of American Derivative Securities", 85, [
        ("6.1 The properties", 85, []),
        ("6.2 Proofs of the Properties", 86, []),
        ("6.3 Compound European Derivative Securities", 88, []),
        ("6.4 Optimal Exercise of American Derivative Security", 89, []),
    ]),
    ("7 Jensen’s Inequality", 91, [
        ("7.1 Jensen’s Inequality for Conditional Expectations", 91, []),
        ("7.2 Optimal Exercise of an American Call", 92, []),
        ("7.3 Stopped Martingales", 94, []),
    ]),
    ("8 Random Walks", 97, [
        ("8.1 First Passage Time", 97, []),
        ("8.2 ξ is almost surely finite", 97, []),
        ("8.3 The moment generating function for ξ", 99, []),
        ("8.4 Expectation of ξ", 100, []),
        ("8.5 The Strong Markov Property", 101, []),
        ("8.6 General First Passage Times", 101, []),
        ("8.7 Example: Perpetual American Put", 102, []),
        ("8.8 Difference Equation", 106, []),
        ("8.9 Distribution of First Passage Times", 107, []),
        ("8.10 The Reflection Principle", 109, []),
    ]),
    ("9 Pricing in terms of Market Probabilities: The Radon-Nikodym Theorem", 111, [
        ("9.1 Radon-Nikodym Theorem", 111, []),
        ("9.2 Radon-Nikodym Martingales", 112, []),
        ("9.3 The State Price Density Process", 113, []),
        ("9.4 Stochastic Volatility Binomial Model", 116, []),
        ("9.5 Another Application of the Radon-Nikodym Theorem", 118, []),
    ]),
    ("10 Capital Asset Pricing", 119, [
        ("10.1 An Optimization Problem", 119, []),
    ]),
    ("11 General Random Variables", 123, [
        ("11.1 Law of a Random Variable", 123, []),
        ("11.2 Density of a Random Variable", 123, []),
        ("11.3 Expectation", 124, []),
        ("11.4 Two random variables", 125, []),
        ("11.5 Marginal Density", 126, []),
        ("11.6 Conditional Expectation", 126, []),
        ("11.7 Conditional Density", 127, []),
        ("11.8 Multivariate Normal Distribution", 129, []),
        ("11.9 Bivariate normal distribution", 130, []),
        ("11.10 MGF of jointly normal random variables", 130, []),
    ]),
    ("12 Semi-Continuous Models", 131, [
        ("12.1 Discrete-time Brownian Motion", 131, []),
        ("12.2 The Stock Price Process", 132, []),
        ("12.3 Remainder of the Market", 133, []),
        ("12.4 Risk-Neutral Measure", 133, []),
        ("12.5 Risk-Neutral Pricing", 134, []),
        ("12.6 Arbitrage", 134, []),
        ("12.7 Stalking the Risk-Neutral Measure", 135, []),
        ("12.8 Pricing a European Call", 138, []),
    ]),
    ("13 Brownian Motion", 139, [
        ("13.1 Symmetric Random Walk", 139, []),
        ("13.2 The Law of Large Numbers", 139, []),
        ("13.3 Central Limit Theorem", 140, []),
        ("13.4 Brownian Motion as a Limit of Random Walks", 141, []),
        ("13.5 Brownian Motion", 142, []),
        ("13.6 Covariance of Brownian Motion", 143, []),
        ("13.7 Finite-Dimensional Distributions of Brownian Motion", 144, []),
        ("13.8 Filtration generated by a Brownian Motion", 144, []),
        ("13.9 Martingale Property", 145, []),
        ("13.10 The Limit of a Binomial Model", 145, []),
        ("13.11 Starting at Points Other Than 0", 147, []),
        ("13.12 Markov Property for Brownian Motion", 147, []),
        ("13.13 Transition Density", 149, []),
        ("13.14 First Passage Time", 149, []),
    ]),
    ("14 The Itô Integral", 153, [
        ("14.1 Brownian Motion", 153, []),
        ("14.2 First Variation", 153, []),
        ("14.3 Quadratic Variation", 155, []),
        ("14.4 Quadratic Variation as Absolute Volatility", 157, []),
        ("14.5 Construction of the Itô Integral", 158, []),
        ("14.6 Itô integral of an elementary integrand", 158, []),
        ("14.7 Properties of the Itô integral of an elementary process", 159, []),
        ("14.8 Itô integral of a general integrand", 162, []),
        ("14.9 Properties of the (general) Itô integral", 163, []),
        ("14.10 Quadratic variation of an Itô integral", 165, []),
    ]),
    ("15 Itô’s Formula", 167, [
        ("15.1 Itô’s formula for one Brownian motion", 167, []),
        ("15.2 Derivation of Itô’s formula", 168, []),
        ("15.3 Geometric Brownian motion", 169, []),
        ("15.4 Quadratic variation of geometric Brownian motion", 170, []),
        ("15.5 Volatility of Geometric Brownian motion", 170, []),
        ("15.6 First derivation of the Black-Scholes formula", 170, []),
        ("15.7 Mean and variance of the Cox-Ingersoll-Ross process", 172, []),
        ("15.8 Multidimensional Brownian Motion", 173, []),
        ("15.9 Cross-variations of Brownian motions", 174, []),
        ("15.10 Multi-dimensional Itô formula", 175, []),
    ]),
    ("16 Markov processes and the Kolmogorov equations", 177, [
        ("16.1 Stochastic Differential Equations", 177, []),
        ("16.2 Markov Property", 178, []),
        ("16.3 Transition density", 179, []),
        ("16.4 The Kolmogorov Backward Equation", 180, []),
        ("16.5 Connection between stochastic calculus and KBE", 181, []),
        ("16.6 Black-Scholes", 183, []),
        ("16.7 Black-Scholes with price-dependent volatility", 186, []),
    ]),
    ("17 Girsanov’s theorem and the risk-neutral measure", 189, [
        ("17.1 Conditional expectations under IP", 191, []),
        ("17.2 Risk-neutral measure", 193, []),
    ]),
    ("18 Martingale Representation Theorem", 197, [
        ("18.1 Martingale Representation Theorem", 197, []),
        ("18.2 A hedging application", 197, []),
        ("18.3 d-dimensional Girsanov Theorem", 199, []),
        ("18.4 d-dimensional Martingale Representation Theorem", 200, []),
        ("18.5 Multi-dimensional market model", 200, []),
    ]),
    ("19 A two-dimensional market model", 203, [
        ("19.1 Hedging when φ < 1", 204, []),
        ("19.2 Hedging when φ = 1", 205, []),
    ]),
    ("20 Pricing Exotic Options", 209, [
        ("20.1 Reflection principle for Brownian motion", 209, []),
        ("20.2 Up and out European call", 212, []),
        ("20.3 A practical issue", 218, []),
    ]),
    ("21 Asian Options", 219, [
        ("21.1 Feynman-Kac Theorem", 220, []),
        ("21.2 Constructing the hedge", 220, []),
        ("21.3 Partial average payoff Asian option", 221, []),
    ]),
    ("22 Summary of Arbitrage Pricing Theory", 223, [
        ("22.1 Binomial model, Hedging Portfolio", 223, []),
        ("22.2 Setting up the continuous model", 225, []),
        ("22.3 Risk-neutral pricing and hedging", 227, []),
        ("22.4 Implementation of risk-neutral pricing and hedging", 229, []),
    ]),
    ("23 Recognizing a Brownian Motion", 233, [
        ("23.1 Identifying volatility and correlation", 235, []),
        ("23.2 Reversing the process", 236, []),
    ]),
    ("24 An outside barrier option", 239, [
        ("24.1 Computing the option value", 242, []),
        ("24.2 The PDE for the outside barrier option", 243, []),
        ("24.3 The hedge", 245, []),
    ]),
    ("25 American Options", 247, [
        ("25.1 Preview of perpetual American put", 247, []),
        ("25.2 First passage times for Brownian motion: first method", 247, []),
        ("25.3 Drift adjustment", 249, []),
        ("25.4 Drift-adjusted Laplace transform", 250, []),
        ("25.5 First passage times: Second method", 251, []),
        ("25.6 Perpetual American put", 252, []),
        ("25.7 Value of the perpetual American put", 256, []),
        ("25.8 Hedging the put", 257, []),
        ("25.9 Perpetual American contingent claim", 259, []),
        ("25.10 Perpetual American call", 259, []),
        ("25.11 Put with expiration", 260, []),
        ("25.12 American contingent claim with expiration", 261, []),
    ]),
    ("26 Options on dividend-paying stocks", 263, [
        ("26.1 American option with convex payoff function", 263, []),
        ("26.2 Dividend paying stock", 264, []),
        ("26.3 Hedging at time t", 266, []),
    ]),
    ("27 Bonds, forward contracts and futures", 267, [
        ("27.1 Forward contracts", 269, []),
        ("27.2 Hedging a forward contract", 269, []),
        ("27.3 Future contracts", 270, []),
        ("27.4 Cash flow from a future contract", 272, []),
        ("27.5 Forward-future spread", 272, []),
        ("27.6 Backwardation and contango", 273, []),
    ]),
    ("28 Term-structure models", 275, [
        ("28.1 Computing arbitrage-free bond prices: first method", 276, []),
        ("28.2 Some interest-rate dependent assets", 276, []),
        ("28.3 Terminology", 277, []),
        ("28.4 Forward rate agreement", 277, []),
        ("28.5 Recovering the interest r (t) from the forward rate", 278, []),
        ("28.6 Computing arbitrage-free bond prices: Heath-Jarrow-Morton method", 279, []),
        ("28.7 Checking for absence of arbitrage", 280, []),
        ("28.8 Implementation of the Heath-Jarrow-Morton model", 281, []),
    ]),
    ("29 Gaussian processes", 285, [
        ("29.1 An example: Brownian Motion", 286, []),
    ]),
    ("30 Hull and White model", 293, [
        ("30.1 Fiddling with the formulas", 295, []),
        ("30.2 Dynamics of the bond price", 296, []),
        ("30.3 Calibration of the Hull & White model", 297, []),
        ("30.4 Option on a bond", 299, []),
    ]),
    ("31 Cox-Ingersoll-Ross model", 303, [
        ("31.1 Equilibrium distribution of r (t)", 306, []),
        ("31.2 Kolmogorov forward equation", 306, []),
        ("31.3 Cox-Ingersoll-Ross equilibrium density", 309, []),
        ("31.4 Bond prices in the CIR model", 310, []),
        ("31.5 Option on a bond", 313, []),
        ("31.6 Deterministic time change of CIR model", 313, []),
        ("31.7 Calibration", 315, []),
        ("31.8 Tracking down ' (0) in the time change of the CIR model", 316, []),
    ]),
    ("32 A two-factor model (Duffie & Kan)", 319, [
        ("32.1 Non-negativity of Y", 320, []),
        ("32.2 Zero-coupon bond prices", 321, []),
        ("32.3 Calibration", 323, []),
    ]),
    ("33 Change of numéraire", 325, [
        ("33.1 Bond price as numéraire", 327, []),
        ("33.2 Stock price as numéraire", 328, []),
        ("33.3 Merton option pricing formula", 329, []),
    ]),
    ("34 Brace-Gatarek-Musiela model", 335, [
        ("34.1 Review of HJM under risk-neutral IP", 335, []),
        ("34.2 Brace-Gatarek-Musiela model", 336, []),
        ("34.3 LIBOR", 337, []),
        ("34.4 Forward LIBOR", 338, []),
        ("34.5 The dynamics of L(t; ξ)", 338, []),
        ("34.6 Implementation of BGM", 340, []),
        ("34.7 Bond prices", 342, []),
        ("34.8 Forward LIBOR under more forward measure", 343, []),
        ("34.9 Pricing an interest rate caplet", 343, []),
        ("34.10 Pricing an interest rate cap", 345, []),
        ("34.11 Calibration of BGM", 345, []),
        ("34.12 Long rates", 346, []),
        ("34.13 Pricing a swap", 346, []),
    ]),
]





# Paths to the input and output PDF files
input_pdf_path = "yourfile.pdf"
output_pdf_path = "output_with_toc.pdf"

# Offset to adjust for the page number shift
offset = 2  # Since the first TOC page is 23 in the actual PDF, the offset is 23 - 1

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