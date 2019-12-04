# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 13:42:25 2019

@author: Mike
"""

import Sentiment_module as s
import csv
import os
import json

years = [2017]
months = [11, 12]
test_folder = "testing_files/"

#write to the csv:	5 classifers resuts + final results + file name + year + month
def write_csv_row(data):
    with open('NLP_sentiment_result.csv', 'a') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(data)
        
#write to the csv:	5 classifers static resuts + final static results + year + month + label
def write_csv2_row(data):
    with open('NLP_sentiment_static_result.csv', 'a') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(data)

save = []
for year in years:
    for month in months:
        
        path = str(test_folder) + str(year) +"/" + str(month)
        out = [[]]
        #read all files under the folder	
        files= os.listdir(path)        
        pos = [0] * 6 
        neg = [0] * 6
        for file in files:
            if not os.path.isdir(file):
                file1 = path + "/" + file
                outtemp = s.sentiment_file(file1)
                for i in range(6): 
                    if outtemp[i] == 'pos': pos[i] += 1
                    if outtemp[i] == 'neg': neg[i] += 1
                outtemp.extend([file, year, month])
                write_csv_row(outtemp)
                
        pos.extend([year, month, "pos"])
        neg.extend([year, month, "neg"])
        write_csv2_row(pos)
        write_csv2_row(neg)
        save.extend([pos, neg])
        
def to_json():
    save_json = json.dumps(save)
    return save_json
    