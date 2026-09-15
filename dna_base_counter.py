"""Count and report the nucleotide bases in a DNA sequence."""


VALID_BASES = {"A", "T", "G", "C"}


def analyze_dna_sequence(sequence: str) -> dict[str, int | float]:
    """Validate a DNA sequence and return its base counts and percentages.

    Raises:
        ValueError: If the sequence is empty or contains non-DNA characters.
    """
    normalized_sequence = sequence.strip().upper()

    if not normalized_sequence:
        raise ValueError("DNA sequence cannot be empty.")

    invalid_characters = sorted(set(normalized_sequence) - VALID_BASES)
    if invalid_characters:
        invalid_display = ", ".join(invalid_characters)
        raise ValueError(
            f"Invalid DNA character(s): {invalid_display}. "
            "Use only A, T, G, and C."
        )

    length = len(normalized_sequence)
    counts = {base: normalized_sequence.count(base) for base in "ATGC"}

    return {
        "length": length,
        **counts,
        **{f"{base}_percentage": (count / length) * 100 for base, count in counts.items()},
    }


def display_results(results: dict[str, int | float]) -> None:
    """Print a readable DNA analysis report."""
    print("\nDNA Nucleotide Counts")
    print("-" * 24)
    print(f"A (Adenine):  {results['A']}")
    print(f"T (Thymine):  {results['T']}")
    print(f"G (Guanine):  {results['G']}")
    print(f"C (Cytosine): {results['C']}")
    print(f"Total length: {results['length']}")
    print("\nNucleotide Percentages")
    print("-" * 24)
    for base, name in (("A", "Adenine"), ("T", "Thymine"), ("G", "Guanine"), ("C", "Cytosine")):
        print(f"{base} ({name}): {results[f'{base}_percentage']:.2f}%")


def main() -> None:
    """Read a DNA sequence from the user and display its analysis."""
    sequence = input("Enter a DNA sequence: ")

    try:
        results = analyze_dna_sequence(sequence)
    except ValueError as error:
        print(f"Error: {error}")
        return

    display_results(results)


if __name__ == "__main__":
    main()