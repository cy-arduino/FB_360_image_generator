# Panorama converter for Facebook
Panorama converter for Facebook

## TODO
1. make a package and upload to pypi
    * https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56
1. stich image automatically
1. add more parameters
1. refactor

## usage
* convert.py [-h] [-o OUTPUTIMG] [-w IMGOUTWIDTH] [-b IMGBGCOLOR] inputImage
   * inputImage: A Panorama image with Spherical projection
   * OUTPUTIMG: A Panorama image that can be accepted by Facebook
* example: 
   * python convert.py example\PANO0001_stitch.jpg  -o example\out.jpg


### requirements of Facebook's Panaroma image:
1. smaller than 6000 × 3000 pixels
1. ratio: 
    * 2:1
1. exif:
    * make: RICOH
    * model: RICOH THETA S

### How to generate  Panorama image with Spherical projection
1. Get DJI Mavic's panorama images(34 pics)
1. Stich images by Microsoft ICE(Image Composite Editor)
    * projection mode: Spherical
