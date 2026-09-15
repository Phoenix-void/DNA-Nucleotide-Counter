"""Tests for the DNA nucleotide counter."""

import unittest

from dna_base_counter import analyze_dna_sequence


class AnalyzeDnaSequenceTests(unittest.TestCase):
    """Verify DNA sequence analysis and validation."""

    def test_normal_dna_sequence(self) -> None:
        results = analyze_dna_sequence("AATGCC")

        self.assertEqual(results["length"], 6)
        self.assertEqual(results["A"], 2)
        self.assertEqual(results["T"], 1)
        self.assertEqual(results["G"], 1)
        self.assertEqual(results["C"], 2)
        self.assertAlmostEqual(results["A_percentage"], 33.33333333333333)

    def test_lowercase_dna_sequence(self) -> None:
        results = analyze_dna_sequence("aatgcc")

        self.assertEqual(results["A"], 2)
        self.assertEqual(results["T"], 1)
        self.assertEqual(results["G"], 1)
        self.assertEqual(results["C"], 2)

    def test_sequence_with_all_four_bases(self) -> None:
        results = analyze_dna_sequence("ATGC")

        for base in "ATGC":
            self.assertEqual(results[base], 1)
            self.assertEqual(results[f"{base}_percentage"], 25.0)

    def test_empty_input(self) -> None:
        with self.assertRaisesRegex(ValueError, "cannot be empty"):
            analyze_dna_sequence("   ")

    def test_invalid_dna_characters(self) -> None:
        with self.assertRaisesRegex(ValueError, "Invalid DNA character"):
            analyze_dna_sequence("ATGNX")


if __name__ == "__main__":
    unittest.main()