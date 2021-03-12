import doctest
import os

import pytest


def test():
    pytest.main(["-s", "-vv"])


def run_doctest():
    for file in os.listdir("examples/"):
        if not file.endswith(".md"):
            continue
        filepath = os.path.join("examples/", file) 
        doctest.testfile(filepath, optionflags=doctest.ELLIPSIS)

    for file in os.listdir("pretty_poly/"):
        if not file.endswith(".py"):
            continue
        filepath = os.path.join("pretty_poly/", file) 
        doctest.testfile(filepath)

    doctest.testfile("README.md")
