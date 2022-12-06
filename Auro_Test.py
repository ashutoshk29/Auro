import xml.etree.ElementTree as ET
from queue import PriorityQueue

t = ET.parse('orders.xml')
 
r = t.getr()
book = {}
for i in range(0, len(r)):
    print(r[i].tag)
    print(r[i].attrib)
    if(r[i].attrib['book'] not in book.keys()):
        book[r[i].attrib['book']] = {"BUY":PriorityQueue(), "SELL":PriorityQueue()}
    
    book[r[i].attrib['book']][r[i].attrib['operation']].put([r[i].attrib['price'], r[i].attrib['volume']])
    while(book[r[i].attrib['book']]["SELL"].get()["price"] < book[r[i].attrib['book']]["BUY"].get()["price"]):
        if(book[r[i].attrib['book']]["SELL"].get()["volume"] < book[r[i].attrib['book']]):
            book[r[i].attrib['book']]["BUY"].get()["volume"] -= book[r[i].attrib['book']]["SELL"].get()["volume"]