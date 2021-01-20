#!/usr/bin/env python
# coding: utf-8

# In[2]:


from datetime import date
import time
import pandas as pd
import urllib.request
from bs4 import BeautifulSoup

import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# In[3]:


allUrl = "http://www.nuforc.org/webreports/ndxevent.html"
allPage = urllib.request.urlopen(allUrl)
allSoup = BeautifulSoup(allPage, 'html.parser')


# In[4]:


table = allSoup.find("table")


# In[5]:


linksByDate = []
for link in table.find_all("a"):
    linksByDate.append(link['href'])


# In[6]:


def getSummary(link):
    try:
        summaryPage = urllib.request.urlopen(link)
        summarySoup = BeautifulSoup(summaryPage, 'html.parser')
        summary = summarySoup.find("tbody").find_all("tr")[1].find("td").text
        return summary
    except Exception:
        pass
   


# In[34]:


sightings = pd.DataFrame()
count = 0
monthRows = {}
link_counter = 0
for month in linksByDate:
    print(month, "is the number ", link_counter, " link")
    monthUrl = 'http://www.nuforc.org/webreports/' + month
    monthPage = urllib.request.urlopen(monthUrl)
    monthSoup = BeautifulSoup(monthPage, 'html.parser')
    monthTable = monthSoup.find("tbody")
    if(monthUrl != "http://www.nuforc.org/webreports/ndxe.html"):
        for x in monthTable.find_all("tr"):
            if(count % 100 == 0):
                print("current count: ", count)
            key = "row " + str(count)
            link = x.find("a")
            if(link is not None):
                report_url = 'http://www.nuforc.org/webreports/' + link["href"]
                row_data = x.find_all("td")
                datetime = row_data[0].text
                city = row_data[1].text
                state = row_data[2].text
                shape = row_data[3].text
                duration = row_data[4].text
                posted = row_data[6].text
                summary = getSummary(report_url)
                monthRows[key] = [report_url, datetime, city, state, shape, summary, duration, posted]
                count = count + 1
    link_counter = link_counter + 1  
sightings = sightings.append(pd.DataFrame.from_dict(monthRows, orient="index", columns=["Link", "Datetime", "City", "State", "Shape", "Summary", "Duration", "Posted"]))    


# In[35]:


sightings.head()


# In[36]:


sightings.to_json('data/nuforcData-2.json', orient="records")
sightings.to_csv('data/nuforcData-2.csv')

