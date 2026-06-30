import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent


def run_cli(*args):
    return subprocess.run(
        [sys.executable, "-m", "cli.main", *args],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )


class LandingCLITests(unittest.TestCase):
    def test_help_works(self):
        result = run_cli("landing", "build", "--help")
        self.assertEqual(result.returncode, 0)
        self.assertIn("--type", result.stdout)
        self.assertIn("--brand", result.stdout)

    def test_type_a_requires_keyword(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            output = Path(tmpdir) / "page.html"
            result = run_cli("landing", "build", "--type", "a", "--brand", "DemoBrand", "--output", str(output))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("--keyword", result.stdout + result.stderr)

    def test_article_requires_title(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            output = Path(tmpdir) / "article.html"
            result = run_cli(
                "landing",
                "build",
                "--type",
                "article",
                "--brand",
                "DemoBrand",
                "--output",
                str(output),
            )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("--title", result.stdout + result.stderr)

    def test_invalid_faq_payload_fails(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            output = Path(tmpdir) / "page.html"
            result = run_cli(
                "landing",
                "build",
                "--type",
                "a",
                "--brand",
                "DemoBrand",
                "--keyword",
                "ai music video generator",
                "--output",
                str(output),
                "--faq-items",
                "{broken",
            )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("faq", (result.stdout + result.stderr).lower())

    def test_output_directory_is_created(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            output = Path(tmpdir) / "nested" / "tool.html"
            result = run_cli(
                "landing",
                "build",
                "--type",
                "b",
                "--brand",
                "DemoBrand",
                "--keyword",
                "band name generator",
                "--output",
                str(output),
            )
            self.assertEqual(result.returncode, 0)
            self.assertTrue(output.exists())

    def test_renders_all_page_types(self):
        cases = [
            ("a", ["--keyword", "ai music video generator"], ["WebApplication", "FAQPage", "Common Questions"]),
            ("b", ["--keyword", "band name generator"], ["WebApplication", "Common Questions"]),
            ("c", ["--keyword", "ai music tools"], ["WebApplication", "domain-data"]),
            ("article", ["--title", "Top 10 AI Music Video Tools"], ["\"@type\": \"Article\"", "6 min read"]),
        ]
        faq_payload = json.dumps(
            [{"question": "What is this?", "answer": "A generated test page."}],
            ensure_ascii=False,
        )

        with tempfile.TemporaryDirectory() as tmpdir:
            for page_type, extra_args, expected_tokens in cases:
                output = Path(tmpdir) / f"{page_type}.html"
                args = [
                    "landing",
                    "build",
                    "--type",
                    page_type,
                    "--brand",
                    "DemoBrand",
                    "--output",
                    str(output),
                ]
                args.extend(extra_args)
                if page_type != "article":
                    args.extend(["--faq-items", faq_payload])
                result = run_cli(*args)
                self.assertEqual(result.returncode, 0, msg=result.stdout + result.stderr)
                html = output.read_text(encoding="utf-8")
                self.assertNotIn("{{", html)
                self.assertIn("<meta name=\"description\"", html)
                self.assertIn("<link rel=\"canonical\"", html)
                self.assertIn("twitter:card", html)
                for token in expected_tokens:
                    self.assertIn(token, html)


if __name__ == "__main__":
    unittest.main()
