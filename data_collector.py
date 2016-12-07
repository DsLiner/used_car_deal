import csv
from bs4 import BeautifulSoup
import codecs

def web_spider(path, max):
    csv_url = path + "data.csv"
    data_csv = open(csv_url, 'w')
    csv_writer = csv.writer(data_csv)
    for i in range(0, max):
        max_page = [3, 7, 3, 4, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 4, 1, 1, 3, 8, 3, 3, 
            1, 2, 2, 3, 2, 1, 1, 1, 1, 1]
        ori_price = [3600, 3100, 3400, 3700, 3900, 2900, 3000, 3400, 3600, 3600, 
            3600, 4000, 2500, 2700, 2800, 3200, 3400, 3800, 3000, 3000, 3300, 3700, 
            2000, 2300, 2400, 2600, 2800, 2200, 2500, 2700, 1900, 3500]
        for j in range(0, max_page[i]):
            url = path + str(i+1) + "_" + str(j+1) + ".html"
            plain_text = codecs.open(url, 'r').read()
            soup = BeautifulSoup(plain_text, "lxml")
            table = soup.find("tbody", {"id":"sr_normal"})
            for row in table.findAll("tr"):
                array = []
                array.append(row.find("span", {"class":"cls"}).strong.get_text())
                array.append(row.find("span", {"class":"cls"}).em.get_text())
                array.append(row.find("span", {"class":"dtl"}).strong.get_text())
                array.append(row.find("span", {"class":"trs"}).get_text())
                array.append(row.find("span", {"class":"fue"}).get_text())
                array.append(ori_price[i])
                array.append(row.find("td", {"class":"yer"}).get_text().split('식')[0])
                km = row.find("td", {"class":"km"}).get_text().split('km')[0]
                km = km.replace(',', '')
                array.append(int(km))
                new_price = int(row.find("td", {"class":"prc"}).strong.get_text().replace(',', ''))
                array.append(new_price)
                array.append(str(int(new_price / ori_price[i] * 100)))
                csv_writer.writerow(array)
    data_csv.close()

web_spider('C:/Users/Surface/Downloads/data/', 32)

