import pywhatkit
#import pywhatkit as kit
#kit.text_to_handwriting("\nHELLO\n Sunnam sriram\n sprogram001\n")
#text=input("Enter the Question Here: ")
#answer=input("Enter the Answer: ")
pywhatkit.text_to_handwriting('\nHELLO\n Sunnam sriram\n sprogram001\n')

import requests

r = requests.get("http://google.com")
print(r.status_code)
