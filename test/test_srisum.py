# Copyright (c) 2026 Qrytics contributors
# Licensed under the MIT license

import base64
import hashlib
import os
import sys
import unittest
from io import StringIO
from tempfile import TemporaryDirectory
from unittest.mock import patch

from srisum.__main__ import main


class MissingFileTest(unittest.TestCase):
    def test_missing_file_reports_clean_error(self):
        argv = ["srisum", "does-not-exist.bin"]
        with (
            patch.object(sys, "argv", argv),
            patch("sys.stdout", new_callable=StringIO) as stdout,
            patch("sys.stderr", new_callable=StringIO) as stderr,
            self.assertRaises(SystemExit) as caught,
        ):
            main()

        self.assertEqual(caught.exception.code, 1)
        self.assertIn("does-not-exist.bin", stderr.getvalue())
        self.assertNotIn("Traceback", stderr.getvalue())
        self.assertEqual(stdout.getvalue(), "")


class ValidFileTest(unittest.TestCase):
    def test_valid_file_prints_hash(self):
        with TemporaryDirectory() as tempdir:
            path = os.path.join(tempdir, "hello.txt")
            with open(path, "wb") as f:
                f.write(b"hello\n")
            expected = "sha256-" + base64.b64encode(
                hashlib.sha256(b"hello\n").digest()
            ).decode("ascii")

            argv = ["srisum", path]
            with (
                patch.object(sys, "argv", argv),
                patch("sys.stdout", new_callable=StringIO) as stdout,
                patch("sys.stderr", new_callable=StringIO) as stderr,
            ):
                main()

            self.assertEqual(stdout.getvalue().strip(), expected)
            self.assertEqual(stderr.getvalue(), "")


if __name__ == "__main__":
    unittest.main()
