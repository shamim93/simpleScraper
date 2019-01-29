from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://coreyms.com/').text
soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link']) 

for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)
    summary = article.find('div', class_='entry-content').p.text
    print(summary)
   
    try:
        emb_video = article.find('iframe', class_='youtube-player') ['src']#['src'] using for remove iframe
        viedo_id = emb_video.split('/')[4] # split to remove / from the link and [4] for the id index
        viedo_id = viedo_id.split('?')[0] #split to remove ? sign and [0] is for separate the 0 ondex for the ID
        yt_link = f'https://youtbe.com/watch?v={viedo_id}'

    except Exception as e:
        raise e

    print(yt_link)
    print(' ')

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()
