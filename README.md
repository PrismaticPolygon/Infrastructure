### Schema

The schema can be downloaded [here](https://wiki.openraildata.com/images/b/b4/TPS_Schema.xsd.gz). It contains several
errors, but they can easily be fixed by adding `</xs:element>` tags in the appropriate places. The fixed version is
included in this repository, as well as the original compressed version (`TPS_Schema.xsd.gz`).

### Data

The data can be downloaded [here]("http://datafeeds.networkrail.co.uk/ntrod/SupportingFileAuthenticate?type=TPS"),
although an account with Network Rail is required. The data, when extracted, is approximately 600MB - too large for Git
with enabling LFS. Only the compressed file (`TPS_Data.tar.bz2`) is therefore included in this repository.