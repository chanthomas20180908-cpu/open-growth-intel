import subprocess
import sys

def test_cli_help():
    """Smoke test: CLI entry point loads without error."""
    result = subprocess.run(
        [sys.executable, "-m", "cli.page_builder"],
        capture_output=True,
        text=True,
    )
    assert "Open Growth Intelligence" in result.stdout or result.returncode == 0
