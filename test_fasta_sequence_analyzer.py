"""Tests for the Biopython FASTA sequence analyzer."""

from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from fasta_sequence_analyzer import analyze_fasta_file


class AnalyzeFastaFileTests(unittest.TestCase):
    """Verify FASTA parsing, DNA validation, and sequence calculations."""

    def create_fasta_file(self, directory: str, contents: str) -> Path:
        """Create a temporary FASTA file for a test."""
        fasta_path = Path(directory) / "test_sequences.fasta"
        fasta_path.write_text(contents, encoding="utf-8")
        return fasta_path

    def test_normal_fasta_sequence(self) -> None:
        with TemporaryDirectory() as directory:
            fasta_path = self.create_fasta_file(directory, ">sequence_one\nATGCGC\n")
            analyses = analyze_fasta_file(fasta_path)

        self.assertEqual(len(analyses), 1)
        self.assertEqual(analyses[0]["id"], "sequence_one")
        self.assertEqual(analyses[0]["length"], 6)
        self.assertEqual(analyses[0]["gc_content"], 66.66666666666666)

    def test_multiple_fasta_sequences(self) -> None:
        with TemporaryDirectory() as directory:
            fasta_path = self.create_fasta_file(
                directory, ">first\nATGC\n>second\nGGCC\n"
            )
            analyses = analyze_fasta_file(fasta_path)

        self.assertEqual(len(analyses), 2)
        self.assertEqual(analyses[0]["id"], "first")
        self.assertEqual(analyses[1]["id"], "second")
        self.assertEqual(analyses[0]["length"], 4)
        self.assertEqual(analyses[1]["gc_content"], 100.0)

    def test_lowercase_sequence_is_normalized(self) -> None:
        with TemporaryDirectory() as directory:
            fasta_path = self.create_fasta_file(directory, ">lowercase\natgc\n")
            analyses = analyze_fasta_file(fasta_path)

        self.assertEqual(analyses[0]["sequence"], "ATGC")
        self.assertEqual(analyses[0]["gc_content"], 50.0)

    def test_empty_fasta_file(self) -> None:
        with TemporaryDirectory() as directory:
            fasta_path = self.create_fasta_file(directory, "")

            with self.assertRaisesRegex(ValueError, "empty"):
                analyze_fasta_file(fasta_path)

    def test_missing_fasta_file(self) -> None:
        with self.assertRaisesRegex(FileNotFoundError, "not found"):
            analyze_fasta_file("missing_sequences.fasta")

    def test_invalid_sequence_characters(self) -> None:
        with TemporaryDirectory() as directory:
            fasta_path = self.create_fasta_file(directory, ">invalid\nATGN\n")

            with self.assertRaisesRegex(ValueError, "invalid DNA character"):
                analyze_fasta_file(fasta_path)


if __name__ == "__main__":
    unittest.main()