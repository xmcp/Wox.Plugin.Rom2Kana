import romkan
import pyperclip
from wox import Wox, WoxAPI
import re

katakana_re=re.compile(r'([A-Z]+)')

class Main(Wox):
#class Main:
    def query(self, key):
        def parse_single(txt):
            if txt.isupper():
                return romkan.to_katakana(txt)
            else:
                return romkan.to_hiragana(txt)
    
        title=''.join(map(parse_single, re.split(katakana_re,key)))

        return [{
            "Title": title,
            "SubTitle": "Copy to Clipboard",
            "IcoPath": "Images\\icon.png",
            "JsonRPCAction": {
                "method": "copy",
                "parameters": [title],
                "dontHideAfterAction": False
            }
        }]

    def copy(self, text):
        pyperclip.copy(text)


if __name__ == "__main__":
    Main()
