# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 13:42:25 2019

@author: Mike
"""

import Sentiment_module as s
import csv
import os
import json

years = ["2015"]
#months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
months = ["01", "02", "03"]
time_analysis = False
#years = ["2017"]
#months = ["12"]
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
if time_analysis: cnt = 0;
for year in years:
    for month in months:
        
        path = str(test_folder) + year +"/" + month
        out = [[]]
        if time_analysis: timeacc = [0] * 5
        #read all files under the folder	
        files= os.listdir(path)        
        pos = [0] * 6 
        neg = [0] * 6
        for file in files:
            if not os.path.isdir(file):
                file1 = path + "/" + file
                if os.stat(file1).st_size == 0: 
                    continue
                outtemp, timetemp = s.sentiment_file(file1, time_analysis)
                for i in range(6): 
                    if outtemp[i] == 'pos': pos[i] += 1
                    if outtemp[i] == 'neg': neg[i] += 1
                outtemp.extend([file, year, month])
                write_csv_row(outtemp)
                if time_analysis:
                    timeacc = [timeacc[i] + timetemp[i] for i in range(len(timetemp))]
                    cnt += 1
        pos.extend([year, month, "pos"])
        neg.extend([year, month, "neg"])
        write_csv2_row(pos)
        write_csv2_row(neg)
        save.extend([pos, neg])

if time_analysis:
    timeacc[:] = [x / cnt for x in timeacc]
    print("each classofoers average calculating time in sec: ", timeacc)
  
def to_json():
    save_json = json.dumps(save)
    return save_json
    