from PyPDF2 import PdfReader, PdfWriter

# Define your TOC entries and their corresponding page numbers
toc_entries = [
    ("Chapter 1. Introduction", 1),
    ("1.1 Exchange-traded markets", 2),
    ("1.2 Over-the-counter markets", 3),
    ("1.3 Forward contracts", 5),
    ("1.4 Futures contracts", 7),
    ("1.5 Options", 7),
    ("1.6 Types of traders", 9),
    ("1.7 Hedgers", 10),
    ("1.8 Speculators", 13),
    ("1.9 Arbitrageurs", 15),
    ("1.10 Dangers", 16),
    ("Summary", 16),
    ("Further reading", 18),
    ("Practice questions", 18),
    ("Further questions", 20),

    ("Chapter 2. Mechanics of futures markets", 22),
    ("2.1 Background", 22),
    ("2.2 Specification of a futures contract", 24),
    ("2.3 Convergence of futures price to spot price", 26),
    ("2.4 The operation of margins", 27),
    ("2.5 OTC markets", 30),
    ("2.6 Market quotes", 33),
    ("2.7 Delivery", 36),
    ("2.8 Types of traders and types of orders", 37),
    ("2.9 Regulation", 38),
    ("2.10 Accounting and tax", 39),
    ("2.11 Forward vs. futures contracts", 41),
    ("Summary", 42),
    ("Further reading", 43),
    ("Practice questions", 43),
    ("Further questions", 45),

    ("Chapter 3. Hedging strategies using futures", 47),
    ("3.1 Basic principles", 47),
    ("3.2 Arguments for and against hedging", 49),
    ("3.3 Basis risk", 52),
    ("3.4 Cross hedging", 56),
    ("3.5 Stock index futures", 60),
    ("3.6 Stack and roll", 65),
    ("Summary", 67),
    ("Further reading", 68),
    ("Practice questions", 69),
    ("Further questions", 71),

    ("Appendix: Capital asset pricing model", 73),

    ("Chapter 4. Interest rates", 75),
    ("4.1 Types of rates", 75),
    ("4.2 Measuring interest rates", 77),
    ("4.3 Zero rates", 80),
    ("4.4 Bond pricing", 80),
    ("4.5 Determining Treasury zero rates", 82),
    ("4.6 Forward rates", 84),
    ("4.7 Forward rate agreements", 86),
    ("4.8 Duration", 89),
    ("4.9 Convexity", 92),
    ("4.10 Theories of the term structure of interest rates", 93),
    ("Summary", 96),
    ("Further reading", 97),
    ("Practice questions", 97),
    ("Further questions", 99),

    ("Chapter 5. Determination of forward and futures prices", 101),
    ("5.1 Investment assets vs. consumption assets", 101),
    ("5.2 Short selling", 102),
    ("5.3 Assumptions and notation", 103),
    ("5.4 Forward price for an investment asset", 104),
    ("5.5 Known income", 107),
    ("5.6 Known yield", 109),
    ("5.7 Valuing forward contracts", 109),
    ("5.8 Are forward prices and futures prices equal?", 111),
    ("5.9 Futures prices of stock indices", 112),
    ("5.10 Forward and futures contracts on currencies", 114),
    ("5.11 Futures on commodities", 117),
    ("5.12 The cost of carry", 120),
    ("5.13 Delivery options", 121),
    ("5.14 Futures prices and the expected future spot price", 121),
    ("Summary", 123),
    ("Further reading", 125),
    ("Practice questions", 125),
    ("Further questions", 127),

    ("Chapter 6. Interest rate futures", 129),
    ("6.1 Day count and quotation conventions", 129),
    ("6.2 Treasury bond futures", 132),
    ("6.3 Eurodollar futures", 137),
    ("6.4 Duration-based hedging strategies using futures", 142),
    ("6.5 Hedging portfolios of assets and liabilities", 143),
    ("Summary", 144),
    ("Further reading", 145),
    ("Practice questions", 145),
    ("Further questions", 147),

    ("Chapter 7. Swaps", 148),
    ("7.1 Mechanics of interest rate swaps", 148),
    ("7.2 Day count issues", 154),
    ("7.3 Confirmations", 155),
    ("7.4 The comparative-advantage argument", 156),
    ("7.5 The nature of swap rates", 158),
    ("7.6 Determining the LIBOR/swap zero rates", 159),
    ("7.7 Valuation of interest rate swaps", 160),
    ("7.8 Overnight indexed swaps", 164),
    ("7.9 Currency swaps", 165),
    ("7.10 Valuation of currency swaps", 168),
    ("7.11 Credit risk", 171),
    ("7.12 Other types of swaps", 173),
    ("Summary", 175),
    ("Further reading", 176),
    ("Practice questions", 176),
    ("Further questions", 178),

    ("Chapter 8. Securitization and the Credit Crisis of 2007", 180),
    ("8.1 Securitization", 180),
    ("8.2 The US housing market", 184),
    ("8.3 What went wrong?", 188),
    ("8.4 The aftermath", 190),
    ("Summary", 191),
    ("Further reading", 192),
    ("Practice questions", 193),
    ("Further questions", 193),

    ("Chapter 9. Mechanics of options markets", 194),
    ("9.1 Types of options", 194),
    ("9.2 Option positions", 196),
    ("9.3 Underlying assets", 198),
    ("9.4 Specification of stock options", 199),
    ("9.5 Trading", 203),
    ("9.6 Commissions", 204),
    ("9.7 Margins", 205),
    ("9.8 The options clearing corporation", 206),
    ("9.9 Regulation", 207),
    ("9.10 Taxation", 207),
    ("9.11 Warrants, employee stock options, and convertibles", 209),
    ("9.12 Over-the-counter markets", 210),
    ("Summary", 210),
    ("Further reading", 211),
    ("Practice questions", 211),
    ("Further questions", 213),

    ("Chapter 10. Properties of stock options", 214),
    ("10.1 Factors affecting option prices", 214),
    ("10.2 Assumptions and notation", 218),
    ("10.3 Upper and lower bounds for option prices", 218),
    ("10.4 Put–call parity", 221),
    ("10.5 Calls on a non-dividend-paying stock", 225),
    ("10.6 Puts on a non-dividend-paying stock", 226),
    ("10.7 Effect of dividends", 229),
    ("Summary", 230),
    ("Further reading", 231),
    ("Practice questions", 231),
    ("Further questions", 233),

    ("Chapter 11. Trading strategies involving options", 234),
    ("11.1 Principal-protected notes", 234),
    ("11.2 Trading an option and the underlying asset", 236),
    ("11.3 Spreads", 238),
    ("11.4 Combinations", 246),
    ("11.5 Other payoffs", 249),
    ("Summary", 249),
    ("Further reading", 250),
    ("Practice questions", 250),
    ("Further questions", 252),

    ("Chapter 12. Binomial trees", 253),
    ("12.1 A one-step binomial model and a no-arbitrage argument", 253),
    ("12.2 Risk-neutral valuation", 257),
    ("12.3 Two-step binomial trees", 259),
    ("12.4 A put example", 262),
    ("12.5 American options", 263),
    ("12.6 Delta", 264),
    ("12.7 Matching volatility with u and d", 265),
    ("12.8 The binomial tree formulas", 267),
    ("12.9 Increasing the number of steps", 268),
    ("12.10 Using DerivaGem", 269),
    ("12.11 Options on other assets", 269),
    ("Summary", 272),
    ("Further reading", 273),
    ("Practice questions", 274),
    ("Further questions", 275),

    ("Chapter 13. Wiener processes and Itoˆ ’s lemma", 280),
    ("13.1 The Markov property", 280),
    ("13.2 Continuous-time stochastic processes", 281),
    ("13.3 The process for a stock price", 286),
    ("13.4 The parameters", 289),
    ("13.5 Correlated processes", 290),
    ("13.6 Itoˆ ’s lemma", 291),
    ("13.7 The lognormal property", 292),
    ("Summary", 293),
    ("Further reading", 294),
    ("Practice questions", 294),
    ("Further questions", 295),

    ("Chapter 14. The Black–Scholes–Merton model", 299),
    ("14.1 Lognormal property of stock prices", 300),
    ("14.2 The distribution of the rate of return", 301),
    ("14.3 The expected return", 302),
    ("14.4 Volatility", 303),
    ("14.5 The idea underlying the Black–Scholes–Merton differential equation", 307),
    ("14.6 Derivation of the Black–Scholes–Merton differential equation", 309),
    ("14.7 Risk-neutral valuation", 311),
    ("14.8 Black–Scholes–Merton pricing formulas", 313),
    ("14.9 Cumulative normal distribution function", 315),
    ("14.10 Warrantsandemployeestockoptions", 316),
    ("14.11 Implied volatilities", 318),
    ("14.12 Dividends", 320),
    ("Summary", 323),
    ("Further reading", 324),
    ("Practice questions", 325),
    ("Further questions", 328),

    ("Chapter 15. Employee stock options", 332),
    ("15.1 Contractual arrangements", 332),
    ("15.2 Do options align the interests of shareholders and managers?", 334),
    ("15.3 Accounting issues", 335),
    ("15.4 Valuation", 336),
    ("15.5 Backdating scandals", 341),
    ("Summary", 342),
    ("Further reading", 343),
    ("Practice questions", 343),
    ("Further questions", 344),

    ("Chapter 16. Options on stock indices and currencies", 345),
    ("16.1 Options on stock indices", 345),
    ("16.2 Currency options", 347),
    ("16.3 Options on stocks paying known dividend yields", 350),
    ("16.4 Valuation of European stock index options", 352),
    ("16.5 Valuation of European currency options", 355),
    ("16.6 American options", 356),
    ("Summary", 357),
    ("Further reading", 357),
    ("Practice questions", 358),
    ("Further questions", 360),

    ("Chapter 17. Futures options", 361),
    ("17.1 Nature of futures options", 361),
    ("17.2 Reasons for the popularity of futures options", 364),
    ("17.3 European spot and futures options", 364),
    ("17.4 Put–call parity", 365),
    ("17.5 Bounds for futures options", 366),
    ("17.6 Valuation of futures options using binomial trees", 367),
    ("17.7 Drift of a futures prices in a risk-neutral world", 369),
    ("17.8 Black’s model for valuing futures options", 370),
    ("17.9 American futures options vs. American spot options", 372),
    ("17.10 Futures-styleoptions", 372),
    ("Summary", 373),
    ("Further reading", 374),
    ("Practice questions", 374),
    ("Further questions", 376),

    ("Chapter 18. The Greek letters", 377),
    ("18.1 Illustration", 377),
    ("18.2 Naked and covered positions", 378),
    ("18.3  A stop-loss strategy", 378),
    ("18.4 Delta hedging", 380),
    ("18.5 Theta", 387),
    ("18.6 Gamma", 389),
    ("18.7 Relationship between delta, theta, and gamma", 392),
    ("18.8 Vega", 393),
    ("18.9 Rho", 395),
    ("18.10 The realities of hedging", 396),
    ("18.11 Scenario analysis", 397),
    ("18.12 Extension of formulas", 397),
    ("18.13 Portfolioinsurance", 400),
    ("18.14 Stock market volatility", 402),
    ("Summary", 402),
    ("Further reading", 404),
    ("Practice questions", 404),
    ("Further questions", 406),

    ("Appendix: Taylor series expansions and hedge parameters", 408),

    ("Chapter 19. Volatility smiles", 409),
    ("19.1 Why the volatility smile is the same for calls and puts", 409),
    ("19.2 Foreign currency options", 411),
    ("19.3 Equity options", 414),
    ("19.4 Alternative ways of characterizing the volatility smile", 415),
    ("19.5 The volatility term structure and volatility surfaces", 416),
    ("19.6 Greek letters", 417),
    ("19.7 The role of the model", 418),
    ("19.8 When a single large jump is anticipated", 419),
    ("Summary", 420),
    ("Further reading", 421),
    ("Practice questions", 421),
    ("Further questions", 423),

    ("Appendix: Determining implied risk-neutral distributions from volatility smiles", 424),
    ("Chapter 20. Basic numerical procedures", 427),
    ("20.1 Binomial trees", 427),
    ("20.2 Using the binomial tree for options on indices, currencies, and futures contracts", 435),
    ("20.3 Binomial model for a dividend-paying stock", 437),
    ("20.4 Alternative procedures for constructing trees", 442),
    ("20.5 Time-dependent parameters", 445),
    ("20.6 Monte Carlo simulation", 446),
    ("20.7 Variance reduction procedures", 452),
    ("20.8 Finite difference methods", 455),
    ("Summary", 466),
    ("Further reading", 466),
    ("Practice questions", 467),
    ("Further questions", 469),

    ("Chapter 21. Value at risk", 471),
    ("21.1 The VaR measure", 471),
    ("21.2 Historical simulation", 474),
    ("21.3 Model-building approach", 478),
    ("21.4 Linear model", 481),
    ("21.5 Quadratic model", 486),
    ("21.6 Monte Carlo simulation", 488),
    ("21.7 Comparison of approaches", 489),
    ("21.8 Stress testing and back testing", 490),
    ("21.9 Principal components analysis", 490),
    ("Summary", 494),
    ("Further reading", 494),
    ("Practice questions", 495),
    ("Further questions", 497),

    ("Chapter 22. Estimating volatilities and correlations", 498),
    ("22.1 Estimating volatility", 498),
    ("22.2 The exponentially weighted moving average model", 500),
    ("22.3 The GARCH (1,1) model", 502),
    ("22.4 Choosing between the models", 503),
    ("22.5 Maximum likelihood methods", 504),
    ("22.6 Using GARCH (1,1) to forecast future volatility", 509),
    ("22.7 Correlations", 512),
    ("22.8 Application of EWMA to four-index example", 515),
    ("Summary", 517),
    ("Further reading", 517),
    ("Practice questions", 518),
    ("Further questions", 519),

    ("Chapter 23. Credit risk", 521),
    ("23.1 Credit ratings", 521),
    ("23.2 Historical default probabilities", 522),
    ("23.3 Recovery rates", 523),
    ("23.4 Estimating default probabilities from bond prices", 524),
    ("23.5 Comparison of default probability estimates", 526),
    ("23.6 Using equity prices to estimate default probabilities", 530),
    ("23.7 Credit risk in derivatives transactions", 531),
    ("23.8 Credit risk mitigation", 534),
    ("23.9 Default correlation", 536),
    ("23.10 CreditVaR", 540),
    ("Summary", 542),
    ("Further reading", 543),
    ("Practice questions", 543),
    ("Further questions", 545),

    ("Chapter 24. Credit derivatives", 547),
    ("24.1 Credit default swaps", 548),
    ("24.2 Valuation of credit default swaps", 551),
    ("24.3 Credit indices", 555),
    ("24.4 The use of fixed coupons", 556),
    ("24.5 CDS forwards and options", 557),
    ("24.6 Basket credit default swaps", 558),
    ("24.7 Total return swaps", 558),
    ("24.8 Collateralized debt obligations", 559),
    ("24.9 Role of correlation in a basket CDS and CDO", 561),
    ("24.10 Valuation of a synthetic CDO", 562),
    ("24.11 Alternatives to the standard market model", 569),
    ("Summary", 570),
    ("Further reading", 571),
    ("Practice questions", 571),
    ("Further questions", 573),

    ("Chapter 25. Exotic options", 574),
    ("25.1 Packages", 574),
    ("25.2 Nonstandard American options", 575),
    ("25.3 Gap options", 575),
    ("25.4 Forward start options", 576),
    ("25.5 Cliquet options", 577),
    ("25.6 Compound options", 577),
    ("25.7 Chooser options", 578),
    ("25.8 Barrier options", 579),
    ("25.9 Binary options", 581),
    ("25.10 Lookback options", 582),
    ("25.11 Shout options", 584),
    ("25.12 Asian options", 584),
    ("25.13 Options to exchange one asset for another", 586),
    ("25.14 Options involving several assets", 587),
    ("25.15 Volatility and variance swaps", 588),
    ("25.16 Static options replication", 591),
    ("Summary", 593),
    ("Further reading", 594),
    ("Practice questions", 594),
    ("Further questions", 596),

    ("Chapter 26. More on models and numerical procedures", 599),
    ("26.1 Alternatives to Black–Scholes–Merton", 600),
    ("26.2 Stochastic volatility models", 605),
    ("26.3 The IVF model", 607),
    ("26.4 Convertible bonds", 608),
    ("26.5 Path-dependent derivatives", 611),
    ("26.6 Barrier options", 615),
    ("26.7 Options on two correlated assets", 618),
    ("26.8 Monte Carlo simulation and American options", 621),
    ("Summary", 625),
    ("Further reading", 626),
    ("Practice questions", 627),
    ("Further questions", 628),

    ("Chapter 27. Martingales and measures", 630),
    ("27.1 The market price of risk", 631),
    ("27.2 Several state variables", 634),
    ("27.3 Martingales", 635),
    ("27.4 Alternative choices for the numeraire", 636),
    ("27.5 Extension to several factors", 640),
    ("27.6 Black’s model revisited", 641),
    ("27.7 Option to exchange one asset for another", 642),
    ("27.8 Change of numeraire", 643),
    ("Summary", 644),
    ("Further reading", 645),
    ("Practice questions", 645),
    ("Further questions", 647),

    ("Chapter 28. Interest rate derivatives: The standard market models", 648),
    ("28.1 Bond options", 648),
    ("28.2 Interest rate caps and floors", 653),
    ("28.3 European swap options", 659),
    ("28.4 Generalizations", 663),
    ("28.5 Hedging interest rate derivatives", 663),
    ("Summary", 664),
    ("Further reading", 665),
    ("Practice questions", 665),
    ("Further questions", 666),

    ("Chapter 29. Convexity, timing, and quanto adjustments", 668),
    ("29.1 Convexity adjustments", 668),
    ("29.2 Timing adjustments", 672),
    ("29.3 Quantos", 674),
    ("Summary", 677),
    ("Further reading", 677),
    ("Practice questions", 678),
    ("Further questions", 679),

    ("Appendix: Proof of the convexity adjustment formula", 681),

    ("Chapter 30. Interest rate derivatives: models of the short rate", 682),
    ("30.1 Background", 682),
    ("30.2 Equilibrium models", 683),
    ("30.3 No-arbitrage models", 689),
    ("30.4 Options on bonds", 694),
    ("30.5 Volatility structures", 695),
    ("30.6 Interest rate trees", 696),
    ("30.7 A general tree-building procedure", 698),
    ("30.8 Calibration", 707),
    ("30.9 Hedging using a one-factor model", 709),
    ("Summary", 710),
    ("Further reading", 710),
    ("Practice questions", 711),
    ("Further questions", 713),

    ("Chapter 31. Interest rate derivatives: HJM and LMM", 715),
    ("31.1 The Heath, Jarrow, and Morton model", 715),
    ("31.2 The LIBOR market model", 718),
    ("31.3 Agency mortgage-backed securities", 728),
    ("Summary", 730),
    ("Further reading", 731),
    ("Practice questions", 731),
    ("Further questions", 732),

    ("Chapter 32. Swaps Revisited", 733),
    ("32.1 Variations on the vanilla deal", 733),
    ("32.2 Compounding swaps", 735),
    ("32.3 Currency swaps", 736),
    ("32.4 More complex swaps", 737),
    ("32.5 Equity swaps", 740),
    ("32.6 Swaps with embedded options", 742),
    ("32.7 Other swaps", 744),
    ("Summary", 745),
    ("Further reading", 746),
    ("Further questions", 747),
    ("Chapter 33. Energy and commodity derivatives", 748),
    ("33.1 Agricultural commodities", 748),
    ("33.2 Metals", 749),
    ("33.3 Energy products", 750),
    ("33.4 Modeling commodity prices", 752),
    ("33.5 Weather derivatives", 758),
    ("33.6 Insurance derivatives", 759),
    ("33.7 Pricing weather and insurance derivatives", 760),
    ("33.8 How an energy producer can hedge risks", 761),
    ("Summary", 762),
    ("Further reading", 762),
    ("Practice questions", 763),
    ("Further question", 764),

    ("Chapter 34. Real options", 765),
    ("34.1 Capital investment appraisal", 765),
    ("34.2 Extension of the risk-neutral valuation framework", 766),
    ("34.3 Estimating the market price of risk", 768),
    ("34.4 Application to the valuation of a business", 769),
    ("34.5 Evaluating options in an investment opportunity", 769),
    ("Summary", 776),
    ("Further reading", 776),
    ("Practice questions", 777),
    ("Further questions", 777),

    ("Chapter 35. Derivatives mishaps and what we can learn from them", 779),
    ("35.1 Lessons for all users of derivatives", 779),
    ("35.2 Lessons for financial institutions", 783),
    ("35.3 Lessons for nonfinancial corporations", 788),
    ("Summary", 790),
    ("Further reading", 790),

    ("Glossary of terms", 791),
    ("DerivaGem software", 812),
    ("Major exchanges trading futures and options", 817),
    ("Table for N(x) when x ≤ 0", 818),
    ("Table for N(x) when x > 0", 819),
    ("Author index", 820),
    ("Subject index", 824)
]

# Paths to the input and output PDF files
input_pdf_path = "yourfile.pdf"
output_pdf_path = "output_with_toc.pdf"

# Offset to adjust for the page number shift
offset = 22  # Since the first TOC page is 23 in the actual PDF, the offset is 23 - 1

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
