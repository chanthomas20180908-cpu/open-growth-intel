import subprocess
import sys
import unittest


class CLISmokeTests(unittest.TestCase):
    def test_page_builder_module_loads(self):
        result = subprocess.run(
            [sys.executable, "-m", "cli.page_builder"],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn("Open Growth Intelligence", result.stdout)

    def test_main_cli_imports(self):
        result = subprocess.run(
            [sys.executable, "-c", "import cli.main; print('ok')"],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn("ok", result.stdout)
