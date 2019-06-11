from setuptools import setup

setup(
    name='FbPanoramaConverter',
    version='0.2',
    description='Panorama converter for Facebook',
    url='https://github.com/cy-arduino/FB_panoroma_converter',
    author='ChihYing Lin',
    author_email='',
    license='MIT',
    packages=['FbPanoramaConverter'],
    install_requires=['piexif', 'Pillow'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)