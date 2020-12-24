from termcolor import cprint
import sys


def error_exit(text):
    cprint(text, "red")
    sys.exit(0)
