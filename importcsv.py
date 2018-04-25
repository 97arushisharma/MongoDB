import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient
#CSV to JSON Conversion
csvfile = open('/home/arushi/Desktop/files/python nltk/output/log20161231.csv', 'r')
reader = csv.DictReader( csvfile )
mongo_client=MongoClient() 
db=mongo_client.logfile
db.segment.drop()
header= [ "ip", "date", "time", "zone", "cik", "accession", "extention", "code", "size", "idx", "norefer", "noagent", "find", "crawler" ,"browser"]

for each in reader:
    row={}
    for field in header:
        row[field]=each[field]

    db.segment.insert(row)

