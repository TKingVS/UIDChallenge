# randomimage
# Thomas King
# Generates a 128*128 pixel random bmp file names image.bmp

from urllib import request, parse
from PIL import Image

# getNums
# Generates a list of random numbers from random.org
# parameters:
#   n: the number of numbers needed
#   max_value: the largest possible number
#   min_value: the smallest possible number (default 0)
# returns: a list of n random numbers between min_value and max_value 
def getNums(n, max_value, min_value = 0):

  # generate URL
  params = parse.urlencode({'num' : n, 'min' : min_value, 'max' : max_value, 'col' : 1, 'base' : 10, 'format' : 'plain', 'rnd' : 'new'})
  url = 'https://www.random.org/integers/?%s' % params

  # send request
  with request.urlopen(url) as req:
    numbers = req.read().decode('utf-8')
    numbers = numbers.split('\n')[:-1] # last string would be ''

    # convert from string to int
    for num in numbers:
      num = int(num)
    
    return numbers

# makeImage
# Creates a random bmp image using random.org
# parameters:
#   name: the name of the file to save the image to
#   width: the width of the image in pixels
#   height: the height of the image in pixels
# returns: nothing
# side effect: creates an image file
def makeImage(name, width, height):
  n = 3 * height * width # number of RBG values needed
  values = [] # array to hold RGB values
  
  # 10000 is maximum number of numbers to request at once, so ask in chunks of 10000
  while (n > 10000):
    values += getNums(10000, 255)
    n -= 10000
  values += getNums(n, 255)

  # create image
  img = Image.new('RGB', (width, height))
  img.putdata(values)
  img.save(name, "BMP")

makeImage('image.bmp', 128, 128)