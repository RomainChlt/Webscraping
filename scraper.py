import requests
import smtplib
import time
import unicodedata
from bs4 import BeautifulSoup

#Original video: https://www.youtube.com/watch?v=Bg9r_yLk7VY
#How to split: https://mkyong.com/python/python-how-to-split-a-string/

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}

def check_price(website,URL,max_price):
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    
    print("\n########")
    print("Website: "+ website)
    #Sonovente.com
    if(website == 'Sonovente'):
        data = soup.find(id="scroll-mask").get_text()
        #TITLE
        data_title = data.split("SonoVente.com")
        title = data_title[0].strip()
        title = title.replace('ô','o')

        #PRICE
        data_price = data_title[1].split("Prix")
        price = data_price[0].strip()
        converted_price = float(price)
    
    if(website == 'PlanetSono'):
        title = soup.find(itemprop="name").get_text()
        title = title.replace('ô','o')

        data = soup.find(id="our_price_display").get_text()
        data_price = data.split(",")
        price = data_price[0]

        converted_price = float(price)

    print(title)
    print(converted_price)



    #Send mail
    if (converted_price > max_price):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login('romain.choulot@gmail.com', 'mvbsgwwxwzitpklr')
        
        subject = 'Price down for '+ title
        print(subject)
        body = 'New price: '+ price+ 'euros\nCheck the link: '+ URL

        msg = f"Subject: {subject}\n\n{body}"

        server.sendmail(
            'romain.choulot@gmail.com',
            'romain.choulot@gmail.com',
            msg
        )
        print('An email has been send')
        server.quit()






#*******************#
#*****SONOVENTE*****#
#*******************#
website = 'Sonovente'
#Pioneer DJ DDJ SB3
URL = 'https://www.sonovente.com/pioneer-ddj-sb-3-p60497.html'
check_price(website, URL, 220.0)
#PIONEER DJ DDJ-400
URL = 'https://www.sonovente.com/pioneer-ddj-400-p62558.html'
check_price(website, URL, 220.0)
#PIONEER DJ DDJ SB 2
URL = 'https://www.sonovente.com/pioneer-ddj-sb-2-p47728.html'
check_price(website, URL, 180.0)

#********************#
#*****PlanetSono*****#
#********************#
website = 'PlanetSono'
#DJ Numark MixtrackPro3
URL = 'https://planetsono.com/achat/3530-controleur-dj-usb-numark-mixtrack-pro-3.html'
check_price(website, URL, 150.0)









