import xmlschema
import requests
import gzip
import os
import tarfile

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

def extract_data():

    if not os.path.exists("TPS_Data.xml"):

        with tarfile.open("TPS_Data.tar.bz2", "r:bz2") as tar:

            for member in tar.getmembers():

                member.path = "TPS_Data.xml"

                tar.extract(member, "")


extract_data()

schema = xmlschema.XMLSchema("TPS_Schema.xsd")

print(schema.is_valid("TPS_Data.xml"))
