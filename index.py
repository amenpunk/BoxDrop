import requests
import pandas as pd
import  csv
import validators
import uuid
import os


def download(file_url, name):
    file_object = requests.get(file_url)
    with open(name, 'wb') as local_file:
        local_file.write(file_object.content)

def main():
    with open('./data.csv','rt')as f:
        data = csv.reader(f)
        for row in data:
            uuidOne = uuid.uuid1()
            name = row[0] + "-"+ row[1]
            pdf_name = name + str(uuidOne) +".pdf"
            url = row[2]
            valid  = validators.url(url)

            directory = name
            parent_dir = "./FILES/"
            path = os.path.join(parent_dir, directory)
            try:
                os.mkdir(path)
                if (valid):
                    print(url)
                    download(url, path +"/"+pdf_name)
            except OSError as error:
                continue




main()
