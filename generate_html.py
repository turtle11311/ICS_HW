#!/usr/bin/env python3
from os import path
from sys import argv
import subprocess

filename = path.splitext(argv[1])[0]
try:
    subprocess.call(
        ["pandoc",
         "--css=github_pandoc.css",
         "--mathjax",
         filename + ".md",
         "-o",
         filename + ".html"
         ])
except FileNotFoundError:
    print("Please install pandoc......")
