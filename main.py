import romkan
import clipboard
from wox import Wox, WoxAPI


class Main(Wox):

    def query(self, key):
        title = romkan.to_hiragana(key)
        results = []
        results.append({
            "Title": title,
            "SubTitle": "Copy to Clipboard",
            "IcoPath": "Images\\icon.png",
            "JsonRPCAction": {
                "method": "copy",
                "parameters": [key],
                "dontHideAfterAction": False
            }
        })
        return results

    def copy(self, text):
        clipboard.put(romkan.to_hiragana(text))


if __name__ == "__main__":
    Main()
