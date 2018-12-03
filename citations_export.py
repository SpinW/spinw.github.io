
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os
import json
import shutil

def postWriter(writeDir, paperDict):
    postFile = os.path.join(writeDir, paperDict['Date'][0] + '-' + paperDict['Paper'][0] + '.md')
    with open(postFile, 'w') as fWriter:
        fWriter.write('---\n')
        fWriter.write('layout: post\n')
        fWriter.write('title: "' + paperDict['Title'][0].strip() + '"\n')
        fWriter.write('urlLink: https://dx.doi.org/' + paperDict['DOI'][0] + '\n')
        fWriter.write('categories: publications\n')
        fWriter.write('---\n')
        fWriter.write('By: ')
        for key, author in enumerate(paperDict['Authors']):
            spAu = author.strip().split(',')
            if key == 3:
                break
            if (key == (len(paperDict['Authors']) - 1)) | (key == 2):
                fWriter.write(spAu[0] + ' *etal*.\n')
            else:
                fWriter.write(spAu[0] + ', ')
        fWriter.write('\n')
        fWriter.write('**' + paperDict['Paper'][0] + '**, Volume:' + paperDict['Volume'][0] + ', Issue:' + paperDict['Issue'][0] + ', Article Number:' + paperDict['Number'][0] + '\n')

url = "http://ets.webofknowledge.com/ETS/ets.do?mark_from=1&product=UA&displayUsageInfo=true&parentQid=14&rurl=http%253A%252F%252Fapps.webofknowledge.com%252Fsummary.do%253Fproduct%253DUA%2526search_mode%253DCitingArticles%2526parentQid%253D4%2526qid%253D14%2526SID%253DF6duvCZsW1lGh1o13uj%2526parentProduct%253DWOS&mark_to=1000&filters=AUTHORSIDENTIFIERS%20ISSN_ISBN%20CITTIMES%20SOURCE%20TITLE%20AUTHORS%20%20&qid=15&SID=F6duvCZsW1lGh1o13uj&totalMarked=92&action=saveToFile&sortBy=PY.D;LD.D;SO.A;VL.D;PG.A;AU.A&displayTimesCited=true&displayCitedRefs=true&fileOpt=html&UserIDForSaveToRID=null"
outFolder = os.path.join('pages', 'publications', '_posts')
outJson = 'publications.json'

if os.path.isdir(outFolder):
    shutil.rmtree(outFolder)
os.mkdir(outFolder)

htmlContent = requests.get(url, verify=False)
soup = BeautifulSoup(htmlContent.content)
citDic = []


for tab in soup("table"):
    thisDict = {'Title': ['-'],
                'Authors': ['-'],
                'Paper': ['-'],
                'DOI': ['-'],
                'Year': ['-'],
                'Volume': ['-'],
                'Issue': ['-'],
                'Number': ['-'],
                'Date': ['-']}
    try:
        content = tab.contents[1]
    except:
        continue
    for field in content.contents:
        try:
            thisField = field.contents[1].contents[0]
            if type(field.contents[2].contents) == list:
                thisValue = field.contents[2].contents[0::2]
            else:
                thisValue = [field.contents[2].contents[0]]
        except:
            continue
        if thisField == 'TI ':
            thisDict['Title'] = thisValue
        elif thisField == 'AU ':
            thisDict['Authors'] = thisValue
        elif thisField == 'SO ':
            thisDict['Paper'] = thisValue
        elif thisField == 'DI ':
            thisDict['DOI'] = thisValue
        elif thisField == 'PY ':
            thisDict['Year'] = thisValue
        elif thisField == 'VL ':
            thisDict['Volume'] = thisValue
        elif thisField == 'IS ':
            thisDict['Issue'] = thisValue
        elif thisField == 'AR ':
            thisDict['Number'] = thisValue
        elif thisField == 'PD ':
            try:
                thisDate = datetime.strptime(thisValue[0], '%b %d %Y')
                thisDict['Date'] = [thisDate.strftime('%Y-%m-%d')]
            except ValueError:
                thisDict['Date'] = ['0001-01-01']
    if thisDict['Title'][0] != '-':
        print(thisDict)
        postWriter(outFolder, thisDict)
        citDic.append(thisDict)

print(len(citDic))
with open(outJson, 'w') as f:
    json.dump(citDic, f)
