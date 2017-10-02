from lxml import html
import time
import requests

main_url = 'https://www.bitcoin.co.id/'
req = requests.get(main_url)
tree = html.fromstring(req.content)
#harga = tree.xpath('//td/input[@id="pair_targ_input"]/@value')
harga = tree.xpath('//div[@class="pull-right"]/span/text()')
harga = (harga[0].split())[3]
#harga = harga[3]
print('Harga bitcoin : {} Rupiah\nLast checked: {}'.format(harga,time.strftime("%d/%m/%Y %H:%M")))


'''
soup = BeautifulSoup(req.text, "html.parser")
div = soup.find('input', {'id': 'pair_targ_input'})['value']
print(div) dikau mau search apa...

daripada langsung ke url yg panjang, maunya scrape dari awal
emang bisa? scraping kayaknya ga kayak gitu deh
soalnya kalo scraping tuh dia ngasih dari web yg udah ada gitu

kalo selenium kaya gitu sih

\ nah iya kalo selenium sebenernya buat bikin test gitu
ohhh



'''
