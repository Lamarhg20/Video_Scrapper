#get around new attempts to at preventing scrapping
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

import time
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())
chromeOptions = webdriver.ChromeOptions()
chromeOptions.AddExcludedArguments('enable-automation');

URL =


driver.get(URL)


#scroll page every 3sec 54 times
for _ in range(2):
    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    time.sleep(3)
#store the html from scroll
html = driver.page_source
#organize and search html by tag
soup = BeautifulSoup(html, 'html.parser')

videos= soup.find_all('div',{'id':'dismissable'})

master_list = []

for video in videos:
    data_dict = {}
    data_dict['title'] = video.find('a', {'id':'video-title'}).text
    data_dict['video_url'] = 'https://www.youtube.com/'+video.find('a', {'id':'video-title'})['href']
    meta = video.find('div', {'id': 'metadata-line'}).find_all('span')
    data_dict['views'] = meta[0].text
    data_dict['age'] = meta[1].text

    master_list.append(data_dict)

df = pd.dataframe(master_list)

def convert_views(df):
    if 'K' in df['views']:
        views = float(df['views'].split('K')[0])*1000
        return views
    elif 'M' in df['views']:
        views = float(df['views'].split('M')[0])*1000000
        return views
#add column
df['clean_views'] = df.apply(convert_views,axis=1)
df['clean_views'] =df['clean_views'].astype(int)

df.to_csv('sample.csv')



driver.find_element_by_tag_name('body').send_keys(Keys.END)


