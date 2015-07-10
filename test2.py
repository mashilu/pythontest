import os
import os.path
import sys

#print("\n".join(["%s = %s" % (k, v) for k, v in sys.modules.items()]))

#print(os.path.expanduser("~"))

(filepath, filename) = os.path.split("c:\\music\\ap\\mahadeva.mp3")

print("%s, %s" % (filepath, filename))


lista = os.listdir("c:\\")

for item in lista:
    print(item)