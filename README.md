# Panorama converter for Facebook
Panorama converter for Facebook

## TODO
1. Make a package and upload to pypi
   * https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56
1. Stitch images automatically

## usage
* convert.py [-h] [-o OUTPUTIMG] [-w IMGOUTWIDTH] [-b IMGBGCOLOR] inputImage
   * inputImage: A Panorama image with Spherical projection
   * OUTPUTIMG: A Panorama image that can be accepted by Facebook
* example: 
   * python convert.py examples\PANO0001_stitch.jpg -o out.jpg

### Requirements of Facebook's Panaroma image:
* smaller than 6000 × 3000 pixels
* ratio(width:height): 
   * 2:1
* exif:
   * make: RICOH
   * model: RICOH THETA S

### How to generate  Panorama image with Spherical projection
1. Get DJI Mavic's panorama images(34 pics)
1. Stitch images by Microsoft ICE(Image Composite Editor)
   * projection mode: Spherical
