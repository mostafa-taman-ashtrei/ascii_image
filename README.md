# Ascii Image

a python script that converts any image to a set of ascii characters and saves the ascii image in a text file. The image can be an image that you provide or the profile pic of a github user

## Get started

clone the repo by running
```bash
$ git clone https://github.com/neoScriptscode/ascii_image.git
```
Install the requirements by running

```bash
$ pip install -r requirements.txt 
```

## Usage
The script requires the following arguments:

1. mode => indicates weather you want to provide an image or get the profile pic of a github user. You can either enter:
    - 'profile' => to get the profile pic of a github user.
    - 'custom'  => to convert an image on your local machine

2. image => if you chose the profile mode then you provide the username as the second arg. If you chose the custom mode then enter the path to your image:
    - mode 'profile' => username
    - mode 'custom' => path to image

### profile mode
```bash
    $python convert.py profile neoscriptscode
```
### custom mode
```bash
    $python convert.py custom <path To Image>
```