from distutils.core import setup

setup(
    name='prarie',
    packages=['prarie'],
    version='0.1',
    license='GNU',
    description='A middleware for Falcon Framework for encoding and decoding JSON requests and responses',
    author='Lucas Limeira',
    author_email='lucasalveslm@gmail.com',
    url='https://github.com/lucasalveslm/prairie',
    download_url='',
    keywords=['falcon', 'framework', 'json',
              'middleware', 'python', 'python2', 'python3', ],
    install_requires=['falcon', ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.7',
    ]
)
