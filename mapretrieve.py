import os
import requests
import csv
from sensitive import *

#Google Streetview API base URL
BASE_URL = 'https://maps.googleapis.com/maps/api/streetview'

#Output path from retrieved images
OUTPUT_PATH = r"./images"

#Proxy configuration dictionary
PROXIES = {}


def imsize_string(imsize):
    """imsize_string

    Converts a (Width x Height) tuple into a string conforming to Google Streetview API
    requirements.

    :param imsize: A size 2 tuple containing the dimensions of the image
    :return: String containing the required size

    >> imsize_string((100,250))
    "100x250"

    """
    return "{0}x{1}".format(*imsize)


def request_params(address, imsize, heading=None):
    """request_params

    Returns the dictionary containing the necessary arguments for the Streetview API call.
    See requests module documentation and the Streetview API documentation (below) for more
    information.

    request.get: http://docs.python-requests.org/en/master/api/#requests.get
    Streetview API: https://developers.google.com/maps/documentation/streetview/

    :param address: A string containing the address being searched on Google Streetview API
    :param imsize: A tuple containing the desired image size (Default value: (244,244))
    :param heading: The compass heading of the image, in degrees. A None value defaults heading
    to the automatic Google Streetview heading (Default value: None)
    :return: Request parameter dictionary
    """
    ret = {
            'size': imsize_string(imsize),
            'key': API_KEY,
            'location': address
        }
    if heading:
        ret['heading'] = heading
    return ret

def retrieve_image(address,imsize=(244,244),heading=None):
    """retrieve_image

    Wrap-up the call to Google Streetview API, handling the communication.
    No error checking is done.

    :param address: A string containing the address being searched on Google Streetview API
    :param imsize: A tuple containing the desired image size (Default value: (244,244))
    :param heading: The compass heading of the image, in degrees. A None value defaults heading
    to the automatic Google Streetview heading (Default value: None)
    :return: Requests object containing the response from the server
    """
    return requests.get(
        BASE_URL,
        params=request_params(address,imsize,heading=heading),
        proxies=PROXIES
    )

def image_filename(cod_setor, coord_id, heading=None):
    """image_filename

    Returns the agreed upon image filename format (IMG_[ID]_[HEADING].jpg)

     >> image_filename(1,60)
     "IMG_00001_060.jpg"
     >> image_filename(15,None)
     "IMG_0015.jpg"

    :param cod_setor: Census sector identifier
    :param coord_id: Unique coordinate ID on that census sector
    :param heading: Optional compass heading identifier (Default: None)
    :return: String following the agreed upon filename format
    """
    if heading is not None:
        return "IMG_{cod_setor:15d}_{coord_id:03d}_{heading:03d}.jpg".format(cod_setor=cod_setor,coord_id=coord_id,heading=heading)
    else:
        return "IMG_{cod_setor:15d}_{coord_id:03d}.jpg".format(cod_setor=cod_setor,coord_id=coord_id)

def retrieve_address(cod_setor, coord_id, address, output_path = "./images", imsize=(244,244), headings=[None]):
    """retrieve_address

    Retrieves images from a Streetview panorama at a given address. The images
    are saved to disk on the output_path location, and are named after the ID
    and HEADING identifiers.

    :param cod_setor: Census Sector Identifier
    :param coord_id: Unique coordinate ID on that census sector
    :param address: Address being searched
    :param imsize: Size two tuple containing the desired images dimensions (Default: (244,244))
    :param headings: A list with the desired headings. A None value defaults to the automatic
    Google Streetview heading (Default: [None])
    :return: None

    """
    for heading in headings:
        r = retrieve_image(address,imsize=imsize,heading=heading)
        if r.status_code == 200:
            folderpath = os.path.join(output_path,str(cod_setor))
            if not os.path.exists(folderpath):
                os.makedirs(folderpath)
            filepath = os.path.join(folderpath,image_filename(cod_setor, coord_id, heading=heading))
            with open(filepath,"wb") as f:
                for chunk in r:
                    f.write(chunk)

def ingest_csv(input):
    return (int(input[0]), int(input[1]), float(input[2]), float(input[3]))

def format_lat_long(lat, long):
    return "{lat},{long}".format(lat=lat,long=long)

def retrieve_geo_csv(fpath, output_path="./images", imsize=(244,244)):
    """retrieve_csv

    Retrieves all images listed on a csv file. This file must have the following three
    semicolon separated fields, with no headers.

    [1] COD_SETOR: Numerical Image Identifier
    [2] COORD_ID: Coordinate Unique ID over the Census Sector
    [3] LAT: Latitude
    [4] LNG: Longitude

    :param fpath: Path to the input CSV
    :param imsize: Size two tuple containing the desired images dimensions (Default: (244,244))
    :return: None
    """

    with open(fpath,"r") as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            cod_setor, coord_id, lat, long = ingest_csv(row)
            retrieve_address(cod_setor, coord_id, format_lat_long(lat,long), imsize=imsize, output_path=output_path)