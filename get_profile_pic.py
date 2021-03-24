import requests
from bs4 import BeautifulSoup as bs


class FindProfilePic:
    def __init__(self, username):
        self.username = username

    def get_pic(self):
        url = f'https://github.com/{self.username}'
        req = requests.get(url)
        soup = bs(req.content, 'html.parser')
        pic = soup.find('img', {'alt': 'Avatar'})['src']

        pic_data = requests.get(pic).content
        pic_path = f'./images/{self.username}.jpg'

        with open(pic_path, 'wb') as f:
            f.write(pic_data)

        return pic_path
