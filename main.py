import os
import requests

#Google Streetview API Key
API_KEY = 'YOUR_API_KEY_HERE'

#Google Streetview API base URL
BASE_URL = 'https://maps.googleapis.com/maps/api/streetview'

#Output path from retrieved images
OUTPUT_PATH = r"D:\Documents\GitHub\Lobsang\images"


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


def retrieve_image(address,imsize=(244,244),heading=0):
    """retrieve_image

    Wrap-up the call to Google Streetview API, handling the communication.
    No error checking is done.

    :param address: A string containing the address being searched on Google Streetview API
    :param imsize: A tuple containing the desired image size (Default value: (244,244))
    :param heading: The compass heading of the image, in degrees (Default value: 0)
    :return: Requests object containing the response from the server
    """
    return requests.get(
        BASE_URL,
        params={
            'size': imsize_string(imsize),
            'key': API_KEY,
            'location': address,
            'heading' : heading
        }
    )


def retrieve_address(id, address, imsize=(244,244), headings=range(0,360,60)):
    """retrieve_address

    Retrieves images from a Streetview panorama at a given address. The images
    are saved to disk on the OUTPUT_PATH location, and are named after the ID
    and HEADING identifiers.

    :param id: ID identifier for image files
    :param address: Address being searched
    :param imsize: Size two tuple containing the desired images dimensions (Default: (244,244))
    :param headings: A list with the desired headings (Default: range(0,360,60))
    :return: None

    """
    for heading in headings:
        r = retrieve_image(address,imsize=imsize,heading=heading)
        if r.status_code == 200:
            filepath = OUTPUT_PATH + "\IMG_{id:06d}_{heading:03d}.jpg".format(id=id,heading=heading)
            with open(filepath,"wb") as f:
                for chunk in r:
                    f.write(chunk)