from translate_po.utilities.io import read_lines
import os

for line in read_lines(os.path.join('./un/ar_001.po')):
    print(line.msgid,'.lINE')