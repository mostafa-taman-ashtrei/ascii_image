from PIL import Image
import sys
import uuid
from get_profile_pic import FindProfilePic
from utils.create_dir import create_dir_if_none_exists

ascii_chars = ['@', '#', 'S', '%', '?', '*', '-', '/', '!', '&', ':', ';']


class AsciiImage:
    def __init__(self, image):
        try:
            img_input = Image.open(image)
            self.image = img_input
        except Exception as e:
            print('Error', e)

    def resize_image(self, new_width=100):
        width, height = self.image.size
        ratio = height / width
        new_height = int(new_width * ratio)
        resized_image = self.image.resize((new_width, new_height))
        return resized_image

    def asciify(self, image):
        pixels = image.getdata()
        chars = ''.join([ascii_chars[pixel//25] for pixel in pixels])
        return chars

    def convert(self, new_width=100):
        resized_image = self.resize_image()
        gray_scale_image = resized_image.convert('L')
        asccified_image = self.asciify(gray_scale_image)
        pixel_count = len(asccified_image)

        ascii_image = '\n'.join(
            asccified_image[i:(i+new_width)] for i in range(0, pixel_count, new_width))

        print(ascii_image)

        dirname = 'ascii'
        create_dir_if_none_exists(dirname)

        with open(f'{dirname}/{uuid.uuid4()}.txt', 'w') as f:
            f.write(ascii_image)


if sys.argv[1] == 'profile':
    pic_finder = FindProfilePic(sys.argv[2])
    image_input = pic_finder.get_pic()
    ascii_converter = AsciiImage(image_input)
    ascii_converter.convert()

elif sys.argv[1] == 'custom':
    image_input = sys.argv[2]
    ascii_converter = AsciiImage(image_input)
    ascii_converter.convert()
