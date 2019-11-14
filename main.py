import xmlschema
import requests
import gzip
import os

def download():

    if not os.path.exists("TPS_Schema.xsd.gz"):

        req = requests.get("https://wiki.openraildata.com/images/b/b4/TPS_Schema.xsd.gz", stream=True)

        with open("TPS_Schema.xsd.gz", "wb") as fp:

            for chunk in req.iter_content(1024):

                fp.write(chunk)

def extract():

    if not os.path.exists("TPS_Schema.xsd"):

        with gzip.open("TPS_Schema.xsd.gz", "rb") as in_file, open("TPS_Schema.xsd", "wb") as out_file:

            out_file.write(in_file.read())

schema = xmlschema.XMLSchema("TPS_Schema.xsd")


