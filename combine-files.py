import pandas as pd 
import sys

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

pd.set_option("display.max_rows", 400, "display.max_columns", 2)
pubmed_df = pd.read_csv('pubmed/pubmeddata.csv', encoding='latin')
crossref_df = pd.read_csv('crossref/crossrefdata.csv', encoding='latin')
scholar_df = pd.read_csv('scholar/scholardata.csv', encoding='latin')
apadois = pd.read_csv("apadois.csv", encoding="latin", index_col=False)

pubmed_df = pubmed_df[~pubmed_df['DOI'].str.contains("No DOI")]
scholar_df = scholar_df.dropna(axis=0)


def combinePrelimData():
    prelimdata = pd.concat([pubmed_df, crossref_df, scholar_df], axis=0, ignore_index=True, verify_integrity=True).drop_duplicates()
    prelimdata.to_csv('prelimdata.csv', index=None)

apadois.drop_duplicates()
apadois.to_csv("apadois.csv", index=None)

def combineAllData(): 
    papers = pd.read_csv("papers.csv", encoding="latin")
    apapapers = pd.read_csv("apadata.csv", encoding="latin")
    allpapers = pd.concat([papers, apapapers], axis=0, ignore_index=True,verify_integrity=True)
# apadata = pd.read_csv("apadata.csv",on_bad_lines='skip', encoding="latin")
# apadata.reset_index(drop=True)
# apadata.columns=["DOI", "Title", "Abstract"]