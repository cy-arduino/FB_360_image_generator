# FB_360_image_generator
360 image generator for Facebook

## Facebook's requirement:
1. smaller than 6000 × 3000 pixels
1. ratio: 
    * 2:1
1. exif:
    * make: RICOH
    * model: RICOH THETA S


image process flow
1. Get DJI Mavic's panorama images(34 pics)
1. Stich images by Microsoft ICE(Image Composite Editor)
    * projection mode: Spherical
1. Use FB_360_image_generator to generate a image that can be accepted by Facebook!
