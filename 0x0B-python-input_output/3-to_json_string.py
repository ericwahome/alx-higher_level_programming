#!/usr/bin/python3
"""
Created on 28.09.2022
@author: Eric Wachira
"""


def write_file(filename="", text=""):
    """
    Writes inputed text to a utf-8 encoded file
    Arguments:
        filename (str): The name of the file to open
        text (str): The text to write in
    Return:
        A file with text written
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
