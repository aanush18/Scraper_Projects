from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
df = {'Language':[],'Tag_Count':[]}
def extract_tagged(url):
    #print('Extracting Content')
    response=requests.get(url,timeout=5)
    content=bs(response.content, "html.parser")
    for tag in content.find_all('a',attrs={'class':'post-tag'}):
        df['Language'].append(tag.text)
    for count in content.find_all('span',attrs={'class':'item-multiplier-count'}):
        df['Tag_Count'].append(count.text)
for i in range(1,3):
    extract_tagged('http://stackoverflow.com/tags?page='+str(i)+'&tab=popular')
    
df['Tag_Count']=[int(i) for i in df['Tag_Count']]

df2= pd.DataFrame(df)
print(df2)
