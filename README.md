# Panaroma converter for Facebook
Panaroma converter for Facebook

## TODO
1. make a package and upload to pypi
    * https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56
1. stich image automatically
1. add more parameters
1. refactor

## usage
* input: A Panaroma image with Spherical projection
* output: A Panaroma image that can be accepted by Facebook


### requirements of Facebook's Panaroma image:
1. smaller than 6000 × 3000 pixels
1. ratio: 
    * 2:1
1. exif:
    * make: RICOH
    * model: RICOH THETA S


### Panorama processing flow
1. Get DJI Mavic's panorama images(34 pics)
1. Stich images by Microsoft ICE(Image Composite Editor)
    * projection mode: Spherical
1. Use FB_360_image_generator to generate a image that can be accepted by Facebook!
