import os
import piexif
import PIL
from PIL import Image
from argparse import ArgumentParser
from sys import stderr

def print_err(*args, **kwargs):
    print(*args, file=stderr, **kwargs)

class FbPanoramaConverter:
	FB_MAX_WIDTH=6000
	FB_RATIO=2
	DEFAULT_OUT_NAME = 'out.jpg'
	
	imgBgColor='black'
	#>0: use specific width
	#0: use input image's width(maxium width is FB_MAX_WIDTH)
	#<0: something wrong
	imgOutWidth=0

	def __init__(self, imgOutWidth=None, imgBgColor=None):
		if imgOutWidth != None and int(imgOutWidth) > 0:
			self.imgOutWidth = int(imgOutWidth)
		if imgBgColor != None:
			self.imgBgColor = imgBgColor
	
	def convert(self, imgInName, imgOutName=None):
		if imgOutName == None:
			imgOutName = self.DEFAULT_OUT_NAME

		#input image
		imgIn = Image.open(imgInName)
		
		#output image
		w=min(self.FB_MAX_WIDTH, imgIn.size[0])
		if self.imgOutWidth > 0:
			w=self.imgOutWidth
		h=int(w/self.FB_RATIO)
		imgOut = Image.new('RGB', (w, h), color=self.imgBgColor)

		#resize input image then paste to output image
		w = imgOut.size[0]
		h = int(imgIn.size[1] * (imgOut.size[0]/imgIn.size[0]))
		if w/h < self.FB_RATIO:
			#input image's ratio is less than FB_RATIO! resize it to fit the output image
			imgOut.paste(imgIn.resize((imgOut.size[0], imgOut.size[1]), Image.LANCZOS))
		else:
			#resize & set offset
			offset = imgOut.size[1] - h
			imgOut.paste(imgIn.resize((w, h),Image.LANCZOS), (0,offset))
		
		#copy exif from imput image and modify manufacturer and device field
		exif_dict = piexif.load(imgInName)
		exif_dict["0th"][271] = b'RICOH'
		exif_dict["0th"][272] = b'RICOH THETA S'
		exif_bytes = piexif.dump(exif_dict)
		
		#save image
		imgOut.save(imgOutName, exif=exif_bytes)


if __name__ == '__main__':
	argp = ArgumentParser()
	argp.add_argument("inputImage", help="input file")
	argp.add_argument("-o", "--output", help="output image file name", dest="outputImg", default=None)
	argp.add_argument("-w", "--width", help="output image width", dest="imgOutWidth", default=None)
	argp.add_argument("-b", "--bg_color", help="background color", dest="imgBgColor", default=None)
	args = argp.parse_args()
	
	mConv=FbPanoramaConverter(args.imgOutWidth, args.imgBgColor)
	mConv.convert(args.inputImage, args.outputImg)

