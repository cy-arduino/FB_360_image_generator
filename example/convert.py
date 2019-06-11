import os
from argparse import ArgumentParser
import FbPanoramaConverter
#from sys import stderr
#def _print_err(*args, **kwargs):
#    print(*args, file=stderr, **kwargs)

if __name__ == '__main__':
	argp = ArgumentParser()
	argp.add_argument("inputImage", help="input file")
	argp.add_argument("-o", "--output", help="output image file name", dest="outputImg", default=None)
	argp.add_argument("-w", "--width", help="output image width", dest="imgOutWidth", default=None)
	argp.add_argument("-b", "--bg_color", help="background color", dest="imgBgColor", default=None)
	args = argp.parse_args()
	
	mConverter=FbPanoramaConverter.Converter(args.imgOutWidth, args.imgBgColor)
	mConverter.convert(args.inputImage, args.outputImg)
