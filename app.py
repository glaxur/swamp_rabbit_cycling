# import csv

from flask import Flask
from flask import request
import requests
import json

app = Flask(__name__)


@app.route("/")
def index():

    response = requests.get('https://api.etsy.com/v2/listings/active?api'
                            '_key=cdwxq4soa7q4zuavbtynj8wx&keywords=bicyc'
                            'le&includes=Images,Shop&sort_on=score')
    data = response.json()

    print(data)

    bicycles = data['results']

    etsy_data = []

    for listing in bicycles:
        print(listing['Images'])

    index_file = open('index.html', 'r')
    index_html = index_file.read()
    index_file.close()

    return index_html
