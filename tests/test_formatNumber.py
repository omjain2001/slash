"""
Copyright (C) 2021 SE Slash - All Rights Reserved
You may use, distribute and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: secheaper@gmail.com

"""
from src.formatter import getNumbers
import sys
import os

# Get the absolute path to the project's root directory
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add the project's root directory to the Python path
sys.path.insert(0, project_root)
# from src import formatter


def test_getNumbers():
    """
    Checks the getNumbers function
    """
    assert getNumbers("some chars and $10.00") == 10.0
    assert getNumbers("some chars and $10.99 some other chars") == 10.99
