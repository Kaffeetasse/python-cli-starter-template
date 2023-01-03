import subprocess
import sys
from unittest import TestCase


class Test(TestCase):
    def test_run_as_module(self):
        """can be run as ``python -m app ...``."""

        result = subprocess.run(
            [sys.executable, "-m", "app", "--help"],
            stdout=subprocess.PIPE,
            check=True,
        )

        assert result.stdout.startswith(b"usage:")
        assert b"--log-level" in result.stdout
