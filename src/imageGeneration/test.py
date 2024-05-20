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
    absoluteFilePath = os.getcwd() + '\\src\\assets\\generated\\' + filePath 
    print(absoluteFilePath)


if __name__ == "__main__":
    url = "https://images.blockadelabs.com/images/imagine/Nebula_equirectangular-jpg_A_large_lake_in_449321714_11042944.jpg?ver=1"
    main(url)