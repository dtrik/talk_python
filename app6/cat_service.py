import requests
import os
import shutil

def get_cat(folder, name):
    url = 'http://consuming-python-services-api.azurewebsites.net/cats/random'
    data = get_data(url)
    save_data(folder, name, data)
    
def get_data(url):
    data = requests.get(url, stream=True)
    return data.raw

def save_data(folder, name, data):
    file_name = os.path.join(folder, name + '.jpg')
    with open(file_name, 'wb') as fout:
        shutil.copyfileobj(data, fout)

