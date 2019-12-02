from newspaper import Article
import pandas as pd
from newspaper import fulltext
import requests
import newspaper
import numpy as np
from datetime import datetime
import random
import string
import os
import shutil
from multiprocessing import Pool
from time import time,sleep


def generate_data(url):
    dict_ = []
    
    try:
        article = Article(url)
        article.download()
        article.parse()

        #Making the date format of type YYYY-MM-DD
        
        date_ = article.publish_date
        #date = f'{year}-{date_.month}-{date_.day}'
        date_ =  f'{date_.year}-{date_.month}-{date_.day}'

        title = article.title

        
        #Appending all the attributes in dictionary
        dict_.append("CNN")
        dict_.append(date_)
        dict_.append(title)
        dict_.append(url)

        #Generating Random File of 32 len to store only the file_name of that article url in dataframe
        #Actual data will be stored in the generated file

        random_file = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
        random_file = random_file + '.txt'
        dict_.append(random_file)


        #Cleaning the raw data, which is done more in detailed as preprocessing script
        #Writing to the file

        text = article.text
        text = text.replace('\n','')
        text = text.encode(encoding='utf-8')
        fp = open(random_file,'w',encoding = 'utf-8')
        fp.write(text.decode())
        fp.close()
        
                    
    except Exception as e:
                    
        print(str(e))
        print('Problem occured in file {random_fie} closing it')
   
    return '|'.join(dict_)



if __name__ == '__main__':
    path = r'C:\Users\Darshan\Music\raman_kannan\NLP\processed'
    os.chdir(path)
    try:
        for site_maps in os.listdir('.'):

                
                start_time = time()

                if ( site_maps.find('Sitemap') == 0):  

                    print(f'Reading from the sitemaps {site_maps}')
                    
                    file_name,file_ext = os.path.splitext(site_maps)
                    site_year,site_month = file_name.split('_')[1],file_name.split('_')[2]
                        
                    df = pd.read_json(site_maps)
                    urls = df['url'].tolist()

                    try:
                        parent_folder = path+f'\\{site_year}'
                        sub_folder = parent_folder + f'\\{site_month}'
                        os.makedirs(parent_folder,exist_ok = True)
                        os.chdir(parent_folder)
                        os.makedirs(sub_folder,exist_ok = True)
                        os.chdir(sub_folder)
                        
                    except Exceptions as e:
                        print('Encountered error while creating directory ',str(e))


                    with Pool(10) as p:
                        data_ = p.map(generate_data,urls)

                    #Changing to orginal directory
                    os.chdir(path)
                    
                    if(len(data_)> 0):
                        with open('Complete_Articles_Data.csv','a+',encoding = 'utf-8') as f:
                            f.write('\n'.join(data_))

                    end_time = time()

                    #Time taken to complete parallelism
                    print('Completed in ',(end_time - start_time) / 60,' secs')

                    #Once sitemap json processed move from the directory                    
                    print(f'Moved {site_maps}' )
                    source = f'C:\\Users\\Darshan\\Music\\raman_kannan\\NLP\\processed\\{site_maps}'
                    dest = f'C:\\Users\\Darshan\\Music\\raman_kannan\\NLP\\processed_\\{site_maps}'    
                    shutil.move(source,dest)
                
    except Exception as e:
        print(str(e))

    print('Request Completed')
