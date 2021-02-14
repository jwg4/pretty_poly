import doctest

import pytest


def test():
    pytest.main(["-s", "-vv"])


def run_doctest():
    doctest.testfile("README.md")
