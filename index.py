import requests
import pandas as pd
import  csv
import validators
import uuid


def download(file_url, name):
    file_object = requests.get(file_url)
    with open(name, 'wb') as local_file:
        local_file.write(file_object.content)

def main():
    with open('../data.csv','rt')as f:
        data = csv.reader(f)
        for row in data:
            uuidOne = uuid.uuid1()
            name = row[0] + "-"+ row[1] + str(uuidOne) +".pdf"
            url = row[4]
            valid  = validators.url(url)
            if (valid):
                print(url)
                download(url, name)



#download("https://api.typeform.com/responses/files/2c0c8deb3a3365160a7d735cbeac4181a55a87f52ec9500063a07c490ff8a3ff/Datos.pdf", "test2.pdf")
main()
