import os
import piexif
from PIL import Image
from argparse import ArgumentParser
from sys import stderr

def print_err(*args, **kwargs):
    print(*args, file=stderr, **kwargs)

class Fb360Converter:
	def __init__(self, inputFile, outputFile, imgOutMaxWidth=None, imgOutRatio=None):
		self.mInFile=inputFile
		self.mOutFile=outputFile
		self.mOutImgMaxWidth=imgOutMaxWidth
		self.mOutImgRatio=imgOutRatio
		
		self.mImgIn = None
		self.mImgInReady = False
		
		self.mImgOut = None
		self.mImgOutReady = False
		
		if self.mOutFile == None:
			self.mOutFile = "FB_out.jpg" 
			
		if self.mOutImgMaxWidth == None:
			self.mOutImgMaxWidth = 6000
		
		if self.mOutImgRatio == None:
			self.mOutImgRatio = 2 
			
		#print("Fb360Converter.init() args=" + self.mInFile, self.mOutFile, self.mOutImgMaxWidth, self.mOutImgRatio)
		
	#load input image
	def load(self):
		#print("Fb360Converter.load()")
		
		self.mImgInReady = False
		self.mImgOutReady = False
		try:
			self.mImgIn = Image.open(self.mInFile)
		except Exception as e:
			print_err("Failed to load input image! error=", e)
			return
		
		self.mImgInReady = True
		
	#convert image	
	def convert(self):
		#print("Fb360Converter.convert()")
		
		if not self.mImgInReady:
			print_err("Input image is not ready! Call load() first!")
		else:
			#prepare output image
			self.mImgOutReady = False
			try:
				w=min(self.mOutImgMaxWidth, self.mImgIn.size[0])
				h=int(w/self.mOutImgRatio)
				self.mImgOut=Image.new('RGB', (w, h), color = 'black')
				
			except Exception as e:
				print_err("Failed to convert output image! error:", e)
				return
			
			#paste input image to output image
			if self.mImgIn.size[1] > self.mImgOut.size[1]:
				self.mImgOut.paste(self.mImgIn.resize(self.mImgOut.size[0], self.mImgOut.size[1], Image.LANCZOS))
			else:
				offset = self.mImgOut.size[1] - self.mImgIn.size[1]
				self.mImgOut.paste(self.mImgIn, (0,offset))
				
			exif_dict = {"0th":{271:b'RICOH', 272:b'RICOH THETA S'}}
			self.mImgOutExif_bytes = piexif.dump(exif_dict)
			
			self.mImgOutReady = True
			
	#save image to disk
	def save(self):
		#print("Fb360Converter.save")
		
		if not self.mImgInReady:
			print_err("Input image is not ready! Call load() first!")
			return
		elif not self.mImgOutReady:
			print_err("Output image is not ready! Call convert() first!")
			return
		else:
			self.mImgOut.save(self.mOutFile, exif=self.mImgOutExif_bytes)
			
						

if __name__ == '__main__':
	argp = ArgumentParser()
	argp.add_argument("inputImage", help="input file")
	argp.add_argument("-o", "--output_image_filename", help="output image file name", dest="outputImg", default=None)
	argp.add_argument("-w", "--output_max_width", help="output image max width", dest="outImgWidth", default=None)
	argp.add_argument("-r", "--output_image_ratio", help="output image ratio", dest="outImgRatio", default=None)
	args = argp.parse_args()
	
	mConv=Fb360Converter(args.inputImage, args.outputImg, args.outImgWidth, args.outImgRatio)
	mConv.load()
	mConv.convert()
	mConv.save()
