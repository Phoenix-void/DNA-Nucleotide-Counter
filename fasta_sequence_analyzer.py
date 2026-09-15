"""Analyze DNA sequences stored in a FASTA file with Biopython."""

from pathlib import Path
import sys

from Bio import SeqIO


VALID_DNA_BASES = {"A", "T", "G", "C"}


def analyze_fasta_file(filename: str | Path) -> list[dict[str, str | int | float]]:
    """Read DNA FASTA records and return each sequence's details.

    Raises:
        FileNotFoundError: If the requested FASTA file does not exist.
        ValueError: If the file is empty or a sequence is empty or non-DNA.
    """
    file_path = Path(filename)
    if not file_path.is_file():
        raise FileNotFoundError(f"FASTA file not found: {file_path}")

    with file_path.open(encoding="utf-8") as fasta_file:
        records = list(SeqIO.parse(fasta_file, "fasta"))

    if not records:
        raise ValueError("The FASTA file is empty or contains no sequence records.")

    analyses = []
    for record in records:
        sequence = str(record.seq).upper()
        if not sequence:
            raise ValueError(f"Sequence '{record.id}' is empty.")

        invalid_characters = sorted(set(sequence) - VALID_DNA_BASES)
        if invalid_characters:
            invalid_display = ", ".join(invalid_characters)
            raise ValueError(
                f"Sequence '{record.id}' contains invalid DNA character(s): "
                f"{invalid_display}. Use only A, T, G, and C."
            )

        sequence_length = len(sequence)
        gc_content = ((sequence.count("G") + sequence.count("C")) / sequence_length) * 100
        analyses.append(
            {
                "id": record.id,
                "sequence": sequence,
                "length": sequence_length,
                "gc_content": gc_content,
            }
        )

    return analyses


def display_results(analyses: list[dict[str, str | int | float]]) -> None:
    """Print the analysis for each FASTA record."""
    for analysis in analyses:
        print(f"Sequence ID: {analysis['id']}")
        print(f"Sequence: {analysis['sequence']}")
        print(f"Sequence Length: {analysis['length']}")
        print(f"GC Content: {analysis['gc_content']:.2f}%")
        print("-" * 30)


def main() -> None:
    """Read a FASTA filename from the command line and display its analysis."""
    if len(sys.argv) != 2:
        print("Usage: python fasta_sequence_analyzer.py <fasta_filename>")
        return

    try:
        analyses = analyze_fasta_file(sys.argv[1])
    except (FileNotFoundError, ValueError) as error:
        print(f"Error: {error}")
        return

    display_results(analyses)


if __name__ == "__main__":
    main()