import argparse
import os

import polib
from googletrans import Translator
from deep_translator import GoogleTranslator

from .utilities.constants import UNTRANSLATED_PATH, TRANSLATED_PATH, LANGUAGE_SOURCE, LANGUAGE_DESTINATION
from .utilities.io import read_lines, save_lines
from .utilities.match import recognize_po_file


def translate(source: str, arguments) -> str:
    """ Translates a single string into target language. """
    translator = GoogleTranslator()
    translator.target = arguments.to
    return translator.translate(text=source)


def create_close_string(line: str) -> str:
    """ Creates single .po file translation target sting. """
    return r"msgstr " + '"' + line + '"' + "\n"


def solve(new_file: str, old_file: str, arguments):
    """ Translates single file. """
    lines = read_lines(old_file)
    for line in lines:
        line.msgstr = polib.unescape(translate(polib.escape(line.msgid), arguments))
    save_lines(new_file, lines)


def run(**kwargs):
    """ Core process that translates all files in a directory.
     :parameter fro:
     :parameter to:
     :parameter src:
     :parameter dest:
     """
    found_files = False

    parser = argparse.ArgumentParser(description='Automatically translate PO files using Google translate.')
    parser.add_argument('--fro', type=str, help='Source language you want to translate from to (Default: en)',
                        default=kwargs.get('fro', LANGUAGE_SOURCE))
    parser.add_argument('--to', type=str, help='Destination language you want to translate to (Default: et)',
                        default=kwargs.get('to', LANGUAGE_DESTINATION))
    parser.add_argument('--src', type=str, help='Source directory or the files you want to translate',
                        default=kwargs.get('src', UNTRANSLATED_PATH))
    parser.add_argument('--dest', type=str, help='Destination directory you want to translated files to end up in',
                        default=kwargs.get('dest', TRANSLATED_PATH))
    arguments = parser.parse_args()

    for file in os.listdir(arguments.src):
        if recognize_po_file(file):
            found_files = True
            print('Starting Translation -> ', kwargs.get('filename'))
            solve(os.path.join(arguments.dest, kwargs.get('filename')), os.path.join(arguments.src, file), arguments)
            print('Done Translation -> ', kwargs.get('filename'))

    if not found_files:
        raise Exception(f"Couldn't find any .po files at: '{arguments.src}'")


if __name__ == '__main__':
    run()
