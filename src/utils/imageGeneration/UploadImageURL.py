import requests

def download_image(url, save_as):
    response = requests.get(url)
    with open(save_as, 'wb') as file:
        file.write(response.content)

image_url = 'https://images.blockadelabs.com/exports/equirectangular-png/Advanced_no_style_equirectangular-png_castle_on_mountain_in_1899935841_10908569.png'
save_as = 'photos/image1.png'

download_image(image_url, save_as)