from os.path import dirname, join
from setuptools import setup


def read(fname):
    return open(join(dirname(__file__), fname)).read()


with open("requirements.txt", "r'") as f:
    install_reqs = f.readlines()

setup(name='pyradar',
      version='0.8.0',
      author="Chad Dotson",
      author_email="chad@cdotson.com",
      description="Tools for downloading and overlaying radar images from the NOAA Ridge radar site.",
      license="GNUv3",
      keywords="noaa radar weather",
      url="https://github.com/chaddotson/py-radar",
      packages=['pyradar', 'scripts'],
      long_description=read("README.txt"),
      install_requires=install_reqs,
      include_package_data=True,
      entry_points={
          'console_scripts': [
              'fetch_radar_image_cli = scripts.fetch_radar_image_cli:main',
          ]
      },
      classifiers=[
          "Development Status :: 4 - Beta",
          "Topic :: Utilities",
          "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
      ],
)
