from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth
import csv
import os, sys

sys.path.insert(1, r'C:\\Users\\Home\\python-projects\\meta-analysis-webscraper\\crossref')
from crossref.crossrefparse import apapsychdois

options = Options()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
s = Service('C:\\Users\\Home\\seleniumdrivers\\chromedriver.exe')

driver = webdriver.Chrome(service = s, options=options)

stealth(driver,
      languages=["en-US", "en"],
      vendor="Google Inc.",
      platform="Win32",
      webgl_vendor="Intel Inc.",
      renderer="Intel Iris OpenGL Engine",
      fix_hairline=True,
  )

#Urls to search through
urls = []
apapsychurls=[]
with open ("scholar/scholar.csv", "r", encoding="utf-8-sig") as f: 
    reader = csv.reader(f)
    # DictReader
    for row in reader: 
        if (row[5] == "None"):
            continue
        elif ('apa.org' in row[5]):
            apapsychurls.append(row[5])
        else: 
            urls.append(row[5])

print(apapsychurls)
print(urls)
del urls[0]
    
#Handle Apa.org
for link in apapsychurls: 
        f = open("test.py", "w+")
        f.writelines([
        "from selenium import webdriver \n",
        "driver = webdriver.Chrome(executable_path=r'C:\\Users\\Home\\seleniumdrivers\\chromedriver.exe') \n",
        f"driver.get('{link}') \n"
        "driver.implicitly_wait(1) \n",
        "doi = driver.find_element(\"xpath\", '//a[contains(text(), \"doi\")]') \n" ,
        "print(doi.text) \n",
        "with open (\"apadois.txt\", \"a\", encoding=\"utf-8\") as f: \n" ,
            "\tf.write(doi.text + \"\\n\")"])
        
        f.close()
        exec(open("test.py").read())
        os.remove("test.py")


# testurls = ["https://www.frontiersin.org/articles/10.3389/fpsyg.2020.01383/full","https://psycnet.apa.org/journals/drm/30/4/287/", "https://www.sciencedirect.com/science/article/pii/S0149763418303361", "https://www.frontiersin.org/articles/10.3389/fpsyg.2020.01383/full", "https://psycnet.apa.org/record/2020-24631-001", "https://www.frontiersin.org/articles/10.3389/fpsyg.2020.01383/full" ]
#return DOIs from rest of scholar links
with open ("scholar/scholardois.csv", "w", encoding="utf-8", newline="") as file: 
    thewriter = csv.writer(file)
    header = ["DOI"]
    thewriter.writerow(header)
    counter = 0

    for url in urls: 
        driver.get(url)
        driver.implicitly_wait(1)
        
        try: 
            doi = driver.find_element("xpath", '//a[contains(text(), "doi")]')
            thewriter.writerow([doi.text])
            print(doi.text)
        except NoSuchElementException: 
            counter = counter + 1
            continue         

print(counter)
