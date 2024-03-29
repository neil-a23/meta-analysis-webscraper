from habanero import Crossref
from csv import writer
from crossrefsearch import results
import sys
import pandas as pd 

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)


information = results['message']['items']

titles = []
dois = []
apadois = []
for i in information:
    if "10.1037" in i["DOI"]:
        apadois.append(i["DOI"])
    elif "10.1023" in i["DOI"]:
        apadois.append(i["DOI"])
    else: 
        if 'title' in i:
            title = ''.join(i['title'])
            titles.append(title)
        dois.append(i["DOI"])

apadf = pd.DataFrame(apadois, columns=["DOI"])
apadf.to_csv("datafiles/apadois.csv", mode="w", index=None)
df = pd.DataFrame(list(zip(dois,titles)), columns=["DOI", "Title"])
df.to_csv("crossref/crossrefdata.csv", index=None)