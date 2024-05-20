import requests
import os

def download_image(url, save_as):
    response = requests.get(url)
    with open(save_as, 'wb') as file:
        file.write(response.content)

def main(url):
    
    splitedURL = url.split('equirectangular-jpg_')   
    fileName = splitedURL[-1]
    
    splitedFileName = fileName.split('jpg')
    fileName = splitedFileName[0]
    
    filePath = fileName + "jpg"
    save_as = os.getcwd() + '\\src\\assets\\generated\\' + filePath 

    download_image(url, save_as)
    
    return save_as

if __name__ == "__main__":
    print()