'''
Open up the stories
Read the firstline
pass it to the gsearch the query
append the link in the 90kArticles.csv with the story name
Discard the links which does not belong to cnn as it has a potential threat of being suspicious links
'''

import sys
import os

class Gsearch_python:
   def __init__(self,name_search):
      self.name = name_search
   def Gsearch(self,fp,file):
      count = 0
      try :
         from googlesearch import search
      except ImportError:
         print("No Module named 'google' Found")
      for i in search(query=self.name,tld='co.in',lang='en',start =1, num=10,stop=1,pause=4):
        print(i)
        if(i.find('.index.html')):
           fp.write(file +','+i)
           fp.write('\n')
         
if __name__=='__main__':
    
    os.chdir(r'C:\Users\Darshan\Music\raman_kannan\NLP\cnn_data\cnn_stories\cnn')
    fp = open('90kAirtcles_Urls.csv','w')
    
    
    
    for file in os.listdir('.'):
        file_name, file_ext = os.path.splitext(file)
        if(file_ext == '.story'):
            fopen = open(file,'r')
            query = fopen.readline()
            gs = Gsearch_python(query)
            gs.Gsearch(fp,file_name)
            fopen.close()
        
    fp.close()
