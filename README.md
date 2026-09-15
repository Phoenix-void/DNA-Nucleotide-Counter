# DNA Nucleotide Counter

A small, beginner-friendly Python program that counts the nucleotide bases in a DNA sequence.

## Objective

Provide a simple way to validate a DNA sequence and report the number and percentage of adenine, thymine, guanine, and cytosine bases.

## Features

- Accepts a DNA sequence from the command line.
- Converts lowercase input to uppercase.
- Counts A (adenine), T (thymine), G (guanine), and C (cytosine).
- Displays sequence length and base percentages.
- Detects empty input and invalid characters with clear error messages.
- Includes automated unit tests.

## Technologies Used

- Python 3
- Python standard library (`unittest`)
- Git and GitHub

## How Nucleotide Counting Works

The program removes leading and trailing whitespace, converts the sequence to uppercase, and verifies that every character is A, T, G, or C. It counts each valid base, calculates the total sequence length, and finds each percentage with:

```text
(base count / total sequence length) * 100
```

## Example Input

```text
AATGCC
```

## Example Output

```text
DNA Nucleotide Counts
------------------------
A (Adenine):  2
T (Thymine):  1
G (Guanine):  1
C (Cytosine): 2
Total length: 6

Nucleotide Percentages
------------------------
A (Adenine): 33.33%
T (Thymine): 16.67%
G (Guanine): 16.67%
C (Cytosine): 33.33%
```

## How to Run the Program

1. Make sure Python 3 is installed.
2. Open a terminal in this project folder.
3. Run:

```bash
python dna_base_counter.py
```

4. Enter a DNA sequence when prompted.

To run the tests:

```bash
python -m unittest -v
```

## Invalid Input Example

```text
Enter a DNA sequence: ATGNX
Error: Invalid DNA character(s): N, X. Use only A, T, G, and C.
```

## Future Improvements

- Accept sequences from FASTA files.
- Support RNA sequences containing uracil (U).
- Report GC content.
- Add a graphical interface or web version.

---

## Project 2 - FASTA Sequence Analyzer

This repository also contains an independent Biopython project for analyzing DNA sequences stored in FASTA files.

### Objective

Demonstrate practical FASTA parsing with Biopython by extracting each sequence ID and sequence, then calculating its length and GC content.

### Biopython and Features

- Uses `Bio.SeqIO.parse()` to read FASTA records.
- Supports files containing one or multiple DNA sequences.
- Extracts and displays each sequence ID and normalized sequence.
- Calculates sequence length and GC content.
- Detects missing files, empty FASTA files, empty records, and invalid DNA characters.

### Installation and Requirements

This project requires Biopython. Install the dependencies from the repository folder:

```bash
python -m pip install -r requirements.txt
```

### FASTA Parsing and GC Content

Each FASTA record is read with `SeqIO.parse()`. The analyzer accepts DNA bases A, T, G, and C (case-insensitive). GC content is calculated with:

```text
((G count + C count) / sequence length) * 100
```

### How to Run

The repository includes `sample_sequences.fasta`, which contains multiple example DNA records:

```bash
python fasta_sequence_analyzer.py sample_sequences.fasta
```

### Example FASTA Input

```text
>example_sequence
ATGCGC
```

### Example Output

```text
Sequence ID: example_sequence
Sequence: ATGCGC
Sequence Length: 6
GC Content: 66.67%
------------------------------
```

### Testing

Run all project tests with:

```bash
python -m unittest -v
```

### Future Improvements

- Support ambiguous IUPAC DNA bases such as N.
- Export results to CSV.
- Add command-line options for a concise output format.