from translate_po.main import run
from googletrans import Translator
import json
import time

translator = Translator()
file = open('translation.json')
translation = json.loads(file.read())
for rec in translation:
    # print(t['code'],'.lang')
    # print(translator.translate('demo', dest=t['code']))
    run(fro="en", to=rec['code'], src="./un", dest="./tr",
        filename="%s.po" % (rec['file_name']))
    print('Sleep To Avoid Time Out')
    time.sleep(2)
    print('Sleep Done')
