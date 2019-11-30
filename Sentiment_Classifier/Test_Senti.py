# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 13:42:25 2019

@author: Mike
"""

import Sentiment_module as s

# for file test:
file1 = "testing_files/test1.txt" # put under the same folder
file2 = "testing_files/test2.txt"
file3 = "testing_files/test3.txt"
print(s.sentiment_file(file1)) # (result, confidency rate)
print(s.sentiment_file(file2))
print(s.sentiment_file(file3))

# for text test:
#print(s.sentiment("This article was rich, clear, willing, ingenuous, attractive, sensational, and hot"))
#print(s.sentiment("This is the best marvellous, imaginative, and realistic one I have seen"))
#print(s.sentiment("This article was utter junk. There were absolutely 0 points. I don't see what the point was at all. Horrible essay, suck"))
