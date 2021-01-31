import doctest

import pytest


def test():
    pytest.main(["-s"])


def run_doctest():
    doctest.testfile("README.md")
