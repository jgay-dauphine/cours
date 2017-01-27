#! /usr/bin/python3

import requests, bs4
from matplotlib import pyplot as plt
from matplotlib import dates as mdates
from datetime import date
import datetime as dt

res = requests.get('https://www.investing.com/indices/us-30-historical-data', 
        headers={ "user-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0" } )
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "lxml")

print(type(soup))

# Id : #
# class : .
# tag : div
elems = soup.select('div #results_box')


print(type(elems))
print(len(elems))
print(type(elems[0]))
# print(elems[0].getText())
# print(str(elems[0]))
print(elems[0].attrs)

elems = soup.select('div #results_box #curr_table tbody tr')
print(len(elems))

values = []
dates = []
for i in range(len(elems)):
    s2 = bs4.BeautifulSoup(str(elems[i]), "lxml")
    tds = s2.select('td')
    char = '+'
    if tds[1].attrs['class'][0] == "redFont":
        char = '-'

    print("%s;%s;%s" % (tds[0].getText(), tds[1].getText(), char))
    values.append(float(tds[1].getText()))
    print(tds[0].attrs['data-real-value'])
    d = int(tds[0].attrs['data-real-value'])
    dates.append(d)

print(len(values))
print(values)

fig = plt.figure(1)
# x = [0,1,2,3,4,5,6,7,8,9]
# y = x

# Subplot( numrows, numcols, id )
ax = plt.subplot(111)
# plt.plot(x, y, 'r') # courbe en rouge !
# plt.xlabel('axe des x')
# plt.ylabel('axe des y')
# plt.title('Un premier graphique')

#ax = plt.subplot(122)
print(dates)
dt_x = [date.fromtimestamp(i) for i in dates]
print(dt_x)
x = [mdates.date2num(i) for i in dt_x]
print(x)

# x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

print(x)
print(values)

ax.plot_date(x, values, 'b')
#ax.plot(x, values, 'b--')
plt.xlabel('axe des x')
plt.ylabel('axe des y')
plt.title('Un premier graphique')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
fig.autofmt_xdate()
plt.show()



