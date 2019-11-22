import logging
from argparse import ArgumentParser
from cy_panorama import Panorama

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("input_img", help="input image file name")
    parser.add_argument("-o", "--output_img", help="output image file name",
                        dest="output_img", default=None)
    parser.add_argument("-b", "--bg_color", help="background color",
                        dest="bg_color", default=None)
    args = parser.parse_args()

    LOG_FMT = "%(asctime)s [%(levelname)s] " \
              "%(filename)s:%(lineno)s %(name)s %(funcName)s() : %(message)s"
    logging.basicConfig(level=logging.DEBUG, format=LOG_FMT)

    p = Panorama(args.input_img)
    p.convert_fb(args.output_img, args.bg_color)
