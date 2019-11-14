import xmlschema
import requests
import gzip
import os
import tarfile
import json
import config

def download_schema():

    if not os.path.exists("TPS_Schema.xsd.gz"):

        req = requests.get("https://wiki.openraildata.com/images/b/b4/TPS_Schema.xsd.gz", stream=True)

        with open("TPS_Schema.xsd.gz", "wb") as fp:

            for chunk in req.iter_content(1024):

                fp.write(chunk)

def extract_schema():

    if not os.path.exists("TPS_Schema.xsd"):

        with gzip.open("TPS_Schema.xsd.gz", "rb") as in_file, open("TPS_Schema.xsd", "wb") as out_file:

            out_file.write(in_file.read())

def download_data():

    if not os.path.exists("TPS_Data.tar.bz2"):

        url = "http://datafeeds.networkrail.co.uk/ntrod/SupportingFileAuthenticate?type=TPS"
        login = config.email
        password = config.password

        req = requests.get(url, auth=(login, password), stream=True)

        with open("TPS_Data.tar.bz2", "wb") as fp:

            for chunk in req.iter_content(1024):

                fp.write(chunk)


def extract_data():

    if not os.path.exists("TPS_Data.xml"):

        with tarfile.open("TPS_Data.tar.bz2", "r:bz2") as tar:

            for member in tar.getmembers():

                member.path = "TPS_Data.xml"

                tar.extract(member, "")

schema = xmlschema.XMLSchema("TPS_Schema.xsd")

data = schema.to_dict("TPS_Data.xml")

with open("TPS_Data.json", "w") as out_file:

    json.dump(data, out_file)