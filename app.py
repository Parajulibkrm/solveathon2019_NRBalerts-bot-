# main program

from flask import Flask
from bs4 import BeautifulSoup
import json
import requests


app = Flask(__name__)


@app.route('/user/')
def notice():
    page = requests.get("https://www.nrb.org.np/whatisnewdetails.php")

    soup = BeautifulSoup(page.content, 'html.parser')

    # print(soup)

    table = soup.findAll("table", {"class": "hancy-table"})[0]
    # print(table)

    row1 = table.findAll("tr")[0]
    #print (row1)
    tdata = row1.findAll('td')[1]
    # print(tdata)
    text = tdata.get_text()
    hreflink = tdata.find_all('a', href=True)[0]['href']
    textfinal = text +" XX " + hreflink
    print(textfinal)
    return textfinal



@app.route('/')
def index():
    return "<h1> Welcome to our Server <h1>"


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
