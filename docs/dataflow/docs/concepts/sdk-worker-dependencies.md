---
url: https://docs.cloud.google.com/dataflow/docs/concepts/sdk-worker-dependencies/
title: SDK and Worker Dependencies \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:05:59.807731+00:00
---

# SDK and Worker Dependencies  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/concepts/sdk-worker-dependencies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  SDK and Worker Dependencies Stay organized with collections  Save and categorize content based on your preferences. 

The Apache Beam SDKs and Dataflow workers depend on common third-party components which then import additional dependencies. The dependencies of the Apache Beam SDKs are preinstalled in the default Dataflow runtime environments.

Some data processing use cases benefit from using additional libraries or classes. In these cases, you might need to manage your pipeline dependencies. For more information about managing dependencies, see [Manage pipeline dependencies in Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/manage-dependencies).

This page contains dependency and worker package information for Apache Beam and Dataflow SDK releases:

  * Apache Beam 2.x SDKs for Java
  * Apache Beam 2.x SDKs for Python
  * Apache Beam 2.x SDKs for Go
  * Cloud Dataflow 2.x SDKs for Java
  * Cloud Dataflow 2.x SDKs for Python
  * Cloud Dataflow 1.x SDKs for Java



## Apache Beam 2.x SDKs

### SDK for Go

Dependency information for Apache Beam SDKs for Go is listed on the [Apache Beam SDK for Go dependencies page](https://beam.apache.org/documentation/sdks/go-dependencies/).

### SDK for Java

Dependency information for Apache Beam SDKs for Java is listed on the [Apache Beam SDK for Java dependencies page](https://beam.apache.org/documentation/sdks/java-dependencies/).

### SDK for Python

Dependency information for Apache Beam SDKs for Python is listed on the [Apache Beam SDK for Python dependencies page](https://beam.apache.org/documentation/sdks/python-dependencies/).

#### Worker dependencies

This section applies to Apache Beam 2.49.0 and earlier. The following tables provide information about the Python dependencies installed on the Dataflow-built workers.

**Note:** Starting in Apache Beam 2.50.0, Dataflow no longer builds a separate container to run Python pipelines. Instead, Dataflow uses the published open source containers. For dependency information for Apache Beam 2.50.0 and later, see the [Apache Beam SDK for Python dependencies page](https://beam.apache.org/documentation/sdks/python-dependencies/). 

#### Version 2.49.0

Dataflow workers have the following packages already installed.

### Python 3.11.4

Package| Version  
---|---  
  
attrs| 23.1.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.12.0  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2023.5.7  
charset-normalizer| 3.1.0  
click| 8.1.3  
cloudpickle| 2.2.1  
crcmod| 1.7  
Cython| 0.29.34  
dill| 0.3.1.1  
dnspython| 2.3.0  
docopt| 0.6.2  
fastavro| 1.7.4  
fasteners| 0.18  
future| 0.18.2  
google-api-core| 2.11.0  
google-apitools| 0.5.31  
google-auth| 2.17.1  
google-auth-httplib2| 0.1.0  
google-cloud-aiplatform| 1.26.1  
google-cloud-bigquery| 3.9.0  
google-cloud-bigquery-storage| 2.19.1  
google-cloud-bigtable| 2.19.0  
google-cloud-core| 2.3.2  
google-cloud-datastore| 2.15.1  
google-cloud-dlp| 3.12.1  
google-cloud-language| 2.9.1  
google-cloud-pubsub| 2.15.2  
google-cloud-pubsublite| 1.7.0  
google-cloud-recommendations-ai| 0.10.3  
google-cloud-resource-manager| 1.10.2  
google-cloud-spanner| 3.30.0  
google-cloud-storage| 2.10.0  
google-cloud-videointelligence| 2.11.1  
google-cloud-vision| 3.4.1  
google-crc32c| 1.5.0  
google-resumable-media| 2.5.0  
googleapis-common-protos| 1.59.1  
grpc-google-iam-v1| 0.12.6  
grpcio| 1.56.0  
grpcio-gcp| 0.2.2  
grpcio-status| 1.56.0  
guppy3| 3.1.3  
hdfs| 2.7.0  
httplib2| 0.22.0  
idna| 3.4  
iniconfig| 2.0.0  
joblib| 1.3.1  
mmh3| 3.1.0  
nltk| 3.8.1  
nose| 1.3.7  
numpy| 1.23.5  
oauth2client| 4.1.3  
objsize| 0.6.1  
orjson| 3.9.1  
overrides| 6.5.0  
packaging| 23.1  
pandas| 1.5.3  
Pillow| 7.2.0  
pip| 23.1.2  
pluggy| 1.2.0  
proto-plus| 1.22.3  
protobuf| 4.23.3  
pyarrow| 11.0.0  
pyasn1| 0.5.0  
pyasn1-modules| 0.3.0  
pydot| 1.4.2  
pymongo| 4.4.0  
pyparsing| 3.1.0  
pytest| 7.2.2  
python-dateutil| 2.8.2  
pytz| 2023.3  
PyYAML| 6.0  
regex| 2022.10.31  
requests| 2.28.2  
rsa| 4.9  
scikit-learn| 1.2.2  
scipy| 1.10.1  
setuptools| 65.5.1  
Shapely| 1.8.5.post1  
six| 1.16.0  
soupsieve| 2.4.1  
sqlparse| 0.4.4  
threadpoolctl| 3.1.0  
tqdm| 4.65.0  
typing_extensions| 4.5.0  
urllib3| 1.26.16  
wheel| 0.40.0  
zstandard| 0.20.0  
  
### Python 3.10.12

Package| Version  
---|---  
  
attrs| 23.1.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.12.0  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2023.5.7  
charset-normalizer| 3.1.0  
click| 8.1.3  
cloudpickle| 2.2.1  
crcmod| 1.7  
Cython| 0.29.34  
dill| 0.3.1.1  
dnspython| 2.3.0  
docopt| 0.6.2  
exceptiongroup| 1.1.2  
fastavro| 1.7.4  
fasteners| 0.18  
future| 0.18.2  
google-api-core| 2.11.0  
google-api-python-client| 2.92.0  
google-apitools| 0.5.31  
google-auth| 2.17.1  
google-auth-httplib2| 0.1.0  
google-cloud-aiplatform| 1.26.1  
google-cloud-bigquery| 3.9.0  
google-cloud-bigquery-storage| 2.19.1  
google-cloud-bigtable| 2.19.0  
google-cloud-core| 2.3.2  
google-cloud-datastore| 2.15.1  
google-cloud-dlp| 3.12.1  
google-cloud-language| 2.9.1  
google-cloud-profiler| 4.0.0  
google-cloud-pubsub| 2.15.2  
google-cloud-pubsublite| 1.7.0  
google-cloud-recommendations-ai| 0.10.3  
google-cloud-resource-manager| 1.10.2  
google-cloud-spanner| 3.30.0  
google-cloud-storage| 2.10.0  
google-cloud-videointelligence| 2.11.1  
google-cloud-vision| 3.4.1  
google-crc32c| 1.5.0  
google-resumable-media| 2.5.0  
googleapis-common-protos| 1.59.1  
grpc-google-iam-v1| 0.12.6  
grpcio| 1.56.0  
grpcio-gcp| 0.2.2  
grpcio-status| 1.56.0  
guppy3| 3.1.3  
hdfs| 2.7.0  
httplib2| 0.22.0  
idna| 3.4  
iniconfig| 2.0.0  
joblib| 1.3.1  
mmh3| 3.1.0  
nltk| 3.8.1  
nose| 1.3.7  
numpy| 1.23.5  
oauth2client| 4.1.3  
objsize| 0.6.1  
orjson| 3.9.1  
overrides| 6.5.0  
packaging| 23.1  
pandas| 1.5.3  
Pillow| 7.2.0  
pip| 23.1.2  
pluggy| 1.2.0  
proto-plus| 1.22.3  
protobuf| 4.23.3  
pyarrow| 11.0.0  
pyasn1| 0.5.0  
pyasn1-modules| 0.3.0  
pydot| 1.4.2  
pymongo| 4.4.0  
pyparsing| 3.1.0  
pytest| 7.2.2  
python-dateutil| 2.8.2  
python-snappy| 0.6.1  
pytz| 2023.3  
PyYAML| 6.0  
regex| 2022.10.31  
requests| 2.28.2  
rsa| 4.9  
scikit-learn| 1.2.2  
scipy| 1.10.1  
setuptools| 65.5.1  
Shapely| 1.8.5.post1  
six| 1.16.0  
soupsieve| 2.4.1  
sqlparse| 0.4.4  
threadpoolctl| 3.1.0  
tomli| 2.0.1  
tqdm| 4.65.0  
typing_extensions| 4.5.0  
uritemplate| 4.1.1  
urllib3| 1.26.16  
wheel| 0.40.0  
zstandard| 0.20.0  
  
### Python 3.9.17

Package| Version  
---|---  
  
attrs| 23.1.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.12.0  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2023.5.7  
charset-normalizer| 3.1.0  
click| 8.1.3  
cloudpickle| 2.2.1  
crcmod| 1.7  
Cython| 0.29.34  
dill| 0.3.1.1  
dnspython| 2.3.0  
docopt| 0.6.2  
exceptiongroup| 1.1.2  
fastavro| 1.7.4  
fasteners| 0.18  
future| 0.18.2  
google-api-core| 2.11.0  
google-api-python-client| 2.92.0  
google-apitools| 0.5.31  
google-auth| 2.17.1  
google-auth-httplib2| 0.1.0  
google-cloud-aiplatform| 1.26.1  
google-cloud-bigquery| 3.9.0  
google-cloud-bigquery-storage| 2.19.1  
google-cloud-bigtable| 2.19.0  
google-cloud-core| 2.3.2  
google-cloud-datastore| 2.15.1  
google-cloud-dlp| 3.12.1  
google-cloud-language| 2.9.1  
google-cloud-profiler| 4.0.0  
google-cloud-pubsub| 2.15.2  
google-cloud-pubsublite| 1.7.0  
google-cloud-recommendations-ai| 0.10.3  
google-cloud-resource-manager| 1.10.2  
google-cloud-spanner| 3.30.0  
google-cloud-storage| 2.10.0  
google-cloud-videointelligence| 2.11.1  
google-cloud-vision| 3.4.1  
google-crc32c| 1.5.0  
google-resumable-media| 2.5.0  
googleapis-common-protos| 1.59.1  
grpc-google-iam-v1| 0.12.6  
grpcio| 1.56.0  
grpcio-gcp| 0.2.2  
grpcio-status| 1.56.0  
guppy3| 3.1.3  
hdfs| 2.7.0  
httplib2| 0.22.0  
idna| 3.4  
iniconfig| 2.0.0  
joblib| 1.3.1  
mmh3| 3.1.0  
nltk| 3.8.1  
nose| 1.3.7  
numpy| 1.23.5  
oauth2client| 4.1.3  
objsize| 0.6.1  
orjson| 3.9.1  
overrides| 6.5.0  
packaging| 23.1  
pandas| 1.5.3  
Pillow| 7.2.0  
pip| 23.1.2  
pluggy| 1.2.0  
proto-plus| 1.22.3  
protobuf| 4.23.3  
pyarrow| 11.0.0  
pyasn1| 0.5.0  
pyasn1-modules| 0.3.0  
pydot| 1.4.2  
pymongo| 4.4.0  
pyparsing| 3.1.0  
pytest| 7.2.2  
python-dateutil| 2.8.2  
python-snappy| 0.6.1  
pytz| 2023.3  
PyYAML| 6.0  
regex| 2022.10.31  
requests| 2.28.2  
rsa| 4.9  
scikit-learn| 1.2.2  
scipy| 1.10.1  
setuptools| 58.1.0  
Shapely| 1.8.5.post1  
six| 1.16.0  
soupsieve| 2.4.1  
sqlparse| 0.4.4  
threadpoolctl| 3.1.0  
tomli| 2.0.1  
tqdm| 4.65.0  
typing_extensions| 4.5.0  
uritemplate| 4.1.1  
urllib3| 1.26.16  
wheel| 0.40.0  
zstandard| 0.20.0  
  
### Python 3.8.17

Package| Version  
---|---  
  
attrs| 23.1.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.12.0  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2023.5.7  
charset-normalizer| 3.1.0  
click| 8.1.3  
cloudpickle| 2.2.1  
crcmod| 1.7  
Cython| 0.29.34  
dill| 0.3.1.1  
dnspython| 2.3.0  
docopt| 0.6.2  
exceptiongroup| 1.1.2  
fastavro| 1.7.4  
fasteners| 0.18  
future| 0.18.2  
google-api-core| 2.11.0  
google-api-python-client| 2.92.0  
google-apitools| 0.5.31  
google-auth| 2.17.1  
google-auth-httplib2| 0.1.0  
google-cloud-aiplatform| 1.26.1  
google-cloud-bigquery| 3.9.0  
google-cloud-bigquery-storage| 2.19.1  
google-cloud-bigtable| 2.19.0  
google-cloud-core| 2.3.2  
google-cloud-datastore| 2.15.1  
google-cloud-dlp| 3.12.1  
google-cloud-language| 2.9.1  
google-cloud-profiler| 4.0.0  
google-cloud-pubsub| 2.15.2  
google-cloud-pubsublite| 1.7.0  
google-cloud-recommendations-ai| 0.10.3  
google-cloud-resource-manager| 1.10.2  
google-cloud-spanner| 3.30.0  
google-cloud-storage| 2.10.0  
google-cloud-videointelligence| 2.11.1  
google-cloud-vision| 3.4.1  
google-crc32c| 1.5.0  
google-resumable-media| 2.5.0  
googleapis-common-protos| 1.59.1  
grpc-google-iam-v1| 0.12.6  
grpcio| 1.56.0  
grpcio-gcp| 0.2.2  
grpcio-status| 1.56.0  
guppy3| 3.1.3  
hdfs| 2.7.0  
httplib2| 0.22.0  
idna| 3.4  
iniconfig| 2.0.0  
joblib| 1.3.1  
mmh3| 3.1.0  
nltk| 3.8.1  
nose| 1.3.7  
numpy| 1.23.5  
oauth2client| 4.1.3  
objsize| 0.6.1  
orjson| 3.9.1  
overrides| 6.5.0  
packaging| 23.1  
pandas| 1.5.3  
Pillow| 7.2.0  
pip| 23.1.2  
pluggy| 1.2.0  
proto-plus| 1.22.3  
protobuf| 4.23.3  
pyarrow| 11.0.0  
pyasn1| 0.5.0  
pyasn1-modules| 0.3.0  
pydot| 1.4.2  
pymongo| 4.4.0  
pyparsing| 3.1.0  
pytest| 7.2.2  
python-dateutil| 2.8.2  
python-snappy| 0.6.1  
pytz| 2023.3  
PyYAML| 6.0  
regex| 2022.10.31  
requests| 2.28.2  
rsa| 4.9  
scikit-learn| 1.2.2  
scipy| 1.10.1  
setuptools| 57.5.0  
Shapely| 1.8.5.post1  
six| 1.16.0  
soupsieve| 2.4.1  
sqlparse| 0.4.4  
threadpoolctl| 3.1.0  
tomli| 2.0.1  
tqdm| 4.65.0  
typing_extensions| 4.5.0  
uritemplate| 4.1.1  
urllib3| 1.26.16  
wheel| 0.40.0  
zstandard| 0.20.0  
  
#### Version 2.48.0

Dataflow workers have the following packages already installed.

### Python 3.11.3

Package| Version  
---|---  
  
attrs| 23.1.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.12.0  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2022.12.7  
charset-normalizer| 3.1.0  
click| 8.1.3  
cloudpickle| 2.2.1  
crcmod| 1.7  
Cython| 0.29.34  
dill| 0.3.1.1  
dnspython| 2.3.0  
docopt| 0.6.2  
fastavro| 1.7.3  
fasteners| 0.18  
future| 0.18.2  
google-api-core| 2.11.0  
google-apitools| 0.5.31  
google-auth| 2.17.1  
google-auth-httplib2| 0.1.0  
google-cloud-bigquery| 3.9.0  
google-cloud-bigquery-storage| 2.19.1  
google-cloud-bigtable| 2.17.0  
google-cloud-core| 2.3.2  
google-cloud-datastore| 2.15.1  
google-cloud-dlp| 3.12.1  
google-cloud-language| 2.9.1  
google-cloud-pubsub| 2.15.2  
google-cloud-pubsublite| 1.7.0  
google-cloud-recommendations-ai| 0.10.3  
google-cloud-spanner| 3.30.0  
google-cloud-videointelligence| 2.11.1  
google-cloud-vision| 3.4.1  
google-crc32c| 1.5.0  
google-resumable-media| 2.5.0  
googleapis-common-protos| 1.59.0  
grpc-google-iam-v1| 0.12.6  
grpcio| 1.54.0  
grpcio-gcp| 0.2.2  
grpcio-status| 1.54.0  
hdfs| 2.7.0  
httplib2| 0.21.0  
idna| 3.4  
iniconfig| 2.0.0  
joblib| 1.2.0  
mmh3| 3.1.0  
nltk| 3.8.1  
nose| 1.3.7  
numpy| 1.23.5  
oauth2client| 4.1.3  
objsize| 0.6.1  
orjson| 3.8.9  
overrides| 6.5.0  
packaging| 23.1  
pandas| 1.5.3  
Pillow| 7.2.0  
pip| 23.1.2  
pluggy| 1.0.0  
proto-plus| 1.22.2  
protobuf| 4.22.1  
pyarrow| 11.0.0  
pyasn1| 0.5.0  
pyasn1-modules| 0.3.0  
pydot| 1.4.2  
pymongo| 4.3.3  
pyparsing| 3.0.9  
pytest| 7.2.2  
python-dateutil| 2.8.2  
pytz| 2023.3  
PyYAML| 6.0  
regex| 2022.10.31  
requests| 2.28.2  
rsa| 4.9  
scikit-learn| 1.2.2  
scipy| 1.10.1  
setuptools| 65.5.1  
six| 1.16.0  
soupsieve| 2.4.1  
sqlparse| 0.4.4  
threadpoolctl| 3.1.0  
tqdm| 4.65.0  
typing_extensions| 4.5.0  
urllib3| 1.26.15  
wheel| 0.40.0  
zstandard| 0.20.0  
  
### Python 3.10.11

Package| Version  
---|---  
  
attrs| 23.1.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.12.0  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2022.12.7  
charset-normalizer| 3.1.0  
click| 8.1.3  
cloudpickle| 2.2.1  
crcmod| 1.7  
Cython| 0.29.34  
dill| 0.3.1.1  
dnspython| 2.3.0  
docopt| 0.6.2  
exceptiongroup| 1.1.1  
fastavro| 1.7.3  
fasteners| 0.18  
future| 0.18.2  
google-api-core| 2.11.0  
google-api-python-client| 2.86.0  
google-apitools| 0.5.31  
google-auth| 2.17.1  
google-auth-httplib2| 0.1.0  
google-cloud-bigquery| 3.9.0  
google-cloud-bigquery-storage| 2.19.1  
google-cloud-bigtable| 2.17.0  
google-cloud-core| 2.3.2  
google-cloud-datastore| 2.15.1  
google-cloud-dlp| 3.12.1  
google-cloud-language| 2.9.1  
google-cloud-profiler| 4.0.0  
google-cloud-pubsub| 2.15.2  
google-cloud-pubsublite| 1.7.0  
google-cloud-recommendations-ai| 0.10.3  
google-cloud-spanner| 3.30.0  
google-cloud-videointelligence| 2.11.1  
google-cloud-vision| 3.4.1  
google-crc32c| 1.5.0  
google-resumable-media| 2.5.0  
googleapis-common-protos| 1.59.0  
grpc-google-iam-v1| 0.12.6  
grpcio| 1.54.0  
grpcio-gcp| 0.2.2  
grpcio-status| 1.54.0  
guppy3| 3.1.2  
hdfs| 2.7.0  
httplib2| 0.21.0  
idna| 3.4  
iniconfig| 2.0.0  
joblib| 1.2.0  
mmh3| 3.1.0  
nltk| 3.8.1  
nose| 1.3.7  
numpy| 1.23.5  
oauth2client| 4.1.3  
objsize| 0.6.1  
orjson| 3.8.9  
overrides| 6.5.0  
packaging| 23.1  
pandas| 1.5.3  
Pillow| 7.2.0  
pip| 23.1.2  
pluggy| 1.0.0  
proto-plus| 1.22.2  
protobuf| 4.22.1  
pyarrow| 11.0.0  
pyasn1| 0.5.0  
pyasn1-modules| 0.3.0  
pydot| 1.4.2  
pymongo| 4.3.3  
pyparsing| 3.0.9  
pytest| 7.2.2  
python-dateutil| 2.8.2  
python-snappy| 0.6.1  
pytz| 2023.3  
PyYAML| 6.0  
regex| 2022.10.31  
requests| 2.28.2  
rsa| 4.9  
scikit-learn| 1.2.2  
scipy| 1.10.1  
setuptools| 65.5.1  
six| 1.16.0  
soupsieve| 2.4.1  
sqlparse| 0.4.4  
threadpoolctl| 3.1.0  
tomli| 2.0.1  
tqdm| 4.65.0  
typing_extensions| 4.5.0  
uritemplate| 4.1.1  
urllib3| 1.26.15  
wheel| 0.40.0  
zstandard| 0.20.0  
  
### Python 3.9.16

Package| Version  
---|---  
  
attrs| 23.1.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.12.0  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2022.12.7  
charset-normalizer| 3.1.0  
click| 8.1.3  
cloudpickle| 2.2.1  
crcmod| 1.7  
Cython| 0.29.34  
dill| 0.3.1.1  
dnspython| 2.3.0  
docopt| 0.6.2  
exceptiongroup| 1.1.1  
fastavro| 1.7.3  
fasteners| 0.18  
future| 0.18.2  
google-api-core| 2.11.0  
google-api-python-client| 2.86.0  
google-apitools| 0.5.31  
google-auth| 2.17.1  
google-auth-httplib2| 0.1.0  
google-cloud-bigquery| 3.9.0  
google-cloud-bigquery-storage| 2.19.1  
google-cloud-bigtable| 2.17.0  
google-cloud-core| 2.3.2  
google-cloud-datastore| 2.15.1  
google-cloud-dlp| 3.12.1  
google-cloud-language| 2.9.1  
google-cloud-profiler| 4.0.0  
google-cloud-pubsub| 2.15.2  
google-cloud-pubsublite| 1.7.0  
google-cloud-recommendations-ai| 0.10.3  
google-cloud-spanner| 3.30.0  
google-cloud-videointelligence| 2.11.1  
google-cloud-vision| 3.4.1  
google-crc32c| 1.5.0  
google-resumable-media| 2.5.0  
googleapis-common-protos| 1.59.0  
grpc-google-iam-v1| 0.12.6  
grpcio| 1.54.0  
grpcio-gcp| 0.2.2  
grpcio-status| 1.54.0  
guppy3| 3.1.2  
hdfs| 2.7.0  
httplib2| 0.21.0  
idna| 3.4  
iniconfig| 2.0.0  
joblib| 1.2.0  
mmh3| 3.1.0  
nltk| 3.8.1  
nose| 1.3.7  
numpy| 1.23.5  
oauth2client| 4.1.3  
objsize| 0.6.1  
orjson| 3.8.9  
overrides| 6.5.0  
packaging| 23.1  
pandas| 1.5.3  
Pillow| 7.2.0  
pip| 23.1.2  
pluggy| 1.0.0  
proto-plus| 1.22.2  
protobuf| 4.22.1  
pyarrow| 11.0.0  
pyasn1| 0.5.0  
pyasn1-modules| 0.3.0  
pydot| 1.4.2  
pymongo| 4.3.3  
pyparsing| 3.0.9  
pytest| 7.2.2  
python-dateutil| 2.8.2  
python-snappy| 0.6.1  
pytz| 2023.3  
PyYAML| 6.0  
regex| 2022.10.31  
requests| 2.28.2  
rsa| 4.9  
scikit-learn| 1.2.2  
scipy| 1.10.1  
setuptools| 58.1.0  
six| 1.16.0  
soupsieve| 2.4.1  
sqlparse| 0.4.4  
threadpoolctl| 3.1.0  
tomli| 2.0.1  
tqdm| 4.65.0  
typing_extensions| 4.5.0  
uritemplate| 4.1.1  
urllib3| 1.26.15  
wheel| 0.40.0  
zstandard| 0.20.0  
  
### Python 3.8.16

Package| Version  
---|---  
  
attrs| 23.1.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.12.0  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2022.12.7  
charset-normalizer| 3.1.0  
click| 8.1.3  
cloudpickle| 2.2.1  
crcmod| 1.7  
Cython| 0.29.34  
dill| 0.3.1.1  
dnspython| 2.3.0  
docopt| 0.6.2  
exceptiongroup| 1.1.1  
fastavro| 1.7.3  
fasteners| 0.18  
future| 0.18.2  
google-api-core| 2.11.0  
google-api-python-client| 2.86.0  
google-apitools| 0.5.31  
google-auth| 2.17.1  
google-auth-httplib2| 0.1.0  
google-cloud-bigquery| 3.9.0  
google-cloud-bigquery-storage| 2.19.1  
google-cloud-bigtable| 2.17.0  
google-cloud-core| 2.3.2  
google-cloud-datastore| 2.15.1  
google-cloud-dlp| 3.12.1  
google-cloud-language| 2.9.1  
google-cloud-profiler| 4.0.0  
google-cloud-pubsub| 2.15.2  
google-cloud-pubsublite| 1.7.0  
google-cloud-recommendations-ai| 0.10.3  
google-cloud-spanner| 3.30.0  
google-cloud-videointelligence| 2.11.1  
google-cloud-vision| 3.4.1  
google-crc32c| 1.5.0  
google-resumable-media| 2.5.0  
googleapis-common-protos| 1.59.0  
grpc-google-iam-v1| 0.12.6  
grpcio| 1.54.0  
grpcio-gcp| 0.2.2  
grpcio-status| 1.54.0  
guppy3| 3.1.2  
hdfs| 2.7.0  
httplib2| 0.21.0  
idna| 3.4  
iniconfig| 2.0.0  
joblib| 1.2.0  
mmh3| 3.1.0  
nltk| 3.8.1  
nose| 1.3.7  
numpy| 1.23.5  
oauth2client| 4.1.3  
objsize| 0.6.1  
orjson| 3.8.9  
overrides| 6.5.0  
packaging| 23.1  
pandas| 1.5.3  
Pillow| 7.2.0  
pip| 23.1.2  
pluggy| 1.0.0  
proto-plus| 1.22.2  
protobuf| 4.22.1  
pyarrow| 11.0.0  
pyasn1| 0.5.0  
pyasn1-modules| 0.3.0  
pydot| 1.4.2  
pymongo| 4.3.3  
pyparsing| 3.0.9  
pytest| 7.2.2  
python-dateutil| 2.8.2  
python-snappy| 0.6.1  
pytz| 2023.3  
PyYAML| 6.0  
regex| 2022.10.31  
requests| 2.28.2  
rsa| 4.9  
scikit-learn| 1.2.2  
scipy| 1.10.1  
setuptools| 57.5.0  
six| 1.16.0  
soupsieve| 2.4.1  
sqlparse| 0.4.4  
threadpoolctl| 3.1.0  
tomli| 2.0.1  
tqdm| 4.65.0  
typing_extensions| 4.5.0  
uritemplate| 4.1.1  
urllib3| 1.26.15  
wheel| 0.40.0  
zstandard| 0.20.0  
  
### Python 3.7.16

Package| Version  
---|---  
  
attrs| 23.1.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.12.0  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2022.12.7  
charset-normalizer| 3.1.0  
click| 8.1.3  
cloudpickle| 2.2.1  
crcmod| 1.7  
Cython| 0.29.34  
dill| 0.3.1.1  
dnspython| 2.3.0  
docopt| 0.6.2  
exceptiongroup| 1.1.1  
fastavro| 1.7.3  
fasteners| 0.18  
future| 0.18.2  
google-api-core| 2.11.0  
google-api-python-client| 2.86.0  
google-apitools| 0.5.31  
google-auth| 2.17.1  
google-auth-httplib2| 0.1.0  
google-cloud-bigquery| 3.9.0  
google-cloud-bigquery-storage| 2.19.1  
google-cloud-bigtable| 2.17.0  
google-cloud-core| 2.3.2  
google-cloud-datastore| 2.15.1  
google-cloud-dlp| 3.12.1  
google-cloud-language| 2.9.1  
google-cloud-profiler| 4.0.0  
google-cloud-pubsub| 2.15.2  
google-cloud-pubsublite| 1.7.0  
google-cloud-recommendations-ai| 0.10.3  
google-cloud-spanner| 3.30.0  
google-cloud-videointelligence| 2.11.1  
google-cloud-vision| 3.4.1  
google-crc32c| 1.5.0  
google-resumable-media| 2.5.0  
googleapis-common-protos| 1.59.0  
grpc-google-iam-v1| 0.12.6  
grpcio| 1.54.0  
grpcio-gcp| 0.2.2  
grpcio-status| 1.54.0  
guppy3| 3.1.2  
hdfs| 2.7.0  
httplib2| 0.21.0  
idna| 3.4  
importlib-metadata| 6.6.0  
iniconfig| 2.0.0  
joblib| 1.2.0  
mmh3| 3.1.0  
nltk| 3.8.1  
nose| 1.3.7  
numpy| 1.21.6  
oauth2client| 4.1.3  
objsize| 0.6.1  
orjson| 3.8.9  
overrides| 6.5.0  
packaging| 23.1  
pandas| 1.3.5  
Pillow| 7.2.0  
pip| 23.1.2  
pluggy| 1.0.0  
proto-plus| 1.22.2  
protobuf| 4.22.1  
pyarrow| 11.0.0  
pyasn1| 0.5.0  
pyasn1-modules| 0.3.0  
pydot| 1.4.2  
pymongo| 4.3.3  
pyparsing| 3.0.9  
pytest| 7.2.2  
python-dateutil| 2.8.2  
python-snappy| 0.6.1  
pytz| 2023.3  
PyYAML| 6.0  
regex| 2022.10.31  
requests| 2.28.2  
rsa| 4.9  
scikit-learn| 1.0.2  
scipy| 1.7.3  
setuptools| 57.5.0  
six| 1.16.0  
soupsieve| 2.4.1  
sqlparse| 0.4.4  
threadpoolctl| 3.1.0  
tomli| 2.0.1  
tqdm| 4.65.0  
typing_extensions| 4.5.0  
uritemplate| 4.1.1  
urllib3| 1.26.15  
wheel| 0.40.0  
zipp| 3.15.0  
zstandard| 0.20.0  
  
#### Version 2.47.0

Dataflow workers have the following packages already installed.

### Python 3.7.16

Package| Version  
---|---  
  
attrs| 22.2.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.12.0  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2022.12.7  
charset-normalizer| 3.1.0  
click| 8.1.3  
cloudpickle| 2.2.1  
crcmod| 1.7  
Cython| 0.29.34  
dill| 0.3.1.1  
dnspython| 2.3.0  
docopt| 0.6.2  
exceptiongroup| 1.1.1  
fastavro| 1.7.3  
fasteners| 0.18  
future| 0.18.2  
google-api-core| 2.11.0  
google-api-python-client| 2.84.0  
google-apitools| 0.5.31  
google-auth| 2.17.1  
google-auth-httplib2| 0.1.0  
google-cloud-bigquery| 3.9.0  
google-cloud-bigquery-storage| 2.19.1  
google-cloud-bigtable| 2.17.0  
google-cloud-core| 2.3.2  
google-cloud-datastore| 2.15.1  
google-cloud-dlp| 3.12.1  
google-cloud-language| 2.9.1  
google-cloud-profiler| 4.0.0  
google-cloud-pubsub| 2.15.2  
google-cloud-pubsublite| 1.7.0  
google-cloud-recommendations-ai| 0.10.3  
google-cloud-spanner| 3.30.0  
google-cloud-videointelligence| 2.11.1  
google-cloud-vision| 3.4.1  
google-crc32c| 1.5.0  
google-resumable-media| 2.4.1  
googleapis-common-protos| 1.59.0  
grpc-google-iam-v1| 0.12.6  
grpcio| 1.53.0  
grpcio-gcp| 0.2.2  
grpcio-status| 1.53.0  
guppy3| 3.1.2  
hdfs| 2.7.0  
httplib2| 0.21.0  
idna| 3.4  
importlib-metadata| 6.1.0  
iniconfig| 2.0.0  
joblib| 1.2.0  
mmh3| 3.1.0  
nltk| 3.8.1  
nose| 1.3.7  
numpy| 1.21.6  
oauth2client| 4.1.3  
objsize| 0.6.1  
orjson| 3.8.9  
overrides| 6.5.0  
packaging| 23.0  
pandas| 1.3.5  
Pillow| 7.2.0  
pip| 23.0.1  
pluggy| 1.0.0  
proto-plus| 1.22.2  
protobuf| 4.22.1  
pyarrow| 11.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.2  
pymongo| 4.3.3  
pyparsing| 3.0.9  
pytest| 7.2.2  
python-dateutil| 2.8.2  
python-snappy| 0.6.1  
pytz| 2023.3  
PyYAML| 6.0  
regex| 2022.10.31  
requests| 2.28.2  
rsa| 4.9  
scikit-learn| 1.0.2  
scipy| 1.7.3  
setuptools| 57.5.0  
six| 1.16.0  
soupsieve| 2.4  
sqlparse| 0.4.3  
threadpoolctl| 3.1.0  
tomli| 2.0.1  
tqdm| 4.65.0  
typing_extensions| 4.5.0  
uritemplate| 4.1.1  
urllib3| 1.26.15  
wheel| 0.40.0  
zipp| 3.15.0  
zstandard| 0.20.0  
  
### Python 3.8.16

Package| Version  
---|---  
  
attrs| 22.2.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.12.0  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2022.12.7  
charset-normalizer| 3.1.0  
click| 8.1.3  
cloudpickle| 2.2.1  
crcmod| 1.7  
Cython| 0.29.34  
dill| 0.3.1.1  
dnspython| 2.3.0  
docopt| 0.6.2  
exceptiongroup| 1.1.1  
fastavro| 1.7.3  
fasteners| 0.18  
future| 0.18.2  
google-api-core| 2.11.0  
google-api-python-client| 2.84.0  
google-apitools| 0.5.31  
google-auth| 2.17.1  
google-auth-httplib2| 0.1.0  
google-cloud-bigquery| 3.9.0  
google-cloud-bigquery-storage| 2.19.1  
google-cloud-bigtable| 2.17.0  
google-cloud-core| 2.3.2  
google-cloud-datastore| 2.15.1  
google-cloud-dlp| 3.12.1  
google-cloud-language| 2.9.1  
google-cloud-profiler| 4.0.0  
google-cloud-pubsub| 2.15.2  
google-cloud-pubsublite| 1.7.0  
google-cloud-recommendations-ai| 0.10.3  
google-cloud-spanner| 3.30.0  
google-cloud-videointelligence| 2.11.1  
google-cloud-vision| 3.4.1  
google-crc32c| 1.5.0  
google-resumable-media| 2.4.1  
googleapis-common-protos| 1.59.0  
grpc-google-iam-v1| 0.12.6  
grpcio| 1.53.0  
grpcio-gcp| 0.2.2  
grpcio-status| 1.53.0  
guppy3| 3.1.2  
hdfs| 2.7.0  
httplib2| 0.21.0  
idna| 3.4  
iniconfig| 2.0.0  
joblib| 1.2.0  
mmh3| 3.1.0  
nltk| 3.8.1  
nose| 1.3.7  
numpy| 1.23.5  
oauth2client| 4.1.3  
objsize| 0.6.1  
orjson| 3.8.9  
overrides| 6.5.0  
packaging| 23.0  
pandas| 1.5.3  
Pillow| 7.2.0  
pip| 23.0.1  
pluggy| 1.0.0  
proto-plus| 1.22.2  
protobuf| 4.22.1  
pyarrow| 11.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.2  
pymongo| 4.3.3  
pyparsing| 3.0.9  
pytest| 7.2.2  
python-dateutil| 2.8.2  
python-snappy| 0.6.1  
pytz| 2023.3  
PyYAML| 6.0  
regex| 2022.10.31  
requests| 2.28.2  
rsa| 4.9  
scikit-learn| 1.2.2  
scipy| 1.10.1  
setuptools| 57.5.0  
six| 1.16.0  
soupsieve| 2.4  
sqlparse| 0.4.3  
threadpoolctl| 3.1.0  
tomli| 2.0.1  
tqdm| 4.65.0  
typing_extensions| 4.5.0  
uritemplate| 4.1.1  
urllib3| 1.26.15  
wheel| 0.40.0  
zstandard| 0.20.0  
  
### Python 3.9.16

Package| Version  
---|---  
  
attrs| 22.2.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.12.0  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2022.12.7  
charset-normalizer| 3.1.0  
click| 8.1.3  
cloudpickle| 2.2.1  
crcmod| 1.7  
Cython| 0.29.34  
dill| 0.3.1.1  
dnspython| 2.3.0  
docopt| 0.6.2  
exceptiongroup| 1.1.1  
fastavro| 1.7.3  
fasteners| 0.18  
future| 0.18.2  
google-api-core| 2.11.0  
google-api-python-client| 2.84.0  
google-apitools| 0.5.31  
google-auth| 2.17.1  
google-auth-httplib2| 0.1.0  
google-cloud-bigquery| 3.9.0  
google-cloud-bigquery-storage| 2.19.1  
google-cloud-bigtable| 2.17.0  
google-cloud-core| 2.3.2  
google-cloud-datastore| 2.15.1  
google-cloud-dlp| 3.12.1  
google-cloud-language| 2.9.1  
google-cloud-profiler| 4.0.0  
google-cloud-pubsub| 2.15.2  
google-cloud-pubsublite| 1.7.0  
google-cloud-recommendations-ai| 0.10.3  
google-cloud-spanner| 3.30.0  
google-cloud-videointelligence| 2.11.1  
google-cloud-vision| 3.4.1  
google-crc32c| 1.5.0  
google-resumable-media| 2.4.1  
googleapis-common-protos| 1.59.0  
grpc-google-iam-v1| 0.12.6  
grpcio| 1.53.0  
grpcio-gcp| 0.2.2  
grpcio-status| 1.53.0  
guppy3| 3.1.2  
hdfs| 2.7.0  
httplib2| 0.21.0  
idna| 3.4  
iniconfig| 2.0.0  
joblib| 1.2.0  
mmh3| 3.1.0  
nltk| 3.8.1  
nose| 1.3.7  
numpy| 1.23.5  
oauth2client| 4.1.3  
objsize| 0.6.1  
orjson| 3.8.9  
overrides| 6.5.0  
packaging| 23.0  
pandas| 1.5.3  
Pillow| 7.2.0  
pip| 23.0.1  
pluggy| 1.0.0  
proto-plus| 1.22.2  
protobuf| 4.22.1  
pyarrow| 11.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.2  
pymongo| 4.3.3  
pyparsing| 3.0.9  
pytest| 7.2.2  
python-dateutil| 2.8.2  
python-snappy| 0.6.1  
pytz| 2023.3  
PyYAML| 6.0  
regex| 2022.10.31  
requests| 2.28.2  
rsa| 4.9  
scikit-learn| 1.2.2  
scipy| 1.10.1  
setuptools| 58.1.0  
six| 1.16.0  
soupsieve| 2.4  
sqlparse| 0.4.3  
threadpoolctl| 3.1.0  
tomli| 2.0.1  
tqdm| 4.65.0  
typing_extensions| 4.5.0  
uritemplate| 4.1.1  
urllib3| 1.26.15  
wheel| 0.40.0  
zstandard| 0.20.0  
  
### Python 3.10.10

Package| Version  
---|---  
  
attrs| 22.2.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.12.0  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2022.12.7  
charset-normalizer| 3.1.0  
click| 8.1.3  
cloudpickle| 2.2.1  
crcmod| 1.7  
Cython| 0.29.34  
dill| 0.3.1.1  
dnspython| 2.3.0  
docopt| 0.6.2  
exceptiongroup| 1.1.1  
fastavro| 1.7.3  
fasteners| 0.18  
future| 0.18.2  
google-api-core| 2.11.0  
google-api-python-client| 2.84.0  
google-apitools| 0.5.31  
google-auth| 2.17.1  
google-auth-httplib2| 0.1.0  
google-cloud-bigquery| 3.9.0  
google-cloud-bigquery-storage| 2.19.1  
google-cloud-bigtable| 2.17.0  
google-cloud-core| 2.3.2  
google-cloud-datastore| 2.15.1  
google-cloud-dlp| 3.12.1  
google-cloud-language| 2.9.1  
google-cloud-profiler| 4.0.0  
google-cloud-pubsub| 2.15.2  
google-cloud-pubsublite| 1.7.0  
google-cloud-recommendations-ai| 0.10.3  
google-cloud-spanner| 3.30.0  
google-cloud-videointelligence| 2.11.1  
google-cloud-vision| 3.4.1  
google-crc32c| 1.5.0  
google-resumable-media| 2.4.1  
googleapis-common-protos| 1.59.0  
grpc-google-iam-v1| 0.12.6  
grpcio| 1.53.0  
grpcio-gcp| 0.2.2  
grpcio-status| 1.53.0  
guppy3| 3.1.2  
hdfs| 2.7.0  
httplib2| 0.21.0  
idna| 3.4  
iniconfig| 2.0.0  
joblib| 1.2.0  
mmh3| 3.1.0  
nltk| 3.8.1  
nose| 1.3.7  
numpy| 1.23.5  
oauth2client| 4.1.3  
objsize| 0.6.1  
orjson| 3.8.9  
overrides| 6.5.0  
packaging| 23.0  
pandas| 1.5.3  
Pillow| 7.2.0  
pip| 23.0.1  
pluggy| 1.0.0  
proto-plus| 1.22.2  
protobuf| 4.22.1  
pyarrow| 11.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.2  
pymongo| 4.3.3  
pyparsing| 3.0.9  
pytest| 7.2.2  
python-dateutil| 2.8.2  
python-snappy| 0.6.1  
pytz| 2023.3  
PyYAML| 6.0  
regex| 2022.10.31  
requests| 2.28.2  
rsa| 4.9  
scikit-learn| 1.2.2  
scipy| 1.10.1  
setuptools| 65.5.1  
six| 1.16.0  
soupsieve| 2.4  
sqlparse| 0.4.3  
threadpoolctl| 3.1.0  
tomli| 2.0.1  
tqdm| 4.65.0  
typing_extensions| 4.5.0  
uritemplate| 4.1.1  
urllib3| 1.26.15  
wheel| 0.40.0  
zstandard| 0.20.0  
  
### Python 3.11.3

Package| Version  
---|---  
  
attrs| 23.1.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.12.0  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2022.12.7  
charset-normalizer| 3.1.0  
click| 8.1.3  
cloudpickle| 2.2.1  
crcmod| 1.7  
Cython| 0.29.34  
dill| 0.3.1.1  
dnspython| 2.3.0  
docopt| 0.6.2  
fastavro| 1.7.3  
fasteners| 0.18  
future| 0.18.2  
google-api-core| 2.11.0  
google-apitools| 0.5.31  
google-auth| 2.17.1  
google-auth-httplib2| 0.1.0  
google-cloud-bigquery| 3.9.0  
google-cloud-bigquery-storage| 2.19.1  
google-cloud-bigtable| 2.17.0  
google-cloud-core| 2.3.2  
google-cloud-datastore| 2.15.1  
google-cloud-dlp| 3.12.1  
google-cloud-language| 2.9.1  
google-cloud-pubsub| 2.15.2  
google-cloud-pubsublite| 1.7.0  
google-cloud-recommendations-ai| 0.10.3  
google-cloud-spanner| 3.30.0  
google-cloud-videointelligence| 2.11.1  
google-cloud-vision| 3.4.1  
google-crc32c| 1.5.0  
google-resumable-media| 2.5.0  
googleapis-common-protos| 1.59.0  
grpc-google-iam-v1| 0.12.6  
grpcio| 1.54.0  
grpcio-gcp| 0.2.2  
grpcio-status| 1.54.0  
hdfs| 2.7.0  
httplib2| 0.21.0  
idna| 3.4  
iniconfig| 2.0.0  
joblib| 1.2.0  
mmh3| 3.1.0  
nltk| 3.8.1  
nose| 1.3.7  
numpy| 1.23.5  
oauth2client| 4.1.3  
objsize| 0.6.1  
orjson| 3.8.9  
overrides| 6.5.0  
packaging| 23.1  
pandas| 1.5.3  
Pillow| 7.2.0  
pip| 23.1.1  
pluggy| 1.0.0  
proto-plus| 1.22.2  
protobuf| 4.22.1  
pyarrow| 11.0.0  
pyasn1| 0.5.0  
pyasn1-modules| 0.3.0  
pydot| 1.4.2  
pymongo| 4.3.3  
pyparsing| 3.0.9  
pytest| 7.2.2  
python-dateutil| 2.8.2  
pytz| 2023.3  
PyYAML| 6.0  
regex| 2022.10.31  
requests| 2.28.2  
rsa| 4.9  
scikit-learn| 1.2.2  
scipy| 1.10.1  
setuptools| 65.5.1  
six| 1.16.0  
soupsieve| 2.4.1  
sqlparse| 0.4.4  
threadpoolctl| 3.1.0  
tqdm| 4.65.0  
typing_extensions| 4.5.0  
urllib3| 1.26.15  
wheel| 0.40.0  
zstandard| 0.20.0  
  
#### Version 2.46.0

Dataflow workers have the following packages already installed.

### Python 3.7.16

Package| Version  
---|---  
  
attrs| 22.2.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.11.1  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2022.12.7  
charset-normalizer| 2.0.12  
click| 8.1.3  
cloudpickle| 2.2.1  
crcmod| 1.7  
Cython| 0.29.32  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 1.5.4  
fasteners| 0.18  
future| 0.18.2  
google-api-core| 2.10.2  
google-api-python-client| 2.76.0  
google-apitools| 0.5.31  
google-auth| 2.9.1  
google-auth-httplib2| 0.1.0  
google-cloud-bigquery| 3.3.5  
google-cloud-bigquery-storage| 2.13.2  
google-cloud-bigtable| 1.7.2  
google-cloud-core| 2.3.2  
google-cloud-datastore| 1.15.5  
google-cloud-dlp| 3.8.0  
google-cloud-language| 1.3.2  
google-cloud-profiler| 3.1.0  
google-cloud-pubsub| 2.13.4  
google-cloud-pubsublite| 1.4.2  
google-cloud-recommendations-ai| 0.7.0  
google-cloud-spanner| 3.21.0  
google-cloud-videointelligence| 1.16.3  
google-cloud-vision| 3.1.4  
google-crc32c| 1.5.0  
google-python-cloud-debugger| 2.18  
google-resumable-media| 2.4.1  
googleapis-common-protos| 1.58.0  
grpc-google-iam-v1| 0.12.6  
grpcio| 1.51.1  
grpcio-gcp| 0.2.2  
grpcio-status| 1.48.2  
guppy3| 3.1.2  
hdfs| 2.7.0  
httplib2| 0.21.0  
idna| 3.4  
importlib-metadata| 6.0.0  
iniconfig| 2.0.0  
joblib| 1.2.0  
mmh3| 3.0.0  
nltk| 3.7  
nose| 1.3.7  
numpy| 1.21.6  
oauth2client| 4.1.3  
objsize| 0.6.1  
orjson| 3.7.11  
overrides| 6.5.0  
packaging| 21.3  
pandas| 1.3.5  
Pillow| 7.2.0  
pip| 23.0  
pluggy| 1.0.0  
proto-plus| 1.22.2  
protobuf| 3.20.3  
py| 1.11.0  
pyarrow| 7.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.2  
pymongo| 3.12.3  
pyparsing| 3.0.9  
pytest| 7.1.2  
python-dateutil| 2.8.2  
python-snappy| 0.6.1  
pytz| 2022.1  
PyYAML| 6.0  
regex| 2022.7.25  
requests| 2.28.0  
rsa| 4.9  
scikit-learn| 1.0.2  
scipy| 1.7.3  
setuptools| 57.5.0  
six| 1.16.0  
soupsieve| 2.3.2.post1  
sqlparse| 0.4.3  
threadpoolctl| 3.1.0  
tomli| 2.0.1  
tqdm| 4.64.1  
typing_extensions| 4.4.0  
uritemplate| 4.1.1  
urllib3| 1.26.14  
wheel| 0.38.4  
zipp| 3.12.1  
zstandard| 0.18.0  
  
### Python 3.8.16

Package| Version  
---|---  
  
attrs| 22.2.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.11.1  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2022.12.7  
charset-normalizer| 2.0.12  
click| 8.1.3  
cloudpickle| 2.2.1  
crcmod| 1.7  
Cython| 0.29.32  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 1.5.4  
fasteners| 0.18  
future| 0.18.2  
google-api-core| 2.10.2  
google-api-python-client| 2.76.0  
google-apitools| 0.5.31  
google-auth| 2.9.1  
google-auth-httplib2| 0.1.0  
google-cloud-bigquery| 3.3.5  
google-cloud-bigquery-storage| 2.13.2  
google-cloud-bigtable| 1.7.2  
google-cloud-core| 2.3.2  
google-cloud-datastore| 1.15.5  
google-cloud-dlp| 3.8.0  
google-cloud-language| 1.3.2  
google-cloud-profiler| 3.1.0  
google-cloud-pubsub| 2.13.4  
google-cloud-pubsublite| 1.4.2  
google-cloud-recommendations-ai| 0.7.0  
google-cloud-spanner| 3.21.0  
google-cloud-videointelligence| 1.16.3  
google-cloud-vision| 3.1.4  
google-crc32c| 1.5.0  
google-python-cloud-debugger| 2.18  
google-resumable-media| 2.4.1  
googleapis-common-protos| 1.58.0  
grpc-google-iam-v1| 0.12.6  
grpcio| 1.51.1  
grpcio-gcp| 0.2.2  
grpcio-status| 1.48.2  
guppy3| 3.1.2  
hdfs| 2.7.0  
httplib2| 0.21.0  
idna| 3.4  
iniconfig| 2.0.0  
joblib| 1.2.0  
mmh3| 3.0.0  
nltk| 3.7  
nose| 1.3.7  
numpy| 1.22.3  
oauth2client| 4.1.3  
objsize| 0.6.1  
orjson| 3.7.11  
overrides| 6.5.0  
packaging| 21.3  
pandas| 1.5.2  
Pillow| 7.2.0  
pip| 23.0  
pluggy| 1.0.0  
proto-plus| 1.22.2  
protobuf| 3.20.3  
py| 1.11.0  
pyarrow| 7.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.2  
pymongo| 3.12.3  
pyparsing| 3.0.9  
pytest| 7.1.2  
python-dateutil| 2.8.2  
python-snappy| 0.6.1  
pytz| 2022.1  
PyYAML| 6.0  
regex| 2022.7.25  
requests| 2.28.0  
rsa| 4.9  
scikit-learn| 1.0.2  
scipy| 1.7.3  
setuptools| 57.5.0  
six| 1.16.0  
soupsieve| 2.3.2.post1  
sqlparse| 0.4.3  
threadpoolctl| 3.1.0  
tomli| 2.0.1  
tqdm| 4.64.1  
typing_extensions| 4.4.0  
uritemplate| 4.1.1  
urllib3| 1.26.14  
wheel| 0.38.4  
zstandard| 0.18.0  
  
### Python 3.9.16

Package| Version  
---|---  
  
attrs| 22.2.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.11.1  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2022.12.7  
charset-normalizer| 2.0.12  
click| 8.1.3  
cloudpickle| 2.2.1  
crcmod| 1.7  
Cython| 0.29.32  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 1.5.4  
fasteners| 0.18  
future| 0.18.2  
google-api-core| 2.10.2  
google-api-python-client| 2.76.0  
google-apitools| 0.5.31  
google-auth| 2.9.1  
google-auth-httplib2| 0.1.0  
google-cloud-bigquery| 3.3.5  
google-cloud-bigquery-storage| 2.13.2  
google-cloud-bigtable| 1.7.2  
google-cloud-core| 2.3.2  
google-cloud-datastore| 1.15.5  
google-cloud-dlp| 3.8.0  
google-cloud-language| 1.3.2  
google-cloud-profiler| 3.1.0  
google-cloud-pubsub| 2.13.4  
google-cloud-pubsublite| 1.4.2  
google-cloud-recommendations-ai| 0.7.0  
google-cloud-spanner| 3.21.0  
google-cloud-videointelligence| 1.16.3  
google-cloud-vision| 3.1.4  
google-crc32c| 1.5.0  
google-python-cloud-debugger| 2.18  
google-resumable-media| 2.4.1  
googleapis-common-protos| 1.58.0  
grpc-google-iam-v1| 0.12.6  
grpcio| 1.51.1  
grpcio-gcp| 0.2.2  
grpcio-status| 1.48.2  
guppy3| 3.1.2  
hdfs| 2.7.0  
httplib2| 0.21.0  
idna| 3.4  
iniconfig| 2.0.0  
joblib| 1.2.0  
mmh3| 3.0.0  
nltk| 3.7  
nose| 1.3.7  
numpy| 1.22.3  
oauth2client| 4.1.3  
objsize| 0.6.1  
orjson| 3.7.11  
overrides| 6.5.0  
packaging| 21.3  
pandas| 1.5.2  
Pillow| 7.2.0  
pip| 23.0  
pluggy| 1.0.0  
proto-plus| 1.22.2  
protobuf| 3.20.3  
py| 1.11.0  
pyarrow| 7.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.2  
pymongo| 3.12.3  
pyparsing| 3.0.9  
pytest| 7.1.2  
python-dateutil| 2.8.2  
python-snappy| 0.6.1  
pytz| 2022.1  
PyYAML| 6.0  
regex| 2022.7.25  
requests| 2.28.0  
rsa| 4.9  
scikit-learn| 1.0.2  
scipy| 1.7.3  
setuptools| 58.1.0  
six| 1.16.0  
soupsieve| 2.3.2.post1  
sqlparse| 0.4.3  
threadpoolctl| 3.1.0  
tomli| 2.0.1  
tqdm| 4.64.1  
typing_extensions| 4.4.0  
uritemplate| 4.1.1  
urllib3| 1.26.14  
wheel| 0.38.4  
zstandard| 0.18.0  
  
### Python 3.10.9

Package| Version  
---|---  
  
attrs| 22.2.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.11.1  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2022.12.7  
charset-normalizer| 2.0.12  
click| 8.1.3  
cloudpickle| 2.2.1  
crcmod| 1.7  
Cython| 0.29.32  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 1.5.4  
fasteners| 0.18  
future| 0.18.2  
google-api-core| 2.10.2  
google-api-python-client| 2.76.0  
google-apitools| 0.5.31  
google-auth| 2.9.1  
google-auth-httplib2| 0.1.0  
google-cloud-bigquery| 3.3.5  
google-cloud-bigquery-storage| 2.13.2  
google-cloud-bigtable| 1.7.2  
google-cloud-core| 2.3.2  
google-cloud-datastore| 1.15.5  
google-cloud-dlp| 3.8.0  
google-cloud-language| 1.3.2  
google-cloud-profiler| 3.1.0  
google-cloud-pubsub| 2.13.4  
google-cloud-pubsublite| 1.4.2  
google-cloud-recommendations-ai| 0.7.0  
google-cloud-spanner| 3.21.0  
google-cloud-videointelligence| 1.16.3  
google-cloud-vision| 3.1.4  
google-crc32c| 1.5.0  
google-resumable-media| 2.4.1  
googleapis-common-protos| 1.58.0  
grpc-google-iam-v1| 0.12.6  
grpcio| 1.51.1  
grpcio-gcp| 0.2.2  
grpcio-status| 1.48.2  
guppy3| 3.1.2  
hdfs| 2.7.0  
httplib2| 0.21.0  
idna| 3.4  
iniconfig| 2.0.0  
joblib| 1.2.0  
mmh3| 3.0.0  
nltk| 3.7  
nose| 1.3.7  
numpy| 1.22.3  
oauth2client| 4.1.3  
objsize| 0.6.1  
orjson| 3.7.11  
overrides| 6.5.0  
packaging| 21.3  
pandas| 1.5.2  
Pillow| 7.2.0  
pip| 23.0  
pluggy| 1.0.0  
proto-plus| 1.22.2  
protobuf| 3.20.3  
py| 1.11.0  
pyarrow| 7.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.2  
pymongo| 3.12.3  
pyparsing| 3.0.9  
pytest| 7.1.2  
python-dateutil| 2.8.2  
python-snappy| 0.6.1  
pytz| 2022.1  
PyYAML| 6.0  
regex| 2022.7.25  
requests| 2.28.0  
rsa| 4.9  
scikit-learn| 1.0.2  
scipy| 1.7.3  
setuptools| 65.5.1  
six| 1.16.0  
soupsieve| 2.3.2.post1  
sqlparse| 0.4.3  
threadpoolctl| 3.1.0  
tomli| 2.0.1  
tqdm| 4.64.1  
typing_extensions| 4.4.0  
uritemplate| 4.1.1  
urllib3| 1.26.14  
wheel| 0.38.4  
zstandard| 0.18.0  
  
#### Version 2.45.0

Dataflow workers have the following packages already installed.

### Python 3.7.16

Package| Version  
---|---  
  
attrs| 22.2.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.11.1  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2022.12.7  
charset-normalizer| 2.0.12  
click| 8.1.3  
cloudpickle| 2.2.1  
crcmod| 1.7  
Cython| 0.29.32  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 1.5.4  
fasteners| 0.18  
future| 0.18.2  
google-api-core| 2.10.2  
google-api-python-client| 2.77.0  
google-apitools| 0.5.31  
google-auth| 2.9.1  
google-auth-httplib2| 0.1.0  
google-cloud-bigquery| 3.3.5  
google-cloud-bigquery-storage| 2.13.2  
google-cloud-bigtable| 1.7.2  
google-cloud-core| 2.3.2  
google-cloud-datastore| 1.15.5  
google-cloud-dlp| 3.8.0  
google-cloud-language| 1.3.2  
google-cloud-profiler| 3.1.0  
google-cloud-pubsub| 2.13.4  
google-cloud-pubsublite| 1.4.2  
google-cloud-recommendations-ai| 0.7.0  
google-cloud-spanner| 3.21.0  
google-cloud-videointelligence| 1.16.3  
google-cloud-vision| 3.1.4  
google-crc32c| 1.5.0  
google-python-cloud-debugger| 2.18  
google-resumable-media| 2.4.1  
googleapis-common-protos| 1.58.0  
grpc-google-iam-v1| 0.12.6  
grpcio| 1.51.1  
grpcio-gcp| 0.2.2  
grpcio-status| 1.48.2  
guppy3| 3.1.2  
hdfs| 2.7.0  
httplib2| 0.20.4  
idna| 3.4  
importlib-metadata| 6.0.0  
iniconfig| 2.0.0  
joblib| 1.2.0  
mmh3| 3.0.0  
nltk| 3.7  
nose| 1.3.7  
numpy| 1.21.6  
oauth2client| 4.1.3  
objsize| 0.6.1  
orjson| 3.7.11  
overrides| 6.5.0  
packaging| 21.3  
pandas| 1.3.5  
Pillow| 7.2.0  
pip| 23.0  
pluggy| 1.0.0  
proto-plus| 1.22.2  
protobuf| 3.20.3  
py| 1.11.0  
pyarrow| 7.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.2  
pymongo| 3.12.3  
pyparsing| 3.0.9  
pytest| 7.1.2  
python-dateutil| 2.8.2  
python-snappy| 0.6.1  
pytz| 2022.1  
PyYAML| 6.0  
regex| 2022.7.25  
requests| 2.28.0  
rsa| 4.9  
scikit-learn| 1.0.2  
scipy| 1.7.3  
setuptools| 57.5.0  
six| 1.16.0  
soupsieve| 2.3.2.post1  
sqlparse| 0.4.3  
threadpoolctl| 3.1.0  
tomli| 2.0.1  
tqdm| 4.64.1  
typing_extensions| 4.4.0  
uritemplate| 4.1.1  
urllib3| 1.26.14  
wheel| 0.38.4  
zipp| 3.13.0  
zstandard| 0.18.0  
  
### Python 3.8.16

Package| Version  
---|---  
  
attrs| 22.2.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.11.1  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2022.12.7  
charset-normalizer| 2.0.12  
click| 8.1.3  
cloudpickle| 2.2.1  
crcmod| 1.7  
Cython| 0.29.32  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 1.5.4  
fasteners| 0.18  
future| 0.18.2  
google-api-core| 2.10.2  
google-api-python-client| 2.77.0  
google-apitools| 0.5.31  
google-auth| 2.9.1  
google-auth-httplib2| 0.1.0  
google-cloud-bigquery| 3.3.5  
google-cloud-bigquery-storage| 2.13.2  
google-cloud-bigtable| 1.7.2  
google-cloud-core| 2.3.2  
google-cloud-datastore| 1.15.5  
google-cloud-dlp| 3.8.0  
google-cloud-language| 1.3.2  
google-cloud-profiler| 3.1.0  
google-cloud-pubsub| 2.13.4  
google-cloud-pubsublite| 1.4.2  
google-cloud-recommendations-ai| 0.7.0  
google-cloud-spanner| 3.21.0  
google-cloud-videointelligence| 1.16.3  
google-cloud-vision| 3.1.4  
google-crc32c| 1.5.0  
google-python-cloud-debugger| 2.18  
google-resumable-media| 2.4.1  
googleapis-common-protos| 1.58.0  
grpc-google-iam-v1| 0.12.6  
grpcio| 1.51.1  
grpcio-gcp| 0.2.2  
grpcio-status| 1.48.2  
guppy3| 3.1.2  
hdfs| 2.7.0  
httplib2| 0.20.4  
idna| 3.4  
iniconfig| 2.0.0  
joblib| 1.2.0  
mmh3| 3.0.0  
nltk| 3.7  
nose| 1.3.7  
numpy| 1.22.3  
oauth2client| 4.1.3  
objsize| 0.6.1  
orjson| 3.7.11  
overrides| 6.5.0  
packaging| 21.3  
pandas| 1.5.2  
Pillow| 7.2.0  
pip| 23.0  
pluggy| 1.0.0  
proto-plus| 1.22.2  
protobuf| 3.20.3  
py| 1.11.0  
pyarrow| 7.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.2  
pymongo| 3.12.3  
pyparsing| 3.0.9  
pytest| 7.1.2  
python-dateutil| 2.8.2  
python-snappy| 0.6.1  
pytz| 2022.1  
PyYAML| 6.0  
regex| 2022.7.25  
requests| 2.28.0  
rsa| 4.9  
scikit-learn| 1.0.2  
scipy| 1.7.3  
setuptools| 57.5.0  
six| 1.16.0  
soupsieve| 2.3.2.post1  
sqlparse| 0.4.3  
threadpoolctl| 3.1.0  
tomli| 2.0.1  
tqdm| 4.64.1  
typing_extensions| 4.4.0  
uritemplate| 4.1.1  
urllib3| 1.26.14  
wheel| 0.38.4  
zstandard| 0.18.0  
  
### Python 3.9.16

Package| Version  
---|---  
  
attrs| 22.2.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.11.1  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2022.12.7  
charset-normalizer| 2.0.12  
click| 8.1.3  
cloudpickle| 2.2.1  
crcmod| 1.7  
Cython| 0.29.32  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 1.5.4  
fasteners| 0.18  
future| 0.18.2  
google-api-core| 2.10.2  
google-api-python-client| 2.77.0  
google-apitools| 0.5.31  
google-auth| 2.9.1  
google-auth-httplib2| 0.1.0  
google-cloud-bigquery| 3.3.5  
google-cloud-bigquery-storage| 2.13.2  
google-cloud-bigtable| 1.7.2  
google-cloud-core| 2.3.2  
google-cloud-datastore| 1.15.5  
google-cloud-dlp| 3.8.0  
google-cloud-language| 1.3.2  
google-cloud-profiler| 3.1.0  
google-cloud-pubsub| 2.13.4  
google-cloud-pubsublite| 1.4.2  
google-cloud-recommendations-ai| 0.7.0  
google-cloud-spanner| 3.21.0  
google-cloud-videointelligence| 1.16.3  
google-cloud-vision| 3.1.4  
google-crc32c| 1.5.0  
google-python-cloud-debugger| 2.18  
google-resumable-media| 2.4.1  
googleapis-common-protos| 1.58.0  
grpc-google-iam-v1| 0.12.6  
grpcio| 1.51.1  
grpcio-gcp| 0.2.2  
grpcio-status| 1.48.2  
guppy3| 3.1.2  
hdfs| 2.7.0  
httplib2| 0.20.4  
idna| 3.4  
iniconfig| 2.0.0  
joblib| 1.2.0  
mmh3| 3.0.0  
nltk| 3.7  
nose| 1.3.7  
numpy| 1.22.3  
oauth2client| 4.1.3  
objsize| 0.6.1  
orjson| 3.7.11  
overrides| 6.5.0  
packaging| 21.3  
pandas| 1.5.2  
Pillow| 7.2.0  
pip| 23.0  
pluggy| 1.0.0  
proto-plus| 1.22.2  
protobuf| 3.20.3  
py| 1.11.0  
pyarrow| 7.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.2  
pymongo| 3.12.3  
pyparsing| 3.0.9  
pytest| 7.1.2  
python-dateutil| 2.8.2  
python-snappy| 0.6.1  
pytz| 2022.1  
PyYAML| 6.0  
regex| 2022.7.25  
requests| 2.28.0  
rsa| 4.9  
scikit-learn| 1.0.2  
scipy| 1.7.3  
setuptools| 58.1.0  
six| 1.16.0  
soupsieve| 2.3.2.post1  
sqlparse| 0.4.3  
threadpoolctl| 3.1.0  
tomli| 2.0.1  
tqdm| 4.64.1  
typing_extensions| 4.4.0  
uritemplate| 4.1.1  
urllib3| 1.26.14  
wheel| 0.38.4  
zstandard| 0.18.0  
  
### Python 3.10.10

Package| Version  
---|---  
  
attrs| 22.2.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.11.1  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2022.12.7  
charset-normalizer| 2.0.12  
click| 8.1.3  
cloudpickle| 2.2.1  
crcmod| 1.7  
Cython| 0.29.32  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 1.5.4  
fasteners| 0.18  
future| 0.18.2  
google-api-core| 2.10.2  
google-api-python-client| 2.77.0  
google-apitools| 0.5.31  
google-auth| 2.9.1  
google-auth-httplib2| 0.1.0  
google-cloud-bigquery| 3.3.5  
google-cloud-bigquery-storage| 2.13.2  
google-cloud-bigtable| 1.7.2  
google-cloud-core| 2.3.2  
google-cloud-datastore| 1.15.5  
google-cloud-dlp| 3.8.0  
google-cloud-language| 1.3.2  
google-cloud-profiler| 3.1.0  
google-cloud-pubsub| 2.13.4  
google-cloud-pubsublite| 1.4.2  
google-cloud-recommendations-ai| 0.7.0  
google-cloud-spanner| 3.21.0  
google-cloud-videointelligence| 1.16.3  
google-cloud-vision| 3.1.4  
google-crc32c| 1.5.0  
google-resumable-media| 2.4.1  
googleapis-common-protos| 1.58.0  
grpc-google-iam-v1| 0.12.6  
grpcio| 1.51.1  
grpcio-gcp| 0.2.2  
grpcio-status| 1.48.2  
guppy3| 3.1.2  
hdfs| 2.7.0  
httplib2| 0.20.4  
idna| 3.4  
iniconfig| 2.0.0  
joblib| 1.2.0  
mmh3| 3.0.0  
nltk| 3.7  
nose| 1.3.7  
numpy| 1.22.3  
oauth2client| 4.1.3  
objsize| 0.6.1  
orjson| 3.7.11  
overrides| 6.5.0  
packaging| 21.3  
pandas| 1.5.2  
Pillow| 7.2.0  
pip| 23.0  
pluggy| 1.0.0  
proto-plus| 1.22.2  
protobuf| 3.20.3  
py| 1.11.0  
pyarrow| 7.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.2  
pymongo| 3.12.3  
pyparsing| 3.0.9  
pytest| 7.1.2  
python-dateutil| 2.8.2  
python-snappy| 0.6.1  
pytz| 2022.1  
PyYAML| 6.0  
regex| 2022.7.25  
requests| 2.28.0  
rsa| 4.9  
scikit-learn| 1.0.2  
scipy| 1.7.3  
setuptools| 65.5.1  
six| 1.16.0  
soupsieve| 2.3.2.post1  
sqlparse| 0.4.3  
threadpoolctl| 3.1.0  
tomli| 2.0.1  
tqdm| 4.64.1  
typing_extensions| 4.4.0  
uritemplate| 4.1.1  
urllib3| 1.26.14  
wheel| 0.38.4  
zstandard| 0.18.0  
  
#### Version 2.44.0

Dataflow workers have the following packages already installed.

### Python 3.7.15

Package| Version  
---|---  
  
attrs| 22.1.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.11.1  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2022.9.24  
charset-normalizer| 2.0.12  
click| 8.1.3  
cloudpickle| 2.2.0  
crcmod| 1.7  
Cython| 0.29.32  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 1.5.4  
fasteners| 0.18  
future| 0.18.2  
google-api-core| 2.10.2  
google-api-python-client| 2.68.0  
google-apitools| 0.5.31  
google-auth| 2.9.1  
google-auth-httplib2| 0.1.0  
google-cloud-bigquery| 3.3.5  
google-cloud-bigquery-storage| 2.13.2  
google-cloud-bigtable| 1.7.2  
google-cloud-core| 2.3.2  
google-cloud-datastore| 1.15.5  
google-cloud-dlp| 3.8.0  
google-cloud-language| 1.3.2  
google-cloud-profiler| 3.1.0  
google-cloud-pubsub| 2.13.4  
google-cloud-pubsublite| 1.4.2  
google-cloud-recommendations-ai| 0.7.0  
google-cloud-spanner| 3.21.0  
google-cloud-videointelligence| 1.16.3  
google-cloud-vision| 3.1.4  
google-crc32c| 1.5.0  
google-python-cloud-debugger| 2.18  
google-resumable-media| 2.4.0  
googleapis-common-protos| 1.57.0  
grpc-google-iam-v1| 0.12.4  
grpcio| 1.51.1  
grpcio-gcp| 0.2.2  
grpcio-status| 1.48.2  
guppy3| 3.1.2  
hdfs| 2.7.0  
httplib2| 0.20.4  
idna| 3.4  
importlib-metadata| 5.1.0  
iniconfig| 1.1.1  
joblib| 1.2.0  
mmh3| 3.0.0  
nltk| 3.7  
nose| 1.3.7  
numpy| 1.21.6  
oauth2client| 4.1.3  
objsize| 0.6.1  
orjson| 3.7.11  
overrides| 6.5.0  
packaging| 21.3  
pandas| 1.3.5  
Pillow| 7.2.0  
pip| 22.3.1  
pluggy| 1.0.0  
proto-plus| 1.22.1  
protobuf| 3.20.3  
py| 1.11.0  
pyarrow| 7.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.2  
pymongo| 3.12.3  
pyparsing| 3.0.9  
pytest| 7.1.2  
python-dateutil| 2.8.2  
python-snappy| 0.6.1  
pytz| 2022.1  
PyYAML| 6.0  
regex| 2022.7.25  
requests| 2.28.0  
rsa| 4.9  
scikit-learn| 1.0.2  
scipy| 1.7.3  
setuptools| 57.5.0  
six| 1.16.0  
soupsieve| 2.3.2.post1  
sqlparse| 0.4.3  
threadpoolctl| 3.1.0  
tomli| 2.0.1  
tqdm| 4.64.1  
typing_extensions| 4.4.0  
uritemplate| 4.1.1  
urllib3| 1.26.13  
wheel| 0.38.4  
zipp| 3.11.0  
zstandard| 0.18.0  
  
### Python 3.8.15

Package| Version  
---|---  
  
attrs| 22.1.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.11.1  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2022.9.24  
charset-normalizer| 2.0.12  
click| 8.1.3  
cloudpickle| 2.2.0  
crcmod| 1.7  
Cython| 0.29.32  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 1.5.4  
fasteners| 0.18  
future| 0.18.2  
google-api-core| 2.10.2  
google-api-python-client| 2.68.0  
google-apitools| 0.5.31  
google-auth| 2.9.1  
google-auth-httplib2| 0.1.0  
google-cloud-bigquery| 3.3.5  
google-cloud-bigquery-storage| 2.13.2  
google-cloud-bigtable| 1.7.2  
google-cloud-core| 2.3.2  
google-cloud-datastore| 1.15.5  
google-cloud-dlp| 3.8.0  
google-cloud-language| 1.3.2  
google-cloud-profiler| 3.1.0  
google-cloud-pubsub| 2.13.4  
google-cloud-pubsublite| 1.4.2  
google-cloud-recommendations-ai| 0.7.0  
google-cloud-spanner| 3.21.0  
google-cloud-videointelligence| 1.16.3  
google-cloud-vision| 3.1.4  
google-crc32c| 1.5.0  
google-python-cloud-debugger| 2.18  
google-resumable-media| 2.4.0  
googleapis-common-protos| 1.57.0  
grpc-google-iam-v1| 0.12.4  
grpcio| 1.51.1  
grpcio-gcp| 0.2.2  
grpcio-status| 1.48.2  
guppy3| 3.1.2  
hdfs| 2.7.0  
httplib2| 0.20.4  
idna| 3.4  
iniconfig| 1.1.1  
joblib| 1.2.0  
mmh3| 3.0.0  
nltk| 3.7  
nose| 1.3.7  
numpy| 1.22.3  
oauth2client| 4.1.3  
objsize| 0.6.1  
orjson| 3.7.11  
overrides| 6.5.0  
packaging| 21.3  
pandas| 1.5.2  
Pillow| 7.2.0  
pip| 22.3.1  
pluggy| 1.0.0  
proto-plus| 1.22.1  
protobuf| 3.20.3  
py| 1.11.0  
pyarrow| 7.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.2  
pymongo| 3.12.3  
pyparsing| 3.0.9  
pytest| 7.1.2  
python-dateutil| 2.8.2  
python-snappy| 0.6.1  
pytz| 2022.1  
PyYAML| 6.0  
regex| 2022.7.25  
requests| 2.28.0  
rsa| 4.9  
scikit-learn| 1.0.2  
scipy| 1.7.3  
setuptools| 57.5.0  
six| 1.16.0  
soupsieve| 2.3.2.post1  
sqlparse| 0.4.3  
threadpoolctl| 3.1.0  
tomli| 2.0.1  
tqdm| 4.64.1  
typing_extensions| 4.4.0  
uritemplate| 4.1.1  
urllib3| 1.26.13  
wheel| 0.38.4  
zstandard| 0.18.0  
  
### Python 3.9.15

Package| Version  
---|---  
  
attrs| 22.1.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.11.1  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2022.9.24  
charset-normalizer| 2.0.12  
click| 8.1.3  
cloudpickle| 2.2.0  
crcmod| 1.7  
Cython| 0.29.32  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 1.5.4  
fasteners| 0.18  
future| 0.18.2  
google-api-core| 2.10.2  
google-api-python-client| 2.68.0  
google-apitools| 0.5.31  
google-auth| 2.9.1  
google-auth-httplib2| 0.1.0  
google-cloud-bigquery| 3.3.5  
google-cloud-bigquery-storage| 2.13.2  
google-cloud-bigtable| 1.7.2  
google-cloud-core| 2.3.2  
google-cloud-datastore| 1.15.5  
google-cloud-dlp| 3.8.0  
google-cloud-language| 1.3.2  
google-cloud-profiler| 3.1.0  
google-cloud-pubsub| 2.13.4  
google-cloud-pubsublite| 1.4.2  
google-cloud-recommendations-ai| 0.7.0  
google-cloud-spanner| 3.21.0  
google-cloud-videointelligence| 1.16.3  
google-cloud-vision| 3.1.4  
google-crc32c| 1.5.0  
google-python-cloud-debugger| 2.18  
google-resumable-media| 2.4.0  
googleapis-common-protos| 1.57.0  
grpc-google-iam-v1| 0.12.4  
grpcio| 1.51.1  
grpcio-gcp| 0.2.2  
grpcio-status| 1.48.2  
guppy3| 3.1.2  
hdfs| 2.7.0  
httplib2| 0.20.4  
idna| 3.4  
iniconfig| 1.1.1  
joblib| 1.2.0  
mmh3| 3.0.0  
nltk| 3.7  
nose| 1.3.7  
numpy| 1.22.3  
oauth2client| 4.1.3  
objsize| 0.6.1  
orjson| 3.7.11  
overrides| 6.5.0  
packaging| 21.3  
pandas| 1.5.2  
Pillow| 7.2.0  
pip| 22.3.1  
pluggy| 1.0.0  
proto-plus| 1.22.1  
protobuf| 3.20.3  
py| 1.11.0  
pyarrow| 7.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.2  
pymongo| 3.12.3  
pyparsing| 3.0.9  
pytest| 7.1.2  
python-dateutil| 2.8.2  
python-snappy| 0.6.1  
pytz| 2022.1  
PyYAML| 6.0  
regex| 2022.7.25  
requests| 2.28.0  
rsa| 4.9  
scikit-learn| 1.0.2  
scipy| 1.7.3  
setuptools| 58.1.0  
six| 1.16.0  
soupsieve| 2.3.2.post1  
sqlparse| 0.4.3  
threadpoolctl| 3.1.0  
tomli| 2.0.1  
tqdm| 4.64.1  
typing_extensions| 4.4.0  
uritemplate| 4.1.1  
urllib3| 1.26.13  
wheel| 0.38.4  
zstandard| 0.18.0  
  
### Python 3.10.8

Package| Version  
---|---  
  
attrs| 22.1.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.11.1  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2022.9.24  
charset-normalizer| 2.0.12  
click| 8.1.3  
cloudpickle| 2.2.0  
crcmod| 1.7  
Cython| 0.29.32  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 1.5.4  
fasteners| 0.18  
future| 0.18.2  
google-api-core| 2.10.2  
google-api-python-client| 2.64.0  
google-apitools| 0.5.31  
google-auth| 2.9.1  
google-auth-httplib2| 0.1.0  
google-cloud-bigquery| 3.3.5  
google-cloud-bigquery-storage| 2.13.2  
google-cloud-bigtable| 1.7.2  
google-cloud-core| 2.3.2  
google-cloud-datastore| 1.15.5  
google-cloud-dlp| 3.8.0  
google-cloud-language| 1.3.2  
google-cloud-profiler| 3.1.0  
google-cloud-pubsub| 2.13.4  
google-cloud-pubsublite| 1.4.2  
google-cloud-recommendations-ai| 0.7.0  
google-cloud-spanner| 3.21.0  
google-cloud-videointelligence| 1.16.3  
google-cloud-vision| 1.0.2  
google-crc32c| 1.5.0  
google-resumable-media| 2.4.0  
googleapis-common-protos| 1.56.4  
grpc-google-iam-v1| 0.12.4  
grpcio| 1.49.1  
grpcio-gcp| 0.2.2  
grpcio-status| 1.48.2  
guppy3| 3.1.2  
hdfs| 2.7.0  
httplib2| 0.20.4  
idna| 3.4  
iniconfig| 1.1.1  
joblib| 1.2.0  
mmh3| 3.0.0  
nltk| 3.7  
nose| 1.3.7  
numpy| 1.22.3  
oauth2client| 4.1.3  
objsize| 0.5.2  
orjson| 3.7.11  
overrides| 6.5.0  
packaging| 21.3  
pandas| 1.4.4  
Pillow| 7.2.0  
pip| 22.2.2  
pluggy| 1.0.0  
proto-plus| 1.22.1  
protobuf| 3.20.3  
py| 1.11.0  
pyarrow| 7.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.2  
pymongo| 3.12.3  
pyparsing| 3.0.9  
pytest| 7.1.2  
python-dateutil| 2.8.2  
python-snappy| 0.6.1  
pytz| 2022.1  
PyYAML| 6.0  
regex| 2022.7.25  
requests| 2.28.0  
rsa| 4.9  
scikit-learn| 1.0.2  
scipy| 1.7.3  
setuptools| 63.2.0  
six| 1.16.0  
soupsieve| 2.3.2.post1  
sqlparse| 0.4.3  
threadpoolctl| 3.1.0  
tomli| 2.0.1  
tqdm| 4.64.1  
typing_extensions| 4.4.0  
uritemplate| 4.1.1  
urllib3| 1.26.12  
wheel| 0.37.1  
zstandard| 0.18.0  
  
#### Version 2.43.0

Dataflow workers have the following packages already installed.

### Python 3.7.15

Package| Version  
---|---  
  
attrs| 22.1.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.11.1  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2022.9.24  
charset-normalizer| 2.0.12  
click| 8.1.3  
cloudpickle| 2.2.0  
crcmod| 1.7  
Cython| 0.29.32  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 1.5.4  
fasteners| 0.18  
future| 0.18.2  
google-api-core| 2.10.2  
google-api-python-client| 2.64.0  
google-apitools| 0.5.31  
google-auth| 2.9.1  
google-auth-httplib2| 0.1.0  
google-cloud-bigquery| 3.3.5  
google-cloud-bigquery-storage| 2.13.2  
google-cloud-bigtable| 1.7.2  
google-cloud-core| 2.3.2  
google-cloud-datastore| 1.15.5  
google-cloud-dlp| 3.8.0  
google-cloud-language| 1.3.2  
google-cloud-profiler| 3.1.0  
google-cloud-pubsub| 2.13.4  
google-cloud-pubsublite| 1.4.2  
google-cloud-recommendations-ai| 0.7.0  
google-cloud-spanner| 3.21.0  
google-cloud-videointelligence| 1.16.3  
google-cloud-vision| 1.0.2  
google-crc32c| 1.5.0  
google-python-cloud-debugger| 2.18  
google-resumable-media| 2.4.0  
googleapis-common-protos| 1.56.4  
grpc-google-iam-v1| 0.12.4  
grpcio| 1.49.1  
grpcio-gcp| 0.2.2  
grpcio-status| 1.48.2  
guppy3| 3.1.2  
hdfs| 2.7.0  
httplib2| 0.20.4  
idna| 3.4  
importlib-metadata| 5.0.0  
iniconfig| 1.1.1  
joblib| 1.2.0  
mmh3| 3.0.0  
nltk| 3.7  
nose| 1.3.7  
numpy| 1.21.6  
oauth2client| 4.1.3  
objsize| 0.5.2  
orjson| 3.7.11  
overrides| 6.5.0  
packaging| 21.3  
pandas| 1.3.5  
Pillow| 7.2.0  
pip| 22.2.2  
pluggy| 1.0.0  
proto-plus| 1.22.1  
protobuf| 3.20.3  
py| 1.11.0  
pyarrow| 7.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.2  
pymongo| 3.12.3  
pyparsing| 3.0.9  
pytest| 7.1.2  
python-dateutil| 2.8.2  
python-snappy| 0.6.1  
pytz| 2022.1  
PyYAML| 6.0  
regex| 2022.7.25  
requests| 2.28.0  
rsa| 4.9  
scikit-learn| 1.0.2  
scipy| 1.7.3  
setuptools| 57.5.0  
six| 1.16.0  
soupsieve| 2.3.2.post1  
sqlparse| 0.4.3  
threadpoolctl| 3.1.0  
tomli| 2.0.1  
tqdm| 4.64.1  
typing_extensions| 4.4.0  
uritemplate| 4.1.1  
urllib3| 1.26.12  
wheel| 0.37.1  
zipp| 3.9.0  
zstandard| 0.18.0  
  
### Python 3.8.15

Package| Version  
---|---  
  
attrs| 22.1.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.11.1  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2022.9.24  
charset-normalizer| 2.0.12  
click| 8.1.3  
cloudpickle| 2.2.0  
crcmod| 1.7  
Cython| 0.29.32  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 1.5.4  
fasteners| 0.18  
future| 0.18.2  
google-api-core| 2.10.2  
google-api-python-client| 2.64.0  
google-apitools| 0.5.31  
google-auth| 2.9.1  
google-auth-httplib2| 0.1.0  
google-cloud-bigquery| 3.3.5  
google-cloud-bigquery-storage| 2.13.2  
google-cloud-bigtable| 1.7.2  
google-cloud-core| 2.3.2  
google-cloud-datastore| 1.15.5  
google-cloud-dlp| 3.8.0  
google-cloud-language| 1.3.2  
google-cloud-profiler| 3.1.0  
google-cloud-pubsub| 2.13.4  
google-cloud-pubsublite| 1.4.2  
google-cloud-recommendations-ai| 0.7.0  
google-cloud-spanner| 3.21.0  
google-cloud-videointelligence| 1.16.3  
google-cloud-vision| 1.0.2  
google-crc32c| 1.5.0  
google-python-cloud-debugger| 2.18  
google-resumable-media| 2.4.0  
googleapis-common-protos| 1.56.4  
grpc-google-iam-v1| 0.12.4  
grpcio| 1.49.1  
grpcio-gcp| 0.2.2  
grpcio-status| 1.48.2  
guppy3| 3.1.2  
hdfs| 2.7.0  
httplib2| 0.20.4  
idna| 3.4  
iniconfig| 1.1.1  
joblib| 1.2.0  
mmh3| 3.0.0  
nltk| 3.7  
nose| 1.3.7  
numpy| 1.22.3  
oauth2client| 4.1.3  
objsize| 0.5.2  
orjson| 3.7.11  
overrides| 6.5.0  
packaging| 21.3  
pandas| 1.4.4  
Pillow| 7.2.0  
pip| 22.2.2  
pluggy| 1.0.0  
proto-plus| 1.22.1  
protobuf| 3.20.3  
py| 1.11.0  
pyarrow| 7.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.2  
pymongo| 3.12.3  
pyparsing| 3.0.9  
pytest| 7.1.2  
python-dateutil| 2.8.2  
python-snappy| 0.6.1  
pytz| 2022.1  
PyYAML| 6.0  
regex| 2022.7.25  
requests| 2.28.0  
rsa| 4.9  
scikit-learn| 1.0.2  
scipy| 1.7.3  
setuptools| 57.5.0  
six| 1.16.0  
soupsieve| 2.3.2.post1  
sqlparse| 0.4.3  
threadpoolctl| 3.1.0  
tomli| 2.0.1  
tqdm| 4.64.1  
typing_extensions| 4.4.0  
uritemplate| 4.1.1  
urllib3| 1.26.12  
wheel| 0.37.1  
zstandard| 0.18.0  
  
### Python 3.9.15

Package| Version  
---|---  
  
attrs| 22.1.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.11.1  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2022.9.24  
charset-normalizer| 2.0.12  
click| 8.1.3  
cloudpickle| 2.2.0  
crcmod| 1.7  
Cython| 0.29.32  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 1.5.4  
fasteners| 0.18  
future| 0.18.2  
google-api-core| 2.10.2  
google-api-python-client| 2.64.0  
google-apitools| 0.5.31  
google-auth| 2.9.1  
google-auth-httplib2| 0.1.0  
google-cloud-bigquery| 3.3.5  
google-cloud-bigquery-storage| 2.13.2  
google-cloud-bigtable| 1.7.2  
google-cloud-core| 2.3.2  
google-cloud-datastore| 1.15.5  
google-cloud-dlp| 3.8.0  
google-cloud-language| 1.3.2  
google-cloud-profiler| 3.1.0  
google-cloud-pubsub| 2.13.4  
google-cloud-pubsublite| 1.4.2  
google-cloud-recommendations-ai| 0.7.0  
google-cloud-spanner| 3.21.0  
google-cloud-videointelligence| 1.16.3  
google-cloud-vision| 1.0.2  
google-crc32c| 1.5.0  
google-python-cloud-debugger| 2.18  
google-resumable-media| 2.4.0  
googleapis-common-protos| 1.56.4  
grpc-google-iam-v1| 0.12.4  
grpcio| 1.49.1  
grpcio-gcp| 0.2.2  
grpcio-status| 1.48.2  
guppy3| 3.1.2  
hdfs| 2.7.0  
httplib2| 0.20.4  
idna| 3.4  
iniconfig| 1.1.1  
joblib| 1.2.0  
mmh3| 3.0.0  
nltk| 3.7  
nose| 1.3.7  
numpy| 1.22.3  
oauth2client| 4.1.3  
objsize| 0.5.2  
orjson| 3.7.11  
overrides| 6.5.0  
packaging| 21.3  
pandas| 1.4.4  
Pillow| 7.2.0  
pip| 22.2.2  
pluggy| 1.0.0  
proto-plus| 1.22.1  
protobuf| 3.20.3  
py| 1.11.0  
pyarrow| 7.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.2  
pymongo| 3.12.3  
pyparsing| 3.0.9  
pytest| 7.1.2  
python-dateutil| 2.8.2  
python-snappy| 0.6.1  
pytz| 2022.1  
PyYAML| 6.0  
regex| 2022.7.25  
requests| 2.28.0  
rsa| 4.9  
scikit-learn| 1.0.2  
scipy| 1.7.3  
setuptools| 58.1.0  
six| 1.16.0  
soupsieve| 2.3.2.post1  
sqlparse| 0.4.3  
threadpoolctl| 3.1.0  
tomli| 2.0.1  
tqdm| 4.64.1  
typing_extensions| 4.4.0  
uritemplate| 4.1.1  
urllib3| 1.26.12  
wheel| 0.37.1  
zstandard| 0.18.0  
  
### Python 3.10.8

Package| Version  
---|---  
  
attrs| 22.1.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.11.1  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2022.9.24  
charset-normalizer| 2.0.12  
click| 8.1.3  
cloudpickle| 2.2.0  
crcmod| 1.7  
Cython| 0.29.32  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 1.5.4  
fasteners| 0.18  
future| 0.18.2  
google-api-core| 2.10.2  
google-api-python-client| 2.64.0  
google-apitools| 0.5.31  
google-auth| 2.9.1  
google-auth-httplib2| 0.1.0  
google-cloud-bigquery| 3.3.5  
google-cloud-bigquery-storage| 2.13.2  
google-cloud-bigtable| 1.7.2  
google-cloud-core| 2.3.2  
google-cloud-datastore| 1.15.5  
google-cloud-dlp| 3.8.0  
google-cloud-language| 1.3.2  
google-cloud-profiler| 3.1.0  
google-cloud-pubsub| 2.13.4  
google-cloud-pubsublite| 1.4.2  
google-cloud-recommendations-ai| 0.7.0  
google-cloud-spanner| 3.21.0  
google-cloud-videointelligence| 1.16.3  
google-cloud-vision| 1.0.2  
google-crc32c| 1.5.0  
google-resumable-media| 2.4.0  
googleapis-common-protos| 1.56.4  
grpc-google-iam-v1| 0.12.4  
grpcio| 1.49.1  
grpcio-gcp| 0.2.2  
grpcio-status| 1.48.2  
guppy3| 3.1.2  
hdfs| 2.7.0  
httplib2| 0.20.4  
idna| 3.4  
iniconfig| 1.1.1  
joblib| 1.2.0  
mmh3| 3.0.0  
nltk| 3.7  
nose| 1.3.7  
numpy| 1.22.3  
oauth2client| 4.1.3  
objsize| 0.5.2  
orjson| 3.7.11  
overrides| 6.5.0  
packaging| 21.3  
pandas| 1.4.4  
Pillow| 7.2.0  
pip| 22.2.2  
pluggy| 1.0.0  
proto-plus| 1.22.1  
protobuf| 3.20.3  
py| 1.11.0  
pyarrow| 7.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.2  
pymongo| 3.12.3  
pyparsing| 3.0.9  
pytest| 7.1.2  
python-dateutil| 2.8.2  
python-snappy| 0.6.1  
pytz| 2022.1  
PyYAML| 6.0  
regex| 2022.7.25  
requests| 2.28.0  
rsa| 4.9  
scikit-learn| 1.0.2  
scipy| 1.7.3  
setuptools| 63.2.0  
six| 1.16.0  
soupsieve| 2.3.2.post1  
sqlparse| 0.4.3  
threadpoolctl| 3.1.0  
tomli| 2.0.1  
tqdm| 4.64.1  
typing_extensions| 4.4.0  
uritemplate| 4.1.1  
urllib3| 1.26.12  
wheel| 0.37.1  
zstandard| 0.18.0  
  
#### Version 2.42.0

Dataflow workers have the following packages already installed.

### Python 3.7.14

Package| Version  
---|---  
  
absl-py| 1.2.0  
astunparse| 1.6.3  
attrs| 22.1.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.11.1  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2022.9.24  
charset-normalizer| 2.0.12  
click| 8.1.3  
cloudpickle| 2.1.0  
crcmod| 1.7  
Cython| 0.29.32  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 1.5.4  
fasteners| 0.18  
flatbuffers| 22.9.24  
future| 0.18.2  
gast| 0.5.3  
google-api-core| 2.8.1  
google-api-python-client| 2.63.0  
google-apitools| 0.5.31  
google-auth| 2.9.1  
google-auth-httplib2| 0.1.0  
google-auth-oauthlib| 0.4.6  
google-cloud-bigquery| 2.34.4  
google-cloud-bigquery-storage| 2.13.2  
google-cloud-bigtable| 1.7.2  
google-cloud-core| 2.3.2  
google-cloud-datastore| 1.15.5  
google-cloud-dlp| 3.8.0  
google-cloud-language| 1.3.2  
google-cloud-profiler| 4.0.0  
google-cloud-pubsub| 2.13.4  
google-cloud-pubsublite| 1.4.2  
google-cloud-recommendations-ai| 0.7.0  
google-cloud-spanner| 1.19.3  
google-cloud-videointelligence| 1.16.3  
google-cloud-vision| 1.0.2  
google-crc32c| 1.5.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.18  
google-resumable-media| 2.3.3  
googleapis-common-protos| 1.56.4  
grpc-google-iam-v1| 0.12.4  
grpcio| 1.49.1  
grpcio-gcp| 0.2.2  
grpcio-status| 1.48.2  
guppy3| 3.1.2  
h5py| 3.7.0  
hdfs| 2.7.0  
httplib2| 0.20.4  
idna| 3.4  
importlib-metadata| 4.12.0  
iniconfig| 1.1.1  
joblib| 1.2.0  
keras| 2.8.0  
Keras-Preprocessing| 1.1.2  
libclang| 14.0.6  
Markdown| 3.4.1  
MarkupSafe| 2.1.1  
mmh3| 3.0.0  
nltk| 3.7  
nose| 1.3.7  
numpy| 1.21.6  
oauth2client| 4.1.3  
oauthlib| 3.2.1  
objsize| 0.5.2  
opt-einsum| 3.3.0  
orjson| 3.7.11  
overrides| 6.2.0  
packaging| 21.3  
pandas| 1.3.5  
Pillow| 7.2.0  
pip| 22.2.2  
pluggy| 1.0.0  
proto-plus| 1.20.6  
protobuf| 3.19.4  
py| 1.11.0  
pyarrow| 7.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.2  
pymongo| 3.12.3  
pyparsing| 3.0.9  
pytest| 7.1.2  
python-dateutil| 2.8.2  
python-snappy| 0.6.1  
pytz| 2022.1  
PyYAML| 6.0  
regex| 2022.7.25  
requests| 2.28.0  
requests-oauthlib| 1.3.1  
rsa| 4.9  
scikit-learn| 1.0.2  
scipy| 1.7.3  
setuptools| 57.5.0  
six| 1.16.0  
soupsieve| 2.3.2.post1  
tensorboard| 2.8.0  
tensorboard-data-server| 0.6.1  
tensorboard-plugin-wit| 1.8.1  
tensorflow| 2.8.0  
tensorflow-io-gcs-filesystem| 0.27.0  
termcolor| 2.0.1  
tf-estimator-nightly| 2.8.0.dev2021122109  
threadpoolctl| 3.1.0  
tomli| 2.0.1  
tqdm| 4.64.1  
typing_extensions| 4.2.0  
uritemplate| 4.1.1  
urllib3| 1.26.12  
Werkzeug| 2.2.2  
wheel| 0.37.1  
wrapt| 1.14.1  
zipp| 3.8.1  
zstandard| 0.18.0  
  
### Python 3.8.14

Package| Version  
---|---  
  
absl-py| 1.2.0  
astunparse| 1.6.3  
attrs| 22.1.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.11.1  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2022.9.24  
charset-normalizer| 2.0.12  
click| 8.1.3  
cloudpickle| 2.1.0  
crcmod| 1.7  
Cython| 0.29.32  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 1.5.4  
fasteners| 0.18  
flatbuffers| 22.9.24  
future| 0.18.2  
gast| 0.5.3  
google-api-core| 2.8.1  
google-api-python-client| 2.63.0  
google-apitools| 0.5.31  
google-auth| 2.9.1  
google-auth-httplib2| 0.1.0  
google-auth-oauthlib| 0.4.6  
google-cloud-bigquery| 2.34.4  
google-cloud-bigquery-storage| 2.13.2  
google-cloud-bigtable| 1.7.2  
google-cloud-core| 2.3.2  
google-cloud-datastore| 1.15.5  
google-cloud-dlp| 3.8.0  
google-cloud-language| 1.3.2  
google-cloud-profiler| 4.0.0  
google-cloud-pubsub| 2.13.4  
google-cloud-pubsublite| 1.4.2  
google-cloud-recommendations-ai| 0.7.0  
google-cloud-spanner| 1.19.3  
google-cloud-videointelligence| 1.16.3  
google-cloud-vision| 1.0.2  
google-crc32c| 1.5.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.18  
google-resumable-media| 2.3.3  
googleapis-common-protos| 1.56.4  
grpc-google-iam-v1| 0.12.4  
grpcio| 1.49.1  
grpcio-gcp| 0.2.2  
grpcio-status| 1.48.2  
guppy3| 3.1.2  
h5py| 3.7.0  
hdfs| 2.7.0  
httplib2| 0.20.4  
idna| 3.4  
importlib-metadata| 4.12.0  
iniconfig| 1.1.1  
joblib| 1.2.0  
keras| 2.8.0  
Keras-Preprocessing| 1.1.2  
libclang| 14.0.6  
Markdown| 3.4.1  
MarkupSafe| 2.1.1  
mmh3| 3.0.0  
nltk| 3.7  
nose| 1.3.7  
numpy| 1.22.3  
oauth2client| 4.1.3  
oauthlib| 3.2.1  
objsize| 0.5.2  
opt-einsum| 3.3.0  
orjson| 3.7.11  
overrides| 6.2.0  
packaging| 21.3  
pandas| 1.4.0  
Pillow| 7.2.0  
pip| 22.2.2  
pluggy| 1.0.0  
proto-plus| 1.20.6  
protobuf| 3.19.4  
py| 1.11.0  
pyarrow| 7.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.2  
pymongo| 3.12.3  
pyparsing| 3.0.9  
pytest| 7.1.2  
python-dateutil| 2.8.2  
python-snappy| 0.6.1  
pytz| 2022.1  
PyYAML| 6.0  
regex| 2022.7.25  
requests| 2.28.0  
requests-oauthlib| 1.3.1  
rsa| 4.9  
scikit-learn| 1.0.2  
scipy| 1.7.3  
setuptools| 57.5.0  
six| 1.16.0  
soupsieve| 2.3.2.post1  
tensorboard| 2.8.0  
tensorboard-data-server| 0.6.1  
tensorboard-plugin-wit| 1.8.1  
tensorflow| 2.8.0  
tensorflow-io-gcs-filesystem| 0.27.0  
termcolor| 2.0.1  
tf-estimator-nightly| 2.8.0.dev2021122109  
threadpoolctl| 3.1.0  
tomli| 2.0.1  
tqdm| 4.64.1  
typing_extensions| 4.2.0  
uritemplate| 4.1.1  
urllib3| 1.26.12  
Werkzeug| 2.2.2  
wheel| 0.37.1  
wrapt| 1.14.1  
zipp| 3.8.1  
zstandard| 0.18.0  
  
### Python 3.9.14

Package| Version  
---|---  
  
absl-py| 1.2.0  
astunparse| 1.6.3  
attrs| 22.1.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.11.1  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2022.9.24  
charset-normalizer| 2.0.12  
click| 8.1.3  
cloudpickle| 2.1.0  
crcmod| 1.7  
Cython| 0.29.32  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 1.5.4  
fasteners| 0.18  
flatbuffers| 22.9.24  
future| 0.18.2  
gast| 0.5.3  
google-api-core| 2.8.1  
google-api-python-client| 2.63.0  
google-apitools| 0.5.31  
google-auth| 2.9.1  
google-auth-httplib2| 0.1.0  
google-auth-oauthlib| 0.4.6  
google-cloud-bigquery| 2.34.4  
google-cloud-bigquery-storage| 2.13.2  
google-cloud-bigtable| 1.7.2  
google-cloud-core| 2.3.2  
google-cloud-datastore| 1.15.5  
google-cloud-dlp| 3.8.0  
google-cloud-language| 1.3.2  
google-cloud-profiler| 4.0.0  
google-cloud-pubsub| 2.13.4  
google-cloud-pubsublite| 1.4.2  
google-cloud-recommendations-ai| 0.7.0  
google-cloud-spanner| 1.19.3  
google-cloud-videointelligence| 1.16.3  
google-cloud-vision| 1.0.2  
google-crc32c| 1.5.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.18  
google-resumable-media| 2.3.3  
googleapis-common-protos| 1.56.4  
grpc-google-iam-v1| 0.12.4  
grpcio| 1.49.1  
grpcio-gcp| 0.2.2  
grpcio-status| 1.48.2  
guppy3| 3.1.2  
h5py| 3.7.0  
hdfs| 2.7.0  
httplib2| 0.20.4  
idna| 3.4  
importlib-metadata| 4.12.0  
iniconfig| 1.1.1  
joblib| 1.2.0  
keras| 2.8.0  
Keras-Preprocessing| 1.1.2  
libclang| 14.0.6  
Markdown| 3.4.1  
MarkupSafe| 2.1.1  
mmh3| 3.0.0  
nltk| 3.7  
nose| 1.3.7  
numpy| 1.22.3  
oauth2client| 4.1.3  
oauthlib| 3.2.1  
objsize| 0.5.2  
opt-einsum| 3.3.0  
orjson| 3.7.11  
overrides| 6.2.0  
packaging| 21.3  
pandas| 1.4.0  
Pillow| 7.2.0  
pip| 22.2.2  
pluggy| 1.0.0  
proto-plus| 1.20.6  
protobuf| 3.19.4  
py| 1.11.0  
pyarrow| 7.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.2  
pymongo| 3.12.3  
pyparsing| 3.0.9  
pytest| 7.1.2  
python-dateutil| 2.8.2  
python-snappy| 0.6.1  
pytz| 2022.1  
PyYAML| 6.0  
regex| 2022.7.25  
requests| 2.28.0  
requests-oauthlib| 1.3.1  
rsa| 4.9  
scikit-learn| 1.0.2  
scipy| 1.7.3  
setuptools| 58.1.0  
six| 1.16.0  
soupsieve| 2.3.2.post1  
tensorboard| 2.8.0  
tensorboard-data-server| 0.6.1  
tensorboard-plugin-wit| 1.8.1  
tensorflow| 2.8.0  
tensorflow-io-gcs-filesystem| 0.27.0  
termcolor| 2.0.1  
tf-estimator-nightly| 2.8.0.dev2021122109  
threadpoolctl| 3.1.0  
tomli| 2.0.1  
tqdm| 4.64.1  
typing_extensions| 4.2.0  
uritemplate| 4.1.1  
urllib3| 1.26.12  
Werkzeug| 2.2.2  
wheel| 0.37.1  
wrapt| 1.14.1  
zipp| 3.8.1  
zstandard| 0.18.0  
  
#### Version 2.41.0

Dataflow workers have the following packages already installed.

### Python 3.7.13

Package| Version  
---|---  
  
absl-py| 1.2.0  
astunparse| 1.6.3  
atomicwrites| 1.4.1  
attrs| 22.1.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.11.1  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2022.6.15  
charset-normalizer| 2.0.12  
click| 8.1.3  
cloudpickle| 2.1.0  
crcmod| 1.7  
Cython| 0.29.30  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 1.5.1  
fasteners| 0.17.3  
flatbuffers| 2.0  
future| 0.18.2  
gast| 0.5.3  
google-api-core| 1.32.0  
google-api-python-client| 2.55.0  
google-apitools| 0.5.31  
google-auth| 1.35.0  
google-auth-httplib2| 0.1.0  
google-auth-oauthlib| 0.4.6  
google-cloud-bigquery| 2.34.4  
google-cloud-bigquery-storage| 2.13.2  
google-cloud-bigtable| 1.7.2  
google-cloud-core| 1.7.2  
google-cloud-datastore| 1.15.5  
google-cloud-dlp| 3.7.1  
google-cloud-language| 1.3.2  
google-cloud-profiler| 3.1.0  
google-cloud-pubsub| 2.13.0  
google-cloud-pubsublite| 1.4.2  
google-cloud-recommendations-ai| 0.2.0  
google-cloud-spanner| 1.19.3  
google-cloud-videointelligence| 1.16.3  
google-cloud-vision| 1.0.2  
google-crc32c| 1.3.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.18  
google-resumable-media| 2.3.3  
googleapis-common-protos| 1.56.4  
grpc-google-iam-v1| 0.12.4  
grpcio| 1.47.0  
grpcio-gcp| 0.2.2  
grpcio-status| 1.47.0  
guppy3| 3.1.2  
h5py| 3.7.0  
hdfs| 2.7.0  
httplib2| 0.20.4  
idna| 3.3  
importlib-metadata| 4.12.0  
joblib| 1.1.0  
keras| 2.8.0  
Keras-Preprocessing| 1.1.2  
libclang| 14.0.6  
Markdown| 3.4.1  
MarkupSafe| 2.1.1  
mmh3| 3.0.0  
more-itertools| 8.13.0  
nltk| 3.7  
nose| 1.3.7  
numpy| 1.21.6  
oauth2client| 4.1.3  
oauthlib| 3.2.0  
opt-einsum| 3.3.0  
orjson| 3.7.2  
overrides| 6.1.0  
packaging| 21.3  
pandas| 1.3.5  
Pillow| 7.2.0  
pip| 22.2.1  
pluggy| 0.13.1  
proto-plus| 1.20.6  
protobuf| 3.19.4  
py| 1.11.0  
pyarrow| 7.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.2  
pymongo| 3.12.3  
pyparsing| 3.0.9  
pytest| 4.6.11  
python-dateutil| 2.8.2  
python-snappy| 0.6.1  
pytz| 2022.1  
PyYAML| 6.0  
regex| 2022.7.25  
requests| 2.28.0  
requests-oauthlib| 1.3.1  
rsa| 4.9  
scikit-learn| 1.0.2  
scipy| 1.7.3  
setuptools| 57.5.0  
six| 1.16.0  
soupsieve| 2.3.2.post1  
tensorboard| 2.8.0  
tensorboard-data-server| 0.6.1  
tensorboard-plugin-wit| 1.8.1  
tensorflow| 2.8.0  
tensorflow-io-gcs-filesystem| 0.26.0  
termcolor| 1.1.0  
tf-estimator-nightly| 2.8.0.dev2021122109  
threadpoolctl| 3.1.0  
tqdm| 4.64.0  
typing-utils| 0.1.0  
typing_extensions| 4.2.0  
uritemplate| 4.1.1  
urllib3| 1.26.11  
wcwidth| 0.2.5  
Werkzeug| 2.2.1  
wheel| 0.37.1  
wrapt| 1.14.1  
zipp| 3.8.1  
  
### Python 3.8.13

Package| Version  
---|---  
  
absl-py| 1.2.0  
astunparse| 1.6.3  
atomicwrites| 1.4.1  
attrs| 22.1.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.11.1  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2022.6.15  
charset-normalizer| 2.0.12  
click| 8.1.3  
cloudpickle| 2.1.0  
crcmod| 1.7  
Cython| 0.29.30  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 1.5.1  
fasteners| 0.17.3  
flatbuffers| 2.0  
future| 0.18.2  
gast| 0.5.3  
google-api-core| 1.32.0  
google-api-python-client| 2.55.0  
google-apitools| 0.5.31  
google-auth| 1.35.0  
google-auth-httplib2| 0.1.0  
google-auth-oauthlib| 0.4.6  
google-cloud-bigquery| 2.34.4  
google-cloud-bigquery-storage| 2.13.2  
google-cloud-bigtable| 1.7.2  
google-cloud-core| 1.7.2  
google-cloud-datastore| 1.15.5  
google-cloud-dlp| 3.7.1  
google-cloud-language| 1.3.2  
google-cloud-profiler| 3.1.0  
google-cloud-pubsub| 2.13.0  
google-cloud-pubsublite| 1.4.2  
google-cloud-recommendations-ai| 0.2.0  
google-cloud-spanner| 1.19.3  
google-cloud-videointelligence| 1.16.3  
google-cloud-vision| 1.0.2  
google-crc32c| 1.3.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.18  
google-resumable-media| 2.3.3  
googleapis-common-protos| 1.56.4  
grpc-google-iam-v1| 0.12.4  
grpcio| 1.47.0  
grpcio-gcp| 0.2.2  
grpcio-status| 1.47.0  
guppy3| 3.1.2  
h5py| 3.7.0  
hdfs| 2.7.0  
httplib2| 0.20.4  
idna| 3.3  
importlib-metadata| 4.12.0  
joblib| 1.1.0  
keras| 2.8.0  
Keras-Preprocessing| 1.1.2  
libclang| 14.0.6  
Markdown| 3.4.1  
MarkupSafe| 2.1.1  
mmh3| 3.0.0  
more-itertools| 8.13.0  
nltk| 3.7  
nose| 1.3.7  
numpy| 1.22.3  
oauth2client| 4.1.3  
oauthlib| 3.2.0  
opt-einsum| 3.3.0  
orjson| 3.7.2  
overrides| 6.1.0  
packaging| 21.3  
pandas| 1.4.0  
Pillow| 7.2.0  
pip| 22.2.1  
pluggy| 0.13.1  
proto-plus| 1.20.6  
protobuf| 3.19.4  
py| 1.11.0  
pyarrow| 7.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.2  
pymongo| 3.12.3  
pyparsing| 3.0.9  
pytest| 4.6.11  
python-dateutil| 2.8.2  
python-snappy| 0.6.1  
pytz| 2022.1  
PyYAML| 6.0  
regex| 2022.7.25  
requests| 2.28.0  
requests-oauthlib| 1.3.1  
rsa| 4.9  
scikit-learn| 1.0.2  
scipy| 1.7.3  
setuptools| 57.5.0  
six| 1.16.0  
soupsieve| 2.3.2.post1  
tensorboard| 2.8.0  
tensorboard-data-server| 0.6.1  
tensorboard-plugin-wit| 1.8.1  
tensorflow| 2.8.0  
tensorflow-io-gcs-filesystem| 0.26.0  
termcolor| 1.1.0  
tf-estimator-nightly| 2.8.0.dev2021122109  
threadpoolctl| 3.1.0  
tqdm| 4.64.0  
typing-utils| 0.1.0  
typing_extensions| 4.2.0  
uritemplate| 4.1.1  
urllib3| 1.26.11  
wcwidth| 0.2.5  
Werkzeug| 2.2.1  
wheel| 0.37.1  
wrapt| 1.14.1  
zipp| 3.8.1  
  
### Python 3.9.13

Package| Version  
---|---  
  
absl-py| 1.2.0  
astunparse| 1.6.3  
atomicwrites| 1.4.1  
attrs| 22.1.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.11.1  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2022.6.15  
charset-normalizer| 2.0.12  
click| 8.1.3  
cloudpickle| 2.1.0  
crcmod| 1.7  
Cython| 0.29.30  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 1.5.1  
fasteners| 0.17.3  
flatbuffers| 2.0  
future| 0.18.2  
gast| 0.5.3  
google-api-core| 1.32.0  
google-api-python-client| 2.55.0  
google-apitools| 0.5.31  
google-auth| 1.35.0  
google-auth-httplib2| 0.1.0  
google-auth-oauthlib| 0.4.6  
google-cloud-bigquery| 2.34.4  
google-cloud-bigquery-storage| 2.13.2  
google-cloud-bigtable| 1.7.2  
google-cloud-core| 1.7.2  
google-cloud-datastore| 1.15.5  
google-cloud-dlp| 3.7.1  
google-cloud-language| 1.3.2  
google-cloud-profiler| 3.1.0  
google-cloud-pubsub| 2.13.0  
google-cloud-pubsublite| 1.4.2  
google-cloud-recommendations-ai| 0.2.0  
google-cloud-spanner| 1.19.3  
google-cloud-videointelligence| 1.16.3  
google-cloud-vision| 1.0.2  
google-crc32c| 1.3.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.18  
google-resumable-media| 2.3.3  
googleapis-common-protos| 1.56.4  
grpc-google-iam-v1| 0.12.4  
grpcio| 1.47.0  
grpcio-gcp| 0.2.2  
grpcio-status| 1.47.0  
guppy3| 3.1.2  
h5py| 3.7.0  
hdfs| 2.7.0  
httplib2| 0.20.4  
idna| 3.3  
importlib-metadata| 4.12.0  
joblib| 1.1.0  
keras| 2.8.0  
Keras-Preprocessing| 1.1.2  
libclang| 14.0.6  
Markdown| 3.4.1  
MarkupSafe| 2.1.1  
mmh3| 3.0.0  
more-itertools| 8.13.0  
nltk| 3.7  
nose| 1.3.7  
numpy| 1.22.3  
oauth2client| 4.1.3  
oauthlib| 3.2.0  
opt-einsum| 3.3.0  
orjson| 3.7.2  
overrides| 6.1.0  
packaging| 21.3  
pandas| 1.4.0  
Pillow| 7.2.0  
pip| 22.2.1  
pluggy| 0.13.1  
proto-plus| 1.20.6  
protobuf| 3.19.4  
py| 1.11.0  
pyarrow| 7.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.2  
pymongo| 3.12.3  
pyparsing| 3.0.9  
pytest| 4.6.11  
python-dateutil| 2.8.2  
python-snappy| 0.6.1  
pytz| 2022.1  
PyYAML| 6.0  
regex| 2022.7.25  
requests| 2.28.0  
requests-oauthlib| 1.3.1  
rsa| 4.9  
scikit-learn| 1.0.2  
scipy| 1.7.3  
setuptools| 58.1.0  
six| 1.16.0  
soupsieve| 2.3.2.post1  
tensorboard| 2.8.0  
tensorboard-data-server| 0.6.1  
tensorboard-plugin-wit| 1.8.1  
tensorflow| 2.8.0  
tensorflow-io-gcs-filesystem| 0.26.0  
termcolor| 1.1.0  
tf-estimator-nightly| 2.8.0.dev2021122109  
threadpoolctl| 3.1.0  
tqdm| 4.64.0  
typing-utils| 0.1.0  
typing_extensions| 4.2.0  
uritemplate| 4.1.1  
urllib3| 1.26.11  
wcwidth| 0.2.5  
Werkzeug| 2.2.1  
wheel| 0.37.1  
wrapt| 1.14.1  
zipp| 3.8.1  
  
#### Version 2.40.0

Dataflow workers have the following packages already installed.

### Python 3.7.13

Package| Version  
---|---  
  
absl-py| 1.1.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 21.4.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.11.1  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2022.6.15  
charset-normalizer| 2.0.12  
click| 8.1.3  
cloudpickle| 2.1.0  
crcmod| 1.7  
Cython| 0.29.30  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 1.5.1  
fasteners| 0.17.3  
flatbuffers| 2.0  
future| 0.18.2  
gast| 0.5.3  
google-api-core| 1.31.6  
google-api-python-client| 2.51.0  
google-apitools| 0.5.31  
google-auth| 1.35.0  
google-auth-httplib2| 0.1.0  
google-auth-oauthlib| 0.4.6  
google-cloud-bigquery| 2.34.4  
google-cloud-bigquery-storage| 2.13.2  
google-cloud-bigtable| 1.7.2  
google-cloud-core| 1.7.2  
google-cloud-datastore| 1.15.5  
google-cloud-dlp| 3.7.1  
google-cloud-language| 1.3.2  
google-cloud-profiler| 3.1.0  
google-cloud-pubsub| 2.13.0  
google-cloud-pubsublite| 1.4.2  
google-cloud-recommendations-ai| 0.2.0  
google-cloud-spanner| 1.19.3  
google-cloud-videointelligence| 1.16.3  
google-cloud-vision| 1.0.2  
google-crc32c| 1.3.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.18  
google-resumable-media| 2.3.3  
googleapis-common-protos| 1.56.3  
grpc-google-iam-v1| 0.12.4  
grpcio| 1.47.0  
grpcio-gcp| 0.2.2  
grpcio-status| 1.47.0  
guppy3| 3.1.2  
h5py| 3.7.0  
hdfs| 2.7.0  
httplib2| 0.20.4  
idna| 3.3  
importlib-metadata| 4.11.4  
joblib| 1.1.0  
keras| 2.8.0  
Keras-Preprocessing| 1.1.2  
libclang| 14.0.1  
Markdown| 3.3.7  
mmh3| 3.0.0  
more-itertools| 8.13.0  
nltk| 3.7  
nose| 1.3.7  
numpy| 1.21.6  
oauth2client| 4.1.3  
oauthlib| 3.2.0  
opt-einsum| 3.3.0  
orjson| 3.7.2  
overrides| 6.1.0  
packaging| 21.3  
pandas| 1.3.5  
Pillow| 7.2.0  
pip| 22.1.2  
pluggy| 0.13.1  
proto-plus| 1.20.6  
protobuf| 3.19.4  
py| 1.11.0  
pyarrow| 7.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.2  
pymongo| 3.12.3  
pyparsing| 3.0.9  
pytest| 4.6.11  
python-dateutil| 2.8.2  
python-snappy| 0.6.1  
pytz| 2022.1  
PyYAML| 6.0  
regex| 2022.6.2  
requests| 2.28.0  
requests-oauthlib| 1.3.1  
rsa| 4.8  
scikit-learn| 1.0.2  
scipy| 1.7.3  
setuptools| 57.5.0  
six| 1.16.0  
soupsieve| 2.3.2.post1  
tensorboard| 2.8.0  
tensorboard-data-server| 0.6.1  
tensorboard-plugin-wit| 1.8.1  
tensorflow| 2.8.0  
tensorflow-io-gcs-filesystem| 0.26.0  
termcolor| 1.1.0  
tf-estimator-nightly| 2.8.0.dev2021122109  
threadpoolctl| 3.1.0  
tqdm| 4.64.0  
typing-utils| 0.1.0  
typing_extensions| 4.2.0  
uritemplate| 4.1.1  
urllib3| 1.26.9  
wcwidth| 0.2.5  
Werkzeug| 2.1.2  
wheel| 0.37.1  
wrapt| 1.14.1  
zipp| 3.8.0  
  
### Python 3.8.13

Package| Version  
---|---  
  
absl-py| 1.1.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 21.4.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.11.1  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2022.6.15  
charset-normalizer| 2.0.12  
click| 8.1.3  
cloudpickle| 2.1.0  
crcmod| 1.7  
Cython| 0.29.30  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 1.5.1  
fasteners| 0.17.3  
flatbuffers| 2.0  
future| 0.18.2  
gast| 0.5.3  
google-api-core| 1.31.6  
google-api-python-client| 2.51.0  
google-apitools| 0.5.31  
google-auth| 1.35.0  
google-auth-httplib2| 0.1.0  
google-auth-oauthlib| 0.4.6  
google-cloud-bigquery| 2.34.4  
google-cloud-bigquery-storage| 2.13.2  
google-cloud-bigtable| 1.7.2  
google-cloud-core| 1.7.2  
google-cloud-datastore| 1.15.5  
google-cloud-dlp| 3.7.1  
google-cloud-language| 1.3.2  
google-cloud-profiler| 3.1.0  
google-cloud-pubsub| 2.13.0  
google-cloud-pubsublite| 1.4.2  
google-cloud-recommendations-ai| 0.2.0  
google-cloud-spanner| 1.19.3  
google-cloud-videointelligence| 1.16.3  
google-cloud-vision| 1.0.2  
google-crc32c| 1.3.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.18  
google-resumable-media| 2.3.3  
googleapis-common-protos| 1.56.3  
grpc-google-iam-v1| 0.12.4  
grpcio| 1.47.0  
grpcio-gcp| 0.2.2  
grpcio-status| 1.47.0  
guppy3| 3.1.2  
h5py| 3.7.0  
hdfs| 2.7.0  
httplib2| 0.20.4  
idna| 3.3  
importlib-metadata| 4.11.4  
joblib| 1.1.0  
keras| 2.8.0  
Keras-Preprocessing| 1.1.2  
libclang| 14.0.1  
Markdown| 3.3.7  
mmh3| 3.0.0  
more-itertools| 8.13.0  
nltk| 3.7  
nose| 1.3.7  
numpy| 1.22.3  
oauth2client| 4.1.3  
oauthlib| 3.2.0  
opt-einsum| 3.3.0  
orjson| 3.7.2  
overrides| 6.1.0  
packaging| 21.3  
pandas| 1.4.0  
Pillow| 7.2.0  
pip| 22.1.2  
pluggy| 0.13.1  
proto-plus| 1.20.6  
protobuf| 3.19.4  
py| 1.11.0  
pyarrow| 7.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.2  
pymongo| 3.12.3  
pyparsing| 3.0.9  
pytest| 4.6.11  
python-dateutil| 2.8.2  
python-snappy| 0.6.1  
pytz| 2022.1  
PyYAML| 6.0  
regex| 2022.6.2  
requests| 2.28.0  
requests-oauthlib| 1.3.1  
rsa| 4.8  
scikit-learn| 1.0.2  
scipy| 1.7.3  
setuptools| 57.5.0  
six| 1.16.0  
soupsieve| 2.3.2.post1  
tensorboard| 2.8.0  
tensorboard-data-server| 0.6.1  
tensorboard-plugin-wit| 1.8.1  
tensorflow| 2.8.0  
tensorflow-io-gcs-filesystem| 0.26.0  
termcolor| 1.1.0  
tf-estimator-nightly| 2.8.0.dev2021122109  
threadpoolctl| 3.1.0  
tqdm| 4.64.0  
typing-utils| 0.1.0  
typing_extensions| 4.2.0  
uritemplate| 4.1.1  
urllib3| 1.26.9  
wcwidth| 0.2.5  
Werkzeug| 2.1.2  
wheel| 0.37.1  
wrapt| 1.14.1  
zipp| 3.8.0  
  
### Python 3.9.12

Package| Version  
---|---  
  
absl-py| 1.1.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 21.4.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.11.1  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2022.6.15  
charset-normalizer| 2.0.12  
click| 8.1.3  
cloudpickle| 2.1.0  
crcmod| 1.7  
Cython| 0.29.30  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 1.5.1  
fasteners| 0.17.3  
flatbuffers| 2.0  
future| 0.18.2  
gast| 0.5.3  
google-api-core| 1.31.6  
google-api-python-client| 2.51.0  
google-apitools| 0.5.31  
google-auth| 1.35.0  
google-auth-httplib2| 0.1.0  
google-auth-oauthlib| 0.4.6  
google-cloud-bigquery| 2.34.4  
google-cloud-bigquery-storage| 2.13.2  
google-cloud-bigtable| 1.7.2  
google-cloud-core| 1.7.2  
google-cloud-datastore| 1.15.5  
google-cloud-dlp| 3.7.1  
google-cloud-language| 1.3.2  
google-cloud-profiler| 3.1.0  
google-cloud-pubsub| 2.13.0  
google-cloud-pubsublite| 1.4.2  
google-cloud-recommendations-ai| 0.2.0  
google-cloud-spanner| 1.19.3  
google-cloud-videointelligence| 1.16.3  
google-cloud-vision| 1.0.2  
google-crc32c| 1.3.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.18  
google-resumable-media| 2.3.3  
googleapis-common-protos| 1.56.3  
grpc-google-iam-v1| 0.12.4  
grpcio| 1.47.0  
grpcio-gcp| 0.2.2  
grpcio-status| 1.47.0  
guppy3| 3.1.2  
h5py| 3.7.0  
hdfs| 2.7.0  
httplib2| 0.20.4  
idna| 3.3  
importlib-metadata| 4.11.4  
joblib| 1.1.0  
keras| 2.8.0  
Keras-Preprocessing| 1.1.2  
libclang| 14.0.1  
Markdown| 3.3.7  
mmh3| 3.0.0  
more-itertools| 8.13.0  
nltk| 3.7  
nose| 1.3.7  
numpy| 1.22.3  
oauth2client| 4.1.3  
oauthlib| 3.2.0  
opt-einsum| 3.3.0  
orjson| 3.7.2  
overrides| 6.1.0  
packaging| 21.3  
pandas| 1.4.0  
Pillow| 7.2.0  
pip| 22.1.2  
pluggy| 0.13.1  
proto-plus| 1.20.6  
protobuf| 3.19.4  
py| 1.11.0  
pyarrow| 7.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.2  
pymongo| 3.12.3  
pyparsing| 3.0.9  
pytest| 4.6.11  
python-dateutil| 2.8.2  
python-snappy| 0.6.1  
pytz| 2022.1  
PyYAML| 6.0  
regex| 2022.6.2  
requests| 2.28.0  
requests-oauthlib| 1.3.1  
rsa| 4.8  
scikit-learn| 1.0.2  
scipy| 1.7.3  
setuptools| 58.1.0  
six| 1.16.0  
soupsieve| 2.3.2.post1  
tensorboard| 2.8.0  
tensorboard-data-server| 0.6.1  
tensorboard-plugin-wit| 1.8.1  
tensorflow| 2.8.0  
tensorflow-io-gcs-filesystem| 0.26.0  
termcolor| 1.1.0  
tf-estimator-nightly| 2.8.0.dev2021122109  
threadpoolctl| 3.1.0  
tqdm| 4.64.0  
typing-utils| 0.1.0  
typing_extensions| 4.2.0  
uritemplate| 4.1.1  
urllib3| 1.26.9  
wcwidth| 0.2.5  
Werkzeug| 2.1.2  
wheel| 0.37.1  
wrapt| 1.14.1  
zipp| 3.8.0  
  
#### Version 2.39.0

Dataflow workers have the following packages already installed.

### Python 3.7.13

Package| Version  
---|---  
  
absl-py| 1.0.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 21.4.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.10.0  
bs4| 0.0.1  
cached-property| 1.5.2  
cachetools| 4.2.4  
certifi| 2021.10.8  
charset-normalizer| 2.0.12  
click| 8.1.2  
cloudpickle| 2.0.0  
crcmod| 1.7  
Cython| 0.29.27  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 1.4.10  
fasteners| 0.17.3  
flatbuffers| 2.0  
future| 0.18.2  
gast| 0.5.3  
google-api-core| 1.31.5  
google-api-python-client| 2.43.0  
google-apitools| 0.5.31  
google-auth| 1.35.0  
google-auth-httplib2| 0.1.0  
google-auth-oauthlib| 0.4.6  
google-cloud-bigquery| 2.34.2  
google-cloud-bigquery-storage| 2.13.0  
google-cloud-bigtable| 1.7.0  
google-cloud-core| 1.7.2  
google-cloud-datastore| 1.15.3  
google-cloud-dlp| 3.6.2  
google-cloud-language| 1.3.0  
google-cloud-profiler| 3.0.7  
google-cloud-pubsub| 2.11.0  
google-cloud-pubsublite| 1.4.1  
google-cloud-recommendations-ai| 0.2.0  
google-cloud-spanner| 1.19.1  
google-cloud-videointelligence| 1.16.1  
google-cloud-vision| 1.0.0  
google-crc32c| 1.3.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.18  
google-resumable-media| 2.3.2  
googleapis-common-protos| 1.56.0  
grpc-google-iam-v1| 0.12.4  
grpcio| 1.44.0  
grpcio-gcp| 0.2.2  
grpcio-status| 1.44.0  
guppy3| 3.1.2  
h5py| 3.6.0  
hdfs| 2.6.0  
httplib2| 0.19.1  
idna| 3.3  
importlib-metadata| 4.11.3  
joblib| 1.1.0  
keras| 2.8.0  
Keras-Preprocessing| 1.1.2  
libclang| 13.0.0  
Markdown| 3.3.6  
mmh3| 3.0.0  
more-itertools| 8.12.0  
nltk| 3.6.5  
nose| 1.3.7  
numpy| 1.21.5  
oauth2client| 4.1.3  
oauthlib| 3.2.0  
opt-einsum| 3.3.0  
orjson| 3.6.6  
overrides| 6.1.0  
packaging| 21.3  
pandas| 1.3.5  
Pillow| 7.2.0  
pip| 22.0.4  
pluggy| 0.13.1  
proto-plus| 1.19.9  
protobuf| 3.19.4  
py| 1.11.0  
pyarrow| 6.0.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.2  
pymongo| 3.12.3  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.2  
python-snappy| 0.6.0  
pytz| 2021.3  
PyYAML| 6.0  
regex| 2022.3.15  
requests| 2.27.1  
requests-oauthlib| 1.3.1  
rsa| 4.8  
scikit-learn| 1.0.2  
scipy| 1.7.3  
setuptools| 57.5.0  
six| 1.16.0  
soupsieve| 2.3.2  
tensorboard| 2.8.0  
tensorboard-data-server| 0.6.1  
tensorboard-plugin-wit| 1.8.1  
tensorflow| 2.8.0  
tensorflow-io-gcs-filesystem| 0.24.0  
termcolor| 1.1.0  
tf-estimator-nightly| 2.8.0.dev2021122109  
threadpoolctl| 3.1.0  
tqdm| 4.64.0  
typing-utils| 0.1.0  
typing_extensions| 4.0.1  
uritemplate| 4.1.1  
urllib3| 1.26.9  
wcwidth| 0.2.5  
Werkzeug| 2.1.1  
wheel| 0.37.1  
wrapt| 1.14.0  
zipp| 3.8.0  
  
### Python 3.8.13

Package| Version  
---|---  
  
absl-py| 1.0.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 21.4.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.10.0  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2021.10.8  
charset-normalizer| 2.0.12  
click| 8.1.2  
cloudpickle| 2.0.0  
crcmod| 1.7  
Cython| 0.29.27  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 1.4.10  
fasteners| 0.17.3  
flatbuffers| 2.0  
future| 0.18.2  
gast| 0.5.3  
google-api-core| 1.31.5  
google-api-python-client| 2.43.0  
google-apitools| 0.5.31  
google-auth| 1.35.0  
google-auth-httplib2| 0.1.0  
google-auth-oauthlib| 0.4.6  
google-cloud-bigquery| 2.34.2  
google-cloud-bigquery-storage| 2.13.0  
google-cloud-bigtable| 1.7.0  
google-cloud-core| 1.7.2  
google-cloud-datastore| 1.15.3  
google-cloud-dlp| 3.6.2  
google-cloud-language| 1.3.0  
google-cloud-profiler| 3.0.7  
google-cloud-pubsub| 2.11.0  
google-cloud-pubsublite| 1.4.1  
google-cloud-recommendations-ai| 0.2.0  
google-cloud-spanner| 1.19.1  
google-cloud-videointelligence| 1.16.1  
google-cloud-vision| 1.0.0  
google-crc32c| 1.3.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.18  
google-resumable-media| 2.3.2  
googleapis-common-protos| 1.56.0  
grpc-google-iam-v1| 0.12.4  
grpcio| 1.44.0  
grpcio-gcp| 0.2.2  
grpcio-status| 1.44.0  
guppy3| 3.1.2  
h5py| 3.6.0  
hdfs| 2.6.0  
httplib2| 0.19.1  
idna| 3.3  
importlib-metadata| 4.11.3  
joblib| 1.1.0  
keras| 2.8.0  
Keras-Preprocessing| 1.1.2  
libclang| 13.0.0  
Markdown| 3.3.6  
mmh3| 3.0.0  
more-itertools| 8.12.0  
nltk| 3.6.5  
nose| 1.3.7  
numpy| 1.22.3  
oauth2client| 4.1.3  
oauthlib| 3.2.0  
opt-einsum| 3.3.0  
orjson| 3.6.6  
overrides| 6.1.0  
packaging| 21.3  
pandas| 1.4.0  
Pillow| 7.2.0  
pip| 22.0.4  
pluggy| 0.13.1  
proto-plus| 1.19.9  
protobuf| 3.19.4  
py| 1.11.0  
pyarrow| 6.0.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.2  
pymongo| 3.12.3  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.2  
python-snappy| 0.6.0  
pytz| 2022.1  
PyYAML| 6.0  
regex| 2022.3.15  
requests| 2.27.1  
requests-oauthlib| 1.3.1  
rsa| 4.8  
scikit-learn| 1.0.2  
scipy| 1.7.3  
setuptools| 57.5.0  
six| 1.16.0  
soupsieve| 2.3.2  
tensorboard| 2.8.0  
tensorboard-data-server| 0.6.1  
tensorboard-plugin-wit| 1.8.1  
tensorflow| 2.8.0  
tensorflow-io-gcs-filesystem| 0.24.0  
termcolor| 1.1.0  
tf-estimator-nightly| 2.8.0.dev2021122109  
threadpoolctl| 3.1.0  
tqdm| 4.64.0  
typing-utils| 0.1.0  
typing_extensions| 4.0.1  
uritemplate| 4.1.1  
urllib3| 1.26.9  
wcwidth| 0.2.5  
Werkzeug| 2.1.1  
wheel| 0.37.1  
wrapt| 1.14.0  
zipp| 3.8.0  
  
### Python 3.9.12

Package| Version  
---|---  
  
absl-py| 1.0.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 21.4.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.10.0  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2021.10.8  
charset-normalizer| 2.0.12  
click| 8.1.2  
cloudpickle| 2.0.0  
crcmod| 1.7  
Cython| 0.29.27  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 1.4.10  
fasteners| 0.17.3  
flatbuffers| 2.0  
future| 0.18.2  
gast| 0.5.3  
google-api-core| 1.31.5  
google-api-python-client| 2.43.0  
google-apitools| 0.5.31  
google-auth| 1.35.0  
google-auth-httplib2| 0.1.0  
google-auth-oauthlib| 0.4.6  
google-cloud-bigquery| 2.34.2  
google-cloud-bigquery-storage| 2.13.0  
google-cloud-bigtable| 1.7.0  
google-cloud-core| 1.7.2  
google-cloud-datastore| 1.15.3  
google-cloud-dlp| 3.6.2  
google-cloud-language| 1.3.0  
google-cloud-profiler| 3.0.7  
google-cloud-pubsub| 2.11.0  
google-cloud-pubsublite| 1.4.1  
google-cloud-recommendations-ai| 0.2.0  
google-cloud-spanner| 1.19.1  
google-cloud-videointelligence| 1.16.1  
google-cloud-vision| 1.0.0  
google-crc32c| 1.3.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.18  
google-resumable-media| 2.3.2  
googleapis-common-protos| 1.56.0  
grpc-google-iam-v1| 0.12.4  
grpcio| 1.44.0  
grpcio-gcp| 0.2.2  
grpcio-status| 1.44.0  
guppy3| 3.1.2  
h5py| 3.6.0  
hdfs| 2.6.0  
httplib2| 0.19.1  
idna| 3.3  
importlib-metadata| 4.11.3  
joblib| 1.1.0  
keras| 2.8.0  
Keras-Preprocessing| 1.1.2  
libclang| 13.0.0  
Markdown| 3.3.6  
mmh3| 3.0.0  
more-itertools| 8.12.0  
nltk| 3.6.5  
nose| 1.3.7  
numpy| 1.22.3  
oauth2client| 4.1.3  
oauthlib| 3.2.0  
opt-einsum| 3.3.0  
orjson| 3.6.6  
overrides| 6.1.0  
packaging| 21.3  
pandas| 1.4.0  
Pillow| 7.2.0  
pip| 22.0.4  
pluggy| 0.13.1  
proto-plus| 1.19.9  
protobuf| 3.19.4  
py| 1.11.0  
pyarrow| 6.0.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.2  
pymongo| 3.12.3  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.2  
python-snappy| 0.6.0  
pytz| 2021.3  
PyYAML| 6.0  
regex| 2022.3.15  
requests| 2.27.1  
requests-oauthlib| 1.3.1  
rsa| 4.8  
scikit-learn| 1.0.2  
scipy| 1.7.3  
setuptools| 58.1.0  
six| 1.16.0  
soupsieve| 2.3.2  
tensorboard| 2.8.0  
tensorboard-data-server| 0.6.1  
tensorboard-plugin-wit| 1.8.1  
tensorflow| 2.8.0  
tensorflow-io-gcs-filesystem| 0.24.0  
termcolor| 1.1.0  
tf-estimator-nightly| 2.8.0.dev2021122109  
threadpoolctl| 3.1.0  
tqdm| 4.64.0  
typing-utils| 0.1.0  
typing_extensions| 4.0.1  
uritemplate| 4.1.1  
urllib3| 1.26.9  
wcwidth| 0.2.5  
Werkzeug| 2.1.1  
wheel| 0.37.1  
wrapt| 1.14.0  
zipp| 3.8.0  
  
#### Version 2.38.0

Dataflow workers have the following packages already installed.

### Python 3.6.15

Package| Version  
---|---  
  
absl-py| 0.15.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 21.4.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.10.0  
bs4| 0.0.1  
cached-property| 1.5.2  
cachetools| 4.2.4  
certifi| 2021.10.8  
charset-normalizer| 2.0.11  
clang| 5.0  
click| 8.0.3  
cloudpickle| 2.0.0  
crcmod| 1.7  
Cython| 0.29.27  
dataclasses| 0.8  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 1.4.7  
fasteners| 0.17.3  
flatbuffers| 1.12  
future| 0.18.2  
gast| 0.4.0  
google-api-core| 1.31.5  
google-api-python-client| 2.36.0  
google-apitools| 0.5.31  
google-auth| 1.35.0  
google-auth-httplib2| 0.1.0  
google-auth-oauthlib| 0.4.6  
google-cloud-bigquery| 2.32.0  
google-cloud-bigquery-storage| 2.11.0  
google-cloud-bigtable| 1.7.0  
google-cloud-core| 1.7.2  
google-cloud-datastore| 1.15.3  
google-cloud-dlp| 3.6.0  
google-cloud-language| 1.3.0  
google-cloud-profiler| 3.0.7  
google-cloud-pubsub| 2.9.0  
google-cloud-pubsublite| 1.3.0  
google-cloud-recommendations-ai| 0.2.0  
google-cloud-spanner| 1.19.1  
google-cloud-videointelligence| 1.16.1  
google-cloud-vision| 1.0.0  
google-crc32c| 1.3.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.18  
google-resumable-media| 2.2.0  
googleapis-common-protos| 1.54.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.43.0  
grpcio-gcp| 0.2.2  
grpcio-status| 1.43.0  
guppy3| 3.1.2  
h5py| 3.1.0  
hdfs| 2.6.0  
httplib2| 0.19.1  
idna| 3.3  
importlib-metadata| 4.8.3  
joblib| 1.1.0  
keras| 2.6.0  
Keras-Preprocessing| 1.1.2  
libcst| 0.4.1  
Markdown| 3.3.6  
mmh3| 3.0.0  
more-itertools| 8.12.0  
mypy-extensions| 0.4.3  
nltk| 3.6.5  
nose| 1.3.7  
numpy| 1.19.5  
oauth2client| 4.1.3  
oauthlib| 3.2.0  
opt-einsum| 3.3.0  
orjson| 3.6.1  
overrides| 6.1.0  
packaging| 21.3  
pandas| 1.1.5  
Pillow| 7.2.0  
pip| 21.3.1  
pluggy| 0.13.1  
proto-plus| 1.19.9  
protobuf| 3.19.4  
py| 1.11.0  
pyarrow| 6.0.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.2  
pymongo| 3.12.3  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.2  
python-snappy| 0.6.0  
pytz| 2021.3  
PyYAML| 6.0  
regex| 2022.1.18  
requests| 2.27.1  
requests-oauthlib| 1.3.1  
rsa| 4.8  
scikit-learn| 0.24.2  
scipy| 1.5.4  
setuptools| 57.5.0  
six| 1.15.0  
soupsieve| 2.3.1  
tensorboard| 2.6.0  
tensorboard-data-server| 0.6.1  
tensorboard-plugin-wit| 1.8.1  
tensorflow| 2.6.2  
tensorflow-estimator| 2.6.0  
termcolor| 1.1.0  
threadpoolctl| 3.1.0  
tqdm| 4.62.3  
typing-extensions| 3.7.4.3  
typing-inspect| 0.7.1  
typing-utils| 0.1.0  
uritemplate| 4.1.1  
urllib3| 1.26.8  
wcwidth| 0.2.5  
Werkzeug| 2.0.3  
wheel| 0.37.0  
wrapt| 1.12.1  
zipp| 3.6.0  
  
### Python 3.7.12

Package| Version  
---|---  
  
absl-py| 1.0.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 21.4.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.10.0  
bs4| 0.0.1  
cached-property| 1.5.2  
cachetools| 4.2.4  
certifi| 2021.10.8  
charset-normalizer| 2.0.11  
click| 8.0.3  
cloudpickle| 2.0.0  
crcmod| 1.7  
Cython| 0.29.27  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 1.4.9  
fasteners| 0.17.3  
flatbuffers| 2.0  
future| 0.18.2  
gast| 0.5.3  
google-api-core| 1.31.5  
google-api-python-client| 2.36.0  
google-apitools| 0.5.31  
google-auth| 1.35.0  
google-auth-httplib2| 0.1.0  
google-auth-oauthlib| 0.4.6  
google-cloud-bigquery| 2.32.0  
google-cloud-bigquery-storage| 2.11.0  
google-cloud-bigtable| 1.7.0  
google-cloud-core| 1.7.2  
google-cloud-datastore| 1.15.3  
google-cloud-dlp| 3.6.0  
google-cloud-language| 1.3.0  
google-cloud-profiler| 3.0.7  
google-cloud-pubsub| 2.9.0  
google-cloud-pubsublite| 1.3.0  
google-cloud-recommendations-ai| 0.2.0  
google-cloud-spanner| 1.19.1  
google-cloud-videointelligence| 1.16.1  
google-cloud-vision| 1.0.0  
google-crc32c| 1.3.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.18  
google-resumable-media| 2.2.0  
googleapis-common-protos| 1.54.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.43.0  
grpcio-gcp| 0.2.2  
grpcio-status| 1.43.0  
guppy3| 3.1.2  
h5py| 3.6.0  
hdfs| 2.6.0  
httplib2| 0.19.1  
idna| 3.3  
importlib-metadata| 4.10.1  
joblib| 1.1.0  
keras| 2.8.0  
Keras-Preprocessing| 1.1.2  
libclang| 13.0.0  
libcst| 0.4.1  
Markdown| 3.3.6  
mmh3| 3.0.0  
more-itertools| 8.12.0  
mypy-extensions| 0.4.3  
nltk| 3.6.5  
nose| 1.3.7  
numpy| 1.21.5  
oauth2client| 4.1.3  
oauthlib| 3.2.0  
opt-einsum| 3.3.0  
orjson| 3.6.6  
overrides| 6.1.0  
packaging| 21.3  
pandas| 1.3.5  
Pillow| 7.2.0  
pip| 22.0.3  
pluggy| 0.13.1  
proto-plus| 1.19.9  
protobuf| 3.19.4  
py| 1.11.0  
pyarrow| 6.0.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.2  
pymongo| 3.12.3  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.2  
python-snappy| 0.6.0  
pytz| 2021.3  
PyYAML| 6.0  
regex| 2022.1.18  
requests| 2.27.1  
requests-oauthlib| 1.3.1  
rsa| 4.8  
scikit-learn| 1.0.2  
scipy| 1.7.3  
setuptools| 57.5.0  
six| 1.16.0  
soupsieve| 2.3.1  
tensorboard| 2.8.0  
tensorboard-data-server| 0.6.1  
tensorboard-plugin-wit| 1.8.1  
tensorflow| 2.8.0  
tensorflow-io-gcs-filesystem| 0.24.0  
termcolor| 1.1.0  
tf-estimator-nightly| 2.8.0.dev2021122109  
threadpoolctl| 3.1.0  
tqdm| 4.62.3  
typing-inspect| 0.7.1  
typing-utils| 0.1.0  
typing_extensions| 4.0.1  
uritemplate| 4.1.1  
urllib3| 1.26.8  
wcwidth| 0.2.5  
Werkzeug| 2.0.3  
wheel| 0.37.1  
wrapt| 1.13.3  
zipp| 3.7.0  
  
### Python 3.8.12

Package| Version  
---|---  
  
absl-py| 1.0.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 21.4.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.10.0  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2021.10.8  
charset-normalizer| 2.0.11  
click| 8.0.3  
cloudpickle| 2.0.0  
crcmod| 1.7  
Cython| 0.29.27  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 1.4.9  
fasteners| 0.17.3  
flatbuffers| 2.0  
future| 0.18.2  
gast| 0.5.3  
google-api-core| 1.31.5  
google-api-python-client| 2.36.0  
google-apitools| 0.5.31  
google-auth| 1.35.0  
google-auth-httplib2| 0.1.0  
google-auth-oauthlib| 0.4.6  
google-cloud-bigquery| 2.32.0  
google-cloud-bigquery-storage| 2.11.0  
google-cloud-bigtable| 1.7.0  
google-cloud-core| 1.7.2  
google-cloud-datastore| 1.15.3  
google-cloud-dlp| 3.6.0  
google-cloud-language| 1.3.0  
google-cloud-profiler| 3.0.7  
google-cloud-pubsub| 2.9.0  
google-cloud-pubsublite| 1.3.0  
google-cloud-recommendations-ai| 0.2.0  
google-cloud-spanner| 1.19.1  
google-cloud-videointelligence| 1.16.1  
google-cloud-vision| 1.0.0  
google-crc32c| 1.3.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.18  
google-resumable-media| 2.2.0  
googleapis-common-protos| 1.54.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.43.0  
grpcio-gcp| 0.2.2  
grpcio-status| 1.43.0  
guppy3| 3.1.2  
h5py| 3.6.0  
hdfs| 2.6.0  
httplib2| 0.19.1  
idna| 3.3  
importlib-metadata| 4.10.1  
joblib| 1.1.0  
keras| 2.8.0  
Keras-Preprocessing| 1.1.2  
libclang| 13.0.0  
libcst| 0.4.1  
Markdown| 3.3.6  
mmh3| 3.0.0  
more-itertools| 8.12.0  
mypy-extensions| 0.4.3  
nltk| 3.6.5  
nose| 1.3.7  
numpy| 1.21.5  
oauth2client| 4.1.3  
oauthlib| 3.2.0  
opt-einsum| 3.3.0  
orjson| 3.6.6  
overrides| 6.1.0  
packaging| 21.3  
pandas| 1.4.0  
Pillow| 7.2.0  
pip| 22.0.3  
pluggy| 0.13.1  
proto-plus| 1.19.9  
protobuf| 3.19.4  
py| 1.11.0  
pyarrow| 6.0.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.2  
pymongo| 3.12.3  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.2  
python-snappy| 0.6.0  
pytz| 2021.3  
PyYAML| 6.0  
regex| 2022.1.18  
requests| 2.27.1  
requests-oauthlib| 1.3.1  
rsa| 4.8  
scikit-learn| 1.0.2  
scipy| 1.7.3  
setuptools| 57.5.0  
six| 1.16.0  
soupsieve| 2.3.1  
tensorboard| 2.8.0  
tensorboard-data-server| 0.6.1  
tensorboard-plugin-wit| 1.8.1  
tensorflow| 2.8.0  
tensorflow-io-gcs-filesystem| 0.24.0  
termcolor| 1.1.0  
tf-estimator-nightly| 2.8.0.dev2021122109  
threadpoolctl| 3.1.0  
tqdm| 4.62.3  
typing-inspect| 0.7.1  
typing-utils| 0.1.0  
typing_extensions| 4.0.1  
uritemplate| 4.1.1  
urllib3| 1.26.8  
wcwidth| 0.2.5  
Werkzeug| 2.0.3  
wheel| 0.37.1  
wrapt| 1.13.3  
zipp| 3.7.0  
  
### Python 3.9.10

Package| Version  
---|---  
  
absl-py| 1.0.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 21.4.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.10.0  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2021.10.8  
charset-normalizer| 2.0.11  
click| 8.0.3  
cloudpickle| 2.0.0  
crcmod| 1.7  
Cython| 0.29.27  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 1.4.9  
fasteners| 0.17.3  
flatbuffers| 2.0  
future| 0.18.2  
gast| 0.5.3  
google-api-core| 1.31.5  
google-api-python-client| 2.36.0  
google-apitools| 0.5.31  
google-auth| 1.35.0  
google-auth-httplib2| 0.1.0  
google-auth-oauthlib| 0.4.6  
google-cloud-bigquery| 2.32.0  
google-cloud-bigquery-storage| 2.11.0  
google-cloud-bigtable| 1.7.0  
google-cloud-core| 1.7.2  
google-cloud-datastore| 1.15.3  
google-cloud-dlp| 3.6.0  
google-cloud-language| 1.3.0  
google-cloud-profiler| 3.0.7  
google-cloud-pubsub| 2.9.0  
google-cloud-pubsublite| 1.3.0  
google-cloud-recommendations-ai| 0.2.0  
google-cloud-spanner| 1.19.1  
google-cloud-videointelligence| 1.16.1  
google-cloud-vision| 1.0.0  
google-crc32c| 1.3.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.18  
google-resumable-media| 2.2.0  
googleapis-common-protos| 1.54.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.43.0  
grpcio-gcp| 0.2.2  
grpcio-status| 1.43.0  
guppy3| 3.1.2  
h5py| 3.6.0  
hdfs| 2.6.0  
httplib2| 0.19.1  
idna| 3.3  
importlib-metadata| 4.10.1  
joblib| 1.1.0  
keras| 2.8.0  
Keras-Preprocessing| 1.1.2  
libclang| 13.0.0  
libcst| 0.4.1  
Markdown| 3.3.6  
mmh3| 3.0.0  
more-itertools| 8.12.0  
mypy-extensions| 0.4.3  
nltk| 3.6.5  
nose| 1.3.7  
numpy| 1.21.5  
oauth2client| 4.1.3  
oauthlib| 3.2.0  
opt-einsum| 3.3.0  
orjson| 3.6.6  
overrides| 6.1.0  
packaging| 21.3  
pandas| 1.4.0  
Pillow| 7.2.0  
pip| 22.0.3  
pluggy| 0.13.1  
proto-plus| 1.19.9  
protobuf| 3.19.4  
py| 1.11.0  
pyarrow| 6.0.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.2  
pymongo| 3.12.3  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.2  
python-snappy| 0.6.0  
pytz| 2021.3  
PyYAML| 6.0  
regex| 2022.1.18  
requests| 2.27.1  
requests-oauthlib| 1.3.1  
rsa| 4.8  
scikit-learn| 1.0.2  
scipy| 1.7.3  
setuptools| 58.1.0  
six| 1.16.0  
soupsieve| 2.3.1  
tensorboard| 2.8.0  
tensorboard-data-server| 0.6.1  
tensorboard-plugin-wit| 1.8.1  
tensorflow| 2.8.0  
tensorflow-io-gcs-filesystem| 0.24.0  
termcolor| 1.1.0  
tf-estimator-nightly| 2.8.0.dev2021122109  
threadpoolctl| 3.1.0  
tqdm| 4.62.3  
typing-inspect| 0.7.1  
typing-utils| 0.1.0  
typing_extensions| 4.0.1  
uritemplate| 4.1.1  
urllib3| 1.26.8  
wcwidth| 0.2.5  
Werkzeug| 2.0.3  
wheel| 0.37.1  
wrapt| 1.13.3  
zipp| 3.7.0  
  
#### Version 2.37.0

Dataflow workers have the following packages already installed.

### Python 3.6.15

Package| Version  
---|---  
  
absl-py| 0.15.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 21.4.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.10.0  
bs4| 0.0.1  
cached-property| 1.5.2  
cachetools| 4.2.4  
certifi| 2021.10.8  
charset-normalizer| 2.0.11  
clang| 5.0  
click| 8.0.3  
cloudpickle| 2.0.0  
crcmod| 1.7  
Cython| 0.29.27  
dataclasses| 0.8  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 1.4.7  
fasteners| 0.17.3  
flatbuffers| 1.12  
future| 0.18.2  
gast| 0.4.0  
google-api-core| 1.31.5  
google-api-python-client| 2.36.0  
google-apitools| 0.5.31  
google-auth| 1.35.0  
google-auth-httplib2| 0.1.0  
google-auth-oauthlib| 0.4.6  
google-cloud-bigquery| 2.32.0  
google-cloud-bigquery-storage| 2.11.0  
google-cloud-bigtable| 1.7.0  
google-cloud-core| 1.7.2  
google-cloud-datastore| 1.15.3  
google-cloud-dlp| 3.6.0  
google-cloud-language| 1.3.0  
google-cloud-profiler| 3.0.7  
google-cloud-pubsub| 2.9.0  
google-cloud-pubsublite| 1.3.0  
google-cloud-recommendations-ai| 0.2.0  
google-cloud-spanner| 1.19.1  
google-cloud-videointelligence| 1.16.1  
google-cloud-vision| 1.0.0  
google-crc32c| 1.3.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.18  
google-resumable-media| 2.2.0  
googleapis-common-protos| 1.54.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.43.0  
grpcio-gcp| 0.2.2  
grpcio-status| 1.43.0  
guppy3| 3.1.2  
h5py| 3.1.0  
hdfs| 2.6.0  
httplib2| 0.19.1  
idna| 3.3  
importlib-metadata| 4.8.3  
joblib| 1.1.0  
keras| 2.6.0  
Keras-Preprocessing| 1.1.2  
libcst| 0.4.1  
Markdown| 3.3.6  
mmh3| 3.0.0  
more-itertools| 8.12.0  
mypy-extensions| 0.4.3  
nltk| 3.6.5  
nose| 1.3.7  
numpy| 1.19.5  
oauth2client| 4.1.3  
oauthlib| 3.2.0  
opt-einsum| 3.3.0  
orjson| 3.6.1  
overrides| 6.1.0  
packaging| 21.3  
pandas| 1.1.5  
Pillow| 7.2.0  
pip| 21.3.1  
pluggy| 0.13.1  
proto-plus| 1.19.9  
protobuf| 3.19.4  
py| 1.11.0  
pyarrow| 6.0.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.2  
pymongo| 3.12.3  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.2  
python-snappy| 0.6.0  
pytz| 2021.3  
requests| 2.27.1  
requests-oauthlib| 1.3.1  
rsa| 4.8  
scikit-learn| 0.24.2  
scipy| 1.5.4  
setuptools| 57.5.0  
six| 1.15.0  
soupsieve| 2.3.1  
tensorboard| 2.6.0  
tensorboard-data-server| 0.6.1  
tensorboard-plugin-wit| 1.8.1  
tensorflow| 2.6.2  
tensorflow-estimator| 2.6.0  
termcolor| 1.1.0  
threadpoolctl| 3.1.0  
tqdm| 4.62.3  
typing-extensions| 3.7.4.3  
typing-inspect| 0.7.1  
typing-utils| 0.1.0  
uritemplate| 4.1.1  
urllib3| 1.26.8  
wcwidth| 0.2.5  
Werkzeug| 2.0.3  
wheel| 0.37.0  
wrapt| 1.12.1  
zipp| 3.6.0  
  
### Python 3.7.12

Package| Version  
---|---  
  
  
absl-py| 1.0.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 21.4.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.10.0  
bs4| 0.0.1  
cached-property| 1.5.2  
cachetools| 4.2.4  
certifi| 2021.10.8  
charset-normalizer| 2.0.11  
click| 8.0.3  
cloudpickle| 2.0.0  
crcmod| 1.7  
Cython| 0.29.27  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 1.4.9  
fasteners| 0.17.3  
flatbuffers| 2.0  
future| 0.18.2  
gast| 0.5.3  
google-api-core| 1.31.5  
google-api-python-client| 2.36.0  
google-apitools| 0.5.31  
google-auth| 1.35.0  
google-auth-httplib2| 0.1.0  
google-auth-oauthlib| 0.4.6  
google-cloud-bigquery| 2.32.0  
google-cloud-bigquery-storage| 2.11.0  
google-cloud-bigtable| 1.7.0  
google-cloud-core| 1.7.2  
google-cloud-datastore| 1.15.3  
google-cloud-dlp| 3.6.0  
google-cloud-language| 1.3.0  
google-cloud-profiler| 3.0.7  
google-cloud-pubsub| 2.9.0  
google-cloud-pubsublite| 1.3.0  
google-cloud-recommendations-ai| 0.2.0  
google-cloud-spanner| 1.19.1  
google-cloud-videointelligence| 1.16.1  
google-cloud-vision| 1.0.0  
google-crc32c| 1.3.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.18  
google-resumable-media| 2.2.0  
googleapis-common-protos| 1.54.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.43.0  
grpcio-gcp| 0.2.2  
grpcio-status| 1.43.0  
guppy3| 3.1.2  
h5py| 3.6.0  
hdfs| 2.6.0  
httplib2| 0.19.1  
idna| 3.3  
importlib-metadata| 4.10.1  
joblib| 1.1.0  
keras| 2.8.0  
Keras-Preprocessing| 1.1.2  
libclang| 13.0.0  
libcst| 0.4.1  
Markdown| 3.3.6  
mmh3| 3.0.0  
more-itertools| 8.12.0  
mypy-extensions| 0.4.3  
nltk| 3.6.5  
nose| 1.3.7  
numpy| 1.21.5  
oauth2client| 4.1.3  
oauthlib| 3.2.0  
opt-einsum| 3.3.0  
orjson| 3.6.6  
overrides| 6.1.0  
packaging| 21.3  
pandas| 1.3.5  
Pillow| 7.2.0  
pip| 22.0.3  
pluggy| 0.13.1  
proto-plus| 1.19.9  
protobuf| 3.19.4  
py| 1.11.0  
pyarrow| 6.0.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.2  
pymongo| 3.12.3  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.2  
python-snappy| 0.6.0  
pytz| 2021.3  
PyYAML| 6.0  
regex| 2022.1.18  
requests| 2.27.1  
requests-oauthlib| 1.3.1  
rsa| 4.8  
scikit-learn| 1.0.2  
scipy| 1.7.3  
setuptools| 57.5.0  
six| 1.16.0  
soupsieve| 2.3.1  
tensorboard| 2.8.0  
tensorboard-data-server| 0.6.1  
tensorboard-plugin-wit| 1.8.1  
tensorflow| 2.8.0  
tensorflow-io-gcs-filesystem| 0.24.0  
termcolor| 1.1.0  
tf-estimator-nightly| 2.8.0.dev2021122109  
threadpoolctl| 3.1.0  
tqdm| 4.62.3  
typing-inspect| 0.7.1  
typing-utils| 0.1.0  
typing_extensions| 4.0.1  
uritemplate| 4.1.1  
urllib3| 1.26.8  
wcwidth| 0.2.5  
Werkzeug| 2.0.3  
wheel| 0.37.1  
wrapt| 1.13.3  
zipp| 3.7.0  
  
### Python 3.8.12

Package| Version  
---|---  
  
absl-py| 1.0.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 21.4.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.10.0  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2021.10.8  
charset-normalizer| 2.0.11  
click| 8.0.3  
cloudpickle| 2.0.0  
crcmod| 1.7  
Cython| 0.29.27  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 1.4.9  
fasteners| 0.17.3  
flatbuffers| 2.0  
future| 0.18.2  
gast| 0.5.3  
google-api-core| 1.31.5  
google-api-python-client| 2.36.0  
google-apitools| 0.5.31  
google-auth| 1.35.0  
google-auth-httplib2| 0.1.0  
google-auth-oauthlib| 0.4.6  
google-cloud-bigquery| 2.32.0  
google-cloud-bigquery-storage| 2.11.0  
google-cloud-bigtable| 1.7.0  
google-cloud-core| 1.7.2  
google-cloud-datastore| 1.15.3  
google-cloud-dlp| 3.6.0  
google-cloud-language| 1.3.0  
google-cloud-profiler| 3.0.7  
google-cloud-pubsub| 2.9.0  
google-cloud-pubsublite| 1.3.0  
google-cloud-recommendations-ai| 0.2.0  
google-cloud-spanner| 1.19.1  
google-cloud-videointelligence| 1.16.1  
google-cloud-vision| 1.0.0  
google-crc32c| 1.3.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.18  
google-resumable-media| 2.2.0  
googleapis-common-protos| 1.54.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.43.0  
grpcio-gcp| 0.2.2  
grpcio-status| 1.43.0  
guppy3| 3.1.2  
h5py| 3.6.0  
hdfs| 2.6.0  
httplib2| 0.19.1  
idna| 3.3  
importlib-metadata| 4.10.1  
joblib| 1.1.0  
keras| 2.8.0  
Keras-Preprocessing| 1.1.2  
libclang| 13.0.0  
libcst| 0.4.1  
Markdown| 3.3.6  
mmh3| 3.0.0  
more-itertools| 8.12.0  
mypy-extensions| 0.4.3  
nltk| 3.6.5  
nose| 1.3.7  
numpy| 1.21.5  
oauth2client| 4.1.3  
oauthlib| 3.2.0  
opt-einsum| 3.3.0  
orjson| 3.6.6  
overrides| 6.1.0  
packaging| 21.3  
pandas| 1.4.0  
Pillow| 7.2.0  
pip| 22.0.3  
pluggy| 0.13.1  
proto-plus| 1.19.9  
protobuf| 3.19.4  
py| 1.11.0  
pyarrow| 6.0.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.2  
pymongo| 3.12.3  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.2  
python-snappy| 0.6.0  
pytz| 2021.3  
PyYAML| 6.0  
regex| 2022.1.18  
requests| 2.27.1  
requests-oauthlib| 1.3.1  
rsa| 4.8  
scikit-learn| 1.0.2  
scipy| 1.7.3  
setuptools| 57.5.0  
six| 1.16.0  
soupsieve| 2.3.1  
tensorboard| 2.8.0  
tensorboard-data-server| 0.6.1  
tensorboard-plugin-wit| 1.8.1  
tensorflow| 2.8.0  
tensorflow-io-gcs-filesystem| 0.24.0  
termcolor| 1.1.0  
tf-estimator-nightly| 2.8.0.dev2021122109  
threadpoolctl| 3.1.0  
tqdm| 4.62.3  
typing-inspect| 0.7.1  
typing-utils| 0.1.0  
typing_extensions| 4.0.1  
uritemplate| 4.1.1  
urllib3| 1.26.8  
wcwidth| 0.2.5  
Werkzeug| 2.0.3  
wheel| 0.37.1  
wrapt| 1.13.3  
zipp| 3.7.0  
  
### Python 3.9.10

Package| Version  
---|---  
  
absl-py| 1.0.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 21.4.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.10.0  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2021.10.8  
charset-normalizer| 2.0.11  
click| 8.0.3  
cloudpickle| 2.0.0  
crcmod| 1.7  
Cython| 0.29.27  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 1.4.9  
fasteners| 0.17.3  
flatbuffers| 2.0  
future| 0.18.2  
gast| 0.5.3  
google-api-core| 1.31.5  
google-api-python-client| 2.36.0  
google-apitools| 0.5.31  
google-auth| 1.35.0  
google-auth-httplib2| 0.1.0  
google-auth-oauthlib| 0.4.6  
google-cloud-bigquery| 2.32.0  
google-cloud-bigquery-storage| 2.11.0  
google-cloud-bigtable| 1.7.0  
google-cloud-core| 1.7.2  
google-cloud-datastore| 1.15.3  
google-cloud-dlp| 3.6.0  
google-cloud-language| 1.3.0  
google-cloud-profiler| 3.0.7  
google-cloud-pubsub| 2.9.0  
google-cloud-pubsublite| 1.3.0  
google-cloud-recommendations-ai| 0.2.0  
google-cloud-spanner| 1.19.1  
google-cloud-videointelligence| 1.16.1  
google-cloud-vision| 1.0.0  
google-crc32c| 1.3.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.18  
google-resumable-media| 2.2.0  
googleapis-common-protos| 1.54.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.43.0  
grpcio-gcp| 0.2.2  
grpcio-status| 1.43.0  
guppy3| 3.1.2  
h5py| 3.6.0  
hdfs| 2.6.0  
httplib2| 0.19.1  
idna| 3.3  
importlib-metadata| 4.10.1  
joblib| 1.1.0  
keras| 2.8.0  
Keras-Preprocessing| 1.1.2  
libclang| 13.0.0  
libcst| 0.4.1  
Markdown| 3.3.6  
mmh3| 3.0.0  
more-itertools| 8.12.0  
mypy-extensions| 0.4.3  
nltk| 3.6.5  
nose| 1.3.7  
numpy| 1.21.5  
oauth2client| 4.1.3  
oauthlib| 3.2.0  
opt-einsum| 3.3.0  
orjson| 3.6.6  
overrides| 6.1.0  
packaging| 21.3  
pandas| 1.4.0  
Pillow| 7.2.0  
pip| 22.0.3  
pluggy| 0.13.1  
proto-plus| 1.19.9  
protobuf| 3.19.4  
py| 1.11.0  
pyarrow| 6.0.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.2  
pymongo| 3.12.3  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.2  
python-snappy| 0.6.0  
pytz| 2021.3  
PyYAML| 6.0  
regex| 2022.1.18  
requests| 2.27.1  
requests-oauthlib| 1.3.1  
rsa| 4.8  
scikit-learn| 1.0.2  
scipy| 1.7.3  
setuptools| 58.1.0  
six| 1.16.0  
soupsieve| 2.3.1  
tensorboard| 2.8.0  
tensorboard-data-server| 0.6.1  
tensorboard-plugin-wit| 1.8.1  
tensorflow| 2.8.0  
tensorflow-io-gcs-filesystem| 0.24.0  
termcolor| 1.1.0  
tf-estimator-nightly| 2.8.0.dev2021122109  
threadpoolctl| 3.1.0  
tqdm| 4.62.3  
typing-inspect| 0.7.1  
typing-utils| 0.1.0  
typing_extensions| 4.0.1  
uritemplate| 4.1.1  
urllib3| 1.26.8  
wcwidth| 0.2.5  
Werkzeug| 2.0.3  
wheel| 0.37.1  
wrapt| 1.13.3  
zipp| 3.7.0  
  
#### Version 2.36.0

Dataflow workers have the following packages already installed.

### Python 3.6.15

Package| Version  
---|---  
  
absl-py| 0.15.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 21.2.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.10.0  
bs4| 0.0.1  
cached-property| 1.5.2  
cachetools| 4.2.4  
certifi| 2021.10.8  
charset-normalizer| 2.0.9  
clang| 5.0  
click| 8.0.3  
cloudpickle| 2.0.0  
crcmod| 1.7  
Cython| 0.29.26  
dataclasses| 0.8  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 1.4.7  
fasteners| 0.16.3  
flatbuffers| 1.12  
future| 0.18.2  
gast| 0.4.0  
google-api-core| 1.31.5  
google-api-python-client| 2.33.0  
google-apitools| 0.5.31  
google-auth| 1.35.0  
google-auth-httplib2| 0.1.0  
google-auth-oauthlib| 0.4.6  
google-cloud-bigquery| 2.31.0  
google-cloud-bigquery-storage| 2.10.1  
google-cloud-bigtable| 1.7.0  
google-cloud-core| 1.7.2  
google-cloud-datastore| 1.15.3  
google-cloud-dlp| 3.4.0  
google-cloud-language| 1.3.0  
google-cloud-profiler| 3.0.6  
google-cloud-pubsub| 1.7.0  
google-cloud-recommendations-ai| 0.2.0  
google-cloud-spanner| 1.19.1  
google-cloud-videointelligence| 1.16.1  
google-cloud-vision| 1.0.0  
google-crc32c| 1.3.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.18  
google-resumable-media| 2.1.0  
googleapis-common-protos| 1.54.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.43.0  
grpcio-gcp| 0.2.2  
grpcio-status| 1.43.0  
guppy3| 3.1.2  
h5py| 3.1.0  
hdfs| 2.6.0  
httplib2| 0.19.1  
idna| 3.3  
importlib-metadata| 4.8.3  
joblib| 1.1.0  
keras| 2.6.0  
Keras-Preprocessing| 1.1.2  
libcst| 0.3.23  
Markdown| 3.3.6  
mmh3| 3.0.0  
more-itertools| 8.12.0  
mypy-extensions| 0.4.3  
nltk| 3.6.5  
nose| 1.3.7  
numpy| 1.19.5  
oauth2client| 4.1.3  
oauthlib| 3.1.1  
opt-einsum| 3.3.0  
orjson| 3.6.1  
packaging| 21.3  
pandas| 1.1.5  
Pillow| 7.2.0  
pip| 21.3.1  
pluggy| 0.13.1  
proto-plus| 1.19.8  
protobuf| 3.19.1  
py| 1.11.0  
pyarrow| 6.0.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.2  
pymongo| 3.12.3  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.2  
python-snappy| 0.6.0  
pytz| 2021.3  
PyYAML| 6.0  
regex| 2021.11.10  
requests| 2.26.0  
requests-oauthlib| 1.3.0  
rsa| 4.8  
scikit-learn| 0.24.2  
scipy| 1.5.4  
setuptools| 57.5.0  
six| 1.15.0  
soupsieve| 2.3.1  
tensorboard| 2.6.0  
tensorboard-data-server| 0.6.1  
tensorboard-plugin-wit| 1.8.0  
tensorflow| 2.6.2  
tensorflow-estimator| 2.6.0  
termcolor| 1.1.0  
threadpoolctl| 3.0.0  
tqdm| 4.62.3  
typing-extensions| 3.7.4.3  
typing-inspect| 0.7.1  
uritemplate| 4.1.1  
urllib3| 1.26.7  
wcwidth| 0.2.5  
Werkzeug| 2.0.2  
wheel| 0.37.0  
wrapt| 1.12.1  
zipp| 3.6.0  
  
### Python 3.7.12

Package| Version  
---|---  
  
absl-py| 1.0.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 21.2.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.10.0  
bs4| 0.0.1  
cached-property| 1.5.2  
cachetools| 4.2.4  
certifi| 2021.10.8  
charset-normalizer| 2.0.9  
click| 8.0.3  
cloudpickle| 2.0.0  
crcmod| 1.7  
Cython| 0.29.26  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 1.4.7  
fasteners| 0.16.3  
flatbuffers| 2.0  
future| 0.18.2  
gast| 0.4.0  
google-api-core| 1.31.5  
google-api-python-client| 2.33.0  
google-apitools| 0.5.31  
google-auth| 1.35.0  
google-auth-httplib2| 0.1.0  
google-auth-oauthlib| 0.4.6  
google-cloud-bigquery| 2.31.0  
google-cloud-bigquery-storage| 2.10.1  
google-cloud-bigtable| 1.7.0  
google-cloud-core| 1.7.2  
google-cloud-datastore| 1.15.3  
google-cloud-dlp| 3.4.0  
google-cloud-language| 1.3.0  
google-cloud-profiler| 3.0.6  
google-cloud-pubsub| 1.7.0  
google-cloud-recommendations-ai| 0.2.0  
google-cloud-spanner| 1.19.1  
google-cloud-videointelligence| 1.16.1  
google-cloud-vision| 1.0.0  
google-crc32c| 1.3.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.18  
google-resumable-media| 2.1.0  
googleapis-common-protos| 1.54.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.43.0  
grpcio-gcp| 0.2.2  
grpcio-status| 1.43.0  
guppy3| 3.1.2  
h5py| 3.6.0  
hdfs| 2.6.0  
httplib2| 0.19.1  
idna| 3.3  
importlib-metadata| 4.10.0  
joblib| 1.1.0  
keras| 2.7.0  
Keras-Preprocessing| 1.1.2  
libclang| 12.0.0  
libcst| 0.3.23  
Markdown| 3.3.6  
mmh3| 3.0.0  
more-itertools| 8.12.0  
mypy-extensions| 0.4.3  
nltk| 3.6.5  
nose| 1.3.7  
numpy| 1.21.4  
oauth2client| 4.1.3  
oauthlib| 3.1.1  
opt-einsum| 3.3.0  
orjson| 3.6.5  
packaging| 21.3  
pandas| 1.3.5  
Pillow| 7.2.0  
pip| 21.3.1  
pluggy| 0.13.1  
proto-plus| 1.19.8  
protobuf| 3.19.1  
py| 1.11.0  
pyarrow| 6.0.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.2  
pymongo| 3.12.3  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.2  
python-snappy| 0.6.0  
pytz| 2021.3  
PyYAML| 6.0  
regex| 2021.11.10  
requests| 2.26.0  
requests-oauthlib| 1.3.0  
rsa| 4.8  
scikit-learn| 1.0.1  
scipy| 1.7.2  
setuptools| 57.5.0  
six| 1.16.0  
soupsieve| 2.3.1  
tensorboard| 2.7.0  
tensorboard-data-server| 0.6.1  
tensorboard-plugin-wit| 1.8.0  
tensorflow| 2.7.0  
tensorflow-estimator| 2.7.0  
tensorflow-io-gcs-filesystem| 0.23.1  
termcolor| 1.1.0  
threadpoolctl| 3.0.0  
tqdm| 4.62.3  
typing-extensions| 3.10.0.2  
typing-inspect| 0.7.1  
uritemplate| 4.1.1  
urllib3| 1.26.7  
wcwidth| 0.2.5  
Werkzeug| 2.0.2  
wheel| 0.37.0  
wrapt| 1.13.3  
zipp| 3.6.0  
  
### Python 3.8.12

Package| Version  
---|---  
  
absl-py| 1.0.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 21.2.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.10.0  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2021.10.8  
charset-normalizer| 2.0.9  
click| 8.0.3  
cloudpickle| 2.0.0  
crcmod| 1.7  
Cython| 0.29.26  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 1.4.7  
fasteners| 0.16.3  
flatbuffers| 2.0  
future| 0.18.2  
gast| 0.4.0  
google-api-core| 1.31.5  
google-api-python-client| 2.33.0  
google-apitools| 0.5.31  
google-auth| 1.35.0  
google-auth-httplib2| 0.1.0  
google-auth-oauthlib| 0.4.6  
google-cloud-bigquery| 2.31.0  
google-cloud-bigquery-storage| 2.10.1  
google-cloud-bigtable| 1.7.0  
google-cloud-core| 1.7.2  
google-cloud-datastore| 1.15.3  
google-cloud-dlp| 3.4.0  
google-cloud-language| 1.3.0  
google-cloud-profiler| 3.0.6  
google-cloud-pubsub| 1.7.0  
google-cloud-recommendations-ai| 0.2.0  
google-cloud-spanner| 1.19.1  
google-cloud-videointelligence| 1.16.1  
google-cloud-vision| 1.0.0  
google-crc32c| 1.3.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.18  
google-resumable-media| 2.1.0  
googleapis-common-protos| 1.54.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.43.0  
grpcio-gcp| 0.2.2  
grpcio-status| 1.43.0  
guppy3| 3.1.2  
h5py| 3.6.0  
hdfs| 2.6.0  
httplib2| 0.19.1  
idna| 3.3  
importlib-metadata| 4.10.0  
joblib| 1.1.0  
keras| 2.7.0  
Keras-Preprocessing| 1.1.2  
libclang| 12.0.0  
libcst| 0.3.23  
Markdown| 3.3.6  
mmh3| 3.0.0  
more-itertools| 8.12.0  
mypy-extensions| 0.4.3  
nltk| 3.6.5  
nose| 1.3.7  
numpy| 1.21.4  
oauth2client| 4.1.3  
oauthlib| 3.1.1  
opt-einsum| 3.3.0  
orjson| 3.6.5  
packaging| 21.3  
pandas| 1.3.5  
Pillow| 7.2.0  
pip| 21.3.1  
pluggy| 0.13.1  
proto-plus| 1.19.8  
protobuf| 3.19.1  
py| 1.11.0  
pyarrow| 6.0.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.2  
pymongo| 3.12.3  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.2  
python-snappy| 0.6.0  
pytz| 2021.3  
PyYAML| 6.0  
regex| 2021.11.10  
requests| 2.26.0  
requests-oauthlib| 1.3.0  
rsa| 4.8  
scikit-learn| 1.0.1  
scipy| 1.7.2  
setuptools| 57.5.0  
six| 1.16.0  
soupsieve| 2.3.1  
tensorboard| 2.7.0  
tensorboard-data-server| 0.6.1  
tensorboard-plugin-wit| 1.8.0  
tensorflow| 2.7.0  
tensorflow-estimator| 2.7.0  
tensorflow-io-gcs-filesystem| 0.23.1  
termcolor| 1.1.0  
threadpoolctl| 3.0.0  
tqdm| 4.62.3  
typing-extensions| 3.10.0.2  
typing-inspect| 0.7.1  
uritemplate| 4.1.1  
urllib3| 1.26.7  
wcwidth| 0.2.5  
Werkzeug| 2.0.2  
wheel| 0.37.0  
wrapt| 1.13.3  
zipp| 3.6.0  
  
#### Version 2.35.0

Dataflow workers have the following packages already installed.

### Python 3.6.15

Package| Version  
---|---  
  
absl-py| 0.15.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 21.2.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.10.0  
bs4| 0.0.1  
cached-property| 1.5.2  
cachetools| 4.2.4  
certifi| 2021.10.8  
charset-normalizer| 2.0.8  
clang| 5.0  
click| 8.0.3  
cloudpickle| 2.0.0  
crcmod| 1.7  
Cython| 0.29.24  
dataclasses| 0.8  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 1.4.7  
fasteners| 0.16.3  
flatbuffers| 1.12  
future| 0.18.2  
gast| 0.4.0  
google-api-core| 1.31.4  
google-api-python-client| 2.31.0  
google-apitools| 0.5.31  
google-auth| 1.35.0  
google-auth-httplib2| 0.1.0  
google-auth-oauthlib| 0.4.6  
google-cloud-bigquery| 2.30.1  
google-cloud-bigquery-storage| 2.10.1  
google-cloud-bigtable| 1.7.0  
google-cloud-core| 1.7.2  
google-cloud-datastore| 1.15.3  
google-cloud-dlp| 3.3.1  
google-cloud-language| 1.3.0  
google-cloud-profiler| 3.0.6  
google-cloud-pubsub| 1.7.0  
google-cloud-recommendations-ai| 0.2.0  
google-cloud-spanner| 1.19.1  
google-cloud-videointelligence| 1.16.1  
google-cloud-vision| 1.0.0  
google-crc32c| 1.3.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.18  
google-resumable-media| 2.1.0  
googleapis-common-protos| 1.53.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.42.0  
grpcio-gcp| 0.2.2  
grpcio-status| 1.42.0  
guppy3| 3.1.2  
h5py| 3.1.0  
hdfs| 2.6.0  
httplib2| 0.19.1  
idna| 3.3  
importlib-metadata| 4.8.2  
joblib| 1.1.0  
keras| 2.6.0  
Keras-Preprocessing| 1.1.2  
libcst| 0.3.23  
Markdown| 3.3.6  
mmh3| 3.0.0  
more-itertools| 8.12.0  
mypy-extensions| 0.4.3  
nltk| 3.6.5  
nose| 1.3.7  
numpy| 1.19.5  
oauth2client| 4.1.3  
oauthlib| 3.1.1  
opt-einsum| 3.3.0  
orjson| 3.6.1  
packaging| 21.3  
pandas| 1.1.5  
Pillow| 7.2.0  
pip| 21.3.1  
pluggy| 0.13.1  
proto-plus| 1.19.8  
protobuf| 3.19.1  
py| 1.11.0  
pyarrow| 6.0.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.2  
pymongo| 3.12.1  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.2  
python-snappy| 0.6.0  
pytz| 2021.3  
PyYAML| 6.0  
regex| 2021.11.10  
requests| 2.26.0  
requests-oauthlib| 1.3.0  
rsa| 4.8  
scikit-learn| 0.24.2  
scipy| 1.5.4  
setuptools| 57.5.0  
six| 1.15.0  
soupsieve| 2.3.1  
tensorboard| 2.6.0  
tensorboard-data-server| 0.6.1  
tensorboard-plugin-wit| 1.8.0  
tensorflow| 2.6.2  
tensorflow-estimator| 2.6.0  
termcolor| 1.1.0  
threadpoolctl| 3.0.0  
tqdm| 4.62.3  
typing-extensions| 3.7.4.3  
typing-inspect| 0.7.1  
uritemplate| 4.1.1  
urllib3| 1.26.7  
wcwidth| 0.2.5  
Werkzeug| 2.0.2  
wheel| 0.37.0  
wrapt| 1.12.1  
zipp| 3.6.0  
  
### Python 3.7.12

Package| Version  
---|---  
  
absl-py| 1.0.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 21.2.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.10.0  
bs4| 0.0.1  
cached-property| 1.5.2  
cachetools| 4.2.4  
certifi| 2021.10.8  
charset-normalizer| 2.0.8  
click| 8.0.3  
cloudpickle| 2.0.0  
crcmod| 1.7  
Cython| 0.29.24  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 1.4.7  
fasteners| 0.16.3  
flatbuffers| 2.0  
future| 0.18.2  
gast| 0.4.0  
google-api-core| 1.31.4  
google-api-python-client| 2.31.0  
google-apitools| 0.5.31  
google-auth| 1.35.0  
google-auth-httplib2| 0.1.0  
google-auth-oauthlib| 0.4.6  
google-cloud-bigquery| 2.30.1  
google-cloud-bigquery-storage| 2.10.1  
google-cloud-bigtable| 1.7.0  
google-cloud-core| 1.7.2  
google-cloud-datastore| 1.15.3  
google-cloud-dlp| 3.3.1  
google-cloud-language| 1.3.0  
google-cloud-profiler| 3.0.6  
google-cloud-pubsub| 1.7.0  
google-cloud-recommendations-ai| 0.2.0  
google-cloud-spanner| 1.19.1  
google-cloud-videointelligence| 1.16.1  
google-cloud-vision| 1.0.0  
google-crc32c| 1.3.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.18  
google-resumable-media| 2.1.0  
googleapis-common-protos| 1.53.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.42.0  
grpcio-gcp| 0.2.2  
grpcio-status| 1.42.0  
guppy3| 3.1.2  
h5py| 3.6.0  
hdfs| 2.6.0  
httplib2| 0.19.1  
idna| 3.3  
importlib-metadata| 4.8.2  
joblib| 1.1.0  
keras| 2.7.0  
Keras-Preprocessing| 1.1.2  
libclang| 12.0.0  
libcst| 0.3.23  
Markdown| 3.3.6  
mmh3| 3.0.0  
more-itertools| 8.12.0  
mypy-extensions| 0.4.3  
nltk| 3.6.5  
nose| 1.3.7  
numpy| 1.20.3  
oauth2client| 4.1.3  
oauthlib| 3.1.1  
opt-einsum| 3.3.0  
orjson| 3.6.4  
packaging| 21.3  
pandas| 1.3.4  
Pillow| 7.2.0  
pip| 21.3.1  
pluggy| 0.13.1  
proto-plus| 1.19.8  
protobuf| 3.19.1  
py| 1.11.0  
pyarrow| 6.0.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.2  
pymongo| 3.12.1  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.2  
python-snappy| 0.6.0  
pytz| 2021.3  
PyYAML| 6.0  
regex| 2021.11.10  
requests| 2.26.0  
requests-oauthlib| 1.3.0  
rsa| 4.8  
scikit-learn| 1.0.1  
scipy| 1.7.2  
setuptools| 57.5.0  
six| 1.16.0  
soupsieve| 2.3.1  
tensorboard| 2.7.0  
tensorboard-data-server| 0.6.1  
tensorboard-plugin-wit| 1.8.0  
tensorflow| 2.7.0  
tensorflow-estimator| 2.7.0  
tensorflow-io-gcs-filesystem| 0.22.0  
termcolor| 1.1.0  
threadpoolctl| 3.0.0  
tqdm| 4.62.3  
typing-extensions| 3.10.0.2  
typing-inspect| 0.7.1  
uritemplate| 4.1.1  
urllib3| 1.26.7  
wcwidth| 0.2.5  
Werkzeug| 2.0.2  
wheel| 0.37.0  
wrapt| 1.13.3  
zipp| 3.6.0  
  
### Python 3.8.12

Package| Version  
---|---  
  
absl-py| 1.0.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 21.2.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.10.0  
bs4| 0.0.1  
cachetools| 4.2.4  
certifi| 2021.10.8  
charset-normalizer| 2.0.8  
click| 8.0.3  
cloudpickle| 2.0.0  
crcmod| 1.7  
Cython| 0.29.24  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 1.4.7  
fasteners| 0.16.3  
flatbuffers| 2.0  
future| 0.18.2  
gast| 0.4.0  
google-api-core| 1.31.4  
google-api-python-client| 2.31.0  
google-apitools| 0.5.31  
google-auth| 1.35.0  
google-auth-httplib2| 0.1.0  
google-auth-oauthlib| 0.4.6  
google-cloud-bigquery| 2.30.1  
google-cloud-bigquery-storage| 2.10.1  
google-cloud-bigtable| 1.7.0  
google-cloud-core| 1.7.2  
google-cloud-datastore| 1.15.3  
google-cloud-dlp| 3.3.1  
google-cloud-language| 1.3.0  
google-cloud-profiler| 3.0.6  
google-cloud-pubsub| 1.7.0  
google-cloud-recommendations-ai| 0.2.0  
google-cloud-spanner| 1.19.1  
google-cloud-videointelligence| 1.16.1  
google-cloud-vision| 1.0.0  
google-crc32c| 1.3.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.18  
google-resumable-media| 2.1.0  
googleapis-common-protos| 1.53.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.42.0  
grpcio-gcp| 0.2.2  
grpcio-status| 1.42.0  
guppy3| 3.1.2  
h5py| 3.6.0  
hdfs| 2.6.0  
httplib2| 0.19.1  
idna| 3.3  
importlib-metadata| 4.8.2  
joblib| 1.1.0  
keras| 2.7.0  
Keras-Preprocessing| 1.1.2  
libclang| 12.0.0  
libcst| 0.3.23  
Markdown| 3.3.6  
mmh3| 3.0.0  
more-itertools| 8.12.0  
mypy-extensions| 0.4.3  
nltk| 3.6.5  
nose| 1.3.7  
numpy| 1.20.3  
oauth2client| 4.1.3  
oauthlib| 3.1.1  
opt-einsum| 3.3.0  
orjson| 3.6.4  
packaging| 21.3  
pandas| 1.3.4  
Pillow| 7.2.0  
pip| 21.3.1  
pluggy| 0.13.1  
proto-plus| 1.19.8  
protobuf| 3.19.1  
py| 1.11.0  
pyarrow| 6.0.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.2  
pymongo| 3.12.1  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.2  
python-snappy| 0.6.0  
pytz| 2021.3  
PyYAML| 6.0  
regex| 2021.11.10  
requests| 2.26.0  
requests-oauthlib| 1.3.0  
rsa| 4.8  
scikit-learn| 1.0.1  
scipy| 1.7.2  
setuptools| 57.5.0  
six| 1.16.0  
soupsieve| 2.3.1  
tensorboard| 2.7.0  
tensorboard-data-server| 0.6.1  
tensorboard-plugin-wit| 1.8.0  
tensorflow| 2.7.0  
tensorflow-estimator| 2.7.0  
tensorflow-io-gcs-filesystem| 0.22.0  
termcolor| 1.1.0  
threadpoolctl| 3.0.0  
tqdm| 4.62.3  
typing-extensions| 3.10.0.2  
typing-inspect| 0.7.1  
uritemplate| 4.1.1  
urllib3| 1.26.7  
wcwidth| 0.2.5  
Werkzeug| 2.0.2  
wheel| 0.37.0  
wrapt| 1.13.3  
zipp| 3.6.0  
  
#### Version 2.34.0

Dataflow workers have the following packages already installed.

### Python 3.6.15

Package| Version  
---|---  
  
absl-py| 0.15.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 21.2.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.9.1  
bs4| 0.0.1  
cached-property| 1.5.2  
cachetools| 3.1.1  
certifi| 2021.10.8  
chardet| 3.0.4  
charset-normalizer| 2.0.7  
clang| 5.0  
click| 8.0.3  
crcmod| 1.7  
Cython| 0.29.21  
dataclasses| 0.8  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.24.2  
fasteners| 0.16.3  
flatbuffers| 1.12  
freezegun| 0.3.15  
future| 0.18.2  
gast| 0.4.0  
google-api-core| 1.31.3  
google-api-python-client| 2.29.0  
google-apitools| 0.5.31  
google-auth| 1.35.0  
google-auth-httplib2| 0.1.0  
google-auth-oauthlib| 0.4.6  
google-cloud-bigquery| 1.26.1  
google-cloud-bigquery-storage| 2.6.3  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.7.2  
google-cloud-datastore| 1.15.3  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-profiler| 3.0.4  
google-cloud-pubsub| 1.0.2  
google-cloud-recommendations-ai| 0.2.0  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-crc32c| 1.3.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.15  
google-resumable-media| 1.3.3  
googleapis-common-protos| 1.53.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.40.0  
grpcio-gcp| 0.2.2  
guppy3| 3.0.10  
h5py| 3.1.0  
hdfs| 2.5.8  
httplib2| 0.17.3  
idna| 2.10  
importlib-metadata| 4.8.1  
joblib| 1.1.0  
keras| 2.6.0  
Keras-Preprocessing| 1.1.2  
libcst| 0.3.21  
Markdown| 3.3.4  
mmh3| 2.5.1  
more-itertools| 8.10.0  
mypy-extensions| 0.4.3  
nltk| 3.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.19.5  
oauth2client| 3.0.0  
oauthlib| 3.1.1  
opt-einsum| 3.3.0  
orjson| 3.6.1  
packaging| 21.2  
pandas| 1.1.5  
Pillow| 7.2.0  
pip| 21.3.1  
pluggy| 0.13.1  
proto-plus| 1.19.6  
protobuf| 3.17.3  
protorpc| 0.12.0  
py| 1.10.0  
pyarrow| 3.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.1  
pymongo| 3.10.1  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2020.1  
PyYAML| 5.3.1  
regex| 2021.11.2  
requests| 2.24.0  
requests-oauthlib| 1.3.0  
rsa| 4.7.2  
scikit-learn| 0.24.1  
scipy| 1.4.1  
setuptools| 57.5.0  
six| 1.15.0  
soupsieve| 2.2.1  
tensorboard| 2.7.0  
tensorboard-data-server| 0.6.1  
tensorboard-plugin-wit| 1.8.0  
tensorflow| 2.6.0  
tensorflow-estimator| 2.7.0  
termcolor| 1.1.0  
threadpoolctl| 3.0.0  
tqdm| 4.62.3  
typing-extensions| 3.7.4.2  
typing-inspect| 0.7.1  
uritemplate| 4.1.1  
urllib3| 1.25.11  
wcwidth| 0.2.5  
Werkzeug| 2.0.2  
wheel| 0.37.0  
wrapt| 1.12.1  
zipp| 3.6.0  
  
### Python 3.7.12

Package| Version  
---|---  
  
absl-py| 0.15.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 21.2.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.9.1  
bs4| 0.0.1  
cached-property| 1.5.2  
cachetools| 3.1.1  
certifi| 2021.10.8  
chardet| 3.0.4  
charset-normalizer| 2.0.7  
clang| 5.0  
click| 8.0.3  
crcmod| 1.7  
Cython| 0.29.21  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.24.2  
fasteners| 0.16.3  
flatbuffers| 1.12  
freezegun| 0.3.15  
future| 0.18.2  
gast| 0.4.0  
google-api-core| 1.31.3  
google-api-python-client| 2.29.0  
google-apitools| 0.5.31  
google-auth| 1.35.0  
google-auth-httplib2| 0.1.0  
google-auth-oauthlib| 0.4.6  
google-cloud-bigquery| 1.26.1  
google-cloud-bigquery-storage| 2.6.3  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.7.2  
google-cloud-datastore| 1.15.3  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-profiler| 3.0.4  
google-cloud-pubsub| 1.0.2  
google-cloud-recommendations-ai| 0.2.0  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-crc32c| 1.3.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.15  
google-resumable-media| 1.3.3  
googleapis-common-protos| 1.53.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.40.0  
grpcio-gcp| 0.2.2  
guppy3| 3.0.10  
h5py| 3.1.0  
hdfs| 2.5.8  
httplib2| 0.17.3  
idna| 2.10  
importlib-metadata| 4.8.1  
joblib| 1.1.0  
keras| 2.6.0  
Keras-Preprocessing| 1.1.2  
libcst| 0.3.21  
Markdown| 3.3.4  
mmh3| 2.5.1  
more-itertools| 8.10.0  
mypy-extensions| 0.4.3  
nltk| 3.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.19.5  
oauth2client| 3.0.0  
oauthlib| 3.1.1  
opt-einsum| 3.3.0  
orjson| 3.6.4  
packaging| 21.2  
pandas| 1.3.3  
Pillow| 7.2.0  
pip| 21.3.1  
pluggy| 0.13.1  
proto-plus| 1.19.6  
protobuf| 3.17.3  
protorpc| 0.12.0  
py| 1.10.0  
pyarrow| 3.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.1  
pymongo| 3.10.1  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2020.1  
PyYAML| 5.3.1  
regex| 2021.11.2  
requests| 2.24.0  
requests-oauthlib| 1.3.0  
rsa| 4.7.2  
scikit-learn| 0.24.1  
scipy| 1.4.1  
setuptools| 57.5.0  
six| 1.15.0  
soupsieve| 2.2.1  
tensorboard| 2.7.0  
tensorboard-data-server| 0.6.1  
tensorboard-plugin-wit| 1.8.0  
tensorflow| 2.6.0  
tensorflow-estimator| 2.7.0  
termcolor| 1.1.0  
threadpoolctl| 3.0.0  
tqdm| 4.62.3  
typing-extensions| 3.7.4.2  
typing-inspect| 0.7.1  
uritemplate| 4.1.1  
urllib3| 1.25.11  
wcwidth| 0.2.5  
Werkzeug| 2.0.2  
wheel| 0.37.0  
wrapt| 1.12.1  
zipp| 3.6.0  
  
### Python 3.8.12

Package| Version  
---|---  
  
absl-py| 0.15.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 21.2.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.9.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2021.10.8  
chardet| 3.0.4  
charset-normalizer| 2.0.7  
clang| 5.0  
click| 8.0.3  
crcmod| 1.7  
Cython| 0.29.21  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.24.2  
fasteners| 0.16.3  
flatbuffers| 1.12  
freezegun| 0.3.15  
future| 0.18.2  
gast| 0.4.0  
google-api-core| 1.31.3  
google-api-python-client| 2.29.0  
google-apitools| 0.5.31  
google-auth| 1.35.0  
google-auth-httplib2| 0.1.0  
google-auth-oauthlib| 0.4.6  
google-cloud-bigquery| 1.26.1  
google-cloud-bigquery-storage| 2.6.3  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.7.2  
google-cloud-datastore| 1.15.3  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-profiler| 3.0.4  
google-cloud-pubsub| 1.0.2  
google-cloud-recommendations-ai| 0.2.0  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-crc32c| 1.3.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.15  
google-resumable-media| 1.3.3  
googleapis-common-protos| 1.53.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.40.0  
grpcio-gcp| 0.2.2  
guppy3| 3.0.10  
h5py| 3.1.0  
hdfs| 2.5.8  
httplib2| 0.17.3  
idna| 2.10  
joblib| 1.1.0  
keras| 2.6.0  
Keras-Preprocessing| 1.1.2  
libcst| 0.3.21  
Markdown| 3.3.4  
mmh3| 2.5.1  
more-itertools| 8.10.0  
mypy-extensions| 0.4.3  
nltk| 3.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.19.5  
oauth2client| 3.0.0  
oauthlib| 3.1.1  
opt-einsum| 3.3.0  
orjson| 3.6.4  
packaging| 21.2  
pandas| 1.3.3  
Pillow| 7.2.0  
pip| 21.3.1  
pluggy| 0.13.1  
proto-plus| 1.19.6  
protobuf| 3.17.3  
protorpc| 0.12.0  
py| 1.10.0  
pyarrow| 3.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.1  
pymongo| 3.10.1  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2020.1  
PyYAML| 5.3.1  
regex| 2021.11.2  
requests| 2.24.0  
requests-oauthlib| 1.3.0  
rsa| 4.7.2  
scikit-learn| 0.24.1  
scipy| 1.4.1  
setuptools| 57.5.0  
six| 1.15.0  
soupsieve| 2.2.1  
tensorboard| 2.7.0  
tensorboard-data-server| 0.6.1  
tensorboard-plugin-wit| 1.8.0  
tensorflow| 2.6.0  
tensorflow-estimator| 2.7.0  
termcolor| 1.1.0  
threadpoolctl| 3.0.0  
tqdm| 4.62.3  
typing-extensions| 3.7.4.2  
typing-inspect| 0.7.1  
uritemplate| 4.1.1  
urllib3| 1.25.11  
wcwidth| 0.2.5  
Werkzeug| 2.0.2  
wheel| 0.37.0  
wrapt| 1.12.1  
  
#### Version 2.33.0

Dataflow workers have the following packages already installed.

### Python 3.6.14

Package| Version  
---|---  
  
absl-py| 0.13.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 21.2.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.9.1  
bs4| 0.0.1  
cached-property| 1.5.2  
cachetools| 3.1.1  
certifi| 2021.5.30  
cffi| 1.14.6  
chardet| 3.0.4  
charset-normalizer| 2.0.4  
click| 8.0.1  
crcmod| 1.7  
Cython| 0.29.21  
dataclasses| 0.8  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.24.2  
fasteners| 0.16.3  
flatbuffers| 1.12  
freezegun| 0.3.15  
future| 0.18.2  
gast| 0.4.0  
google-api-core| 1.31.2  
google-api-python-client| 2.18.0  
google-apitools| 0.5.31  
google-auth| 1.35.0  
google-auth-httplib2| 0.1.0  
google-auth-oauthlib| 0.4.5  
google-cloud-bigquery| 1.26.1  
google-cloud-bigquery-storage| 2.4.0  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.7.2  
google-cloud-datastore| 1.15.3  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-profiler| 3.0.4  
google-cloud-pubsub| 1.0.2  
google-cloud-recommendations-ai| 0.2.0  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-crc32c| 1.1.2  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.15  
google-resumable-media| 1.3.3  
googleapis-common-protos| 1.53.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.34.1  
grpcio-gcp| 0.2.2  
guppy3| 3.0.10  
h5py| 3.1.0  
hdfs| 2.5.8  
httplib2| 0.17.3  
idna| 2.10  
importlib-metadata| 4.6.4  
joblib| 1.0.1  
keras-nightly| 2.5.0.dev2021032900  
Keras-Preprocessing| 1.1.2  
libcst| 0.3.20  
Markdown| 3.3.4  
mmh3| 2.5.1  
more-itertools| 8.8.0  
mypy-extensions| 0.4.3  
nltk| 3.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.19.5  
oauth2client| 3.0.0  
oauthlib| 3.1.1  
opt-einsum| 3.3.0  
orjson| 3.6.1  
packaging| 21.0  
pandas| 1.1.5  
Pillow| 7.2.0  
pip| 21.2.4  
pluggy| 0.13.1  
proto-plus| 1.19.0  
protobuf| 3.12.2  
protorpc| 0.12.0  
py| 1.10.0  
pyarrow| 3.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pycparser| 2.20  
pydot| 1.4.1  
pymongo| 3.10.1  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2020.1  
PyYAML| 5.3.1  
regex| 2021.8.21  
requests| 2.24.0  
requests-oauthlib| 1.3.0  
rsa| 4.7.2  
scikit-learn| 0.24.1  
scipy| 1.4.1  
setuptools| 57.4.0  
six| 1.15.0  
soupsieve| 2.2.1  
tensorboard| 2.6.0  
tensorboard-data-server| 0.6.1  
tensorboard-plugin-wit| 1.8.0  
tensorflow| 2.5.0  
tensorflow-estimator| 2.5.0  
termcolor| 1.1.0  
threadpoolctl| 2.2.0  
tqdm| 4.62.2  
typing-extensions| 3.7.4.2  
typing-inspect| 0.7.1  
uritemplate| 3.0.1  
urllib3| 1.25.11  
wcwidth| 0.2.5  
Werkzeug| 2.0.1  
wheel| 0.37.0  
wrapt| 1.12.1  
zipp| 3.5.0  
  
### Python 3.7.11

Package| Version  
---|---  
  
absl-py| 0.13.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 21.2.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.9.1  
bs4| 0.0.1  
cached-property| 1.5.2  
cachetools| 3.1.1  
certifi| 2021.5.30  
cffi| 1.14.6  
chardet| 3.0.4  
charset-normalizer| 2.0.4  
click| 8.0.1  
crcmod| 1.7  
Cython| 0.29.21  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.24.2  
fasteners| 0.16.3  
flatbuffers| 1.12  
freezegun| 0.3.15  
future| 0.18.2  
gast| 0.4.0  
google-api-core| 1.31.2  
google-api-python-client| 2.18.0  
google-apitools| 0.5.31  
google-auth| 1.35.0  
google-auth-httplib2| 0.1.0  
google-auth-oauthlib| 0.4.5  
google-cloud-bigquery| 1.26.1  
google-cloud-bigquery-storage| 2.4.0  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.7.2  
google-cloud-datastore| 1.15.3  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-profiler| 3.0.4  
google-cloud-pubsub| 1.0.2  
google-cloud-recommendations-ai| 0.2.0  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-crc32c| 1.1.2  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.15  
google-resumable-media| 1.3.3  
googleapis-common-protos| 1.53.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.34.1  
grpcio-gcp| 0.2.2  
guppy3| 3.0.10  
h5py| 3.1.0  
hdfs| 2.5.8  
httplib2| 0.17.3  
idna| 2.10  
importlib-metadata| 4.6.4  
joblib| 1.0.1  
keras-nightly| 2.5.0.dev2021032900  
Keras-Preprocessing| 1.1.2  
libcst| 0.3.20  
Markdown| 3.3.4  
mmh3| 2.5.1  
more-itertools| 8.8.0  
mypy-extensions| 0.4.3  
nltk| 3.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.19.5  
oauth2client| 3.0.0  
oauthlib| 3.1.1  
opt-einsum| 3.3.0  
orjson| 3.6.3  
packaging| 21.0  
pandas| 1.2.4  
Pillow| 7.2.0  
pip| 21.2.4  
pluggy| 0.13.1  
proto-plus| 1.19.0  
protobuf| 3.12.2  
protorpc| 0.12.0  
py| 1.10.0  
pyarrow| 3.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pycparser| 2.20  
pydot| 1.4.1  
pymongo| 3.10.1  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2020.1  
PyYAML| 5.3.1  
regex| 2021.8.21  
requests| 2.24.0  
requests-oauthlib| 1.3.0  
rsa| 4.7.2  
scikit-learn| 0.24.1  
scipy| 1.4.1  
setuptools| 57.4.0  
six| 1.15.0  
soupsieve| 2.2.1  
tensorboard| 2.6.0  
tensorboard-data-server| 0.6.1  
tensorboard-plugin-wit| 1.8.0  
tensorflow| 2.5.0  
tensorflow-estimator| 2.5.0  
termcolor| 1.1.0  
threadpoolctl| 2.2.0  
tqdm| 4.62.2  
typing-extensions| 3.7.4.2  
typing-inspect| 0.7.1  
uritemplate| 3.0.1  
urllib3| 1.25.11  
wcwidth| 0.2.5  
Werkzeug| 2.0.1  
wheel| 0.37.0  
wrapt| 1.12.1  
zipp| 3.5.0  
  
### Python 3.8.11

Package| Version  
---|---  
  
absl-py| 0.13.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 21.2.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.9.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2021.5.30  
cffi| 1.14.6  
chardet| 3.0.4  
charset-normalizer| 2.0.4  
click| 8.0.1  
crcmod| 1.7  
Cython| 0.29.21  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.24.2  
fasteners| 0.16.3  
flatbuffers| 1.12  
freezegun| 0.3.15  
future| 0.18.2  
gast| 0.4.0  
google-api-core| 1.31.2  
google-api-python-client| 2.18.0  
google-apitools| 0.5.31  
google-auth| 1.35.0  
google-auth-httplib2| 0.1.0  
google-auth-oauthlib| 0.4.5  
google-cloud-bigquery| 1.26.1  
google-cloud-bigquery-storage| 2.4.0  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.7.2  
google-cloud-datastore| 1.15.3  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-profiler| 3.0.4  
google-cloud-pubsub| 1.0.2  
google-cloud-recommendations-ai| 0.2.0  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-crc32c| 1.1.2  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.15  
google-resumable-media| 1.3.3  
googleapis-common-protos| 1.53.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.34.1  
grpcio-gcp| 0.2.2  
guppy3| 3.0.10  
h5py| 3.1.0  
hdfs| 2.5.8  
httplib2| 0.17.3  
idna| 2.10  
joblib| 1.0.1  
keras-nightly| 2.5.0.dev2021032900  
Keras-Preprocessing| 1.1.2  
libcst| 0.3.20  
Markdown| 3.3.4  
mmh3| 2.5.1  
more-itertools| 8.8.0  
mypy-extensions| 0.4.3  
nltk| 3.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.19.5  
oauth2client| 3.0.0  
oauthlib| 3.1.1  
opt-einsum| 3.3.0  
orjson| 3.6.3  
packaging| 21.0  
pandas| 1.2.4  
Pillow| 7.2.0  
pip| 21.2.4  
pluggy| 0.13.1  
proto-plus| 1.19.0  
protobuf| 3.12.2  
protorpc| 0.12.0  
py| 1.10.0  
pyarrow| 3.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pycparser| 2.20  
pydot| 1.4.1  
pymongo| 3.10.1  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2020.1  
PyYAML| 5.3.1  
regex| 2021.8.21  
requests| 2.24.0  
requests-oauthlib| 1.3.0  
rsa| 4.7.2  
scikit-learn| 0.24.1  
scipy| 1.4.1  
setuptools| 57.4.0  
six| 1.15.0  
soupsieve| 2.2.1  
tensorboard| 2.6.0  
tensorboard-data-server| 0.6.1  
tensorboard-plugin-wit| 1.8.0  
tensorflow| 2.5.0  
tensorflow-estimator| 2.5.0  
termcolor| 1.1.0  
threadpoolctl| 2.2.0  
tqdm| 4.62.2  
typing-extensions| 3.7.4.2  
typing-inspect| 0.7.1  
uritemplate| 3.0.1  
urllib3| 1.25.11  
wcwidth| 0.2.5  
Werkzeug| 2.0.1  
wheel| 0.37.0  
wrapt| 1.12.1  
  
#### Version 2.32.0

Dataflow workers have the following packages already installed.

### Python 3.6.14

Package| Version  
---|---  
  
absl-py| 0.13.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 21.2.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.9.1  
bs4| 0.0.1  
cached-property| 1.5.2  
cachetools| 3.1.1  
certifi| 2021.5.30  
cffi| 1.14.6  
chardet| 3.0.4  
charset-normalizer| 2.0.4  
click| 8.0.1  
crcmod| 1.7  
Cython| 0.29.21  
dataclasses| 0.8  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.24.2  
fasteners| 0.16.3  
flatbuffers| 1.12  
freezegun| 0.3.15  
future| 0.18.2  
gast| 0.4.0  
google-api-core| 1.31.1  
google-api-python-client| 2.15.0  
google-apitools| 0.5.31  
google-auth| 1.34.0  
google-auth-httplib2| 0.1.0  
google-auth-oauthlib| 0.4.5  
google-cloud-bigquery| 1.26.1  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.7.2  
google-cloud-datastore| 1.15.3  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-profiler| 3.0.4  
google-cloud-pubsub| 1.0.2  
google-cloud-recommendations-ai| 0.2.0  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-crc32c| 1.1.2  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.15  
google-resumable-media| 1.3.3  
googleapis-common-protos| 1.53.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.34.1  
grpcio-gcp| 0.2.2  
guppy3| 3.0.10  
h5py| 3.1.0  
hdfs| 2.5.8  
httplib2| 0.17.3  
idna| 2.10  
importlib-metadata| 4.6.3  
joblib| 1.0.1  
keras-nightly| 3.5.0.dev2021032900  
Keras-Preprocessing| 1.1.2  
Markdown| 3.3.4  
mmh3| 2.5.1  
more-itertools| 8.8.0  
nltk| 3.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.19.5  
oauth2client| 3.0.0  
oauthlib| 3.1.1  
opt-einsum| 3.3.0  
orjson| 3.6.1  
packaging| 21.0  
pandas| 1.1.5  
Pillow| 7.2.0  
pip| 21.2.3  
pluggy| 0.13.1  
proto-plus| 1.19.0  
protobuf| 3.12.2  
protorpc| 0.12.0  
py| 1.10.0  
pyarrow| 3.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pycparser| 2.20  
pydot| 1.4.1  
pymongo| 3.10.1  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2020.1  
PyYAML| 5.3.1  
regex| 2021.8.3  
requests| 2.24.0  
requests-oauthlib| 1.3.0  
rsa| 4.7.2  
scikit-learn| 0.24.1  
scipy| 1.4.1  
setuptools| 57.4.0  
six| 1.15.0  
soupsieve| 2.2.1  
tensorboard| 2.6.0  
tensorboard-data-server| 0.6.1  
tensorboard-plugin-wit| 1.8.0  
tensorflow| 2.5.0  
tensorflow-estimator| 2.5.0  
termcolor| 1.1.0  
threadpoolctl| 2.2.0  
tqdm| 4.62.0  
typing-extensions| 3.7.4.2  
uritemplate| 3.0.1  
urllib3| 1.25.11  
wcwidth| 0.2.5  
Werkzeug| 2.0.1  
wheel| 0.36.2  
wrapt| 1.12.1  
zipp| 3.5.0  
  
### Python 3.7.11

Package| Version  
---|---  
  
absl-py| 0.13.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 21.2.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.9.1  
bs4| 0.0.1  
cached-property| 1.5.2  
cachetools| 3.1.1  
certifi| 2021.5.30  
cffi| 1.14.6  
chardet| 3.0.4  
charset-normalizer| 2.0.4  
click| 8.0.1  
crcmod| 1.7  
Cython| 0.29.21  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.24.2  
fasteners| 0.16.3  
flatbuffers| 1.12  
freezegun| 0.3.15  
future| 0.18.2  
gast| 0.4.0  
google-api-core| 1.31.1  
google-api-python-client| 2.15.0  
google-apitools| 0.5.31  
google-auth| 1.34.0  
google-auth-httplib2| 0.1.0  
google-auth-oauthlib| 0.4.5  
google-cloud-bigquery| 1.26.1  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.7.2  
google-cloud-datastore| 1.15.3  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-profiler| 3.0.4  
google-cloud-pubsub| 1.0.2  
google-cloud-recommendations-ai| 0.2.0  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-crc32c| 1.1.2  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.15  
google-resumable-media| 1.3.3  
googleapis-common-protos| 1.53.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.34.1  
grpcio-gcp| 0.2.2  
guppy3| 3.0.10  
h5py| 3.1.0  
hdfs| 2.5.8  
httplib2| 0.17.3  
idna| 2.10  
importlib-metadata| 4.6.3  
joblib| 1.0.1  
keras-nightly| 2.5.0.dev2021032900  
Keras-Preprocessing| 1.1.2  
Markdown| 3.3.4  
mmh3| 2.5.1  
more-itertools| 8.8.0  
nltk| 3.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.19.5  
oauth2client| 3.0.0  
oauthlib| 3.1.1  
opt-einsum| 3.3.0  
orjson| 3.6.1  
packaging| 21.0  
pandas| 1.2.4  
Pillow| 7.2.0  
pip| 21.2.3  
pluggy| 0.13.1  
proto-plus| 1.19.0  
protobuf| 3.12.2  
protorpc| 0.12.0  
py| 1.10.0  
pyarrow| 3.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pycparser| 2.20  
pydot| 1.4.1  
pymongo| 3.10.1  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2020.1  
PyYAML| 5.3.1  
regex| 2021.8.3  
requests| 2.24.0  
requests-oauthlib| 1.3.0  
rsa| 4.7.2  
scikit-learn| 0.24.1  
scipy| 1.4.1  
setuptools| 57.4.0  
six| 1.15.0  
soupsieve| 2.2.1  
tensorboard| 2.6.0  
tensorboard-data-server| 0.6.1  
tensorboard-plugin-wit| 1.8.0  
tensorflow| 2.5.0  
tensorflow-estimator| 2.5.0  
termcolor| 1.1.0  
threadpoolctl| 2.2.0  
tqdm| 4.62.0  
typing-extensions| 3.7.4.2  
uritemplate| 3.0.1  
urllib3| 1.25.11  
wcwidth| 0.2.5  
Werkzeug| 2.0.1  
wheel| 0.36.2  
wrapt| 1.12.1  
zipp| 3.5.0  
  
### Python 3.8.11

Package| Version  
---|---  
  
absl-py| 0.13.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 21.2.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.9.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2021.5.30  
cffi| 1.14.6  
chardet| 3.0.4  
charset-normalizer| 2.0.4  
click| 8.0.1  
crcmod| 1.7  
Cython| 0.29.21  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.24.2  
fasteners| 0.16.3  
flatbuffers| 1.12  
freezegun| 0.3.15  
future| 0.18.2  
gast| 0.4.0  
google-api-core| 1.31.1  
google-api-python-client| 2.15.0  
google-apitools| 0.5.31  
google-auth| 1.34.0  
google-auth-httplib2| 0.1.0  
google-auth-oauthlib| 0.4.5  
google-cloud-bigquery| 1.26.1  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.7.2  
google-cloud-datastore| 1.15.3  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-profiler| 3.0.4  
google-cloud-pubsub| 1.0.2  
google-cloud-recommendations-ai| 0.2.0  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-crc32c| 1.1.2  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.15  
google-resumable-media| 1.3.3  
googleapis-common-protos| 1.53.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.34.1  
grpcio-gcp| 0.2.2  
guppy3| 3.0.10  
h5py| 3.1.0  
hdfs| 2.5.8  
httplib2| 0.17.3  
idna| 2.10  
joblib| 1.0.1  
keras-nightly| 2.5.0.dev2021032900  
Keras-Preprocessing| 1.1.2  
Markdown| 3.3.4  
mmh3| 2.5.1  
more-itertools| 8.8.0  
nltk| 3.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.19.5  
oauth2client| 3.0.0  
oauthlib| 3.1.1  
opt-einsum| 3.3.0  
orjson| 3.6.1  
packaging| 21.0  
pandas| 1.2.4  
Pillow| 7.2.0  
pip| 21.2.3  
pluggy| 0.13.1  
proto-plus| 1.19.0  
protobuf| 3.12.2  
protorpc| 0.12.0  
py| 1.10.0  
pyarrow| 3.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pycparser| 2.20  
pydot| 1.4.1  
pymongo| 3.10.1  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2020.1  
PyYAML| 5.3.1  
regex| 2021.8.3  
requests| 2.24.0  
requests-oauthlib| 1.3.0  
rsa| 4.7.2  
scikit-learn| 0.24.1  
scipy| 1.4.1  
setuptools| 57.4.0  
six| 1.15.0  
soupsieve| 2.2.1  
tensorboard| 2.6.0  
tensorboard-data-server| 0.6.1  
tensorboard-plugin-wit| 1.8.0  
tensorflow| 2.5.0  
tensorflow-estimator| 2.5.0  
termcolor| 1.1.0  
threadpoolctl| 2.2.0  
tqdm| 4.62.0  
typing-extensions| 3.7.4.2  
uritemplate| 3.0.1  
urllib3| 1.25.11  
wcwidth| 0.2.5  
Werkzeug| 2.0.1  
wheel| 0.36.2  
wrapt| 1.12.1  
  
#### Version 2.31.0

Dataflow workers have the following packages already installed.

### Python 3.6.13

Package| Version  
---|---  
  
absl-py| 0.12.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 21.2.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.9.1  
bs4| 0.0.1  
cached-property| 1.5.2  
cachetools| 3.1.1  
certifi| 2020.12.5  
cffi| 1.14.5  
chardet| 3.0.4  
click| 8.0.1  
crcmod| 1.7  
Cython| 0.29.21  
dataclasses| 0.8  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.24.2  
fasteners| 0.16  
flatbuffers| 1.12  
freezegun| 0.3.15  
future| 0.18.2  
gast| 0.4.0  
google-api-core| 1.28.0  
google-api-python-client| 2.5.0  
google-apitools| 0.5.31  
google-auth| 1.30.1  
google-auth-httplib2| 0.1.0  
google-auth-oauthlib| 0.4.4  
google-cloud-bigquery| 1.26.1  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-profiler| 3.0.4  
google-cloud-pubsub| 1.0.2  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-crc32c| 1.1.2  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.15  
google-resumable-media| 1.3.0  
googleapis-common-protos| 1.53.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.34.1  
grpcio-gcp| 0.2.2  
guppy3| 3.0.10  
h5py| 3.1.0  
hdfs| 2.5.8  
httplib2| 0.17.3  
idna| 2.10  
importlib-metadata| 4.0.1  
joblib| 1.0.1  
keras-nightly| 2.5.0.dev2021032900  
Keras-Preprocessing| 1.1.2  
Markdown| 3.3.4  
mmh3| 2.5.1  
more-itertools| 8.8.0  
nltk| 3.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.19.5  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 3.3.0  
packaging| 20.9  
pandas| 1.1.5  
Pillow| 7.2.0  
pip| 21.1.2  
pluggy| 0.13.1  
protobuf| 3.12.2  
protorpc| 0.12.0  
py| 1.10.0  
pyarrow| 3.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pycparser| 2.20  
pydot| 1.4.1  
pymongo| 3.10.1  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2020.1  
PyYAML| 5.3.1  
regex| 2021.4.4  
requests| 2.24.0  
requests-oauthlib| 1.3.0  
rsa| 4.7.2  
scikit-learn| 0.24.1  
scipy| 1.4.1  
setuptools| 57.0.0  
six| 1.15.0  
soupsieve| 2.2.1  
tensorboard| 2.5.0  
tensorboard-data-server| 0.6.1  
tensorboard-plugin-wit| 1.8.0  
tensorflow| 2.5.0  
tensorflow-estimator| 2.5.0  
termcolor| 1.1.0  
threadpoolctl| 2.1.0  
tqdm| 4.61.0  
typing-extensions| 3.7.4.2  
uritemplate| 3.0.1  
urllib3| 1.25.11  
wcwidth| 0.2.5  
Werkzeug| 2.0.1  
wheel| 0.36.2  
wrapt| 1.12.1  
zipp| 3.4.1  
  
### Python 3.7.10

Package| Version  
---|---  
  
absl-py| 0.12.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 21.2.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.9.1  
bs4| 0.0.1  
cached-property| 1.5.2  
cachetools| 3.1.1  
certifi| 2020.12.5  
cffi| 1.14.5  
chardet| 3.0.4  
click| 8.0.1  
crcmod| 1.7  
Cython| 0.29.21  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.24.2  
fasteners| 0.16  
flatbuffers| 1.12  
freezegun| 0.3.15  
future| 0.18.2  
gast| 0.4.0  
google-api-core| 1.28.0  
google-api-python-client| 2.5.0  
google-apitools| 0.5.31  
google-auth| 1.30.1  
google-auth-httplib2| 0.1.0  
google-auth-oauthlib| 0.4.4  
google-cloud-bigquery| 1.26.1  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-profiler| 3.0.4  
google-cloud-pubsub| 1.0.2  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-crc32c| 1.1.2  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.15  
google-resumable-media| 1.3.0  
googleapis-common-protos| 1.53.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.34.1  
grpcio-gcp| 0.2.2  
guppy3| 3.0.10  
h5py| 3.1.0  
hdfs| 2.5.8  
httplib2| 0.17.3  
idna| 2.10  
importlib-metadata| 4.0.1  
joblib| 1.0.1  
keras-nightly| 2.5.0.dev2021032900  
Keras-Preprocessing| 1.1.2  
Markdown| 3.3.4  
mmh3| 2.5.1  
more-itertools| 8.8.0  
nltk| 3.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.19.5  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 3.3.0  
packaging| 20.9  
pandas| 1.2.4  
Pillow| 7.2.0  
pip| 21.1.2  
pluggy| 0.13.1  
protobuf| 3.12.2  
protorpc| 0.12.0  
py| 1.10.0  
pyarrow| 3.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pycparser| 2.20  
pydot| 1.4.1  
pymongo| 3.10.1  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2020.1  
PyYAML| 5.3.1  
regex| 2021.4.4  
requests| 2.24.0  
requests-oauthlib| 1.3.0  
rsa| 4.7.2  
scikit-learn| 0.24.1  
scipy| 1.4.1  
setuptools| 57.0.0  
six| 1.15.0  
soupsieve| 2.2.1  
tensorboard| 2.5.0  
tensorboard-data-server| 0.6.1  
tensorboard-plugin-wit| 1.8.0  
tensorflow| 2.5.0  
tensorflow-estimator| 2.5.0  
termcolor| 1.1.0  
threadpoolctl| 2.1.0  
tqdm| 4.61.0  
typing-extensions| 3.7.4.2  
uritemplate| 3.0.1  
urllib3| 1.25.11  
wcwidth| 0.2.5  
Werkzeug| 2.0.1  
wheel| 0.36.2  
wrapt| 1.12.1  
zipp| 3.4.1  
  
### Python 3.8.10

Package| Version  
---|---  
  
absl-py| 0.12.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 21.2.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.9.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2020.12.5  
cffi| 1.14.5  
chardet| 3.0.4  
click| 8.0.1  
crcmod| 1.7  
Cython| 0.29.21  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.24.2  
fasteners| 0.16  
flatbuffers| 1.12  
freezegun| 0.3.15  
future| 0.18.2  
gast| 0.4.0  
google-api-core| 1.28.0  
google-api-python-client| 2.5.0  
google-apitools| 0.5.31  
google-auth| 1.30.1  
google-auth-httplib2| 0.1.0  
google-auth-oauthlib| 0.4.4  
google-cloud-bigquery| 1.26.1  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-profiler| 3.0.4  
google-cloud-pubsub| 1.0.2  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-crc32c| 1.1.2  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.15  
google-resumable-media| 1.3.0  
googleapis-common-protos| 1.53.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.34.1  
grpcio-gcp| 0.2.2  
guppy3| 3.0.10  
h5py| 3.1.0  
hdfs| 2.5.8  
httplib2| 0.17.3  
idna| 2.10  
joblib| 1.0.1  
keras-nightly| 2.5.0.dev2021032900  
Keras-Preprocessing| 1.1.2  
Markdown| 3.3.4  
mmh3| 2.5.1  
more-itertools| 8.8.0  
nltk| 3.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.19.5  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 3.3.0  
packaging| 20.9  
pandas| 1.2.4  
Pillow| 7.2.0  
pip| 21.1.2  
pluggy| 0.13.1  
protobuf| 3.12.2  
protorpc| 0.12.0  
py| 1.10.0  
pyarrow| 3.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pycparser| 2.20  
pydot| 1.4.1  
pymongo| 3.10.1  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2020.1  
PyYAML| 5.3.1  
regex| 2021.4.4  
requests| 2.24.0  
requests-oauthlib| 1.3.0  
rsa| 4.7.2  
scikit-learn| 0.24.1  
scipy| 1.4.1  
setuptools| 57.0.0  
six| 1.15.0  
soupsieve| 2.2.1  
tensorboard| 2.5.0  
tensorboard-data-server| 0.6.1  
tensorboard-plugin-wit| 1.8.0  
tensorflow| 2.5.0  
tensorflow-estimator| 2.5.0  
termcolor| 1.1.0  
threadpoolctl| 2.1.0  
tqdm| 4.61.0  
typing-extensions| 3.7.4.2  
uritemplate| 3.0.1  
urllib3| 1.25.11  
wcwidth| 0.2.5  
Werkzeug| 2.0.1  
wheel| 0.36.2  
wrapt| 1.12.1  
  
#### Version 2.30.0

Dataflow workers have the following packages already installed.

### Python 3.6.13

Package| Version  
---|---  
  
absl-py| 0.12.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 21.2.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.9.1  
bs4| 0.0.1  
cached-property| 1.5.2  
cachetools| 3.1.1  
certifi| 2020.12.5  
cffi| 1.14.5  
chardet| 3.0.4  
click| 8.0.1  
crcmod| 1.7  
Cython| 0.29.21  
dataclasses| 0.8  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.24.2  
fasteners| 0.16  
flatbuffers| 1.12  
freezegun| 0.3.15  
future| 0.18.2  
gast| 0.4.0  
google-api-core| 1.28.0  
google-api-python-client| 2.5.0  
google-apitools| 0.5.31  
google-auth| 1.30.0  
google-auth-httplib2| 0.1.0  
google-auth-oauthlib| 0.4.4  
google-cloud-bigquery| 1.26.1  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-pubsub| 1.0.2  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-crc32c| 1.1.2  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.15  
google-resumable-media| 1.3.0  
googleapis-common-protos| 1.53.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.34.1  
grpcio-gcp| 0.2.2  
guppy3| 3.0.10  
h5py| 3.1.0  
hdfs| 2.5.8  
httplib2| 0.17.3  
idna| 2.10  
importlib-metadata| 4.0.1  
joblib| 1.0.1  
keras-nightly| 2.5.0.dev2021032900  
Keras-Preprocessing| 1.1.2  
Markdown| 3.3.4  
mmh3| 2.5.1  
more-itertools| 8.7.0  
nltk| 3.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.19.5  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 3.3.0  
packaging| 20.9  
pandas| 1.1.5  
Pillow| 7.2.0  
pip| 21.1.1  
pluggy| 0.13.1  
protobuf| 3.12.2  
protorpc| 0.12.0  
py| 1.10.0  
pyarrow| 3.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pycparser| 2.20  
pydot| 1.4.1  
pymongo| 3.10.1  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2020.1  
PyYAML| 5.3.1  
regex| 2021.4.4  
requests| 2.24.0  
requests-oauthlib| 1.3.0  
rsa| 4.7.2  
scikit-learn| 0.24.1  
scipy| 1.4.1  
setuptools| 56.2.0  
six| 1.15.0  
soupsieve| 2.2.1  
tensorboard| 2.5.0  
tensorboard-data-server| 0.6.1  
tensorboard-plugin-wit| 1.8.0  
tensorflow| 2.5.0  
tensorflow-estimator| 2.5.0  
termcolor| 1.1.0  
threadpoolctl| 2.1.0  
tqdm| 4.60.0  
typing-extensions| 3.7.4.2  
uritemplate| 3.0.1  
urllib3| 1.25.11  
wcwidth| 0.2.5  
Werkzeug| 2.0.1  
wheel| 0.36.2  
wrapt| 1.12.1  
zipp| 3.4.1  
  
### Python 3.7.10

Package| Version  
---|---  
  
absl-py| 0.12.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 21.2.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.9.1  
bs4| 0.0.1  
cached-property| 1.5.2  
cachetools| 3.1.1  
certifi| 2020.12.5  
cffi| 1.14.5  
chardet| 3.0.4  
click| 8.0.1  
crcmod| 1.7  
Cython| 0.29.21  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.24.2  
fasteners| 0.16  
flatbuffers| 1.12  
freezegun| 0.3.15  
future| 0.18.2  
gast| 0.4.0  
google-api-core| 1.28.0  
google-api-python-client| 2.5.0  
google-apitools| 0.5.31  
google-auth| 1.30.0  
google-auth-httplib2| 0.1.0  
google-auth-oauthlib| 0.4.4  
google-cloud-bigquery| 1.26.1  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-pubsub| 1.0.2  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-crc32c| 1.1.2  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.15  
google-resumable-media| 1.3.0  
googleapis-common-protos| 1.53.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.34.1  
grpcio-gcp| 0.2.2  
guppy3| 3.0.10  
h5py| 3.1.0  
hdfs| 2.5.8  
httplib2| 0.17.3  
idna| 2.10  
importlib-metadata| 4.0.1  
joblib| 1.0.1  
keras-nightly| 2.5.0.dev2021032900  
Keras-Preprocessing| 1.1.2  
Markdown| 3.3.4  
mmh3| 2.5.1  
more-itertools| 8.7.0  
nltk| 3.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.19.5  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 3.3.0  
packaging| 20.9  
pandas| 1.2.4  
Pillow| 7.2.0  
pip| 21.1.1  
pluggy| 0.13.1  
protobuf| 3.12.2  
protorpc| 0.12.0  
py| 1.10.0  
pyarrow| 3.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pycparser| 2.20  
pydot| 1.4.1  
pymongo| 3.10.1  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2020.1  
PyYAML| 5.3.1  
regex| 2021.4.4  
requests| 2.24.0  
requests-oauthlib| 1.3.0  
rsa| 4.7.2  
scikit-learn| 0.24.1  
scipy| 1.4.1  
setuptools| 56.2.0  
six| 1.15.0  
soupsieve| 2.2.1  
tensorboard| 2.5.0  
tensorboard-data-server| 0.6.1  
tensorboard-plugin-wit| 1.8.0  
tensorflow| 2.5.0  
tensorflow-estimator| 2.5.0  
termcolor| 1.1.0  
threadpoolctl| 2.1.0  
tqdm| 4.60.0  
typing-extensions| 3.7.4.2  
uritemplate| 3.0.1  
urllib3| 1.25.11  
wcwidth| 0.2.5  
Werkzeug| 2.0.1  
wheel| 0.36.2  
wrapt| 1.12.1  
zipp| 3.4.1  
  
### Python 3.8.10

Package| Version  
---|---  
  
absl-py| 0.12.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 21.2.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.9.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2020.12.5  
cffi| 1.14.5  
chardet| 3.0.4  
click| 8.0.1  
crcmod| 1.7  
Cython| 0.29.21  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.24.2  
fasteners| 0.16  
flatbuffers| 1.12  
freezegun| 0.3.15  
future| 0.18.2  
gast| 0.4.0  
google-api-core| 1.28.0  
google-api-python-client| 2.5.0  
google-apitools| 0.5.31  
google-auth| 1.30.0  
google-auth-httplib2| 0.1.0  
google-auth-oauthlib| 0.4.4  
google-cloud-bigquery| 1.26.1  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-pubsub| 1.0.2  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-crc32c| 1.1.2  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.15  
google-resumable-media| 1.3.0  
googleapis-common-protos| 1.53.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.34.1  
grpcio-gcp| 0.2.2  
guppy3| 3.0.10  
h5py| 3.1.0  
hdfs| 2.5.8  
httplib2| 0.17.3  
idna| 2.10  
joblib| 1.0.1  
keras-nightly| 2.5.0.dev2021032900  
Keras-Preprocessing| 1.1.2  
Markdown| 3.3.4  
mmh3| 2.5.1  
more-itertools| 8.7.0  
nltk| 3.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.19.5  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 3.3.0  
packaging| 20.9  
pandas| 1.2.4  
Pillow| 7.2.0  
pip| 21.1.1  
pluggy| 0.13.1  
protobuf| 3.12.2  
protorpc| 0.12.0  
py| 1.10.0  
pyarrow| 3.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pycparser| 2.20  
pydot| 1.4.1  
pymongo| 3.10.1  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2020.1  
PyYAML| 5.3.1  
regex| 2021.4.4  
requests| 2.24.0  
requests-oauthlib| 1.3.0  
rsa| 4.7.2  
scikit-learn| 0.24.1  
scipy| 1.4.1  
setuptools| 56.2.0  
six| 1.15.0  
soupsieve| 2.2.1  
tensorboard| 2.5.0  
tensorboard-data-server| 0.6.1  
tensorboard-plugin-wit| 1.8.0  
tensorflow| 2.5.0  
tensorflow-estimator| 2.5.0  
termcolor| 1.1.0  
threadpoolctl| 2.1.0  
tqdm| 4.60.0  
typing-extensions| 3.7.4.2  
uritemplate| 3.0.1  
urllib3| 1.25.11  
wcwidth| 0.2.5  
Werkzeug| 2.0.1  
wheel| 0.36.2  
wrapt| 1.12.1  
  
#### Version 2.29.0

Dataflow workers have the following packages already installed.

**Note:** Version 2.24.0 was the last Apache Beam SDK version to support Python 2 and Python 3.5.

### Python 3.6.13

Package| Version  
---|---  
  
absl-py| 0.12.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 20.3.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.9.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2020.12.5  
cffi| 1.14.5  
chardet| 3.0.4  
click| 7.1.2  
crcmod| 1.7  
Cython| 0.29.21  
dataclasses| 0.8  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.24.2  
fasteners| 0.16  
flatbuffers| 1.12  
freezegun| 0.3.15  
future| 0.18.2  
gast| 0.3.3  
google-api-core| 1.26.3  
google-api-python-client| 2.2.0  
google-apitools| 0.5.31  
google-auth| 1.29.0  
google-auth-httplib2| 0.1.0  
google-auth-oauthlib| 0.4.4  
google-cloud-bigquery| 1.26.1  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-pubsub| 1.0.2  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-crc32c| 1.1.2  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.15  
google-resumable-media| 1.2.0  
googleapis-common-protos| 1.53.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.32.0  
grpcio-gcp| 0.2.2  
guppy3| 3.0.10  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.17.3  
idna| 2.10  
importlib-metadata| 4.0.0  
joblib| 1.0.1  
Keras-Preprocessing| 1.1.2  
Markdown| 3.3.4  
mmh3| 2.5.1  
mock| 2.0.0  
more-itertools| 8.7.0  
nltk| 3.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.19.5  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 3.3.0  
packaging| 20.9  
pandas| 1.1.5  
pbr| 5.5.1  
Pillow| 7.2.0  
pip| 21.0.1  
pluggy| 0.13.1  
protobuf| 3.12.2  
protorpc| 0.12.0  
py| 1.10.0  
pyarrow| 3.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pycparser| 2.20  
pydot| 1.4.1  
pymongo| 3.10.1  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2020.1  
PyYAML| 5.3.1  
regex| 2021.4.4  
requests| 2.24.0  
requests-oauthlib| 1.3.0  
rsa| 4.7.2  
scikit-learn| 0.22.1  
scipy| 1.4.1  
setuptools| 56.0.0  
six| 1.15.0  
soupsieve| 2.2.1  
tensorboard| 2.5.0  
tensorboard-data-server| 0.6.0  
tensorboard-plugin-wit| 1.8.0  
tensorflow| 2.4.1  
tensorflow-estimator| 2.4.0  
termcolor| 1.1.0  
tqdm| 4.60.0  
typing-extensions| 3.7.4.2  
uritemplate| 3.0.1  
urllib3| 1.25.11  
wcwidth| 0.2.5  
Werkzeug| 1.0.1  
wheel| 0.36.2  
wrapt| 1.12.1  
zipp| 3.4.1  
  
### Python 3.7.10

Package| Version  
---|---  
  
absl-py| 0.12.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 20.3.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.9.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2020.12.5  
cffi| 1.14.5  
chardet| 3.0.4  
click| 7.1.2  
crcmod| 1.7  
Cython| 0.29.21  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.24.2  
fasteners| 0.16  
flatbuffers| 1.12  
freezegun| 0.3.15  
future| 0.18.2  
gast| 0.3.3  
google-api-core| 1.26.3  
google-api-python-client| 2.2.0  
google-apitools| 0.5.31  
google-auth| 1.29.0  
google-auth-httplib2| 0.1.0  
google-auth-oauthlib| 0.4.4  
google-cloud-bigquery| 1.26.1  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-pubsub| 1.0.2  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-crc32c| 1.1.2  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.15  
google-resumable-media| 1.2.0  
googleapis-common-protos| 1.53.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.32.0  
grpcio-gcp| 0.2.2  
guppy3| 3.0.10  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.17.3  
idna| 2.10  
importlib-metadata| 4.0.0  
joblib| 1.0.1  
Keras-Preprocessing| 1.1.2  
Markdown| 3.3.4  
mmh3| 2.5.1  
mock| 2.0.0  
more-itertools| 8.7.0  
nltk| 3.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.19.5  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 3.3.0  
packaging| 20.9  
pandas| 1.2.2  
pbr| 5.5.1  
Pillow| 7.2.0  
pip| 21.0.1  
pluggy| 0.13.1  
protobuf| 3.12.2  
protorpc| 0.12.0  
py| 1.10.0  
pyarrow| 3.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pycparser| 2.20  
pydot| 1.4.1  
pymongo| 3.10.1  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2020.1  
PyYAML| 5.3.1  
regex| 2021.4.4  
requests| 2.24.0  
requests-oauthlib| 1.3.0  
rsa| 4.7.2  
scikit-learn| 0.22.1  
scipy| 1.4.1  
setuptools| 56.0.0  
six| 1.15.0  
soupsieve| 2.2.1  
tensorboard| 2.5.0  
tensorboard-data-server| 0.6.0  
tensorboard-plugin-wit| 1.8.0  
tensorflow| 2.4.1  
tensorflow-estimator| 2.4.0  
termcolor| 1.1.0  
tqdm| 4.60.0  
typing-extensions| 3.7.4.2  
uritemplate| 3.0.1  
urllib3| 1.25.11  
wcwidth| 0.2.5  
Werkzeug| 1.0.1  
wheel| 0.36.2  
wrapt| 1.12.1  
zipp| 3.4.1  
  
### Python 3.8.9

Package| Version  
---|---  
  
absl-py| 0.12.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 20.3.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.9.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2020.12.5  
cffi| 1.14.5  
chardet| 3.0.4  
click| 7.1.2  
crcmod| 1.7  
Cython| 0.29.21  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.24.2  
fasteners| 0.16  
flatbuffers| 1.12  
freezegun| 0.3.15  
future| 0.18.2  
gast| 0.3.3  
google-api-core| 1.26.3  
google-api-python-client| 2.2.0  
google-apitools| 0.5.31  
google-auth| 1.29.0  
google-auth-httplib2| 0.1.0  
google-auth-oauthlib| 0.4.4  
google-cloud-bigquery| 1.26.1  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-pubsub| 1.0.2  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-crc32c| 1.1.2  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.15  
google-resumable-media| 1.2.0  
googleapis-common-protos| 1.53.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.32.0  
grpcio-gcp| 0.2.2  
guppy3| 3.0.10  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.17.3  
idna| 2.10  
joblib| 1.0.1  
Keras-Preprocessing| 1.1.2  
Markdown| 3.3.4  
mmh3| 2.5.1  
mock| 2.0.0  
more-itertools| 8.7.0  
nltk| 3.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.19.5  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 3.3.0  
packaging| 20.9  
pandas| 1.2.2  
pbr| 5.5.1  
Pillow| 7.2.0  
pip| 21.0.1  
pluggy| 0.13.1  
protobuf| 3.12.2  
protorpc| 0.12.0  
py| 1.10.0  
pyarrow| 3.0.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pycparser| 2.20  
pydot| 1.4.1  
pymongo| 3.10.1  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2020.1  
PyYAML| 5.3.1  
regex| 2021.4.4  
requests| 2.24.0  
requests-oauthlib| 1.3.0  
rsa| 4.7.2  
scikit-learn| 0.22.1  
scipy| 1.4.1  
setuptools| 56.0.0  
six| 1.15.0  
soupsieve| 2.2.1  
tensorboard| 2.5.0  
tensorboard-data-server| 0.6.0  
tensorboard-plugin-wit| 1.8.0  
tensorflow| 2.4.1  
tensorflow-estimator| 2.4.0  
termcolor| 1.1.0  
tqdm| 4.60.0  
typing-extensions| 3.7.4.2  
uritemplate| 3.0.1  
urllib3| 1.25.11  
wcwidth| 0.2.5  
Werkzeug| 1.0.1  
wheel| 0.36.2  
wrapt| 1.12.1  
  
#### Version 2.28.0

Dataflow workers have the following packages already installed.

**Note:** Version 2.24.0 was the last Apache Beam SDK version to support Python 2 and Python 3.5.

### Python 3.6.12

Package| Version  
---|---  
  
absl-py| 0.11.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 20.3.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.9.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2020.12.5  
cffi| 1.14.4  
chardet| 3.0.4  
click| 7.1.2  
crcmod| 1.7  
Cython| 0.29.21  
dataclasses| 0.8  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.24.2  
fasteners| 0.16  
flatbuffers| 1.12  
freezegun| 0.3.15  
future| 0.18.2  
gast| 0.3.3  
google-api-core| 1.26.0  
google-api-python-client| 1.12.8  
google-apitools| 0.5.31  
google-auth| 1.25.0  
google-auth-httplib2| 0.0.4  
google-auth-oauthlib| 0.4.2  
google-cloud-bigquery| 1.26.1  
google-cloud-bigtable| 1.0.0  
google-cloud-build| 2.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-pubsub| 1.0.2  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-crc32c| 1.1.2  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.15  
google-resumable-media| 1.2.0  
googleapis-common-protos| 1.52.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.32.0  
grpcio-gcp| 0.2.2  
guppy3| 3.0.10  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.17.3  
idna| 2.10  
importlib-metadata| 3.4.0  
joblib| 1.0.0  
Keras-Preprocessing| 1.1.2  
libcst| 0.3.16  
Markdown| 3.3.3  
mmh3| 2.5.1  
mock| 2.0.0  
more-itertools| 8.7.0  
mypy-extensions| 0.4.3  
nltk| 3.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.19.5  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 3.3.0  
packaging| 20.9  
pandas| 1.1.4  
pbr| 5.5.1  
Pillow| 7.2.0  
pip| 21.0.1  
pluggy| 0.13.1  
proto-plus| 1.13.0  
protobuf| 3.12.2  
protorpc| 0.12.0  
py| 1.10.0  
pyarrow| 0.17.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pycparser| 2.20  
pydot| 1.4.1  
pymongo| 3.10.1  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2020.1  
PyYAML| 5.3.1  
regex| 2020.11.13  
requests| 2.24.0  
requests-oauthlib| 1.3.0  
rsa| 4.7  
scikit-learn| 0.22.1  
scipy| 1.4.1  
setuptools| 53.0.0  
six| 1.15.0  
soupsieve| 2.1  
tensorboard| 2.4.1  
tensorboard-plugin-wit| 1.8.0  
tensorflow| 2.4.1  
tensorflow-estimator| 2.4.0  
termcolor| 1.1.0  
tqdm| 4.56.0  
typing-extensions| 3.7.4.2  
typing-inspect| 0.6.0  
uritemplate| 3.0.1  
urllib3| 1.25.11  
wcwidth| 0.2.5  
Werkzeug| 1.0.1  
wheel| 0.36.2  
wrapt| 1.12.1  
zipp| 3.4.0  
  
### Python 3.7.9

Package| Version  
---|---  
  
absl-py| 0.11.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 20.3.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.9.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2020.12.5  
cffi| 1.14.4  
chardet| 3.0.4  
click| 7.1.2  
crcmod| 1.7  
Cython| 0.29.21  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.24.2  
fasteners| 0.16  
flatbuffers| 1.12  
freezegun| 0.3.15  
future| 0.18.2  
gast| 0.3.3  
google-api-core| 1.26.0  
google-api-python-client| 1.12.8  
google-apitools| 0.5.31  
google-auth| 1.25.0  
google-auth-httplib2| 0.0.4  
google-auth-oauthlib| 0.4.2  
google-cloud-bigquery| 1.26.1  
google-cloud-bigtable| 1.0.0  
google-cloud-build| 2.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-pubsub| 1.0.2  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-crc32c| 1.1.2  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.15  
google-resumable-media| 1.2.0  
googleapis-common-protos| 1.52.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.32.0  
grpcio-gcp| 0.2.2  
guppy3| 3.0.10  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.17.3  
idna| 2.10  
importlib-metadata| 3.4.0  
joblib| 1.0.0  
Keras-Preprocessing| 1.1.2  
libcst| 0.3.16  
Markdown| 3.3.3  
mmh3| 2.5.1  
mock| 2.0.0  
more-itertools| 8.7.0  
mypy-extensions| 0.4.3  
nltk| 3.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.19.5  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 3.3.0  
packaging| 20.9  
pandas| 1.1.4  
pbr| 5.5.1  
Pillow| 7.2.0  
pip| 21.0.1  
pluggy| 0.13.1  
proto-plus| 1.13.0  
protobuf| 3.12.2  
protorpc| 0.12.0  
py| 1.10.0  
pyarrow| 0.17.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pycparser| 2.20  
pydot| 1.4.1  
pymongo| 3.10.1  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2020.1  
PyYAML| 5.3.1  
regex| 2020.11.13  
requests| 2.24.0  
requests-oauthlib| 1.3.0  
rsa| 4.7  
scikit-learn| 0.22.1  
scipy| 1.4.1  
setuptools| 53.0.0  
six| 1.15.0  
soupsieve| 2.1  
tensorboard| 2.4.1  
tensorboard-plugin-wit| 1.8.0  
tensorflow| 2.4.1  
tensorflow-estimator| 2.4.0  
termcolor| 1.1.0  
tqdm| 4.56.0  
typing-extensions| 3.7.4.2  
typing-inspect| 0.6.0  
uritemplate| 3.0.1  
urllib3| 1.25.11  
wcwidth| 0.2.5  
Werkzeug| 1.0.1  
wheel| 0.36.2  
wrapt| 1.12.1  
zipp| 3.4.0  
  
### Python 3.8.7

Package| Version  
---|---  
  
absl-py| 0.11.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 20.3.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.9.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2020.12.5  
cffi| 1.14.4  
chardet| 3.0.4  
click| 7.1.2  
crcmod| 1.7  
Cython| 0.29.21  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.24.2  
fasteners| 0.16  
flatbuffers| 1.12  
freezegun| 0.3.15  
future| 0.18.2  
gast| 0.3.3  
google-api-core| 1.26.0  
google-api-python-client| 1.12.8  
google-apitools| 0.5.31  
google-auth| 1.25.0  
google-auth-httplib2| 0.0.4  
google-auth-oauthlib| 0.4.2  
google-cloud-bigquery| 1.26.1  
google-cloud-bigtable| 1.0.0  
google-cloud-build| 2.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-pubsub| 1.0.2  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-crc32c| 1.1.2  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.15  
google-resumable-media| 1.2.0  
googleapis-common-protos| 1.52.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.32.0  
grpcio-gcp| 0.2.2  
guppy3| 3.0.10  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.17.3  
idna| 2.10  
joblib| 1.0.0  
Keras-Preprocessing| 1.1.2  
libcst| 0.3.16  
Markdown| 3.3.3  
mmh3| 2.5.1  
mock| 2.0.0  
more-itertools| 8.7.0  
mypy-extensions| 0.4.3  
nltk| 3.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.19.5  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 3.3.0  
packaging| 20.9  
pandas| 1.1.4  
pbr| 5.5.1  
Pillow| 7.2.0  
pip| 21.0.1  
pluggy| 0.13.1  
proto-plus| 1.13.0  
protobuf| 3.12.2  
protorpc| 0.12.0  
py| 1.10.0  
pyarrow| 0.17.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pycparser| 2.20  
pydot| 1.4.1  
pymongo| 3.10.1  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2020.1  
PyYAML| 5.3.1  
regex| 2020.11.13  
requests| 2.24.0  
requests-oauthlib| 1.3.0  
rsa| 4.7  
scikit-learn| 0.22.1  
scipy| 1.4.1  
setuptools| 53.0.0  
six| 1.15.0  
soupsieve| 2.1  
tensorboard| 2.4.1  
tensorboard-plugin-wit| 1.8.0  
tensorflow| 2.4.1  
tensorflow-estimator| 2.4.0  
termcolor| 1.1.0  
tqdm| 4.56.0  
typing-extensions| 3.7.4.2  
typing-inspect| 0.6.0  
uritemplate| 3.0.1  
urllib3| 1.25.11  
wcwidth| 0.2.5  
Werkzeug| 1.0.1  
wheel| 0.36.2  
wrapt| 1.12.1  
  
#### Version 2.27.0

Dataflow workers have the following packages already installed.

**Note:** Version 2.24.0 was the last Apache Beam SDK version to support Python 2 and Python 3.5.

### Python 3.6.12

Package| Version  
---|---  
  
absl-py| 0.11.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 20.3.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.9.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2020.11.8  
cffi| 1.14.3  
chardet| 3.0.4  
click| 7.1.2  
crcmod| 1.7  
Cython| 0.29.21  
dataclasses| 0.7  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.24.2  
fasteners| 0.15  
freezegun| 0.3.15  
future| 0.18.2  
gast| 0.3.3  
google-api-core| 1.23.0  
google-api-python-client| 1.12.5  
google-apitools| 0.5.31  
google-auth| 1.23.0  
google-auth-httplib2| 0.0.4  
google-auth-oauthlib| 0.4.2  
google-cloud-bigquery| 1.26.1  
google-cloud-bigtable| 1.0.0  
google-cloud-build| 2.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-pubsub| 1.0.2  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-crc32c| 1.0.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.15  
google-resumable-media| 1.1.0  
googleapis-common-protos| 1.52.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.30.0  
grpcio-gcp| 0.2.2  
guppy3| 3.0.10  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.17.3  
idna| 2.10  
importlib-metadata| 2.0.0  
joblib| 0.17.0  
Keras-Preprocessing| 1.1.2  
libcst| 0.3.13  
Markdown| 3.3.3  
mmh3| 2.5.1  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 8.6.0  
mypy-extensions| 0.4.3  
nltk| 3.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.18.4  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 3.3.0  
packaging| 20.4  
pandas| 1.1.4  
pbr| 5.5.1  
Pillow| 7.2.0  
pip| 20.2.4  
pluggy| 0.13.1  
proto-plus| 1.11.0  
protobuf| 3.12.2  
protorpc| 0.12.0  
py| 1.9.0  
pyarrow| 0.17.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pycparser| 2.20  
pydot| 1.4.1  
pymongo| 3.10.1  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2020.1  
PyYAML| 5.3.1  
regex| 2020.11.11  
requests| 2.24.0  
requests-oauthlib| 1.3.0  
rsa| 4.6  
scikit-learn| 0.22.1  
scipy| 1.4.1  
setuptools| 50.3.2  
six| 1.15.0  
soupsieve| 2.0.1  
tensorboard| 2.4.0  
tensorboard-plugin-wit| 1.7.0  
tensorflow| 2.3.0  
tensorflow-estimator| 2.3.0  
termcolor| 1.1.0  
tqdm| 4.51.0  
typing-extensions| 3.7.4.2  
typing-inspect| 0.6.0  
uritemplate| 3.0.1  
urllib3| 1.25.11  
wcwidth| 0.2.5  
Werkzeug| 1.0.1  
wheel| 0.35.1  
wrapt| 1.12.1  
zipp| 3.4.0  
  
### Python 3.7.9

Package| Version  
---|---  
  
absl-py| 0.11.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 20.3.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.9.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2020.11.8  
cffi| 1.14.3  
chardet| 3.0.4  
click| 7.1.2  
crcmod| 1.7  
Cython| 0.29.21  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.24.2  
fasteners| 0.15  
freezegun| 0.3.15  
future| 0.18.2  
gast| 0.3.3  
google-api-core| 1.23.0  
google-api-python-client| 1.12.5  
google-apitools| 0.5.31  
google-auth| 1.23.0  
google-auth-httplib2| 0.0.4  
google-auth-oauthlib| 0.4.2  
google-cloud-bigquery| 1.26.1  
google-cloud-bigtable| 1.0.0  
google-cloud-build| 2.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-pubsub| 1.0.2  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-crc32c| 1.0.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.15  
google-resumable-media| 1.1.0  
googleapis-common-protos| 1.52.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.30.0  
grpcio-gcp| 0.2.2  
guppy3| 3.0.10  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.17.3  
idna| 2.10  
importlib-metadata| 2.0.0  
joblib| 0.17.0  
Keras-Preprocessing| 1.1.2  
libcst| 0.3.13  
Markdown| 3.3.3  
mmh3| 2.5.1  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 8.6.0  
mypy-extensions| 0.4.3  
nltk| 3.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.18.4  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 3.3.0  
packaging| 20.4  
pandas| 1.1.4  
pbr| 5.5.1  
Pillow| 7.2.0  
pip| 20.2.4  
pluggy| 0.13.1  
proto-plus| 1.11.0  
protobuf| 3.12.2  
protorpc| 0.12.0  
py| 1.9.0  
pyarrow| 0.17.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pycparser| 2.20  
pydot| 1.4.1  
pymongo| 3.10.1  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2020.1  
PyYAML| 5.3.1  
regex| 2020.11.11  
requests| 2.24.0  
requests-oauthlib| 1.3.0  
rsa| 4.6  
scikit-learn| 0.22.1  
scipy| 1.4.1  
setuptools| 50.3.2  
six| 1.15.0  
soupsieve| 2.0.1  
tensorboard| 2.4.0  
tensorboard-plugin-wit| 1.7.0  
tensorflow| 2.3.0  
tensorflow-estimator| 2.3.0  
termcolor| 1.1.0  
tqdm| 4.51.0  
typing-extensions| 3.7.4.2  
typing-inspect| 0.6.0  
uritemplate| 3.0.1  
urllib3| 1.25.11  
wcwidth| 0.2.5  
Werkzeug| 1.0.1  
wheel| 0.35.1  
wrapt| 1.12.1  
zipp| 3.4.0  
  
### Python 3.8.6

Package| Version  
---|---  
  
absl-py| 0.11.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 20.3.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.9.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2020.11.8  
cffi| 1.14.3  
chardet| 3.0.4  
click| 7.1.2  
crcmod| 1.7  
Cython| 0.29.21  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.24.2  
fasteners| 0.15  
freezegun| 0.3.15  
future| 0.18.2  
gast| 0.3.3  
google-api-core| 1.23.0  
google-api-python-client| 1.12.5  
google-apitools| 0.5.31  
google-auth| 1.23.0  
google-auth-httplib2| 0.0.4  
google-auth-oauthlib| 0.4.2  
google-cloud-bigquery| 1.26.1  
google-cloud-bigtable| 1.0.0  
google-cloud-build| 2.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-pubsub| 1.0.2  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-crc32c| 1.0.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.15  
google-resumable-media| 1.1.0  
googleapis-common-protos| 1.52.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.30.0  
grpcio-gcp| 0.2.2  
guppy3| 3.0.10  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.17.3  
idna| 2.10  
joblib| 0.17.0  
Keras-Preprocessing| 1.1.2  
libcst| 0.3.13  
Markdown| 3.3.3  
mmh3| 2.5.1  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 8.6.0  
mypy-extensions| 0.4.3  
nltk| 3.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.18.4  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 3.3.0  
packaging| 20.4  
pandas| 1.1.4  
pbr| 5.5.1  
Pillow| 7.2.0  
pip| 20.2.4  
pluggy| 0.13.1  
proto-plus| 1.11.0  
protobuf| 3.12.2  
protorpc| 0.12.0  
py| 1.9.0  
pyarrow| 0.17.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pycparser| 2.20  
pydot| 1.4.1  
pymongo| 3.10.1  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2020.1  
PyYAML| 5.3.1  
regex| 2020.11.11  
requests| 2.24.0  
requests-oauthlib| 1.3.0  
rsa| 4.6  
scikit-learn| 0.22.1  
scipy| 1.4.1  
setuptools| 50.3.2  
six| 1.15.0  
soupsieve| 2.0.1  
tensorboard| 2.4.0  
tensorboard-plugin-wit| 1.7.0  
tensorflow| 2.3.0  
tensorflow-estimator| 2.3.0  
termcolor| 1.1.0  
tqdm| 4.51.0  
typing-extensions| 3.7.4.2  
typing-inspect| 0.6.0  
uritemplate| 3.0.1  
urllib3| 1.25.11  
wcwidth| 0.2.5  
Werkzeug| 1.0.1  
wheel| 0.35.1  
wrapt| 1.12.1  
  
#### Version 2.26.0

Dataflow workers have the following packages already installed.

**Note:** Version 2.24.0 was the last Apache Beam SDK version to support Python 2 and Python 3.5.

### Python 3.6.12

Package| Version  
---|---  
  
absl-py| 0.11.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 20.3.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.9.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2020.11.8  
cffi| 1.14.3  
chardet| 3.0.4  
click| 7.1.2  
crcmod| 1.7  
Cython| 0.29.21  
dataclasses| 0.7  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.24.2  
fasteners| 0.15  
freezegun| 0.3.15  
future| 0.18.2  
gast| 0.3.3  
google-api-core| 1.23.0  
google-api-python-client| 1.12.5  
google-apitools| 0.5.31  
google-auth| 1.23.0  
google-auth-httplib2| 0.0.4  
google-auth-oauthlib| 0.4.2  
google-cloud-bigquery| 1.26.1  
google-cloud-bigtable| 1.0.0  
google-cloud-build| 2.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-pubsub| 1.0.2  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-crc32c| 1.0.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.15  
google-resumable-media| 1.1.0  
googleapis-common-protos| 1.52.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.30.0  
grpcio-gcp| 0.2.2  
guppy3| 3.0.10  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.17.3  
idna| 2.10  
importlib-metadata| 2.0.0  
joblib| 0.17.0  
Keras-Preprocessing| 1.1.2  
libcst| 0.3.13  
Markdown| 3.3.3  
mmh3| 2.5.1  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 8.6.0  
mypy-extensions| 0.4.3  
nltk| 3.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.18.4  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 3.3.0  
packaging| 20.4  
pandas| 1.1.4  
pbr| 5.5.1  
Pillow| 7.2.0  
pip| 20.2.4  
pluggy| 0.13.1  
proto-plus| 1.11.0  
protobuf| 3.12.2  
protorpc| 0.12.0  
py| 1.9.0  
pyarrow| 0.17.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pycparser| 2.20  
pydot| 1.4.1  
pymongo| 3.10.1  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2020.1  
PyYAML| 5.3.1  
regex| 2020.11.11  
requests| 2.24.0  
requests-oauthlib| 1.3.0  
rsa| 4.6  
scikit-learn| 0.22.1  
scipy| 1.4.1  
setuptools| 50.3.2  
six| 1.15.0  
soupsieve| 2.0.1  
tensorboard| 2.4.0  
tensorboard-plugin-wit| 1.7.0  
tensorflow| 2.3.0  
tensorflow-estimator| 2.3.0  
termcolor| 1.1.0  
tqdm| 4.51.0  
typing-extensions| 3.7.4.2  
typing-inspect| 0.6.0  
uritemplate| 3.0.1  
urllib3| 1.25.11  
wcwidth| 0.2.5  
Werkzeug| 1.0.1  
wheel| 0.35.1  
wrapt| 1.12.1  
zipp| 3.4.0  
  
### Python 3.7.9

Package| Version  
---|---  
  
absl-py| 0.11.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 20.3.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.9.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2020.11.8  
cffi| 1.14.3  
chardet| 3.0.4  
click| 7.1.2  
crcmod| 1.7  
Cython| 0.29.21  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.24.2  
fasteners| 0.15  
freezegun| 0.3.15  
future| 0.18.2  
gast| 0.3.3  
google-api-core| 1.23.0  
google-api-python-client| 1.12.5  
google-apitools| 0.5.31  
google-auth| 1.23.0  
google-auth-httplib2| 0.0.4  
google-auth-oauthlib| 0.4.2  
google-cloud-bigquery| 1.26.1  
google-cloud-bigtable| 1.0.0  
google-cloud-build| 2.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-pubsub| 1.0.2  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-crc32c| 1.0.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.15  
google-resumable-media| 1.1.0  
googleapis-common-protos| 1.52.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.30.0  
grpcio-gcp| 0.2.2  
guppy3| 3.0.10  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.17.3  
idna| 2.10  
importlib-metadata| 2.0.0  
joblib| 0.17.0  
Keras-Preprocessing| 1.1.2  
libcst| 0.3.13  
Markdown| 3.3.3  
mmh3| 2.5.1  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 8.6.0  
mypy-extensions| 0.4.3  
nltk| 3.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.18.4  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 3.3.0  
packaging| 20.4  
pandas| 1.1.4  
pbr| 5.5.1  
Pillow| 7.2.0  
pip| 20.2.4  
pluggy| 0.13.1  
proto-plus| 1.11.0  
protobuf| 3.12.2  
protorpc| 0.12.0  
py| 1.9.0  
pyarrow| 0.17.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pycparser| 2.20  
pydot| 1.4.1  
pymongo| 3.10.1  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2020.1  
PyYAML| 5.3.1  
regex| 2020.11.11  
requests| 2.24.0  
requests-oauthlib| 1.3.0  
rsa| 4.6  
scikit-learn| 0.22.1  
scipy| 1.4.1  
setuptools| 50.3.2  
six| 1.15.0  
soupsieve| 2.0.1  
tensorboard| 2.4.0  
tensorboard-plugin-wit| 1.7.0  
tensorflow| 2.3.0  
tensorflow-estimator| 2.3.0  
termcolor| 1.1.0  
tqdm| 4.51.0  
typing-extensions| 3.7.4.2  
typing-inspect| 0.6.0  
uritemplate| 3.0.1  
urllib3| 1.25.11  
wcwidth| 0.2.5  
Werkzeug| 1.0.1  
wheel| 0.35.1  
wrapt| 1.12.1  
zipp| 3.4.0  
  
### Python 3.8.6

Package| Version  
---|---  
  
absl-py| 0.11.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 20.3.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.9.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2020.11.8  
cffi| 1.14.3  
chardet| 3.0.4  
click| 7.1.2  
crcmod| 1.7  
Cython| 0.29.21  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.24.2  
fasteners| 0.15  
freezegun| 0.3.15  
future| 0.18.2  
gast| 0.3.3  
google-api-core| 1.23.0  
google-api-python-client| 1.12.5  
google-apitools| 0.5.31  
google-auth| 1.23.0  
google-auth-httplib2| 0.0.4  
google-auth-oauthlib| 0.4.2  
google-cloud-bigquery| 1.26.1  
google-cloud-bigtable| 1.0.0  
google-cloud-build| 2.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-pubsub| 1.0.2  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-crc32c| 1.0.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.15  
google-resumable-media| 1.1.0  
googleapis-common-protos| 1.52.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.30.0  
grpcio-gcp| 0.2.2  
guppy3| 3.0.10  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.17.3  
idna| 2.10  
joblib| 0.17.0  
Keras-Preprocessing| 1.1.2  
libcst| 0.3.13  
Markdown| 3.3.3  
mmh3| 2.5.1  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 8.6.0  
mypy-extensions| 0.4.3  
nltk| 3.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.18.4  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 3.3.0  
packaging| 20.4  
pandas| 1.1.4  
pbr| 5.5.1  
Pillow| 7.2.0  
pip| 20.2.4  
pluggy| 0.13.1  
proto-plus| 1.11.0  
protobuf| 3.12.2  
protorpc| 0.12.0  
py| 1.9.0  
pyarrow| 0.17.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pycparser| 2.20  
pydot| 1.4.1  
pymongo| 3.10.1  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2020.1  
PyYAML| 5.3.1  
regex| 2020.11.11  
requests| 2.24.0  
requests-oauthlib| 1.3.0  
rsa| 4.6  
scikit-learn| 0.22.1  
scipy| 1.4.1  
setuptools| 50.3.2  
six| 1.15.0  
soupsieve| 2.0.1  
tensorboard| 2.4.0  
tensorboard-plugin-wit| 1.7.0  
tensorflow| 2.3.0  
tensorflow-estimator| 2.3.0  
termcolor| 1.1.0  
tqdm| 4.51.0  
typing-extensions| 3.7.4.2  
typing-inspect| 0.6.0  
uritemplate| 3.0.1  
urllib3| 1.25.11  
wcwidth| 0.2.5  
Werkzeug| 1.0.1  
wheel| 0.35.1  
wrapt| 1.12.1  
  
#### Version 2.25.0

Dataflow workers have the following packages already installed.

**Note:** Version 2.24.0 was the last Apache Beam SDK version to support Python 2 and Python 3.5.

### Python 3.6.12

Package| Version  
---|---  
  
absl-py| 0.10.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 20.2.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.9.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2020.6.20  
cffi| 1.14.3  
chardet| 3.0.4  
click| 7.1.2  
crcmod| 1.7  
Cython| 0.29.21  
dataclasses| 0.7  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.24.2  
fasteners| 0.15  
freezegun| 0.3.15  
future| 0.18.2  
gast| 0.3.3  
google-api-core| 1.22.4  
google-api-python-client| 1.12.3  
google-apitools| 0.5.31  
google-auth| 1.22.1  
google-auth-httplib2| 0.0.4  
google-auth-oauthlib| 0.4.1  
google-cloud-bigquery| 1.26.1  
google-cloud-bigtable| 1.0.0  
google-cloud-build| 2.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-pubsub| 1.0.2  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-crc32c| 1.0.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.15  
google-resumable-media| 1.1.0  
googleapis-common-protos| 1.52.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.30.0  
grpcio-gcp| 0.2.2  
guppy3| 3.0.10  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.17.3  
idna| 2.10  
importlib-metadata| 2.0.0  
joblib| 0.17.0  
Keras-Preprocessing| 1.1.2  
libcst| 0.3.12  
Markdown| 3.2.2  
mmh3| 2.5.1  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 8.5.0  
mypy-extensions| 0.4.3  
nltk| 3.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.18.4  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 3.3.0  
packaging| 20.4  
pandas| 0.25.3  
pbr| 5.5.0  
Pillow| 7.2.0  
pip| 20.2.3  
pluggy| 0.13.1  
proto-plus| 1.10.0  
protobuf| 3.12.2  
protorpc| 0.12.0  
py| 1.9.0  
pyarrow| 0.17.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pycparser| 2.20  
pydot| 1.4.1  
pymongo| 3.10.1  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2020.1  
PyYAML| 5.3.1  
regex| 2020.9.27  
requests| 2.24.0  
requests-oauthlib| 1.3.0  
rsa| 4.6  
scikit-learn| 0.22.1  
scipy| 1.4.1  
setuptools| 50.3.0  
six| 1.15.0  
soupsieve| 2.0.1  
tensorboard| 2.3.0  
tensorboard-plugin-wit| 1.7.0  
tensorflow| 2.3.0  
tensorflow-estimator| 2.3.0  
termcolor| 1.1.0  
tqdm| 4.50.0  
typing-extensions| 3.7.4.2  
typing-inspect| 0.6.0  
uritemplate| 3.0.1  
urllib3| 1.25.10  
wcwidth| 0.2.5  
Werkzeug| 1.0.1  
wheel| 0.35.1  
wrapt| 1.12.1  
zipp| 3.3.0  
  
### Python 3.7.9

Package| Version  
---|---  
  
absl-py| 0.10.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 20.2.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.9.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2020.6.20  
cffi| 1.14.3  
chardet| 3.0.4  
click| 7.1.2  
crcmod| 1.7  
Cython| 0.29.21  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.24.2  
fasteners| 0.15  
freezegun| 0.3.15  
future| 0.18.2  
gast| 0.3.3  
google-api-core| 1.22.4  
google-api-python-client| 1.12.3  
google-apitools| 0.5.31  
google-auth| 1.22.1  
google-auth-httplib2| 0.0.4  
google-auth-oauthlib| 0.4.1  
google-cloud-bigquery| 1.26.1  
google-cloud-bigtable| 1.0.0  
google-cloud-build| 2.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-pubsub| 1.0.2  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-crc32c| 1.0.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.15  
google-resumable-media| 1.1.0  
googleapis-common-protos| 1.52.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.30.0  
grpcio-gcp| 0.2.2  
guppy3| 3.0.10  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.17.3  
idna| 2.10  
importlib-metadata| 2.0.0  
joblib| 0.17.0  
Keras-Preprocessing| 1.1.2  
libcst| 0.3.12  
Markdown| 3.2.2  
mmh3| 2.5.1  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 8.5.0  
mypy-extensions| 0.4.3  
nltk| 3.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.18.4  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 3.3.0  
packaging| 20.4  
pandas| 0.25.3  
pbr| 5.5.0  
Pillow| 7.2.0  
pip| 20.2.3  
pluggy| 0.13.1  
proto-plus| 1.10.0  
protobuf| 3.12.2  
protorpc| 0.12.0  
py| 1.9.0  
pyarrow| 0.17.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pycparser| 2.20  
pydot| 1.4.1  
pymongo| 3.10.1  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2020.1  
PyYAML| 5.3.1  
regex| 2020.9.27  
requests| 2.24.0  
requests-oauthlib| 1.3.0  
rsa| 4.6  
scikit-learn| 0.22.1  
scipy| 1.4.1  
setuptools| 50.3.0  
six| 1.15.0  
soupsieve| 2.0.1  
tensorboard| 2.3.0  
tensorboard-plugin-wit| 1.7.0  
tensorflow| 2.3.0  
tensorflow-estimator| 2.3.0  
termcolor| 1.1.0  
tqdm| 4.50.0  
typing-extensions| 3.7.4.2  
typing-inspect| 0.6.0  
uritemplate| 3.0.1  
urllib3| 1.25.10  
wcwidth| 0.2.5  
Werkzeug| 1.0.1  
wheel| 0.35.1  
wrapt| 1.12.1  
zipp| 3.3.0  
  
### Python 3.8.6

Package| Version  
---|---  
  
absl-py| 0.10.0  
astunparse| 1.6.3  
atomicwrites| 1.4.0  
attrs| 20.2.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.9.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2020.6.20  
cffi| 1.14.3  
chardet| 3.0.4  
click| 7.1.2  
crcmod| 1.7  
Cython| 0.29.21  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.24.2  
fasteners| 0.15  
freezegun| 0.3.15  
future| 0.18.2  
gast| 0.3.3  
google-api-core| 1.22.4  
google-api-python-client| 1.12.3  
google-apitools| 0.5.31  
google-auth| 1.22.1  
google-auth-httplib2| 0.0.4  
google-auth-oauthlib| 0.4.1  
google-cloud-bigquery| 1.26.1  
google-cloud-bigtable| 1.0.0  
google-cloud-build| 2.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-pubsub| 1.0.2  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-crc32c| 1.0.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.15  
google-resumable-media| 1.1.0  
googleapis-common-protos| 1.52.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.30.0  
grpcio-gcp| 0.2.2  
guppy3| 3.0.10  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.17.3  
idna| 2.10  
joblib| 0.17.0  
Keras-Preprocessing| 1.1.2  
libcst| 0.3.12  
Markdown| 3.2.2  
mmh3| 2.5.1  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 8.5.0  
mypy-extensions| 0.4.3  
nltk| 3.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.18.4  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 3.3.0  
packaging| 20.4  
pandas| 0.25.3  
pbr| 5.5.0  
Pillow| 7.2.0  
pip| 20.2.3  
pluggy| 0.13.1  
proto-plus| 1.10.0  
protobuf| 3.12.2  
protorpc| 0.12.0  
py| 1.9.0  
pyarrow| 0.17.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pycparser| 2.20  
pydot| 1.4.1  
pymongo| 3.10.1  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2020.1  
PyYAML| 5.3.1  
regex| 2020.9.27  
requests| 2.24.0  
requests-oauthlib| 1.3.0  
rsa| 4.6  
scikit-learn| 0.22.1  
scipy| 1.4.1  
setuptools| 50.3.0  
six| 1.15.0  
soupsieve| 2.0.1  
tensorboard| 2.3.0  
tensorboard-plugin-wit| 1.7.0  
tensorflow| 2.3.0  
tensorflow-estimator| 2.3.0  
termcolor| 1.1.0  
tqdm| 4.50.0  
typing-extensions| 3.7.4.2  
typing-inspect| 0.6.0  
uritemplate| 3.0.1  
urllib3| 1.25.10  
wcwidth| 0.2.5  
Werkzeug| 1.0.1  
wheel| 0.35.1  
wrapt| 1.12.1  
  
#### Version 2.24.0

Dataflow workers have the following packages already installed.

**Note:** This version is the last Apache Beam SDK version to support Python 2 and Python 3.5.

### Python 2.7.18

Package| Version  
---|---  
  
absl-py| 0.10.0  
astor| 0.8.1  
atomicwrites| 1.4.0  
attrs| 20.1.0  
avro| 1.8.2  
backports.functools-lru-cache| 1.6.1  
backports.weakref| 1.0.post1  
beautifulsoup4| 4.9.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2020.6.20  
chardet| 3.0.4  
configparser| 4.0.2  
contextlib2| 0.6.0.post1  
crcmod| 1.7  
Cython| 0.29.21  
dill| 0.3.1.1  
docopt| 0.6.2  
enum34| 1.1.10  
fastavro| 0.23.5  
fasteners| 0.15  
freezegun| 0.3.15  
funcsigs| 1.0.2  
functools32| 3.2.3.post2  
future| 0.18.2  
futures| 3.3.0  
gast| 0.2.2  
google-api-core| 1.22.2  
google-api-python-client| 1.11.0  
google-apitools| 0.5.31  
google-auth| 1.21.1  
google-auth-httplib2| 0.0.4  
google-auth-oauthlib| 0.4.1  
google-cloud-bigquery| 1.26.1  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-pubsub| 1.0.2  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 1.9  
google-resumable-media| 1.0.0  
googleapis-common-protos| 1.52.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.30.0  
grpcio-gcp| 0.2.2  
guppy| 0.1.11  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.17.3  
idna| 2.10  
importlib-metadata| 1.7.0  
Keras-Applications| 1.0.8  
Keras-Preprocessing| 1.1.2  
Markdown| 3.1.1  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 5.0.0  
nltk| 3.4.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.16.5  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 2.3.2  
packaging| 20.4  
pandas| 0.24.2  
pathlib2| 2.3.5  
pbr| 5.5.0  
Pillow| 6.2.2  
pip| 20.2.2  
pluggy| 0.13.1  
protobuf| 3.12.2  
protorpc| 0.12.0  
py| 1.9.0  
pyarrow| 0.16.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.1  
pymongo| 3.10.1  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2020.1  
PyVCF| 0.6.8  
PyYAML| 5.3.1  
requests| 2.24.0  
requests-oauthlib| 1.3.0  
rsa| 4.0  
scandir| 1.10.0  
scikit-learn| 0.20.4  
scipy| 1.2.2  
setuptools| 44.1.0  
singledispatch| 3.4.0.3  
six| 1.15.0  
soupsieve| 1.9.6  
tensorboard| 2.1.0  
tensorflow| 2.1.0  
tensorflow-estimator| 2.1.0  
termcolor| 1.1.0  
typing| 3.7.4.1  
typing-extensions| 3.7.4.2  
uritemplate| 3.0.1  
urllib3| 1.25.10  
wcwidth| 0.2.5  
Werkzeug| 1.0.1  
wheel| 0.34.2  
wrapt| 1.12.1  
zipp| 1.2.0  
  
### Python 3.5.9

Package| Version  
---|---  
  
absl-py| 0.10.0  
astor| 0.8.1  
atomicwrites| 1.4.0  
attrs| 20.1.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.9.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2020.6.20  
cffi| 1.14.2  
chardet| 3.0.4  
click| 7.1.2  
crcmod| 1.7  
Cython| 0.29.21  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.23.5  
fasteners| 0.15  
freezegun| 0.3.15  
future| 0.18.2  
gast| 0.2.2  
google-api-core| 1.22.2  
google-apitools| 0.5.31  
google-auth| 1.21.1  
google-auth-oauthlib| 0.4.1  
google-cloud-bigquery| 1.26.1  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-pubsub| 1.0.2  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-crc32c| 1.0.0  
google-pasta| 0.2.0  
google-resumable-media| 1.0.0  
googleapis-common-protos| 1.52.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.30.0  
grpcio-gcp| 0.2.2  
guppy3| 3.0.10  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.17.3  
idna| 2.10  
importlib-metadata| 1.7.0  
joblib| 0.14.1  
Keras-Applications| 1.0.8  
Keras-Preprocessing| 1.1.0  
Markdown| 3.2.2  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 8.5.0  
nltk| 3.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.18.4  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 3.3.0  
packaging| 20.4  
pandas| 0.25.3  
pathlib2| 2.3.5  
pbr| 5.5.0  
Pillow| 7.2.0  
pip| 20.2.2  
pluggy| 0.13.1  
protobuf| 3.12.2  
protorpc| 0.12.0  
py| 1.9.0  
pyarrow| 0.17.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pycparser| 2.20  
pydot| 1.4.1  
pymongo| 3.10.1  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2020.1  
PyYAML| 5.3.1  
regex| 2020.7.14  
requests| 2.24.0  
requests-oauthlib| 1.3.0  
rsa| 4.6  
scikit-learn| 0.22.1  
scipy| 1.4.1  
setuptools| 49.3.1  
six| 1.15.0  
soupsieve| 2.0.1  
tensorboard| 2.1.1  
tensorflow| 2.1.1  
tensorflow-estimator| 2.1.0  
termcolor| 1.1.0  
tqdm| 4.48.2  
typing-extensions| 3.7.4.2  
urllib3| 1.25.10  
wcwidth| 0.2.5  
Werkzeug| 1.0.1  
wheel| 0.34.2  
wrapt| 1.12.1  
zipp| 1.2.0  
  
### Python 3.6.12

Package| Version  
---|---  
  
absl-py| 0.10.0  
astor| 0.8.1  
atomicwrites| 1.4.0  
attrs| 20.1.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.9.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2020.6.20  
cffi| 1.14.2  
chardet| 3.0.4  
click| 7.1.2  
crcmod| 1.7  
Cython| 0.29.21  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.23.5  
fasteners| 0.15  
freezegun| 0.3.15  
future| 0.18.2  
gast| 0.2.2  
google-api-core| 1.22.2  
google-api-python-client| 1.11.0  
google-apitools| 0.5.31  
google-auth| 1.21.1  
google-auth-httplib2| 0.0.4  
google-auth-oauthlib| 0.4.1  
google-cloud-bigquery| 1.26.1  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-pubsub| 1.0.2  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-crc32c| 1.0.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.15  
google-resumable-media| 1.0.0  
googleapis-common-protos| 1.52.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.30.0  
grpcio-gcp| 0.2.2  
guppy3| 3.0.10  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.17.3  
idna| 2.10  
importlib-metadata| 1.7.0  
joblib| 0.16.0  
Keras-Applications| 1.0.8  
Keras-Preprocessing| 1.1.0  
Markdown| 3.2.2  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 8.5.0  
nltk| 3.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.18.4  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 3.3.0  
packaging| 20.4  
pandas| 0.25.3  
pbr| 5.5.0  
Pillow| 7.2.0  
pip| 20.2.2  
pluggy| 0.13.1  
protobuf| 3.12.2  
protorpc| 0.12.0  
py| 1.9.0  
pyarrow| 0.17.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pycparser| 2.20  
pydot| 1.4.1  
pymongo| 3.10.1  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2020.1  
PyYAML| 5.3.1  
regex| 2020.7.14  
requests| 2.24.0  
requests-oauthlib| 1.3.0  
rsa| 4.6  
scikit-learn| 0.22.1  
scipy| 1.4.1  
setuptools| 49.6.0  
six| 1.15.0  
soupsieve| 2.0.1  
tensorboard| 2.1.1  
tensorflow| 2.1.1  
tensorflow-estimator| 2.1.0  
termcolor| 1.1.0  
tqdm| 4.48.2  
typing-extensions| 3.7.4.2  
uritemplate| 3.0.1  
urllib3| 1.25.10  
wcwidth| 0.2.5  
Werkzeug| 1.0.1  
wheel| 0.35.1  
wrapt| 1.12.1  
zipp| 3.1.0  
  
### Python 3.7.9

Package| Version  
---|---  
  
absl-py| 0.10.0  
astor| 0.8.1  
atomicwrites| 1.4.0  
attrs| 20.1.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.9.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2020.6.20  
cffi| 1.14.2  
chardet| 3.0.4  
click| 7.1.2  
crcmod| 1.7  
Cython| 0.29.21  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.23.5  
fasteners| 0.15  
freezegun| 0.3.15  
future| 0.18.2  
gast| 0.2.2  
google-api-core| 1.22.2  
google-api-python-client| 1.11.0  
google-apitools| 0.5.31  
google-auth| 1.21.1  
google-auth-httplib2| 0.0.4  
google-auth-oauthlib| 0.4.1  
google-cloud-bigquery| 1.26.1  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-pubsub| 1.0.2  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-crc32c| 1.0.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.15  
google-resumable-media| 1.0.0  
googleapis-common-protos| 1.52.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.30.0  
grpcio-gcp| 0.2.2  
guppy3| 3.0.10  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.17.3  
idna| 2.10  
importlib-metadata| 1.7.0  
joblib| 0.16.0  
Keras-Applications| 1.0.8  
Keras-Preprocessing| 1.1.0  
Markdown| 3.2.2  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 8.5.0  
nltk| 3.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.18.4  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 3.3.0  
packaging| 20.4  
pandas| 0.25.3  
pbr| 5.5.0  
Pillow| 7.2.0  
pip| 20.2.2  
pluggy| 0.13.1  
protobuf| 3.12.2  
protorpc| 0.12.0  
py| 1.9.0  
pyarrow| 0.17.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pycparser| 2.20  
pydot| 1.4.1  
pymongo| 3.10.1  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2020.1  
PyYAML| 5.3.1  
regex| 2020.7.14  
requests| 2.24.0  
requests-oauthlib| 1.3.0  
rsa| 4.6  
scikit-learn| 0.22.1  
scipy| 1.4.1  
setuptools| 49.6.0  
six| 1.15.0  
soupsieve| 2.0.1  
tensorboard| 2.1.1  
tensorflow| 2.1.1  
tensorflow-estimator| 2.1.0  
termcolor| 1.1.0  
tqdm| 4.48.2  
typing-extensions| 3.7.4.2  
uritemplate| 3.0.1  
urllib3| 1.25.10  
wcwidth| 0.2.5  
Werkzeug| 1.0.1  
wheel| 0.35.1  
wrapt| 1.12.1  
zipp| 3.1.0  
  
### Python 3.8.5

Package| Version  
---|---  
  
atomicwrites| 1.4.0  
attrs| 20.1.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.9.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2020.6.20  
cffi| 1.14.2  
chardet| 3.0.4  
click| 7.1.2  
crcmod| 1.7  
Cython| 0.29.21  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.23.5  
fasteners| 0.15  
freezegun| 0.3.15  
future| 0.18.2  
google-api-core| 1.22.2  
google-api-python-client| 1.11.0  
google-apitools| 0.5.31  
google-auth| 1.21.1  
google-auth-httplib2| 0.0.4  
google-cloud-bigquery| 1.26.1  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-pubsub| 1.0.2  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-crc32c| 1.0.0  
google-python-cloud-debugger| 2.15  
google-resumable-media| 1.0.0  
googleapis-common-protos| 1.52.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.30.0  
grpcio-gcp| 0.2.2  
guppy3| 3.0.10  
hdfs| 2.5.8  
httplib2| 0.17.3  
idna| 2.10  
joblib| 0.16.0  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 8.5.0  
nltk| 3.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.18.4  
oauth2client| 3.0.0  
packaging| 20.4  
pandas| 0.25.3  
pbr| 5.5.0  
Pillow| 7.2.0  
pip| 20.2.2  
pluggy| 0.13.1  
protobuf| 3.12.2  
protorpc| 0.12.0  
py| 1.9.0  
pyarrow| 0.17.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pycparser| 2.20  
pydot| 1.4.1  
pymongo| 3.10.1  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2020.1  
PyYAML| 5.3.1  
regex| 2020.7.14  
requests| 2.24.0  
rsa| 4.6  
scikit-learn| 0.22.1  
scipy| 1.4.1  
setuptools| 49.3.1  
six| 1.15.0  
soupsieve| 2.0.1  
tqdm| 4.48.2  
typing-extensions| 3.7.4.2  
uritemplate| 3.0.1  
urllib3| 1.25.10  
wcwidth| 0.2.5  
wheel| 0.34.2  
  
#### Version 2.23.0

Dataflow workers have the following packages already installed.

### Python 2.7.18

Package| Version  
---|---  
  
absl-py| 0.9.0  
astor| 0.8.1  
atomicwrites| 1.4.0  
attrs| 19.3.0  
avro| 1.8.2  
backports.functools-lru-cache| 1.6.1  
backports.weakref| 1.0.post1  
beautifulsoup4| 4.9.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2020.6.20  
chardet| 3.0.4  
configparser| 4.0.2  
contextlib2| 0.6.0.post1  
crcmod| 1.7  
Cython| 0.29.20  
dill| 0.3.1.1  
docopt| 0.6.2  
enum34| 1.1.10  
fastavro| 0.23.5  
fasteners| 0.15  
freezegun| 0.3.12  
funcsigs| 1.0.2  
functools32| 3.2.3.post2  
future| 0.18.2  
futures| 3.3.0  
gast| 0.2.2  
google-api-core| 1.21.0  
google-api-python-client| 1.9.3  
google-apitools| 0.5.31  
google-auth| 1.18.0  
google-auth-httplib2| 0.0.3  
google-auth-oauthlib| 0.4.1  
google-cloud-bigquery| 1.24.0  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-pubsub| 1.0.2  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 1.9  
google-resumable-media| 0.5.1  
googleapis-common-protos| 1.52.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.30.0  
grpcio-gcp| 0.2.2  
guppy| 0.1.11  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.17.3  
idna| 2.10  
importlib-metadata| 1.7.0  
Keras-Applications| 1.0.8  
Keras-Preprocessing| 1.1.2  
Markdown| 3.1.1  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 5.0.0  
nltk| 3.4.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.16.5  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 2.3.2  
packaging| 20.4  
pandas| 0.24.2  
pathlib2| 2.3.5  
pbr| 5.4.5  
Pillow| 6.2.2  
pip| 20.1.1  
pluggy| 0.13.1  
protobuf| 3.12.2  
protorpc| 0.12.0  
py| 1.9.0  
pyarrow| 0.16.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.1  
pymongo| 3.10.1  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2020.1  
PyVCF| 0.6.8  
PyYAML| 5.3.1  
requests| 2.24.0  
requests-oauthlib| 1.3.0  
rsa| 4.0  
scandir| 1.10.0  
scikit-learn| 0.20.4  
scipy| 1.2.2  
setuptools| 44.1.0  
singledispatch| 3.4.0.3  
six| 1.15.0  
soupsieve| 1.9.6  
tensorboard| 2.1.0  
tensorflow| 2.1.0  
tensorflow-estimator| 2.1.0  
termcolor| 1.1.0  
typing| 3.7.4.1  
typing-extensions| 3.7.4.2  
uritemplate| 3.0.1  
urllib3| 1.25.9  
wcwidth| 0.2.5  
Werkzeug| 1.0.1  
wheel| 0.34.2  
wrapt| 1.12.1  
zipp| 1.2.0  
  
### Python 3.5.9

Package| Version  
---|---  
  
absl-py| 0.9.0  
astor| 0.8.1  
atomicwrites| 1.4.0  
attrs| 19.3.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.9.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2020.6.20  
chardet| 3.0.4  
click| 7.1.2  
crcmod| 1.7  
Cython| 0.29.20  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.23.5  
fasteners| 0.15  
freezegun| 0.3.12  
future| 0.18.2  
gast| 0.2.2  
google-api-core| 1.21.0  
google-apitools| 0.5.31  
google-auth| 1.18.0  
google-auth-oauthlib| 0.4.1  
google-cloud-bigquery| 1.24.0  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-pubsub| 1.0.2  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-pasta| 0.2.0  
google-resumable-media| 0.5.1  
googleapis-common-protos| 1.52.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.30.0  
grpcio-gcp| 0.2.2  
guppy3| 3.0.9  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.17.3  
idna| 2.10  
importlib-metadata| 1.7.0  
joblib| 0.14.1  
Keras-Applications| 1.0.8  
Keras-Preprocessing| 1.1.0  
Markdown| 3.2.2  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 8.4.0  
nltk| 3.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.18.4  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 3.2.1  
packaging| 20.4  
pandas| 0.25.2  
pathlib2| 2.3.5  
pbr| 5.4.5  
Pillow| 7.1.2  
pip| 20.1.1  
pluggy| 0.13.1  
protobuf| 3.12.2  
protorpc| 0.12.0  
py| 1.9.0  
pyarrow| 0.17.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.1  
pymongo| 3.10.1  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2020.1  
PyYAML| 5.3.1  
regex| 2020.6.8  
requests| 2.24.0  
requests-oauthlib| 1.3.0  
rsa| 4.6  
scikit-learn| 0.21.3  
scipy| 1.4.1  
setuptools| 47.1.1  
six| 1.15.0  
soupsieve| 2.0.1  
tensorboard| 2.1.1  
tensorflow| 2.1.1  
tensorflow-estimator| 2.1.0  
termcolor| 1.1.0  
tqdm| 4.47.0  
typing-extensions| 3.7.4.2  
urllib3| 1.25.9  
wcwidth| 0.2.5  
Werkzeug| 1.0.1  
wheel| 0.34.2  
wrapt| 1.12.1  
zipp| 1.2.0  
  
### Python 3.6.10

Package| Version  
---|---  
  
absl-py| 0.9.0  
astor| 0.8.1  
atomicwrites| 1.4.0  
attrs| 19.3.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.9.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2020.6.20  
chardet| 3.0.4  
click| 7.1.2  
crcmod| 1.7  
Cython| 0.29.20  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.23.5  
fasteners| 0.15  
freezegun| 0.3.12  
future| 0.18.2  
gast| 0.2.2  
google-api-core| 1.21.0  
google-api-python-client| 1.9.3  
google-apitools| 0.5.31  
google-auth| 1.18.0  
google-auth-httplib2| 0.0.3  
google-auth-oauthlib| 0.4.1  
google-cloud-bigquery| 1.24.0  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-pubsub| 1.0.2  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.15  
google-resumable-media| 0.5.1  
googleapis-common-protos| 1.52.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.30.0  
grpcio-gcp| 0.2.2  
guppy3| 3.0.9  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.17.3  
idna| 2.10  
importlib-metadata| 1.7.0  
joblib| 0.15.1  
Keras-Applications| 1.0.8  
Keras-Preprocessing| 1.1.0  
Markdown| 3.2.2  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 8.4.0  
nltk| 3.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.18.4  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 3.2.1  
packaging| 20.4  
pandas| 0.25.2  
pbr| 5.4.5  
Pillow| 7.1.2  
pip| 20.1.1  
pluggy| 0.13.1  
protobuf| 3.12.2  
protorpc| 0.12.0  
py| 1.9.0  
pyarrow| 0.17.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.1  
pymongo| 3.10.1  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2020.1  
PyYAML| 5.3.1  
regex| 2020.6.8  
requests| 2.24.0  
requests-oauthlib| 1.3.0  
rsa| 4.6  
scikit-learn| 0.21.3  
scipy| 1.4.1  
setuptools| 47.1.1  
six| 1.15.0  
soupsieve| 2.0.1  
tensorboard| 2.1.1  
tensorflow| 2.1.1  
tensorflow-estimator| 2.1.0  
termcolor| 1.1.0  
tqdm| 4.47.0  
typing-extensions| 3.7.4.2  
uritemplate| 3.0.1  
urllib3| 1.25.9  
wcwidth| 0.2.5  
Werkzeug| 1.0.1  
wheel| 0.34.2  
wrapt| 1.12.1  
zipp| 3.1.0  
  
### Python 3.7.7

Package| Version  
---|---  
  
absl-py| 0.9.0  
astor| 0.8.1  
atomicwrites| 1.4.0  
attrs| 19.3.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.9.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2020.6.20  
chardet| 3.0.4  
click| 7.1.2  
crcmod| 1.7  
Cython| 0.29.20  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.23.5  
fasteners| 0.15  
freezegun| 0.3.12  
future| 0.18.2  
gast| 0.2.2  
google-api-core| 1.21.0  
google-api-python-client| 1.9.3  
google-apitools| 0.5.31  
google-auth| 1.18.0  
google-auth-httplib2| 0.0.3  
google-auth-oauthlib| 0.4.1  
google-cloud-bigquery| 1.24.0  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-pubsub| 1.0.2  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 2.15  
google-resumable-media| 0.5.1  
googleapis-common-protos| 1.52.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.30.0  
grpcio-gcp| 0.2.2  
guppy3| 3.0.9  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.17.3  
idna| 2.10  
importlib-metadata| 1.7.0  
joblib| 0.15.1  
Keras-Applications| 1.0.8  
Keras-Preprocessing| 1.1.0  
Markdown| 3.2.2  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 8.4.0  
nltk| 3.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.18.4  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 3.2.1  
packaging| 20.4  
pandas| 0.25.2  
pbr| 5.4.5  
Pillow| 7.1.2  
pip| 20.1.1  
pluggy| 0.13.1  
protobuf| 3.12.2  
protorpc| 0.12.0  
py| 1.9.0  
pyarrow| 0.17.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.1  
pymongo| 3.10.1  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2020.1  
PyYAML| 5.3.1  
regex| 2020.6.8  
requests| 2.24.0  
requests-oauthlib| 1.3.0  
rsa| 4.6  
scikit-learn| 0.21.3  
scipy| 1.4.1  
setuptools| 47.1.1  
six| 1.15.0  
soupsieve| 2.0.1  
tensorboard| 2.1.1  
tensorflow| 2.1.1  
tensorflow-estimator| 2.1.0  
termcolor| 1.1.0  
tqdm| 4.47.0  
typing-extensions| 3.7.4.2  
uritemplate| 3.0.1  
urllib3| 1.25.9  
wcwidth| 0.2.5  
Werkzeug| 1.0.1  
wheel| 0.34.2  
wrapt| 1.12.1  
zipp| 3.1.0  
  
### Python 3.8.3

Package| Version  
---|---  
  
atomicwrites| 1.4.0  
attrs| 19.3.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.9.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2020.6.20  
chardet| 3.0.4  
click| 7.1.2  
crcmod| 1.7  
Cython| 0.29.20  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.23.5  
fasteners| 0.15  
freezegun| 0.3.12  
future| 0.18.2  
google-api-core| 1.21.0  
google-api-python-client| 1.9.3  
google-apitools| 0.5.31  
google-auth| 1.18.0  
google-auth-httplib2| 0.0.3  
google-cloud-bigquery| 1.24.0  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-pubsub| 1.0.2  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-python-cloud-debugger| 2.15  
google-resumable-media| 0.5.1  
googleapis-common-protos| 1.52.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.30.0  
grpcio-gcp| 0.2.2  
guppy3| 3.0.9  
hdfs| 2.5.8  
httplib2| 0.17.3  
idna| 2.10  
joblib| 0.15.1  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 8.4.0  
nltk| 3.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.18.4  
oauth2client| 3.0.0  
packaging| 20.4  
pandas| 0.25.2  
pbr| 5.4.5  
Pillow| 7.1.2  
pip| 20.1.1  
pluggy| 0.13.1  
protobuf| 3.12.2  
protorpc| 0.12.0  
py| 1.9.0  
pyarrow| 0.17.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.1  
pymongo| 3.10.1  
pyparsing| 2.4.7  
pytest| 4.6.11  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2020.1  
PyYAML| 5.3.1  
regex| 2020.6.8  
requests| 2.24.0  
rsa| 4.6  
scikit-learn| 0.21.3  
scipy| 1.4.1  
setuptools| 47.1.1  
six| 1.15.0  
soupsieve| 2.0.1  
tqdm| 4.47.0  
typing-extensions| 3.7.4.2  
uritemplate| 3.0.1  
urllib3| 1.25.9  
wcwidth| 0.2.5  
wheel| 0.34.2  
  
#### Version 2.22.0

Dataflow workers have the following packages already installed.

### Python 2.7.18

Package| Version  
---|---  
  
absl-py| 0.9.0  
astor| 0.8.1  
atomicwrites| 1.4.0  
attrs| 19.3.0  
avro| 1.8.2  
backports.functools-lru-cache| 1.6.1  
backports.weakref| 1.0.post1  
beautifulsoup4| 4.8.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2020.4.5.1  
chardet| 3.0.4  
configparser| 4.0.2  
contextlib2| 0.6.0.post1  
crcmod| 1.7  
Cython| 0.29.13  
dill| 0.3.1.1  
docopt| 0.6.2  
enum34| 1.1.10  
fastavro| 0.23.2  
fasteners| 0.15  
freezegun| 0.3.12  
funcsigs| 1.0.2  
functools32| 3.2.3.post2  
future| 0.18.2  
futures| 3.3.0  
gast| 0.2.2  
google-api-core| 1.17.0  
google-api-python-client| 1.8.4  
google-apitools| 0.5.31  
google-auth| 1.16.0  
google-auth-httplib2| 0.0.3  
google-auth-oauthlib| 0.4.1  
google-cloud-bigquery| 1.24.0  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-pubsub| 1.0.2  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 1.9  
google-resumable-media| 0.5.0  
googleapis-common-protos| 1.51.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.24.3  
grpcio-gcp| 0.2.2  
guppy| 0.1.11  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.17.3  
idna| 2.9  
importlib-metadata| 1.6.0  
Keras-Applications| 1.0.8  
Keras-Preprocessing| 1.1.2  
Markdown| 3.1.1  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 5.0.0  
nltk| 3.4.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.16.5  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 2.3.2  
packaging| 20.4  
pandas| 0.24.2  
pathlib2| 2.3.5  
pbr| 5.4.5  
Pillow| 6.2.2  
pip| 20.1.1  
pluggy| 0.13.1  
protobuf| 3.11.1  
protorpc| 0.12.0  
py| 1.8.1  
pyarrow| 0.16.0  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.1  
pymongo| 3.9.0  
pyparsing| 2.4.7  
pytest| 4.6.6  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2019.3  
PyVCF| 0.6.8  
PyYAML| 3.13  
requests| 2.23.0  
requests-oauthlib| 1.3.0  
rsa| 4.0  
scandir| 1.10.0  
scikit-learn| 0.20.4  
scipy| 1.2.2  
setuptools| 44.1.0  
singledispatch| 3.4.0.3  
six| 1.15.0  
soupsieve| 1.9.6  
tensorboard| 2.1.0  
tensorflow| 2.1.0  
tensorflow-estimator| 2.1.0  
termcolor| 1.1.0  
typing| 3.7.4.1  
typing-extensions| 3.7.4.1  
uritemplate| 3.0.1  
urllib3| 1.25.9  
wcwidth| 0.2.2  
Werkzeug| 1.0.1  
wheel| 0.34.2  
wrapt| 1.12.1  
zipp| 1.2.0  
  
### Python 3.5.9

Package| Version  
---|---  
  
absl-py| 0.9.0  
astor| 0.8.1  
atomicwrites| 1.4.0  
attrs| 19.3.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.8.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2020.4.5.1  
chardet| 3.0.4  
crcmod| 1.7  
Cython| 0.29.13  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.23.2  
fasteners| 0.15  
freezegun| 0.3.12  
future| 0.18.2  
gast| 0.2.2  
google-api-core| 1.17.0  
google-apitools| 0.5.31  
google-auth| 1.16.0  
google-auth-oauthlib| 0.4.1  
google-cloud-bigquery| 1.24.0  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-pubsub| 1.0.2  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-pasta| 0.2.0  
google-resumable-media| 0.5.0  
googleapis-common-protos| 1.51.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.24.3  
grpcio-gcp| 0.2.2  
guppy3| 3.0.9  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.17.3  
idna| 2.9  
importlib-metadata| 1.6.0  
joblib| 0.14.1  
Keras-Applications| 1.0.8  
Keras-Preprocessing| 1.1.2  
Markdown| 3.2.2  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 8.3.0  
nltk| 3.4.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.17.3  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 3.2.1  
packaging| 20.4  
pandas| 0.25.2  
pathlib2| 2.3.5  
pbr| 5.4.5  
Pillow| 7.1.2  
pip| 20.1.1  
pluggy| 0.13.1  
protobuf| 3.11.1  
protorpc| 0.12.0  
py| 1.8.1  
pyarrow| 0.17.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.1  
pymongo| 3.9.0  
pyparsing| 2.4.7  
pytest| 4.6.6  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2019.3  
PyYAML| 3.13  
requests| 2.23.0  
requests-oauthlib| 1.3.0  
rsa| 4.0  
scikit-learn| 0.21.3  
scipy| 1.4.1  
setuptools| 46.4.0  
six| 1.15.0  
soupsieve| 2.0.1  
tensorboard| 2.1.1  
tensorflow| 2.1.0  
tensorflow-estimator| 2.1.0  
termcolor| 1.1.0  
typing-extensions| 3.7.4.1  
urllib3| 1.25.9  
wcwidth| 0.2.2  
Werkzeug| 1.0.1  
wheel| 0.34.2  
wrapt| 1.12.1  
zipp| 1.2.0  
  
### Python 3.6.10

Package| Version  
---|---  
  
absl-py| 0.9.0  
astor| 0.8.1  
atomicwrites| 1.4.0  
attrs| 19.3.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.8.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2020.4.5.1  
chardet| 3.0.4  
crcmod| 1.7  
Cython| 0.29.13  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.23.2  
fasteners| 0.15  
freezegun| 0.3.12  
future| 0.18.2  
gast| 0.2.2  
google-api-core| 1.17.0  
google-apitools| 0.5.31  
google-auth| 1.16.0  
google-auth-oauthlib| 0.4.1  
google-cloud-bigquery| 1.24.0  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-pubsub| 1.0.2  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-pasta| 0.2.0  
google-resumable-media| 0.5.0  
googleapis-common-protos| 1.51.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.24.3  
grpcio-gcp| 0.2.2  
guppy3| 3.0.9  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.17.3  
idna| 2.9  
importlib-metadata| 1.6.0  
joblib| 0.15.1  
Keras-Applications| 1.0.8  
Keras-Preprocessing| 1.1.2  
Markdown| 3.2.2  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 8.3.0  
nltk| 3.4.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.17.3  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 3.2.1  
packaging| 20.4  
pandas| 0.25.2  
pbr| 5.4.5  
Pillow| 7.1.2  
pip| 20.1.1  
pluggy| 0.13.1  
protobuf| 3.11.1  
protorpc| 0.12.0  
py| 1.8.1  
pyarrow| 0.17.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.1  
pymongo| 3.9.0  
pyparsing| 2.4.7  
pytest| 4.6.6  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2019.3  
PyYAML| 3.13  
requests| 2.23.0  
requests-oauthlib| 1.3.0  
rsa| 4.0  
scikit-learn| 0.21.3  
scipy| 1.4.1  
setuptools| 46.4.0  
six| 1.15.0  
soupsieve| 2.0.1  
tensorboard| 2.1.1  
tensorflow| 2.1.0  
tensorflow-estimator| 2.1.0  
termcolor| 1.1.0  
typing-extensions| 3.7.4.1  
urllib3| 1.25.9  
wcwidth| 0.2.2  
Werkzeug| 1.0.1  
wheel| 0.34.2  
wrapt| 1.12.1  
zipp| 3.1.0  
  
### Python 3.7.7

Package| Version  
---|---  
  
absl-py| 0.9.0  
astor| 0.8.1  
atomicwrites| 1.4.0  
attrs| 19.3.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.8.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2020.4.5.1  
chardet| 3.0.4  
crcmod| 1.7  
Cython| 0.29.13  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.23.2  
fasteners| 0.15  
freezegun| 0.3.12  
future| 0.18.2  
gast| 0.2.2  
google-api-core| 1.17.0  
google-apitools| 0.5.31  
google-auth| 1.16.0  
google-auth-oauthlib| 0.4.1  
google-cloud-bigquery| 1.24.0  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-pubsub| 1.0.2  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-pasta| 0.2.0  
google-resumable-media| 0.5.0  
googleapis-common-protos| 1.51.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.24.3  
grpcio-gcp| 0.2.2  
guppy3| 3.0.9  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.17.3  
idna| 2.9  
importlib-metadata| 1.6.0  
joblib| 0.15.1  
Keras-Applications| 1.0.8  
Keras-Preprocessing| 1.1.2  
Markdown| 3.2.2  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 8.3.0  
nltk| 3.4.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.17.3  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 3.2.1  
packaging| 20.4  
pandas| 0.25.2  
pbr| 5.4.5  
Pillow| 7.1.2  
pip| 20.1.1  
pluggy| 0.13.1  
protobuf| 3.11.1  
protorpc| 0.12.0  
py| 1.8.1  
pyarrow| 0.17.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.1  
pymongo| 3.9.0  
pyparsing| 2.4.7  
pytest| 4.6.6  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2019.3  
PyYAML| 3.13  
requests| 2.23.0  
requests-oauthlib| 1.3.0  
rsa| 4.0  
scikit-learn| 0.21.3  
scipy| 1.4.1  
setuptools| 46.4.0  
six| 1.15.0  
soupsieve| 2.0.1  
tensorboard| 2.1.1  
tensorflow| 2.1.0  
tensorflow-estimator| 2.1.0  
termcolor| 1.1.0  
typing-extensions| 3.7.4.1  
urllib3| 1.25.9  
wcwidth| 0.2.2  
Werkzeug| 1.0.1  
wheel| 0.34.2  
wrapt| 1.12.1  
zipp| 3.1.0  
  
#### Version 2.21.0

Dataflow workers have the following packages already installed.

### Python 2.7.18

Package| Version  
---|---  
  
absl-py| 0.9.0  
astor| 0.8.1  
atomicwrites| 1.4.0  
attrs| 19.3.0  
avro| 1.8.2  
backports.functools-lru-cache| 1.6.1  
backports.weakref| 1.0.post1  
beautifulsoup4| 4.8.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2020.4.5.1  
chardet| 3.0.4  
configparser| 4.0.2  
contextlib2| 0.6.0.post1  
crcmod| 1.7  
Cython| 0.29.13  
dill| 0.3.1.1  
docopt| 0.6.2  
enum34| 1.1.10  
fastavro| 0.21.24  
fasteners| 0.15  
freezegun| 0.3.12  
funcsigs| 1.0.2  
functools32| 3.2.3.post2  
future| 0.18.2  
futures| 3.3.0  
gast| 0.2.2  
google-api-core| 1.17.0  
google-api-python-client| 1.8.3  
google-apitools| 0.5.28  
google-auth| 1.15.0  
google-auth-httplib2| 0.0.3  
google-auth-oauthlib| 0.4.1  
google-cloud-bigquery| 1.24.0  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-pubsub| 1.0.2  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 1.9  
google-resumable-media| 0.5.0  
googleapis-common-protos| 1.51.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.24.3  
grpcio-gcp| 0.2.2  
guppy| 0.1.11  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.12.0  
idna| 2.9  
importlib-metadata| 1.6.0  
Keras-Applications| 1.0.8  
Keras-Preprocessing| 1.1.2  
Markdown| 3.1.1  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 5.0.0  
nltk| 3.4.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.16.5  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 2.3.2  
packaging| 20.4  
pandas| 0.24.2  
pathlib2| 2.3.5  
pbr| 5.4.5  
Pillow| 6.2.2  
pip| 20.1.1  
pluggy| 0.13.1  
protobuf| 3.11.1  
protorpc| 0.12.0  
py| 1.8.1  
pyarrow| 0.15.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.1  
pymongo| 3.9.0  
pyparsing| 2.4.7  
pytest| 4.6.6  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2019.3  
PyVCF| 0.6.8  
PyYAML| 3.13  
requests| 2.23.0  
requests-oauthlib| 1.3.0  
rsa| 4.0  
scandir| 1.10.0  
scikit-learn| 0.20.4  
scipy| 1.2.2  
setuptools| 44.1.0  
singledispatch| 3.4.0.3  
six| 1.14.0  
soupsieve| 1.9.6  
tensorboard| 2.1.0  
tensorflow| 2.1.0  
tensorflow-estimator| 2.1.0  
termcolor| 1.1.0  
typing| 3.7.4.1  
typing-extensions| 3.7.4.1  
uritemplate| 3.0.1  
urllib3| 1.25.9  
wcwidth| 0.1.9  
Werkzeug| 1.0.1  
wheel| 0.34.2  
wrapt| 1.12.1  
zipp| 1.2.0  
  
### Python 3.5.9

Package| Version  
---|---  
  
absl-py| 0.9.0  
astor| 0.8.1  
atomicwrites| 1.4.0  
attrs| 19.3.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.8.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2020.4.5.1  
chardet| 3.0.4  
crcmod| 1.7  
Cython| 0.29.13  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.21.24  
fasteners| 0.15  
freezegun| 0.3.12  
future| 0.18.2  
gast| 0.2.2  
google-api-core| 1.17.0  
google-apitools| 0.5.28  
google-auth| 1.15.0  
google-auth-oauthlib| 0.4.1  
google-cloud-bigquery| 1.24.0  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-pubsub| 1.0.2  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-pasta| 0.2.0  
google-resumable-media| 0.5.0  
googleapis-common-protos| 1.51.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.24.3  
grpcio-gcp| 0.2.2  
guppy3| 3.0.9  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.12.0  
idna| 2.9  
importlib-metadata| 1.6.0  
joblib| 0.14.1  
Keras-Applications| 1.0.8  
Keras-Preprocessing| 1.1.2  
Markdown| 3.2.2  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 8.3.0  
nltk| 3.4.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.17.3  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 3.2.1  
packaging| 20.4  
pandas| 0.25.2  
pathlib2| 2.3.5  
pbr| 5.4.5  
Pillow| 7.1.2  
pip| 20.1.1  
pluggy| 0.13.1  
protobuf| 3.11.1  
protorpc| 0.12.0  
py| 1.8.1  
pyarrow| 0.15.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.1  
pymongo| 3.9.0  
pyparsing| 2.4.7  
pytest| 4.6.6  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2019.3  
PyYAML| 3.13  
requests| 2.23.0  
requests-oauthlib| 1.3.0  
rsa| 4.0  
scikit-learn| 0.21.3  
scipy| 1.4.1  
setuptools| 46.3.1  
six| 1.14.0  
soupsieve| 2.0.1  
tensorboard| 2.1.1  
tensorflow| 2.1.0  
tensorflow-estimator| 2.1.0  
termcolor| 1.1.0  
typing-extensions| 3.7.4.1  
urllib3| 1.25.9  
wcwidth| 0.1.9  
Werkzeug| 1.0.1  
wheel| 0.34.2  
wrapt| 1.12.1  
zipp| 1.2.0  
  
### Python 3.6.10

Package| Version  
---|---  
  
absl-py| 0.9.0  
astor| 0.8.1  
atomicwrites| 1.4.0  
attrs| 19.3.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.8.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2020.4.5.1  
chardet| 3.0.4  
crcmod| 1.7  
Cython| 0.29.13  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.21.24  
fasteners| 0.15  
freezegun| 0.3.12  
future| 0.18.2  
gast| 0.2.2  
google-api-core| 1.17.0  
google-apitools| 0.5.28  
google-auth| 1.15.0  
google-auth-oauthlib| 0.4.1  
google-cloud-bigquery| 1.24.0  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-pubsub| 1.0.2  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-pasta| 0.2.0  
google-resumable-media| 0.5.0  
googleapis-common-protos| 1.51.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.24.3  
grpcio-gcp| 0.2.2  
guppy3| 3.0.9  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.12.0  
idna| 2.9  
importlib-metadata| 1.6.0  
joblib| 0.15.1  
Keras-Applications| 1.0.8  
Keras-Preprocessing| 1.1.2  
Markdown| 3.2.2  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 8.3.0  
nltk| 3.4.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.17.3  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 3.2.1  
packaging| 20.4  
pandas| 0.25.2  
pbr| 5.4.5  
Pillow| 7.1.2  
pip| 20.1.1  
pluggy| 0.13.1  
protobuf| 3.11.1  
protorpc| 0.12.0  
py| 1.8.1  
pyarrow| 0.15.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.1  
pymongo| 3.9.0  
pyparsing| 2.4.7  
pytest| 4.6.6  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2019.3  
PyYAML| 3.13  
requests| 2.23.0  
requests-oauthlib| 1.3.0  
rsa| 4.0  
scikit-learn| 0.21.3  
scipy| 1.4.1  
setuptools| 46.3.1  
six| 1.14.0  
soupsieve| 2.0.1  
tensorboard| 2.1.1  
tensorflow| 2.1.0  
tensorflow-estimator| 2.1.0  
termcolor| 1.1.0  
typing-extensions| 3.7.4.1  
urllib3| 1.25.9  
wcwidth| 0.1.9  
Werkzeug| 1.0.1  
wheel| 0.34.2  
wrapt| 1.12.1  
zipp| 3.1.0  
  
### Python 3.7.7

Package| Version  
---|---  
  
absl-py| 0.9.0  
astor| 0.8.1  
atomicwrites| 1.4.0  
attrs| 19.3.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.8.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2020.4.5.1  
chardet| 3.0.4  
crcmod| 1.7  
Cython| 0.29.13  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.21.24  
fasteners| 0.15  
freezegun| 0.3.12  
future| 0.18.2  
gast| 0.2.2  
google-api-core| 1.17.0  
google-apitools| 0.5.28  
google-auth| 1.15.0  
google-auth-oauthlib| 0.4.1  
google-cloud-bigquery| 1.24.0  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-pubsub| 1.0.2  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-pasta| 0.2.0  
google-resumable-media| 0.5.0  
googleapis-common-protos| 1.51.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.24.3  
grpcio-gcp| 0.2.2  
guppy3| 3.0.9  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.12.0  
idna| 2.9  
importlib-metadata| 1.6.0  
joblib| 0.15.1  
Keras-Applications| 1.0.8  
Keras-Preprocessing| 1.1.2  
Markdown| 3.2.2  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 8.3.0  
nltk| 3.4.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.17.3  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 3.2.1  
packaging| 20.4  
pandas| 0.25.2  
pbr| 5.4.5  
Pillow| 7.1.2  
pip| 20.1.1  
pluggy| 0.13.1  
protobuf| 3.11.1  
protorpc| 0.12.0  
py| 1.8.1  
pyarrow| 0.15.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.1  
pymongo| 3.9.0  
pyparsing| 2.4.7  
pytest| 4.6.6  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2019.3  
PyYAML| 3.13  
requests| 2.23.0  
requests-oauthlib| 1.3.0  
rsa| 4.0  
scikit-learn| 0.21.3  
scipy| 1.4.1  
setuptools| 46.3.1  
six| 1.14.0  
soupsieve| 2.0.1  
tensorboard| 2.1.1  
tensorflow| 2.1.0  
tensorflow-estimator| 2.1.0  
termcolor| 1.1.0  
typing-extensions| 3.7.4.1  
urllib3| 1.25.9  
wcwidth| 0.1.9  
Werkzeug| 1.0.1  
wheel| 0.34.2  
wrapt| 1.12.1  
zipp| 3.1.0  
  
#### Version 2.20.0

Dataflow workers have the following packages already installed.

### Python 2.7.17

Package| Version  
---|---  
  
absl-py| 0.9.0  
astor| 0.8.1  
atomicwrites| 1.3.0  
attrs| 19.3.0  
avro| 1.8.2  
backports.functools-lru-cache| 1.6.1  
backports.weakref| 1.0.post1  
beautifulsoup4| 4.8.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2019.11.28  
chardet| 3.0.4  
configparser| 4.0.2  
contextlib2| 0.6.0.post1  
crcmod| 1.7  
Cython| 0.29.13  
dill| 0.3.1.1  
docopt| 0.6.2  
enum34| 1.1.10  
fastavro| 0.21.24  
fasteners| 0.15  
freezegun| 0.3.12  
funcsigs| 1.0.2  
functools32| 3.2.3.post2  
future| 0.17.1  
futures| 3.3.0  
gast| 0.2.2  
google-api-core| 1.16.0  
google-api-python-client| 1.8.0  
google-apitools| 0.5.28  
google-auth| 1.11.3  
google-auth-httplib2| 0.0.3  
google-auth-oauthlib| 0.4.1  
google-cloud-bigquery| 1.24.0  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-pubsub| 1.0.2  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-pasta| 0.2.0  
google-python-cloud-debugger| 1.9  
google-resumable-media| 0.5.0  
googleapis-common-protos| 1.51.0  
googledatastore| 7.0.2  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.24.3  
grpcio-gcp| 0.2.2  
guppy| 0.1.11  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.12.0  
idna| 2.9  
importlib-metadata| 1.5.0  
Keras-Applications| 1.0.8  
Keras-Preprocessing| 1.1.0  
Markdown| 3.1.1  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 5.0.0  
nltk| 3.4.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.16.5  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 2.3.2  
packaging| 20.3  
pandas| 0.24.2  
pathlib2| 2.3.5  
pbr| 5.4.4  
Pillow| 6.2.1  
pip| 20.0.2  
pluggy| 0.13.1  
proto-google-cloud-datastore-v1| 0.90.4  
protobuf| 3.11.1  
protorpc| 0.12.0  
py| 1.8.1  
pyarrow| 0.15.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.1  
pymongo| 3.9.0  
pyparsing| 2.4.6  
pytest| 4.6.6  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2019.3  
PyVCF| 0.6.8  
PyYAML| 3.13  
requests| 2.23.0  
requests-oauthlib| 1.3.0  
rsa| 4.0  
scandir| 1.10.0  
scikit-learn| 0.20.4  
scipy| 1.2.2  
setuptools| 44.0.0  
singledispatch| 3.4.0.3  
six| 1.14.0  
soupsieve| 1.9.5  
tensorboard| 2.1.0  
tensorflow| 2.1.0  
tensorflow-estimator| 2.1.0  
termcolor| 1.1.0  
typing| 3.7.4.1  
typing-extensions| 3.7.4.1  
uritemplate| 3.0.1  
urllib3| 1.25.8  
wcwidth| 0.1.8  
Werkzeug| 1.0.0  
wheel| 0.34.2  
wrapt| 1.12.1  
zipp| 1.2.0  
  
### Python 3.5.9

Package| Version  
---|---  
  
absl-py| 0.9.0  
astor| 0.8.1  
atomicwrites| 1.3.0  
attrs| 19.3.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.8.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2019.11.28  
chardet| 3.0.4  
crcmod| 1.7  
Cython| 0.29.13  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.21.24  
fasteners| 0.15  
freezegun| 0.3.12  
future| 0.17.1  
gast| 0.2.2  
google-api-core| 1.16.0  
google-apitools| 0.5.28  
google-auth| 1.11.3  
google-auth-oauthlib| 0.4.1  
google-cloud-bigquery| 1.24.0  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-pubsub| 1.0.2  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-pasta| 0.2.0  
google-resumable-media| 0.5.0  
googleapis-common-protos| 1.51.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.24.3  
grpcio-gcp| 0.2.2  
guppy3| 3.0.9  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.12.0  
idna| 2.9  
importlib-metadata| 1.5.0  
joblib| 0.14.1  
Keras-Applications| 1.0.8  
Keras-Preprocessing| 1.1.0  
Markdown| 3.2.1  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 8.2.0  
nltk| 3.4.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.17.3  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 3.2.0  
packaging| 20.3  
pandas| 0.25.2  
pathlib2| 2.3.5  
pbr| 5.4.4  
Pillow| 6.2.1  
pip| 20.0.2  
pluggy| 0.13.1  
protobuf| 3.11.1  
protorpc| 0.12.0  
py| 1.8.1  
pyarrow| 0.15.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.1  
pymongo| 3.9.0  
pyparsing| 2.4.6  
pytest| 4.6.6  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2019.3  
PyYAML| 3.13  
requests| 2.23.0  
requests-oauthlib| 1.3.0  
rsa| 4.0  
scikit-learn| 0.21.3  
scipy| 1.4.1  
setuptools| 45.2.0  
six| 1.14.0  
soupsieve| 2.0  
tensorboard| 2.1.1  
tensorflow| 2.1.0  
tensorflow-estimator| 2.1.0  
termcolor| 1.1.0  
typing-extensions| 3.7.4.1  
urllib3| 1.25.8  
wcwidth| 0.1.8  
Werkzeug| 1.0.0  
wheel| 0.34.2  
wrapt| 1.12.1  
zipp| 1.2.0  
  
### Python 3.6.10

Package| Version  
---|---  
  
absl-py| 0.9.0  
astor| 0.8.1  
atomicwrites| 1.3.0  
attrs| 19.3.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.8.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2019.11.28  
chardet| 3.0.4  
crcmod| 1.7  
Cython| 0.29.13  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.21.24  
fasteners| 0.15  
freezegun| 0.3.12  
future| 0.17.1  
gast| 0.2.2  
google-api-core| 1.16.0  
google-apitools| 0.5.28  
google-auth| 1.11.3  
google-auth-oauthlib| 0.4.1  
google-cloud-bigquery| 1.24.0  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-pubsub| 1.0.2  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-pasta| 0.2.0  
google-resumable-media| 0.5.0  
googleapis-common-protos| 1.51.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.24.3  
grpcio-gcp| 0.2.2  
guppy3| 3.0.9  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.12.0  
idna| 2.9  
importlib-metadata| 1.5.0  
joblib| 0.14.1  
Keras-Applications| 1.0.8  
Keras-Preprocessing| 1.1.0  
Markdown| 3.2.1  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 8.2.0  
nltk| 3.4.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.17.3  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 3.2.0  
packaging| 20.3  
pandas| 0.25.2  
pbr| 5.4.4  
Pillow| 6.2.1  
pip| 20.0.2  
pluggy| 0.13.1  
protobuf| 3.11.1  
protorpc| 0.12.0  
py| 1.8.1  
pyarrow| 0.15.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.1  
pymongo| 3.9.0  
pyparsing| 2.4.6  
pytest| 4.6.6  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2019.3  
PyYAML| 3.13  
requests| 2.23.0  
requests-oauthlib| 1.3.0  
rsa| 4.0  
scikit-learn| 0.21.3  
scipy| 1.4.1  
setuptools| 45.2.0  
six| 1.14.0  
soupsieve| 2.0  
tensorboard| 2.1.1  
tensorflow| 2.1.0  
tensorflow-estimator| 2.1.0  
termcolor| 1.1.0  
typing-extensions| 3.7.4.1  
urllib3| 1.25.8  
wcwidth| 0.1.8  
Werkzeug| 1.0.0  
wheel| 0.34.2  
wrapt| 1.12.1  
zipp| 3.1.0  
  
### Python 3.7.7

Package| Version  
---|---  
  
absl-py| 0.9.0  
astor| 0.8.1  
atomicwrites| 1.3.0  
attrs| 19.3.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.8.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2019.11.28  
chardet| 3.0.4  
crcmod| 1.7  
Cython| 0.29.13  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.21.24  
fasteners| 0.15  
freezegun| 0.3.12  
future| 0.17.1  
gast| 0.2.2  
google-api-core| 1.16.0  
google-apitools| 0.5.28  
google-auth| 1.11.3  
google-auth-oauthlib| 0.4.1  
google-cloud-bigquery| 1.24.0  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-dlp| 0.13.0  
google-cloud-language| 1.3.0  
google-cloud-pubsub| 1.0.2  
google-cloud-spanner| 1.13.0  
google-cloud-videointelligence| 1.13.0  
google-cloud-vision| 0.42.0  
google-pasta| 0.2.0  
google-resumable-media| 0.5.0  
googleapis-common-protos| 1.51.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.24.3  
grpcio-gcp| 0.2.2  
guppy3| 3.0.9  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.12.0  
idna| 2.9  
importlib-metadata| 1.5.0  
joblib| 0.14.1  
Keras-Applications| 1.0.8  
Keras-Preprocessing| 1.1.0  
Markdown| 3.2.1  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 8.2.0  
nltk| 3.4.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.17.3  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 3.2.0  
packaging| 20.3  
pandas| 0.25.2  
pbr| 5.4.4  
Pillow| 6.2.1  
pip| 20.0.2  
pluggy| 0.13.1  
protobuf| 3.11.1  
protorpc| 0.12.0  
py| 1.8.1  
pyarrow| 0.15.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.1  
pymongo| 3.9.0  
pyparsing| 2.4.6  
pytest| 4.6.6  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2019.3  
PyYAML| 3.13  
requests| 2.23.0  
requests-oauthlib| 1.3.0  
rsa| 4.0  
scikit-learn| 0.21.3  
scipy| 1.4.1  
setuptools| 46.0.0  
six| 1.14.0  
soupsieve| 2.0  
tensorboard| 2.1.1  
tensorflow| 2.1.0  
tensorflow-estimator| 2.1.0  
termcolor| 1.1.0  
typing-extensions| 3.7.4.1  
urllib3| 1.25.8  
wcwidth| 0.1.8  
Werkzeug| 1.0.0  
wheel| 0.34.2  
wrapt| 1.12.1  
zipp| 3.1.0  
  
#### Version 2.19.0

Dataflow workers have the following packages already installed.

### Python 2.7.13

Package| Version  
---|---  
  
absl-py| 0.9.0  
astor| 0.8.1  
atomicwrites| 1.3.0  
attrs| 19.3.0  
avro| 1.8.2  
backports.functools-lru-cache| 1.6.1  
backports.weakref| 1.0.post1  
beautifulsoup4| 4.8.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2019.11.28  
chardet| 3.0.4  
configparser| 4.0.2  
contextlib2| 0.6.0.post1  
crcmod| 1.7  
Cython| 0.29.13  
dill| 0.3.1.1  
docopt| 0.6.2  
enum34| 1.1.6  
fastavro| 0.21.24  
fasteners| 0.15  
freezegun| 0.3.12  
funcsigs| 1.0.2  
functools32| 3.2.3.post2  
future| 0.17.1  
futures| 3.3.0  
gast| 0.2.2  
google-api-core| 1.16.0  
google-api-python-client| 1.7.11  
google-apitools| 0.5.28  
google-auth| 1.11.0  
google-auth-httplib2| 0.0.3  
google-auth-oauthlib| 0.4.1  
google-cloud-bigquery| 1.17.1  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-pubsub| 1.0.2  
google-pasta| 0.1.8  
google-python-cloud-debugger| 1.9  
google-resumable-media| 0.4.1  
googleapis-common-protos| 1.51.0  
googledatastore| 7.0.2  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.24.3  
guppy| 0.1.11  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.12.0  
idna| 2.8  
importlib-metadata| 1.5.0  
Keras-Applications| 1.0.8  
Keras-Preprocessing| 1.1.0  
Markdown| 3.1.1  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 5.0.0  
nltk| 3.4.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.16.5  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 2.3.2  
packaging| 20.1  
pandas| 0.24.2  
pathlib2| 2.3.5  
pbr| 5.4.4  
Pillow| 6.2.1  
pip| 20.0.2  
pluggy| 0.13.1  
proto-google-cloud-datastore-v1| 0.90.4  
protobuf| 3.11.1  
protorpc| 0.12.0  
py| 1.8.1  
pyarrow| 0.15.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.1  
pymongo| 3.9.0  
pyparsing| 2.4.6  
pytest| 4.6.6  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2019.3  
PyVCF| 0.6.8  
PyYAML| 3.13  
requests| 2.22.0  
requests-oauthlib| 1.3.0  
rsa| 4.0  
scandir| 1.10.0  
scikit-learn| 0.20.4  
scipy| 1.2.2  
setuptools| 44.0.0  
singledispatch| 3.4.0.3  
six| 1.14.0  
soupsieve| 1.9.5  
tensorboard| 2.1.0  
tensorflow-cpu| 2.1.0  
tensorflow-estimator| 2.1.0  
termcolor| 1.1.0  
typing| 3.7.4.1  
typing-extensions| 3.7.4.1  
uritemplate| 3.0.1  
urllib3| 1.25.8  
wcwidth| 0.1.8  
Werkzeug| 0.16.1  
wheel| 0.34.2  
wrapt| 1.11.2  
zipp| 1.1.0  
  
### Python 3.5.9

Package| Version  
---|---  
  
absl-py| 0.9.0  
astor| 0.8.1  
atomicwrites| 1.3.0  
attrs| 19.3.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.8.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2019.11.28  
chardet| 3.0.4  
crcmod| 1.7  
Cython| 0.29.13  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.21.24  
fasteners| 0.15  
freezegun| 0.3.12  
future| 0.17.1  
gast| 0.2.2  
google-api-core| 1.16.0  
google-apitools| 0.5.28  
google-auth| 1.11.0  
google-auth-oauthlib| 0.4.1  
google-cloud-bigquery| 1.17.1  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-pubsub| 1.0.2  
google-pasta| 0.1.8  
google-resumable-media| 0.4.1  
googleapis-common-protos| 1.51.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.24.3  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.12.0  
idna| 2.8  
importlib-metadata| 1.5.0  
joblib| 0.14.1  
Keras-Applications| 1.0.8  
Keras-Preprocessing| 1.1.0  
Markdown| 3.1.1  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 8.2.0  
nltk| 3.4.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.17.3  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 3.1.0  
packaging| 20.1  
pandas| 0.25.2  
pathlib2| 2.3.5  
pbr| 5.4.4  
Pillow| 6.2.1  
pip| 20.0.2  
pluggy| 0.13.1  
protobuf| 3.11.1  
protorpc| 0.12.0  
py| 1.8.1  
pyarrow| 0.15.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.1  
pymongo| 3.9.0  
pyparsing| 2.4.6  
pytest| 4.6.6  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2019.3  
PyYAML| 3.13  
requests| 2.22.0  
requests-oauthlib| 1.3.0  
rsa| 4.0  
scikit-learn| 0.21.3  
scipy| 1.4.1  
setuptools| 45.1.0  
six| 1.14.0  
soupsieve| 1.9.5  
tensorboard| 2.1.0  
tensorflow-cpu| 2.1.0  
tensorflow-estimator| 2.1.0  
termcolor| 1.1.0  
typing| 3.7.4.1  
typing-extensions| 3.7.4.1  
urllib3| 1.25.8  
wcwidth| 0.1.8  
Werkzeug| 0.16.1  
wheel| 0.34.2  
wrapt| 1.11.2  
zipp| 1.1.0  
  
### Python 3.6.10

Package| Version  
---|---  
  
absl-py| 0.9.0  
astor| 0.8.1  
atomicwrites| 1.3.0  
attrs| 19.3.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.8.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2019.11.28  
chardet| 3.0.4  
crcmod| 1.7  
Cython| 0.29.13  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.21.24  
fasteners| 0.15  
freezegun| 0.3.12  
future| 0.17.1  
gast| 0.2.2  
google-api-core| 1.16.0  
google-apitools| 0.5.28  
google-auth| 1.11.0  
google-auth-oauthlib| 0.4.1  
google-cloud-bigquery| 1.17.1  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-pubsub| 1.0.2  
google-pasta| 0.1.8  
google-resumable-media| 0.4.1  
googleapis-common-protos| 1.51.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.24.3  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.12.0  
idna| 2.8  
importlib-metadata| 1.5.0  
joblib| 0.14.1  
Keras-Applications| 1.0.8  
Keras-Preprocessing| 1.1.0  
Markdown| 3.1.1  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 8.2.0  
nltk| 3.4.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.17.3  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 3.1.0  
packaging| 20.1  
pandas| 0.25.2  
pbr| 5.4.4  
Pillow| 6.2.1  
pip| 20.0.2  
pluggy| 0.13.1  
protobuf| 3.11.1  
protorpc| 0.12.0  
py| 1.8.1  
pyarrow| 0.15.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.1  
pymongo| 3.9.0  
pyparsing| 2.4.6  
pytest| 4.6.6  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2019.3  
PyYAML| 3.13  
requests| 2.22.0  
requests-oauthlib| 1.3.0  
rsa| 4.0  
scikit-learn| 0.21.3  
scipy| 1.4.1  
setuptools| 45.1.0  
six| 1.14.0  
soupsieve| 1.9.5  
tensorboard| 2.1.0  
tensorflow-cpu| 2.1.0  
tensorflow-estimator| 2.1.0  
termcolor| 1.1.0  
typing| 3.7.4.1  
typing-extensions| 3.7.4.1  
urllib3| 1.25.8  
wcwidth| 0.1.8  
Werkzeug| 0.16.1  
wheel| 0.34.2  
wrapt| 1.11.2  
zipp| 2.1.0  
  
### Python 3.7.6

Package| Version  
---|---  
  
absl-py| 0.9.0  
astor| 0.8.1  
atomicwrites| 1.3.0  
attrs| 19.3.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.8.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2019.11.28  
chardet| 3.0.4  
crcmod| 1.7  
Cython| 0.29.13  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.21.24  
fasteners| 0.15  
freezegun| 0.3.12  
future| 0.17.1  
gast| 0.2.2  
google-api-core| 1.16.0  
google-apitools| 0.5.28  
google-auth| 1.11.0  
google-auth-oauthlib| 0.4.1  
google-cloud-bigquery| 1.17.1  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-pubsub| 1.0.2  
google-pasta| 0.1.8  
google-resumable-media| 0.4.1  
googleapis-common-protos| 1.51.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.24.3  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.12.0  
idna| 2.8  
importlib-metadata| 1.5.0  
joblib| 0.14.1  
Keras-Applications| 1.0.8  
Keras-Preprocessing| 1.1.0  
Markdown| 3.1.1  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 8.2.0  
nltk| 3.4.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.17.3  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 3.1.0  
packaging| 20.1  
pandas| 0.25.2  
pbr| 5.4.4  
Pillow| 6.2.1  
pip| 20.0.2  
pluggy| 0.13.1  
protobuf| 3.11.1  
protorpc| 0.12.0  
py| 1.8.1  
pyarrow| 0.15.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.8  
pydot| 1.4.1  
pymongo| 3.9.0  
pyparsing| 2.4.6  
pytest| 4.6.6  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2019.3  
PyYAML| 3.13  
requests| 2.22.0  
requests-oauthlib| 1.3.0  
rsa| 4.0  
scikit-learn| 0.21.3  
scipy| 1.4.1  
setuptools| 45.1.0  
six| 1.14.0  
soupsieve| 1.9.5  
tensorboard| 2.1.0  
tensorflow-cpu| 2.1.0  
tensorflow-estimator| 2.1.0  
termcolor| 1.1.0  
typing| 3.7.4.1  
typing-extensions| 3.7.4.1  
urllib3| 1.25.8  
wcwidth| 0.1.8  
Werkzeug| 0.16.1  
wheel| 0.34.2  
wrapt| 1.11.2  
zipp| 2.1.0  
  
#### Version 2.18.0

Dataflow workers have the following packages already installed.

### Python 2.7.13

Package| Version  
---|---  
  
absl-py| 0.8.1  
astor| 0.8.0  
atomicwrites| 1.3.0  
attrs| 19.3.0  
avro| 1.8.2  
backports.functools-lru-cache| 1.6.1  
backports.weakref| 1.0.post1  
beautifulsoup4| 4.8.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2019.11.28  
chardet| 3.0.4  
configparser| 4.0.2  
contextlib2| 0.6.0.post1  
crcmod| 1.7  
Cython| 0.29.13  
dill| 0.3.1.1  
docopt| 0.6.2  
enum34| 1.1.6  
fastavro| 0.21.24  
fasteners| 0.15  
funcsigs| 1.0.2  
functools32| 3.2.3.post2  
future| 0.17.1  
futures| 3.3.0  
gast| 0.2.2  
google-api-core| 1.14.3  
google-api-python-client| 1.7.11  
google-apitools| 0.5.28  
google-auth| 1.7.2  
google-auth-httplib2| 0.0.3  
google-auth-oauthlib| 0.4.1  
google-cloud-bigquery| 1.17.1  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-pubsub| 1.0.2  
google-pasta| 0.1.8  
google-python-cloud-debugger| 1.9  
google-resumable-media| 0.4.1  
googleapis-common-protos| 1.6.0  
googledatastore| 7.0.2  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.24.3  
guppy| 0.1.11  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.12.0  
idna| 2.8  
importlib-metadata| 1.2.0  
Keras-Applications| 1.0.8  
Keras-Preprocessing| 1.1.0  
Markdown| 3.1.1  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 5.0.0  
nltk| 3.4.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.16.5  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 2.3.2  
packaging| 19.2  
pandas| 0.24.2  
pathlib2| 2.3.5  
pbr| 5.4.4  
Pillow| 6.2.1  
pip| 19.3.1  
pluggy| 0.13.1  
proto-google-cloud-datastore-v1| 0.90.4  
protobuf| 3.11.1  
protorpc| 0.12.0  
py| 1.8.0  
pyarrow| 0.15.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.7  
pydot| 1.4.1  
pymongo| 3.9.0  
pyparsing| 2.4.5  
pytest| 4.6.6  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2019.3  
PyVCF| 0.6.8  
PyYAML| 3.13  
requests| 2.22.0  
requests-oauthlib| 1.3.0  
rsa| 4.0  
scandir| 1.10.0  
scikit-learn| 0.20.4  
scipy| 1.2.2  
setuptools| 42.0.2  
singledispatch| 3.4.0.3  
six| 1.13.0  
soupsieve| 1.9.5  
tensorboard| 2.0.2  
tensorflow-cpu| 2.1.0rc0  
tensorflow-estimator| 2.0.1  
termcolor| 1.1.0  
typing| 3.6.6  
uritemplate| 3.0.0  
urllib3| 1.25.7  
wcwidth| 0.1.7  
Werkzeug| 0.16.0  
wheel| 0.33.6  
wrapt| 1.11.2  
zipp| 0.6.0  
  
### Python 3.5.9

Package| Version  
---|---  
  
absl-py| 0.8.1  
astor| 0.8.0  
atomicwrites| 1.3.0  
attrs| 19.3.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.8.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2019.11.28  
chardet| 3.0.4  
crcmod| 1.7  
Cython| 0.29.13  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.21.24  
fasteners| 0.15  
future| 0.17.1  
gast| 0.2.2  
google-api-core| 1.14.3  
google-apitools| 0.5.28  
google-auth| 1.7.2  
google-auth-oauthlib| 0.4.1  
google-cloud-bigquery| 1.17.1  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-pubsub| 1.0.2  
google-pasta| 0.1.8  
google-resumable-media| 0.4.1  
googleapis-common-protos| 1.6.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.24.3  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.12.0  
idna| 2.8  
importlib-metadata| 1.2.0  
joblib| 0.14.0  
Keras-Applications| 1.0.8  
Keras-Preprocessing| 1.1.0  
Markdown| 3.1.1  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 8.0.2  
nltk| 3.4.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.17.3  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 3.1.0  
packaging| 19.2  
pandas| 0.25.2  
pathlib2| 2.3.5  
pbr| 5.4.4  
Pillow| 6.2.1  
pip| 19.3.1  
pluggy| 0.13.1  
protobuf| 3.11.1  
protorpc| 0.12.0  
py| 1.8.0  
pyarrow| 0.15.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.7  
pydot| 1.4.1  
pymongo| 3.9.0  
pyparsing| 2.4.5  
pytest| 4.6.6  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2019.3  
PyYAML| 3.13  
requests| 2.22.0  
requests-oauthlib| 1.3.0  
rsa| 4.0  
scikit-learn| 0.21.3  
scipy| 1.3.1  
setuptools| 41.6.0  
six| 1.13.0  
soupsieve| 1.9.5  
tensorboard| 2.0.2  
tensorflow-cpu| 2.1.0rc0  
tensorflow-estimator| 2.0.1  
termcolor| 1.1.0  
urllib3| 1.25.7  
wcwidth| 0.1.7  
Werkzeug| 0.16.0  
wheel| 0.33.6  
wrapt| 1.11.2  
zipp| 0.6.0  
  
### Python 3.6.9

Package| Version  
---|---  
  
absl-py| 0.8.1  
astor| 0.8.0  
atomicwrites| 1.3.0  
attrs| 19.3.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.8.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2019.11.28  
chardet| 3.0.4  
crcmod| 1.7  
Cython| 0.29.13  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.21.24  
fasteners| 0.15  
future| 0.17.1  
gast| 0.2.2  
google-api-core| 1.14.3  
google-apitools| 0.5.28  
google-auth| 1.7.2  
google-auth-oauthlib| 0.4.1  
google-cloud-bigquery| 1.17.1  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-pubsub| 1.0.2  
google-pasta| 0.1.8  
google-resumable-media| 0.4.1  
googleapis-common-protos| 1.6.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.24.3  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.12.0  
idna| 2.8  
importlib-metadata| 1.2.0  
joblib| 0.14.0  
Keras-Applications| 1.0.8  
Keras-Preprocessing| 1.1.0  
Markdown| 3.1.1  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 8.0.2  
nltk| 3.4.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.17.3  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 3.1.0  
packaging| 19.2  
pandas| 0.25.2  
pbr| 5.4.4  
Pillow| 6.2.1  
pip| 19.3.1  
pluggy| 0.13.1  
protobuf| 3.11.1  
protorpc| 0.12.0  
py| 1.8.0  
pyarrow| 0.15.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.7  
pydot| 1.4.1  
pymongo| 3.9.0  
pyparsing| 2.4.5  
pytest| 4.6.6  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2019.3  
PyYAML| 3.13  
requests| 2.22.0  
requests-oauthlib| 1.3.0  
rsa| 4.0  
scikit-learn| 0.21.3  
scipy| 1.3.1  
setuptools| 41.6.0  
six| 1.13.0  
soupsieve| 1.9.5  
tensorboard| 2.0.2  
tensorflow-cpu| 2.1.0rc0  
tensorflow-estimator| 2.0.1  
termcolor| 1.1.0  
urllib3| 1.25.7  
wcwidth| 0.1.7  
Werkzeug| 0.16.0  
wheel| 0.33.6  
wrapt| 1.11.2  
zipp| 0.6.0  
  
### Python 3.7.5

Package| Version  
---|---  
  
absl-py| 0.8.1  
astor| 0.8.0  
atomicwrites| 1.3.0  
attrs| 19.3.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.8.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2019.11.28  
chardet| 3.0.4  
crcmod| 1.7  
Cython| 0.29.13  
dill| 0.3.1.1  
docopt| 0.6.2  
fastavro| 0.21.24  
fasteners| 0.15  
future| 0.17.1  
gast| 0.2.2  
google-api-core| 1.14.3  
google-apitools| 0.5.28  
google-auth| 1.7.2  
google-auth-oauthlib| 0.4.1  
google-cloud-bigquery| 1.17.1  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.1.0  
google-cloud-datastore| 1.7.4  
google-cloud-pubsub| 1.0.2  
google-pasta| 0.1.8  
google-resumable-media| 0.4.1  
googleapis-common-protos| 1.6.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.24.3  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.12.0  
idna| 2.8  
importlib-metadata| 1.2.0  
joblib| 0.14.0  
Keras-Applications| 1.0.8  
Keras-Preprocessing| 1.1.0  
Markdown| 3.1.1  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 8.0.2  
nltk| 3.4.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.17.3  
oauth2client| 3.0.0  
oauthlib| 3.1.0  
opt-einsum| 3.1.0  
packaging| 19.2  
pandas| 0.25.2  
pbr| 5.4.4  
Pillow| 6.2.1  
pip| 19.3.1  
pluggy| 0.13.1  
protobuf| 3.11.1  
protorpc| 0.12.0  
py| 1.8.0  
pyarrow| 0.15.1  
pyasn1| 0.4.8  
pyasn1-modules| 0.2.7  
pydot| 1.4.1  
pymongo| 3.9.0  
pyparsing| 2.4.5  
pytest| 4.6.6  
python-dateutil| 2.8.1  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2019.3  
PyYAML| 3.13  
requests| 2.22.0  
requests-oauthlib| 1.3.0  
rsa| 4.0  
scikit-learn| 0.21.3  
scipy| 1.3.1  
setuptools| 41.6.0  
six| 1.13.0  
soupsieve| 1.9.5  
tensorboard| 2.0.2  
tensorflow-cpu| 2.1.0rc0  
tensorflow-estimator| 2.0.1  
termcolor| 1.1.0  
urllib3| 1.25.7  
wcwidth| 0.1.7  
Werkzeug| 0.16.0  
wheel| 0.33.6  
wrapt| 1.11.2  
zipp| 0.6.0  
  
#### Version 2.17.0

Dataflow workers have the following packages already installed.

### Python 2.7.13

Package| Version  
---|---  
  
absl-py| 0.8.1  
astor| 0.8.0  
atomicwrites| 1.3.0  
attrs| 19.3.0  
avro| 1.8.2  
backports.functools-lru-cache| 1.6.1  
backports.weakref| 1.0.post1  
beautifulsoup4| 4.8.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2019.9.11  
chardet| 3.0.4  
configparser| 4.0.2  
contextlib2| 0.6.0.post1  
crcmod| 1.7  
Cython| 0.29.13  
dill| 0.3.0  
docopt| 0.6.2  
enum34| 1.1.6  
fastavro| 0.21.24  
fasteners| 0.15  
funcsigs| 1.0.2  
functools32| 3.2.3.post2  
future| 0.17.1  
futures| 3.3.0  
gast| 0.2.2  
google-api-core| 1.14.3  
google-api-python-client| 1.7.11  
google-apitools| 0.5.28  
google-auth| 1.7.0  
google-auth-httplib2| 0.0.3  
google-cloud-bigquery| 1.17.1  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.0.3  
google-cloud-datastore| 1.7.4  
google-cloud-pubsub| 1.0.2  
google-pasta| 0.1.8  
google-python-cloud-debugger| 1.9  
google-resumable-media| 0.4.1  
googleapis-common-protos| 1.6.0  
googledatastore| 7.0.2  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.24.3  
guppy| 0.1.11  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.12.0  
idna| 2.8  
importlib-metadata| 0.23  
Keras-Applications| 1.0.8  
Keras-Preprocessing| 1.1.0  
Markdown| 3.1.1  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 5.0.0  
nltk| 3.4.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.16.5  
oauth2client| 3.0.0  
opt-einsum| 2.3.2  
packaging| 19.2  
pandas| 0.24.2  
pathlib2| 2.3.5  
pbr| 5.4.3  
Pillow| 6.2.1  
pip| 19.3.1  
pluggy| 0.13.0  
proto-google-cloud-datastore-v1| 0.90.4  
protobuf| 3.10.0  
protorpc| 0.12.0  
py| 1.8.0  
pyarrow| 0.15.1  
pyasn1| 0.4.7  
pyasn1-modules| 0.2.7  
pydot| 1.4.1  
pymongo| 3.9.0  
pyparsing| 2.4.4  
pytest| 4.6.6  
python-dateutil| 2.8.0  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2019.3  
PyVCF| 0.6.8  
PyYAML| 3.13  
requests| 2.22.0  
rsa| 4.0  
scandir| 1.10.0  
scikit-learn| 0.20.4  
scipy| 1.2.2  
setuptools| 41.6.0  
singledispatch| 3.4.0.3  
six| 1.13.0  
soupsieve| 1.9.5  
tensorboard| 1.15.0  
tensorflow-cpu| 1.15.0  
tensorflow-estimator| 1.15.1  
termcolor| 1.1.0  
typing| 3.6.6  
uritemplate| 3.0.0  
urllib3| 1.25.6  
wcwidth| 0.1.7  
Werkzeug| 0.16.0  
wheel| 0.33.6  
wrapt| 1.11.2  
zipp| 0.6.0  
  
### Python 3.5.7

Package| Version  
---|---  
  
absl-py| 0.8.1  
astor| 0.8.0  
atomicwrites| 1.3.0  
attrs| 19.3.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.8.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2019.9.11  
chardet| 3.0.4  
crcmod| 1.7  
Cython| 0.29.13  
dill| 0.3.0  
docopt| 0.6.2  
fastavro| 0.21.24  
fasteners| 0.15  
future| 0.17.1  
gast| 0.2.2  
google-api-core| 1.14.3  
google-apitools| 0.5.28  
google-auth| 1.7.0  
google-cloud-bigquery| 1.17.1  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.0.3  
google-cloud-datastore| 1.7.4  
google-cloud-pubsub| 1.0.2  
google-pasta| 0.1.8  
google-resumable-media| 0.4.1  
googleapis-common-protos| 1.6.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.24.3  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.12.0  
idna| 2.8  
importlib-metadata| 0.23  
joblib| 0.14.0  
Keras-Applications| 1.0.8  
Keras-Preprocessing| 1.1.0  
Markdown| 3.1.1  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 7.2.0  
nltk| 3.4.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.17.3  
oauth2client| 3.0.0  
opt-einsum| 3.1.0  
packaging| 19.2  
pandas| 0.25.2  
pathlib2| 2.3.5  
pbr| 5.4.3  
Pillow| 6.2.1  
pip| 19.3.1  
pluggy| 0.13.0  
protobuf| 3.10.0  
protorpc| 0.12.0  
py| 1.8.0  
pyarrow| 0.15.1  
pyasn1| 0.4.7  
pyasn1-modules| 0.2.7  
pydot| 1.4.1  
pymongo| 3.9.0  
pyparsing| 2.4.4  
pytest| 4.6.6  
python-dateutil| 2.8.0  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2019.3  
PyYAML| 3.13  
requests| 2.22.0  
rsa| 4.0  
scikit-learn| 0.21.3  
scipy| 1.3.1  
setuptools| 41.6.0  
six| 1.13.0  
soupsieve| 1.9.5  
tensorboard| 1.15.0  
tensorflow-cpu| 1.15.0  
tensorflow-estimator| 1.15.1  
termcolor| 1.1.0  
urllib3| 1.25.6  
wcwidth| 0.1.7  
Werkzeug| 0.16.0  
wheel| 0.33.6  
wrapt| 1.11.2  
zipp| 0.6.0  
  
### Python 3.6.9

Package| Version  
---|---  
  
absl-py| 0.8.1  
astor| 0.8.0  
atomicwrites| 1.3.0  
attrs| 19.3.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.8.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2019.9.11  
chardet| 3.0.4  
crcmod| 1.7  
Cython| 0.29.13  
dill| 0.3.0  
docopt| 0.6.2  
fastavro| 0.21.24  
fasteners| 0.15  
future| 0.17.1  
gast| 0.2.2  
google-api-core| 1.14.3  
google-apitools| 0.5.28  
google-auth| 1.7.0  
google-cloud-bigquery| 1.17.1  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.0.3  
google-cloud-datastore| 1.7.4  
google-cloud-pubsub| 1.0.2  
google-pasta| 0.1.8  
google-resumable-media| 0.4.1  
googleapis-common-protos| 1.6.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.24.3  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.12.0  
idna| 2.8  
importlib-metadata| 0.23  
joblib| 0.14.0  
Keras-Applications| 1.0.8  
Keras-Preprocessing| 1.1.0  
Markdown| 3.1.1  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 7.2.0  
nltk| 3.4.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.17.3  
oauth2client| 3.0.0  
opt-einsum| 3.1.0  
packaging| 19.2  
pandas| 0.25.2  
pbr| 5.4.3  
Pillow| 6.2.1  
pip| 19.3.1  
pluggy| 0.13.0  
protobuf| 3.10.0  
protorpc| 0.12.0  
py| 1.8.0  
pyarrow| 0.15.1  
pyasn1| 0.4.7  
pyasn1-modules| 0.2.7  
pydot| 1.4.1  
pymongo| 3.9.0  
pyparsing| 2.4.4  
pytest| 4.6.6  
python-dateutil| 2.8.0  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2019.3  
PyYAML| 3.13  
requests| 2.22.0  
rsa| 4.0  
scikit-learn| 0.21.3  
scipy| 1.3.1  
setuptools| 41.4.0  
six| 1.13.0  
soupsieve| 1.9.5  
tensorboard| 1.15.0  
tensorflow-cpu| 1.15.0  
tensorflow-estimator| 1.15.1  
termcolor| 1.1.0  
urllib3| 1.25.6  
wcwidth| 0.1.7  
Werkzeug| 0.16.0  
wheel| 0.33.6  
wrapt| 1.11.2  
zipp| 0.6.0  
  
### Python 3.7.4

Package| Version  
---|---  
  
absl-py| 0.8.1  
astor| 0.8.0  
atomicwrites| 1.3.0  
attrs| 19.3.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.8.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2019.9.11  
chardet| 3.0.4  
crcmod| 1.7  
Cython| 0.29.13  
dill| 0.3.0  
docopt| 0.6.2  
fastavro| 0.21.24  
fasteners| 0.15  
future| 0.17.1  
gast| 0.2.2  
google-api-core| 1.14.3  
google-apitools| 0.5.28  
google-auth| 1.7.0  
google-cloud-bigquery| 1.17.1  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.0.3  
google-cloud-datastore| 1.7.4  
google-cloud-pubsub| 1.0.2  
google-pasta| 0.1.8  
google-resumable-media| 0.4.1  
googleapis-common-protos| 1.6.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.24.3  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.12.0  
idna| 2.8  
importlib-metadata| 0.23  
joblib| 0.14.0  
Keras-Applications| 1.0.8  
Keras-Preprocessing| 1.1.0  
Markdown| 3.1.1  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 7.2.0  
nltk| 3.4.5  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.17.3  
oauth2client| 3.0.0  
opt-einsum| 3.1.0  
packaging| 19.2  
pandas| 0.25.2  
pbr| 5.4.3  
Pillow| 6.2.1  
pip| 19.3.1  
pluggy| 0.13.0  
protobuf| 3.10.0  
protorpc| 0.12.0  
py| 1.8.0  
pyarrow| 0.15.1  
pyasn1| 0.4.7  
pyasn1-modules| 0.2.7  
pydot| 1.4.1  
pymongo| 3.9.0  
pyparsing| 2.4.4  
pytest| 4.6.6  
python-dateutil| 2.8.0  
python-gflags| 3.1.2  
python-snappy| 0.5.4  
pytz| 2019.3  
PyYAML| 3.13  
requests| 2.22.0  
rsa| 4.0  
scikit-learn| 0.21.3  
scipy| 1.3.1  
setuptools| 41.4.0  
six| 1.13.0  
soupsieve| 1.9.5  
tensorboard| 1.15.0  
tensorflow-cpu| 1.15.0  
tensorflow-estimator| 1.15.1  
termcolor| 1.1.0  
urllib3| 1.25.6  
wcwidth| 0.1.7  
Werkzeug| 0.16.0  
wheel| 0.33.6  
wrapt| 1.11.2  
zipp| 0.6.0  
  
#### Version 2.16.0

Dataflow workers have the following packages already installed.

### Python 2.7.13

Package| Version  
---|---  
  
absl-py| 0.8.1  
astor| 0.8.0  
atomicwrites| 1.3.0  
attrs| 19.2.0  
avro| 1.8.2  
backports.functools-lru-cache| 1.5  
backports.weakref| 1.0.post1  
beautifulsoup4| 4.7.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2019.9.11  
chardet| 3.0.4  
configparser| 4.0.2  
contextlib2| 0.6.0  
crcmod| 1.7  
Cython| 0.29.10  
dill| 0.3.0  
docopt| 0.6.2  
enum34| 1.1.6  
fastavro| 0.21.24  
fasteners| 0.15  
funcsigs| 1.0.2  
functools32| 3.2.3.post2  
future| 0.17.1  
futures| 3.2.0  
gast| 0.2.2  
google-api-core| 1.14.3  
google-api-python-client| 1.7.11  
google-apitools| 0.5.28  
google-auth| 1.6.3  
google-auth-httplib2| 0.0.3  
google-cloud-bigquery| 1.17.0  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.0.3  
google-cloud-datastore| 1.7.4  
google-cloud-pubsub| 1.0.0  
google-pasta| 0.1.7  
google-python-cloud-debugger| 1.9  
google-resumable-media| 0.4.1  
googleapis-common-protos| 1.6.0  
googledatastore| 7.0.2  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.23.0  
guppy| 0.1.10  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.12.0  
idna| 2.8  
importlib-metadata| 0.23  
Keras-Applications| 1.0.8  
Keras-Preprocessing| 1.1.0  
Markdown| 3.1.1  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 5.0.0  
nltk| 3.4.3  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.16.5  
oauth2client| 3.0.0  
opt-einsum| 2.3.2  
pandas| 0.24.2  
pathlib2| 2.3.5  
pbr| 5.4.3  
Pillow| 6.0.0  
pip| 19.2.3  
pluggy| 0.13.0  
proto-google-cloud-datastore-v1| 0.90.4  
protobuf| 3.9.1  
protorpc| 0.12.0  
py| 1.8.0  
pyarrow| 0.14.1  
pyasn1| 0.4.7  
pyasn1-modules| 0.2.6  
pydot| 1.4.1  
pymongo| 3.8.0  
pyparsing| 2.4.2  
pytest| 4.4.0  
python-dateutil| 2.8.0  
python-gflags| 3.0.6  
python-snappy| 0.5.4  
pytz| 2019.2  
PyVCF| 0.6.8  
PyYAML| 3.13  
requests| 2.22.0  
rsa| 4.0  
scandir| 1.10.0  
scikit-learn| 0.20.3  
scipy| 1.2.2  
setuptools| 41.4.0  
singledispatch| 3.4.0.3  
six| 1.12.0  
soupsieve| 1.9.4  
tensorboard| 1.15.0  
tensorflow-cpu| 1.15.0rc3  
tensorflow-estimator| 1.15.1  
termcolor| 1.1.0  
typing| 3.6.6  
uritemplate| 3.0.0  
urllib3| 1.25.6  
Werkzeug| 0.16.0  
wheel| 0.33.6  
wrapt| 1.11.2  
zipp| 0.6.0  
  
### Python 3.5.7

Package| Version  
---|---  
  
absl-py| 0.8.1  
astor| 0.8.0  
atomicwrites| 1.3.0  
attrs| 19.2.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.7.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2019.9.11  
chardet| 3.0.4  
crcmod| 1.7  
Cython| 0.29.10  
dill| 0.3.0  
docopt| 0.6.2  
fastavro| 0.21.24  
fasteners| 0.15  
future| 0.17.1  
gast| 0.2.2  
google-api-core| 1.14.3  
google-apitools| 0.5.28  
google-auth| 1.6.3  
google-cloud-bigquery| 1.17.0  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.0.3  
google-cloud-datastore| 1.7.4  
google-cloud-pubsub| 1.0.0  
google-pasta| 0.1.7  
google-resumable-media| 0.4.1  
googleapis-common-protos| 1.6.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.23.0  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.12.0  
idna| 2.8  
importlib-metadata| 0.23  
Keras-Applications| 1.0.8  
Keras-Preprocessing| 1.1.0  
Markdown| 3.1.1  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 7.2.0  
nltk| 3.4.3  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.17.2  
oauth2client| 3.0.0  
opt-einsum| 3.1.0  
pandas| 0.24.2  
pathlib2| 2.3.5  
pbr| 5.4.3  
Pillow| 6.0.0  
pip| 19.2.3  
pluggy| 0.13.0  
protobuf| 3.9.1  
protorpc| 0.12.0  
py| 1.8.0  
pyarrow| 0.14.1  
pyasn1| 0.4.7  
pyasn1-modules| 0.2.6  
pydot| 1.4.1  
pymongo| 3.8.0  
pyparsing| 2.4.2  
pytest| 4.4.0  
python-dateutil| 2.8.0  
python-gflags| 3.0.6  
python-snappy| 0.5.4  
pytz| 2019.2  
PyYAML| 3.13  
requests| 2.22.0  
rsa| 4.0  
scikit-learn| 0.20.3  
scipy| 1.3.1  
setuptools| 41.2.0  
six| 1.12.0  
soupsieve| 1.9.4  
tensorboard| 1.15.0  
tensorflow-cpu| 1.15.0rc3  
tensorflow-estimator| 1.15.1  
termcolor| 1.1.0  
urllib3| 1.25.6  
Werkzeug| 0.16.0  
wheel| 0.33.6  
wrapt| 1.11.2  
zipp| 0.6.0  
  
### Python 3.6.9

Package| Version  
---|---  
  
absl-py| 0.8.1  
astor| 0.8.0  
atomicwrites| 1.3.0  
attrs| 19.2.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.7.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2019.9.11  
chardet| 3.0.4  
crcmod| 1.7  
Cython| 0.29.10  
dill| 0.3.0  
docopt| 0.6.2  
fastavro| 0.21.24  
fasteners| 0.15  
future| 0.17.1  
gast| 0.2.2  
google-api-core| 1.14.3  
google-apitools| 0.5.28  
google-auth| 1.6.3  
google-cloud-bigquery| 1.17.0  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.0.3  
google-cloud-datastore| 1.7.4  
google-cloud-pubsub| 1.0.0  
google-pasta| 0.1.7  
google-resumable-media| 0.4.1  
googleapis-common-protos| 1.6.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.23.0  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.12.0  
idna| 2.8  
importlib-metadata| 0.23  
Keras-Applications| 1.0.8  
Keras-Preprocessing| 1.1.0  
Markdown| 3.1.1  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 7.2.0  
nltk| 3.4.3  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.17.2  
oauth2client| 3.0.0  
opt-einsum| 3.1.0  
pandas| 0.24.2  
pbr| 5.4.3  
Pillow| 6.0.0  
pip| 19.2.3  
pluggy| 0.13.0  
protobuf| 3.9.1  
protorpc| 0.12.0  
py| 1.8.0  
pyarrow| 0.14.1  
pyasn1| 0.4.7  
pyasn1-modules| 0.2.6  
pydot| 1.4.1  
pymongo| 3.8.0  
pyparsing| 2.4.2  
pytest| 4.4.0  
python-dateutil| 2.8.0  
python-gflags| 3.0.6  
python-snappy| 0.5.4  
pytz| 2019.2  
PyYAML| 3.13  
requests| 2.22.0  
rsa| 4.0  
scikit-learn| 0.20.3  
scipy| 1.3.1  
setuptools| 41.2.0  
six| 1.12.0  
soupsieve| 1.9.4  
tensorboard| 1.15.0  
tensorflow-cpu| 1.15.0rc3  
tensorflow-estimator| 1.15.1  
termcolor| 1.1.0  
urllib3| 1.25.6  
Werkzeug| 0.16.0  
wheel| 0.33.6  
wrapt| 1.11.2  
zipp| 0.6.0  
  
### Python 3.7.4

Package| Version  
---|---  
  
absl-py| 0.8.1  
astor| 0.8.0  
atomicwrites| 1.3.0  
attrs| 19.2.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.7.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2019.9.11  
chardet| 3.0.4  
crcmod| 1.7  
Cython| 0.29.10  
dill| 0.3.0  
docopt| 0.6.2  
fastavro| 0.21.24  
fasteners| 0.15  
future| 0.17.1  
gast| 0.2.2  
google-api-core| 1.14.3  
google-apitools| 0.5.28  
google-auth| 1.6.3  
google-cloud-bigquery| 1.17.0  
google-cloud-bigtable| 1.0.0  
google-cloud-core| 1.0.3  
google-cloud-datastore| 1.7.4  
google-cloud-pubsub| 1.0.0  
google-pasta| 0.1.7  
google-resumable-media| 0.4.1  
googleapis-common-protos| 1.6.0  
grpc-google-iam-v1| 0.12.3  
grpcio| 1.23.0  
h5py| 2.10.0  
hdfs| 2.5.8  
httplib2| 0.12.0  
idna| 2.8  
importlib-metadata| 0.23  
Keras-Applications| 1.0.8  
Keras-Preprocessing| 1.1.0  
Markdown| 3.1.1  
mock| 2.0.0  
monotonic| 1.5  
more-itertools| 7.2.0  
nltk| 3.4.3  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.17.2  
oauth2client| 3.0.0  
opt-einsum| 3.1.0  
pandas| 0.24.2  
pbr| 5.4.3  
Pillow| 6.0.0  
pip| 19.2.3  
pluggy| 0.13.0  
protobuf| 3.9.1  
protorpc| 0.12.0  
py| 1.8.0  
pyarrow| 0.14.1  
pyasn1| 0.4.7  
pyasn1-modules| 0.2.6  
pydot| 1.4.1  
pymongo| 3.8.0  
pyparsing| 2.4.2  
pytest| 4.4.0  
python-dateutil| 2.8.0  
python-gflags| 3.0.6  
python-snappy| 0.5.4  
pytz| 2019.2  
PyYAML| 3.13  
requests| 2.22.0  
rsa| 4.0  
scikit-learn| 0.20.3  
scipy| 1.3.1  
setuptools| 41.2.0  
six| 1.12.0  
soupsieve| 1.9.4  
tensorboard| 1.15.0  
tensorflow-cpu| 1.15.0rc3  
tensorflow-estimator| 1.15.1  
termcolor| 1.1.0  
urllib3| 1.25.6  
Werkzeug| 0.16.0  
wheel| 0.33.6  
wrapt| 1.11.2  
zipp| 0.6.0  
  
#### Version 2.15.0

Dataflow workers have the following packages already installed.

### Python 2.7.13

Package| Version  
---|---  
  
absl-py| 0.7.1  
astor| 0.8.0  
avro| 1.8.2  
backports.functools-lru-cache| 1.5  
backports.weakref| 1.0.post1  
beautifulsoup4| 4.7.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2019.6.16  
chardet| 3.0.4  
crcmod| 1.7  
Cython| 0.29.10  
dill| 0.2.9  
docopt| 0.6.2  
enum34| 1.1.6  
fastavro| 0.21.24  
fasteners| 0.15  
funcsigs| 1.0.2  
future| 0.17.1  
futures| 3.2.0  
gast| 0.2.2  
google-api-core| 1.14.0  
google-api-python-client| 1.7.10  
google-apitools| 0.5.28  
google-auth| 1.6.3  
google-auth-httplib2| 0.0.3  
google-cloud-bigquery| 1.17.0  
google-cloud-bigtable| 0.32.1  
google-cloud-core| 1.0.2  
google-cloud-datastore| 1.7.4  
google-cloud-pubsub| 0.39.1  
google-pasta| 0.1.7  
google-python-cloud-debugger| 1.9  
google-resumable-media| 0.3.2  
googleapis-common-protos| 1.6.0  
googledatastore| 7.0.2  
grpc-google-iam-v1| 0.11.4  
grpcio| 1.22.0  
guppy| 0.1.10  
h5py| 2.9.0  
hdfs| 2.5.8  
httplib2| 0.12.0  
idna| 2.8  
Keras-Applications| 1.0.8  
Keras-Preprocessing| 1.1.0  
Markdown| 3.1.1  
mock| 2.0.0  
monotonic| 1.5  
nltk| 3.4.3  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.16.4  
oauth2client| 3.0.0  
pandas| 0.24.2  
pbr| 5.4.1  
Pillow| 6.0.0  
pip| 19.2.1  
proto-google-cloud-datastore-v1| 0.90.4  
protobuf| 3.9.0  
protorpc| 0.12.0  
pyarrow| 0.14.1  
pyasn1| 0.4.5  
pyasn1-modules| 0.2.5  
pydot| 1.4.1  
pymongo| 3.8.0  
pyparsing| 2.4.1.1  
python-dateutil| 2.8.0  
python-gflags| 3.0.6  
python-snappy| 0.5.4  
pytz| 2019.1  
PyVCF| 0.6.8  
PyYAML| 3.13  
requests| 2.22.0  
rsa| 4.0  
scikit-learn| 0.20.3  
scipy| 1.2.2  
setuptools| 41.0.1  
singledispatch| 3.4.0.3  
six| 1.12.0  
soupsieve| 1.9.2  
tensorboard| 1.14.0  
tensorflow| 1.14.0  
tensorflow-estimator| 1.14.0  
termcolor| 1.1.0  
typing| 3.6.6  
uritemplate| 3.0.0  
urllib3| 1.25.3  
Werkzeug| 0.15.5  
wheel| 0.33.4  
wrapt| 1.11.2  
  
### Python 3.5.7

Package| Version  
---|---  
  
absl-py| 0.7.1  
astor| 0.8.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.7.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2019.6.16  
chardet| 3.0.4  
crcmod| 1.7  
Cython| 0.29.10  
dill| 0.2.9  
docopt| 0.6.2  
fastavro| 0.21.24  
fasteners| 0.15  
future| 0.17.1  
gast| 0.2.2  
google-api-core| 1.14.0  
google-apitools| 0.5.28  
google-auth| 1.6.3  
google-cloud-bigquery| 1.17.0  
google-cloud-bigtable| 0.32.1  
google-cloud-core| 1.0.2  
google-cloud-datastore| 1.7.4  
google-cloud-pubsub| 0.39.1  
google-pasta| 0.1.7  
google-resumable-media| 0.3.2  
googleapis-common-protos| 1.6.0  
grpc-google-iam-v1| 0.11.4  
grpcio| 1.22.0  
h5py| 2.9.0  
hdfs| 2.5.8  
httplib2| 0.12.0  
idna| 2.8  
Keras-Applications| 1.0.8  
Keras-Preprocessing| 1.1.0  
Markdown| 3.1.1  
mock| 2.0.0  
monotonic| 1.5  
nltk| 3.4.3  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.16.4  
oauth2client| 3.0.0  
pandas| 0.24.2  
pbr| 5.4.1  
Pillow| 6.0.0  
pip| 19.2.1  
protobuf| 3.9.0  
protorpc| 0.12.0  
pyarrow| 0.14.1  
pyasn1| 0.4.5  
pyasn1-modules| 0.2.5  
pydot| 1.4.1  
pymongo| 3.8.0  
pyparsing| 2.4.1.1  
python-dateutil| 2.8.0  
python-gflags| 3.0.6  
python-snappy| 0.5.4  
pytz| 2019.1  
PyYAML| 3.13  
requests| 2.22.0  
rsa| 4.0  
scikit-learn| 0.20.3  
scipy| 1.2.2  
setuptools| 41.0.1  
six| 1.12.0  
soupsieve| 1.9.2  
tensorboard| 1.14.0  
tensorflow| 1.14.0  
tensorflow-estimator| 1.14.0  
termcolor| 1.1.0  
urllib3| 1.25.3  
Werkzeug| 0.15.5  
wheel| 0.33.4  
wrapt| 1.11.2  
  
### Python 3.6.9

Package| Version  
---|---  
  
absl-py| 0.7.1  
astor| 0.8.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.7.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2019.6.16  
chardet| 3.0.4  
crcmod| 1.7  
Cython| 0.29.10  
dill| 0.2.9  
docopt| 0.6.2  
fastavro| 0.21.24  
fasteners| 0.15  
future| 0.17.1  
gast| 0.2.2  
google-api-core| 1.14.0  
google-apitools| 0.5.28  
google-auth| 1.6.3  
google-cloud-bigquery| 1.17.0  
google-cloud-bigtable| 0.32.1  
google-cloud-core| 1.0.2  
google-cloud-datastore| 1.7.4  
google-cloud-pubsub| 0.39.1  
google-pasta| 0.1.7  
google-resumable-media| 0.3.2  
googleapis-common-protos| 1.6.0  
grpc-google-iam-v1| 0.11.4  
grpcio| 1.22.0  
h5py| 2.9.0  
hdfs| 2.5.8  
httplib2| 0.12.0  
idna| 2.8  
Keras-Applications| 1.0.8  
Keras-Preprocessing| 1.1.0  
Markdown| 3.1.1  
mock| 2.0.0  
monotonic| 1.5  
nltk| 3.4.3  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.16.4  
oauth2client| 3.0.0  
pandas| 0.24.2  
pbr| 5.4.1  
Pillow| 6.0.0  
pip| 19.2.1  
protobuf| 3.9.0  
protorpc| 0.12.0  
pyarrow| 0.14.1  
pyasn1| 0.4.5  
pyasn1-modules| 0.2.5  
pydot| 1.4.1  
pymongo| 3.8.0  
pyparsing| 2.4.1.1  
python-dateutil| 2.8.0  
python-gflags| 3.0.6  
python-snappy| 0.5.4  
pytz| 2019.1  
PyYAML| 3.13  
requests| 2.22.0  
rsa| 4.0  
scikit-learn| 0.20.3  
scipy| 1.2.2  
setuptools| 41.0.1  
six| 1.12.0  
soupsieve| 1.9.2  
tensorboard| 1.14.0  
tensorflow| 1.14.0  
tensorflow-estimator| 1.14.0  
termcolor| 1.1.0  
urllib3| 1.25.3  
Werkzeug| 0.15.5  
wheel| 0.33.4  
wrapt| 1.11.2  
  
### Python 3.7.4

Package| Version  
---|---  
  
absl-py| 0.7.1  
astor| 0.8.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.7.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2019.6.16  
chardet| 3.0.4  
crcmod| 1.7  
Cython| 0.29.10  
dill| 0.2.9  
docopt| 0.6.2  
fastavro| 0.21.24  
fasteners| 0.15  
future| 0.17.1  
gast| 0.2.2  
google-api-core| 1.14.0  
google-apitools| 0.5.28  
google-auth| 1.6.3  
google-cloud-bigquery| 1.17.0  
google-cloud-bigtable| 0.32.1  
google-cloud-core| 1.0.2  
google-cloud-datastore| 1.7.4  
google-cloud-pubsub| 0.39.1  
google-pasta| 0.1.7  
google-resumable-media| 0.3.2  
googleapis-common-protos| 1.6.0  
grpc-google-iam-v1| td>0.11.4  
grpcio| 1.22.0  
h5py| 2.9.0  
hdfs| 2.5.8  
httplib2| 0.12.0  
idna| 2.8  
Keras-Applications| 1.0.8  
Keras-Preprocessing| 1.1.0  
Markdown| 3.1.1  
mock| 2.0.0  
monotonic| 1.5  
nltk| 3.4.3  
nose| 1.3.7  
nose-xunitmp| 0.4.1  
numpy| 1.16.4  
oauth2client| 3.0.0  
pandas| 0.24.2  
pbr| 5.4.1  
Pillow| 6.0.0  
pip| 19.2.1  
protobuf| 3.9.0  
protorpc| 0.12.0  
pyarrow| 0.14.1  
pyasn1| 0.4.5  
pyasn1-modules| 0.2.5  
pydot| 1.4.1  
pymongo| 3.8.0  
pyparsing| 2.4.1.1  
python-dateutil| 2.8.0  
python-gflags| 3.0.6  
python-snappy| 0.5.4  
pytz| 2019.1  
PyYAML| 3.13  
requests| 2.22.0  
rsa| 4.0  
scikit-learn| 0.20.3  
scipy| 1.2.2  
setuptools| 41.0.1  
six| 1.12.0  
soupsieve| 1.9.2  
tensorboard| 1.14.0  
tensorflow| 1.14.0  
tensorflow-estimator| 1.14.0  
termcolor| 1.1.0  
urllib3| 1.25.3  
Werkzeug| 0.15.5  
wheel| 0.33.4  
wrapt| 1.11.2  
  
#### Version 2.14.0

Dataflow workers have the following packages already installed.

### Python 2.7.13

Package| Version  
---|---  
  
absl-py| 0.7.1  
astor| 0.8.0  
avro| 1.8.2  
backports.functools-lru-cache| 1.5  
backports.weakref| 1.0.post1  
beautifulsoup4| 4.7.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2019.6.16  
chardet| 3.0.4  
crcmod| 1.7  
Cython| 0.29.10  
dill| 0.2.9  
docopt| 0.6.2  
enum34| 1.1.6  
fastavro| 0.21.24  
fasteners| 0.15  
funcsigs| 1.0.2  
future| 0.17.1  
futures| 3.2.0  
gast| 0.2.2  
google-api-core| 1.12.0  
google-api-python-client| 1.7.9  
google-apitools| 0.5.28  
google-auth| 1.6.3  
google-auth-httplib2| 0.0.3  
google-cloud-bigquery| 1.6.0  
google-cloud-bigtable| 0.32.1  
google-cloud-core| 0.29.1  
google-cloud-datastore| 1.7.4  
google-cloud-pubsub| 0.39.1  
google-pasta| 0.1.7  
google-python-cloud-debugger| 1.9  
google-resumable-media| 0.3.2  
googleapis-common-protos| 1.6.0  
googledatastore| 7.0.2  
grpc-google-iam-v1| 0.11.4  
grpcio| 1.21.1  
guppy| 0.1.10  
h5py| 2.9.0  
hdfs| 2.5.6  
httplib2| 0.12.0  
idna| 2.8  
Keras-Applications| 1.0.8  
Keras-Preprocessing| 1.1.0  
Markdown| 3.1.1  
mock| 2.0.0  
monotonic| 1.5  
nltk| 3.4.3  
nose| 1.3.7  
numpy| 1.16.4  
oauth2client| 3.0.0  
pandas| 0.24.2  
pbr| 5.3.0  
Pillow| 6.0.0  
pip| 19.1.1  
proto-google-cloud-datastore-v1| 0.90.4  
protobuf| 3.8.0  
protorpc| 0.12.0  
pyarrow| 0.13.0  
pyasn1| 0.4.5  
pyasn1-modules| 0.2.5  
pydot| 1.4.1  
pymongo| 3.8.0  
pyparsing| 2.4.0  
python-dateutil| 2.8.0  
python-gflags| 3.0.6  
python-snappy| 0.5.4  
pytz| 2019.1  
PyVCF| 0.6.8  
PyYAML| 3.13  
requests| 2.22.0  
rsa| 4.0  
scikit-learn| 0.20.3  
scipy| 1.2.2  
setuptools| 41.0.1  
singledispatch| 3.4.0.3  
six| 1.12.0  
soupsieve| 1.9.1  
tensorboard| 1.14.0  
tensorflow| 1.14.0  
tensorflow-estimator| 1.14.0  
termcolor| 1.1.0  
typing| 3.6.6  
uritemplate| 3.0.0  
urllib3| 1.25.3  
Werkzeug| 0.15.4  
wheel| 0.33.4  
wrapt| 1.11.2  
  
### Python 3.5.7

Package| Version  
---|---  
  
absl-py| 0.7.1  
astor| 0.8.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.7.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2019.6.16  
chardet| 3.0.4  
crcmod| 1.7  
Cython| 0.29.10  
dill| 0.2.9  
docopt| 0.6.2  
fastavro| 0.21.24  
fasteners| 0.15  
future| 0.17.1  
gast| 0.2.2  
google-api-core| 1.12.0  
google-apitools| 0.5.28  
google-auth| 1.6.3  
google-cloud-bigquery| 1.6.0  
google-cloud-bigtable| 0.32.1  
google-cloud-core| 0.29.1  
google-cloud-datastore| 1.7.4  
google-cloud-pubsub| 0.39.1  
google-pasta| 0.1.7  
google-resumable-media| 0.3.2  
googleapis-common-protos| 1.6.0  
grpc-google-iam-v1| 0.11.4  
grpcio| 1.21.1  
h5py| 2.9.0  
hdfs| 2.5.6  
httplib2| 0.12.0  
idna| 2.8  
Keras-Applications| 1.0.8  
Keras-Preprocessing| 1.1.0  
Markdown| 3.1.1  
mock| 2.0.0  
monotonic| 1.5  
nltk| 3.4.3  
nose| 1.3.7  
numpy| 1.16.4  
oauth2client| 3.0.0  
pandas| 0.24.2  
pbr| 5.3.0  
Pillow| 6.0.0  
pip| 19.1.1  
protobuf| 3.8.0  
protorpc| 0.12.0  
pyarrow| 0.13.0  
pyasn1| 0.4.5  
pyasn1-modules| 0.2.5  
pydot| 1.4.1  
pymongo| 3.8.0  
pyparsing| 2.4.0  
python-dateutil| 2.8.0  
python-gflags| 3.0.6  
python-snappy| 0.5.4  
pytz| 2019.1  
PyYAML| 3.13  
requests| 2.22.0  
rsa| 4.0  
scikit-learn| 0.20.3  
scipy| 1.2.2  
setuptools| 41.0.1  
six| 1.12.0  
soupsieve| 1.9.1  
tensorboard| 1.14.0  
tensorflow| 1.14.0  
tensorflow-estimator| 1.14.0  
termcolor| 1.1.0  
urllib3| 1.25.3  
Werkzeug| 0.15.4  
wheel| 0.33.4  
wrapt| 1.11.2  
  
### Python 3.6.8

Package| Version  
---|---  
  
absl-py| 0.7.1  
astor| 0.8.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.7.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2019.6.16  
chardet| 3.0.4  
crcmod| 1.7  
Cython| 0.29.10  
dill| 0.2.9  
docopt| 0.6.2  
fastavro| 0.21.24  
fasteners| 0.15  
future| 0.17.1  
gast| 0.2.2  
google-api-core| 1.12.0  
google-apitools| 0.5.28  
google-auth| 1.6.3  
google-cloud-bigquery| 1.6.0  
google-cloud-bigtable| 0.32.1  
google-cloud-core| 0.29.1  
google-cloud-datastore| 1.7.4  
google-cloud-pubsub| 0.39.1  
google-pasta| 0.1.7  
google-resumable-media| 0.3.2  
googleapis-common-protos| 1.6.0  
grpc-google-iam-v1| 0.11.4  
grpcio| 1.21.1  
h5py| 2.9.0  
hdfs| 2.5.6  
httplib2| 0.12.0  
idna| 2.8  
Keras-Applications| 1.0.8  
Keras-Preprocessing| 1.1.0  
Markdown| 3.1.1  
mock| 2.0.0  
monotonic| 1.5  
nltk| 3.4.3  
nose| 1.3.7  
numpy| 1.16.4  
oauth2client| 3.0.0  
pandas| 0.24.2  
pbr| 5.3.0  
Pillow| 6.0.0  
pip| 19.1.1  
protobuf| 3.8.0  
protorpc| 0.12.0  
pyarrow| 0.13.0  
pyasn1| 0.4.5  
pyasn1-modules| 0.2.5  
pydot| 1.4.1  
pymongo| 3.8.0  
pyparsing| 2.4.0  
python-dateutil| 2.8.0  
python-gflags| 3.0.6  
python-snappy| 0.5.4  
pytz| 2019.1  
PyYAML| 3.13  
requests| 2.22.0  
rsa| 4.0  
scikit-learn| 0.20.3  
scipy| 1.2.2  
setuptools| 41.0.1  
six| 1.12.0  
soupsieve| 1.9.1  
tensorboard| 1.14.0  
tensorflow| 1.14.0  
tensorflow-estimator| 1.14.0  
termcolor| 1.1.0  
urllib3| 1.25.3  
Werkzeug| 0.15.4  
wheel| 0.33.4  
wrapt| 1.11.2  
  
### Python 3.7.3

Package| Version  
---|---  
  
absl-py| 0.7.1  
astor| 0.8.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.7.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2019.6.16  
chardet| 3.0.4  
crcmod| 1.7  
Cython| 0.29.10  
dill| 0.2.9  
docopt| 0.6.2  
fastavro| 0.21.24  
fasteners| 0.15  
future| 0.17.1  
gast| 0.2.2  
google-api-core| 1.12.0  
google-apitools| 0.5.28  
google-auth| 1.6.3  
google-cloud-bigquery| 1.6.0  
google-cloud-bigtable| 0.32.1  
google-cloud-core| 0.29.1  
google-cloud-datastore| 1.7.4  
google-cloud-pubsub| 0.39.1  
google-pasta| 0.1.7  
google-resumable-media| 0.3.2  
googleapis-common-protos| 1.6.0  
grpc-google-iam-v1| 0.11.4  
grpcio| 1.21.1  
h5py| 2.9.0  
hdfs| 2.5.6  
httplib2| 0.12.0  
idna| 2.8  
Keras-Applications| 1.0.8  
Keras-Preprocessing| 1.1.0  
Markdown| 3.1.1  
mock| 2.0.0  
monotonic| 1.5  
nltk| 3.4.3  
nose| 1.3.7  
numpy| 1.16.4  
oauth2client| 3.0.0  
pandas| 0.24.2  
pbr| 5.3.0  
Pillow| 6.0.0  
pip| 19.1.1  
protobuf| 3.8.0  
protorpc| 0.12.0  
pyarrow| 0.13.0  
pyasn1| 0.4.5  
pyasn1-modules| 0.2.5  
pydot| 1.4.1  
pymongo| 3.8.0  
pyparsing| 2.4.0  
python-dateutil| 2.8.0  
python-gflags| 3.0.6  
python-snappy| 0.5.4  
pytz| 2019.1  
PyYAML| 3.13  
requests| 2.22.0  
rsa| 4.0  
scikit-learn| 0.20.3  
scipy| 1.2.2  
setuptools| 41.0.1  
six| 1.12.0  
soupsieve| 1.9.1  
tensorboard| 1.14.0  
tensorflow| 1.14.0  
tensorflow-estimator| 1.14.0  
termcolor| 1.1.0  
urllib3| 1.25.3  
Werkzeug| 0.15.4  
wheel| 0.33.4  
wrapt| 1.11.2  
  
#### Version 2.13.0

Dataflow workers have the following packages already installed.

### Python 2.7

Package| Version  
---|---  
  
absl-py| 0.7.1  
astor| 0.8.0  
avro| 1.8.2  
backports.weakref| 1.0.post1  
beautifulsoup4| 4.5.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2019.3.9  
chardet| 3.0.4  
crcmod| 1.7  
Cython| 0.28.1  
dill| 0.2.9  
docopt| 0.6.2  
enum34| 1.1.6  
fastavro| 0.21.14  
fasteners| 0.15  
funcsigs| 1.0.2  
future| 0.17.1  
futures| 3.2.0  
gast| 0.2.2  
google-api-core| 1.11.1  
google-api-python-client| 1.7.9  
google-apitools| 0.5.28  
google-auth| 1.6.3  
google-auth-httplib2| 0.0.3  
google-cloud-bigquery| 1.6.0  
google-cloud-bigtable| 0.32.1  
google-cloud-core| 0.29.1  
google-cloud-datastore| 1.7.3  
google-cloud-pubsub| 0.39.1  
google-pasta| 0.1.6  
google-python-cloud-debugger| 1.9  
google-resumable-media| 0.3.2  
googleapis-common-protos| 1.6.0  
googledatastore| 7.0.2  
grpc-google-iam-v1| 0.11.4  
grpcio| 1.20.1  
guppy| 0.1.10  
h5py| 2.9.0  
hdfs| 2.5.2  
httplib2| 0.12.0  
idna| 2.8  
Keras-Applications| 1.0.7  
Keras-Preprocessing| 1.0.9  
Markdown| 3.1.1  
mock| 2.0.0  
monotonic| 1.5  
nltk| 3.2.1  
nose| 1.3.7  
numpy| 1.16.3  
oauth2client| 3.0.0  
pandas| 0.24.2  
pbr| 5.2.0  
Pillow| 3.4.1  
pip| 19.1.1  
proto-google-cloud-datastore-v1| 0.90.4  
protobuf| 3.7.1  
protorpc| 0.11.1  
pyarrow| 0.13.0  
pyasn1| 0.4.5  
pyasn1-modules| 0.2.5  
pydot| 1.2.4  
pyparsing| 2.4.0  
python-dateutil| 2.8.0  
python-gflags| 3.0.6  
python-snappy| 0.5.3  
pytz| 2019.1  
PyVCF| 0.6.8  
PyYAML| 3.13  
requests| 2.22.0  
rsa| 4.0  
scikit-learn| 0.20.3  
scipy| 1.2.1  
setuptools| 41.0.1  
six| 1.12.0  
tensorboard| 1.13.1  
tensorflow| 1.14.0rc0  
termcolor| 1.1.0  
tf-estimator-nightly| 1.14.0.dev2019042301  
typing| 3.6.6  
uritemplate| 3.0.0  
urllib3| 1.25.3  
Werkzeug| 0.15.4  
wheel| 0.32.1  
wrapt| 1.11.1  
  
### Python 3.5

Package| Version  
---|---  
  
absl-py| 0.7.1  
astor| 0.8.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.5.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2019.3.9  
chardet| 3.0.4  
crcmod| 1.7  
Cython| 0.28.1  
dill| 0.2.9  
docopt| 0.6.2  
fastavro| 0.21.14  
fasteners| 0.15  
future| 0.17.1  
gast| 0.2.2  
google-api-core| 1.11.1  
google-apitools| 0.5.28  
google-auth| 1.6.3  
google-cloud-bigquery| 1.6.0  
google-cloud-bigtable| 0.32.1  
google-cloud-core| 0.29.1  
google-cloud-datastore| 1.7.3  
google-cloud-pubsub| 0.39.1  
google-pasta| 0.1.6  
google-resumable-media| 0.3.2  
googleapis-common-protos| 1.6.0  
grpc-google-iam-v1| 0.11.4  
grpcio| 1.20.1  
h5py| 2.9.0  
hdfs| 2.5.2  
httplib2| 0.12.0  
idna| 2.8  
Keras-Applications| 1.0.7  
Keras-Preprocessing| 1.0.9  
Markdown| 3.1.1  
mock| 2.0.0  
monotonic| 1.5  
nltk| 3.2.1  
nose| 1.3.7  
numpy| 1.16.3  
oauth2client| 3.0.0  
pandas| 0.24.2  
pbr| 5.2.0  
Pillow| 3.4.1  
pip| 19.1.1  
protobuf| 3.7.1  
protorpc| 0.11.1  
pyarrow| 0.13.0  
pyasn1| 0.4.5  
pyasn1-modules| 0.2.5  
pydot| 1.2.4  
pyparsing| 2.4.0  
python-dateutil| 2.8.0  
python-gflags| 3.0.6  
python-snappy| 0.5.3  
pytz| 2019.1  
PyYAML| 3.13  
requests| 2.22.0  
rsa| 4.0  
scikit-learn| 0.20.3  
scipy| 1.2.1  
setuptools| 41.0.1  
six| 1.12.0  
tensorboard| 1.13.1  
tensorflow| 1.14.0rc0  
termcolor| 1.1.0  
tf-estimator-nightly| 1.14.0.dev2019042301  
urllib3| 1.25.3  
Werkzeug| 0.15.4  
wheel| 0.32.1  
wrapt| 1.11.1  
  
### Python 3.6

Package| Version  
---|---  
  
absl-py| 0.7.1  
astor| 0.8.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.5.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2019.3.9  
chardet| 3.0.4  
crcmod| 1.7  
Cython| 0.28.1  
dill| 0.2.9  
docopt| 0.6.2  
fastavro| 0.21.14  
fasteners| 0.15  
future| 0.17.1  
gast| 0.2.2  
google-api-core| 1.11.1  
google-apitools| 0.5.28  
google-auth| 1.6.3  
google-cloud-bigquery| 1.6.0  
google-cloud-bigtable| 0.32.1  
google-cloud-core| 0.29.1  
google-cloud-datastore| 1.7.3  
google-cloud-pubsub| 0.39.1  
google-pasta| 0.1.6  
google-resumable-media| 0.3.2  
googleapis-common-protos| 1.6.0  
grpc-google-iam-v1| 0.11.4  
grpcio| 1.20.1  
h5py| 2.9.0  
hdfs| 2.5.2  
httplib2| 0.12.0  
idna| 2.8  
Keras-Applications| 1.0.7  
Keras-Preprocessing| 1.0.9  
Markdown| 3.1.1  
mock| 2.0.0  
monotonic| 1.5  
nltk| 3.2.1  
nose| 1.3.7  
numpy| 1.16.3  
oauth2client| 3.0.0  
pandas| 0.24.2  
pbr| 5.2.0  
Pillow| 3.4.1  
pip| 19.1.1  
protobuf| 3.7.1  
protorpc| 0.11.1  
pyarrow| 0.13.0  
pyasn1| 0.4.5  
pyasn1-modules| 0.2.5  
pydot| 1.2.4  
pyparsing| 2.4.0  
python-dateutil| 2.8.0  
python-gflags| 3.0.6  
python-snappy| 0.5.3  
pytz| 2019.1  
PyYAML| 3.13  
requests| 2.22.0  
rsa| 4.0  
scikit-learn| 0.20.3  
scipy| 1.2.1  
setuptools| 41.0.1  
six| 1.12.0  
tensorboard| 1.13.1  
tensorflow| 1.14.0rc0  
termcolor| 1.1.0  
tf-estimator-nightly| 1.14.0.dev2019042301  
urllib3| 1.25.3  
Werkzeug| 0.15.4  
wheel| 0.32.1  
wrapt| 1.11.1  
  
### Python 3.7

Package| Version  
---|---  
  
absl-py| 0.7.1  
astor| 0.8.0  
avro-python3| 1.8.2  
beautifulsoup4| 4.5.1  
bs4| 0.0.1  
cachetools| 3.1.1  
certifi| 2019.3.9  
chardet| 3.0.4  
crcmod| 1.7  
Cython| 0.28.1  
dill| 0.2.9  
docopt| 0.6.2  
fastavro| 0.21.14  
fasteners| 0.15  
future| 0.17.1  
gast| 0.2.2  
google-api-core| 1.11.1  
google-apitools| 0.5.28  
google-auth| 1.6.3  
google-cloud-bigquery| 1.6.0  
google-cloud-bigtable| 0.32.1  
google-cloud-core| 0.29.1  
google-cloud-datastore| 1.7.3  
google-cloud-pubsub| 0.39.1  
google-pasta| 0.1.6  
google-resumable-media| 0.3.2  
googleapis-common-protos| 1.6.0  
grpc-google-iam-v1| 0.11.4  
grpcio| 1.20.1  
h5py| 2.9.0  
hdfs| 2.5.2  
httplib2| 0.12.0  
idna| 2.8  
Keras-Applications| 1.0.7  
Keras-Preprocessing| 1.0.9  
Markdown| 3.1.1  
mock| 2.0.0  
monotonic| 1.5  
nltk| 3.2.1  
nose| 1.3.7  
numpy| 1.16.3  
oauth2client| 3.0.0  
pandas| 0.24.2  
pbr| 5.2.0  
Pillow| 3.4.1  
pip| 19.1.1  
protobuf| 3.7.1  
protorpc| 0.11.1  
pyarrow| 0.13.0  
pyasn1| 0.4.5  
pyasn1-modules| 0.2.5  
pydot| 1.2.4  
pyparsing| 2.4.0  
python-dateutil| 2.8.0  
python-gflags| 3.0.6  
python-snappy| 0.5.3  
pytz| 2019.1  
PyYAML| 3.13  
requests| 2.22.0  
rsa| 4.0  
scikit-learn| 0.20.3  
scipy| 1.2.1  
setuptools| 41.0.1  
six| 1.12.0  
tensorboard| 1.13.1  
tensorflow| 1.14.0rc0  
termcolor| 1.1.0  
tf-estimator-nightly| 1.14.0.dev2019042301  
urllib3| 1.25.3  
Werkzeug| 0.15.4  
wheel| 0.32.1  
wrapt| 1.11.1  
  
#### Version 2.12.0

Dataflow workers have the following packages already installed.

Package| Version  
---|---  
  
absl-py| 0.7.0  
astor| 0.7.1  
avro| 1.8.2  
backports.weakref| 1.0.post1  
beautifulsoup4| 4.5.1  
bs4| 0.0.1  
cachetools| 3.1.0  
certifi| 2018.11.29  
chardet| 3.0.4  
crcmod| 1.7  
Cython| 0.28.1  
dill| 0.2.9  
docopt| 0.6.2  
enum34| 1.1.6  
fastavro| 0.21.14  
fasteners| 0.14.1  
funcsigs| 1.0.2  
future| 0.17.1  
futures| 3.2.0  
gast| 0.2.2  
google-api-core| 1.8.0  
google-api-python-client| 1.7.8  
google-apitools| 0.5.26  
google-auth| 1.6.3  
google-auth-httplib2| 0.0.3  
google-cloud-bigquery| 1.6.0  
google-cloud-bigtable| 0.31.1  
google-cloud-core| 0.28.1  
google-cloud-pubsub| 0.39.0  
google-python-cloud-debugger| 1.9  
google-resumable-media| 0.3.2  
googleapis-common-protos| 1.5.8  
googledatastore| 7.0.2  
grpc-google-iam-v1| 0.11.4  
grpcio| 1.15.0  
guppy| 0.1.10  
h5py| 2.9.0  
hdfs| 2.2.2  
httplib2| 0.9.2  
idna| 2.8  
Keras-Applications| 1.0.7  
Keras-Preprocessing| 1.0.9  
Markdown| 3.0.1  
mock| 2.0.0  
monotonic| 1.5  
nltk| 3.2.1  
nose| 1.3.7  
numpy| 1.16.0  
oauth2client| 3.0.0  
pandas| 0.23.4  
pbr| 5.1.3  
Pillow| 3.4.1  
pip| 19.0.3  
proto-google-cloud-datastore-v1| 0.90.4  
protobuf| 3.7.0  
protorpc| 0.11.1  
pyarrow| 0.11.1  
pyasn1| 0.4.5  
pyasn1-modules| 0.2.4  
pydot| 1.2.4  
pyparsing| 2.3.1  
python-dateutil| 2.8.0  
python-gflags| 3.0.6  
python-snappy| 0.5.3  
pytz| 2018.9  
PyVCF| 0.6.8  
PyYAML| 3.13  
requests| 2.21.0  
rsa| 4.0  
scikit-learn| 0.20.2  
scipy| 1.2.0  
setuptools| 40.8.0  
six| 1.12.0  
tensorboard| 1.13.0  
tensorflow| 1.13.1  
tensorflow-estimator| 1.13.0  
termcolor| 1.1.0  
typing| 3.6.6  
uritemplate| 3.0.0  
urllib3| 1.24.1  
Werkzeug| 0.14.1  
wheel| 0.32.1  
  
#### Version 2.11.0

Dataflow workers have the following packages already installed.

Package| Version  
---|---  
  
absl-py| 0.7.0  
astor| 0.7.1  
avro| 1.8.2  
backports.weakref| 1.0.post1  
beautifulsoup4| 4.5.1  
bs4| 0.0.1  
cachetools| 3.1.0  
certifi| 2018.11.29  
chardet| 3.0.4  
crcmod| 1.7  
Cython| 0.28.1  
dill| 0.2.9  
docopt| 0.6.2  
enum34| 1.1.6  
fastavro| 0.21.14  
fasteners| 0.14.1  
funcsigs| 1.0.2  
future| 0.17.1  
futures| 3.2.0  
gast| 0.2.2  
google-api-core| 1.8.0  
google-api-python-client| 1.7.8  
google-apitools| 0.5.26  
google-auth| 1.6.3  
google-auth-httplib2| 0.0.3  
google-cloud-bigquery| 1.6.0  
google-cloud-bigtable| 0.31.1  
google-cloud-core| 0.28.1  
google-cloud-pubsub| 0.39.0  
google-python-cloud-debugger| 1.9  
google-resumable-media| 0.3.2  
googleapis-common-protos| 1.5.8  
googledatastore| 7.0.2  
grpc-google-iam-v1| 0.11.4  
grpcio| 1.15.0  
guppy| 0.1.10  
h5py| 2.9.0  
hdfs| 2.2.2  
httplib2| 0.9.2  
idna| 2.8  
Keras-Applications| 1.0.7  
Keras-Preprocessing| 1.0.9  
Markdown| 3.0.1  
mock| 2.0.0  
monotonic| 1.5  
nltk| 3.2.1  
nose| 1.3.7  
numpy| 1.16.0  
oauth2client| 3.0.0  
pandas| 0.23.4  
pbr| 5.1.2  
Pillow| 3.4.1  
pip| 19.0.3  
proto-google-cloud-datastore-v1| 0.90.4  
protobuf| 3.7.0rc2  
protorpc| 0.11.1  
pyarrow| 0.11.1  
pyasn1| 0.4.5  
pyasn1-modules| 0.2.4  
pydot| 1.2.4  
pyparsing| 2.3.1  
python-dateutil| 2.8.0  
python-gflags| 3.0.6  
python-snappy| 0.5.3  
pytz| 2018.9  
PyVCF| 0.6.8  
PyYAML| 3.13  
requests| 2.21.0  
rsa| 4.0  
scikit-learn| 0.20.2  
scipy| 1.2.0  
setuptools| 40.8.0  
six| 1.12.0  
tensorboard| 1.13.0  
tensorflow| 1.13.1  
tensorflow-estimator| 1.13.0  
termcolor| 1.1.0  
typing| 3.6.6  
uritemplate| 3.0.0  
urllib3| 1.24.1  
Werkzeug| 0.14.1  
wheel| 0.32.1  
  
#### Version 2.10.0

Dataflow workers have the following packages already installed.

Package| Version  
---|---  
  
absl-py| 0.7.0  
astor| 0.7.1  
avro| 1.8.2  
backports.weakref| 1.0.post1  
beautifulsoup4| 4.5.1  
bs4| 0.0.1  
cachetools| 3.0.0  
certifi| 2018.11.29  
chardet| 3.0.4  
crcmod| 1.7  
Cython| 0.28.1  
dill| 0.2.9  
docopt| 0.6.2  
enum34| 1.1.6  
fastavro| 0.21.14  
fasteners| 0.14.1  
funcsigs| 1.0.2  
future| 0.17.1  
futures| 3.2.0  
gast| 0.2.2  
google-api-core| 1.7.0  
google-api-python-client| 1.7.7  
google-apitools| 0.5.24  
google-auth| 1.6.2  
google-auth-httplib2| 0.0.3  
google-cloud-bigquery| 1.6.0  
google-cloud-core| 0.28.1  
google-cloud-pubsub| 0.39.0  
google-python-cloud-debugger| 1.9  
google-resumable-media| 0.3.2  
googleapis-common-protos| 1.5.6  
googledatastore| 7.0.2  
grpc-google-iam-v1| 0.11.4  
grpcio| 1.15.0  
guppy| 0.1.10  
h5py| 2.9.0  
hdfs| 2.2.2  
httplib2| 0.9.2  
idna| 2.8  
Keras-Applications| 1.0.6  
Keras-Preprocessing| 1.0.5  
Markdown| 3.0.1  
mock| 2.0.0  
monotonic| 1.5  
nltk| 3.2.1  
nose| 1.3.7  
numpy| 1.16.0  
oauth2client| 3.0.0  
pandas| 0.23.4  
pbr| 5.1.1  
Pillow| 3.4.1  
pip| 19.0.1  
proto-google-cloud-datastore-v1| 0.90.4  
protobuf| 3.6.1  
protorpc| 0.11.1  
pyarrow| 0.11.1  
pyasn1| 0.4.5  
pyasn1-modules| 0.2.3  
pydot| 1.2.4  
pyparsing| 2.3.1  
python-dateutil| 2.7.5  
python-gflags| 3.0.6  
python-snappy| 0.5.3  
pytz| 2018.9  
PyVCF| 0.6.8  
PyYAML| 3.13  
requests| 2.21.0  
rsa| 4.0  
scikit-learn| 0.20.2  
scipy| 1.2.0  
setuptools| 40.6.3  
six| 1.12.0  
tensorboard| 1.12.2  
tensorflow| 1.13.0rc0  
tensorflow-estimator| 1.10.12  
termcolor| 1.1.0  
typing| 3.6.6  
uritemplate| 3.0.0  
urllib3| 1.24.1  
Werkzeug| 0.14.1  
wheel| 0.32.1  
  
#### Version 2.9.0

Dataflow workers have the following packages already installed.

Package| Version  
---|---  
  
absl-py| 0.6.1  
astor| 0.7.1  
avro| 1.8.2  
backports.weakref| 1.0.post1  
beautifulsoup4| 4.5.1  
bs4| 0.0.1  
cachetools| 3.0.0  
certifi| 2018.10.15  
chardet| 3.0.4  
crcmod| 1.7  
cython| 0.28.1  
dill| 0.2.8.2  
docopt| 0.6.2  
enum34| 1.1.6  
fastavro| 0.21.4  
fasteners| 0.14.1  
funcsigs| 1.0.2  
future| 0.16.0  
futures| 3.2.0  
grpcio| 1.15.0  
gast| 0.2.0  
google-api-core| 1.5.2  
google-api-python-client| 1.7.4  
google-apitools| 0.5.24  
google-auth| 1.6.1  
google-auth-httplib2| 0.0.3  
google-cloud-bigquery| 1.6.0  
google-cloud-core| 0.28.1  
google-cloud-pubsub| 0.35.4  
google-python-cloud-debugger| 1.9  
google-resumable-media| 0.3.1  
googleapis-common-protos| 1.5.5  
googledatastore| 7.0.2  
grpc-google-iam-v1| 0.11.4  
grpcio| 1.15.0  
guppy| 0.1.10  
h5py| 2.8.0  
hdfs| 2.1.0  
httplib2| 0.9.2  
idna| 2.7  
Keras-Applications| 1.0.6  
Keras-Preprocessing| 1.0.5  
Markdown| 3.0.1  
mock| 2.0.0  
monotonic| 1.5  
nltk| 3.2.1  
nose| 1.3.7  
numpy| 1.15.2  
oauth2client| 3.0.0  
pandas| 0.23.4  
pbr| 5.1.1  
pillow| 3.4.1  
pip| 18.1  
proto-google-cloud-datastore-v1| 0.90.4  
protobuf| 3.6.1  
protorpc| 0.11.1  
pyasn1| 0.4.4  
pyasn1-modules| 0.2.2  
pydot| 1.2.4  
pyparsin| 2.3.0  
python-dateutil| 2.7.5  
python-gflags| 3.0.6  
python-snappy| 0.5.3  
pytz| 2018.4  
pyvcf| 0.6.8  
pyyaml| 3.13  
requests| 2.20.1  
rsa| 4.0  
scikit-learn| 0.19.1  
scipy| 1.1.0  
six| 1.11.0  
tensorboard| 1.12.0  
tensorflow| 1.12.0  
termcolor| 1.1.0  
typing| 3.6.1  
uritemplate| 3.0.0  
urllib3| 1.24.1  
Werkzeug| 0.14.1  
wheel| 0.32.1  
  
#### Version 2.8.0

Dataflow workers have the following packages already installed.

Package| Version  
---|---  
  
absl-py| 0.5.0  
astor| 0.7.1  
avro| 1.8.2  
backports.weakref| 1.0.post1  
beautifulsoup4| 4.5.1  
bs4| 0.0.1  
cachetools| 2.1.0  
certifi| 2018.8.24  
chardet| 3.0.4  
crcmod| 1.7  
cython| 0.28.1  
dill| 0.2.8.2  
fastavro| 0.21.4  
fasteners| 0.14.1  
funcsigs| 1.0.2  
future| 0.16.0  
futures| 3.2.0  
gapic-google-cloud-pubsub-v1| 1.15.4  
gast| 0.2.0  
grpcio| 1.15.0  
google-apitools| 0.5.20  
google-cloud-bigquery| 0.25.0  
google-cloud-pubsub| 0.26.0  
google-python-cloud-debugger| 1.9.1  
googledatastore| 7.0.1  
guppy| 0.1.10  
h5py| 2.8.0  
hdfs| 2.1.0  
httplib2| 0.9.2  
idna| 2.7  
Keras-Applications| 1.0.6  
Keras-Preprocessing| 1.0.5  
mock| 2.0.0  
monotonic| 1.5  
nltk| 3.2.1  
nose| 1.3.7  
numpy| 1.15.2  
oauth2client| 3.0.0  
pandas| 0.23.4  
pbr| 4.3.0  
pillow| 3.4.1  
pip| 18.0  
ply| 3.8  
proto-google-cloud-datastore-v1| 0.90.4  
proto-google-cloud-pubsub-v1| 0.15.4  
protobuf| 3.6.1  
protorpc| 0.11.1  
pyasn1| 0.4.4  
pyasn1-modules| 0.2.2  
pydot| 1.2.4  
pyparsing| 2.2.2  
python-dateutil| 2.7.3  
python-gflags| 3.0.6  
python-snappy| 0.5.3  
pytz| 2018.4  
pyvcf| 0.6.8  
pyyaml| 3.12  
requests| 2.19.1  
scikit-learn| 0.19.1  
scipy| 1.1.0  
six| 1.11.0  
tensorflow| 1.11.0  
termcolor| 1.1.0  
typing| 3.6.1  
uritemplate| 3.0.0  
urllib3| 1.23  
Werkzeug| 0.14.1  
wheel| 0.32.1  
  
#### Version 2.7.0

Dataflow workers have the following packages already installed.

Package| Version  
---|---  
  
absl-py| 0.2.2  
astor| 0.7.1  
avro| 1.8.2  
beautifulsoup4| 4.5.1  
backports.weakref| 1.0.post1  
bs4| 0.0.1  
cachetools| 2.1.0  
certifi| 2018.4.16  
chardet| 3.0.4  
crcmod| 1.7  
cython| 0.28.1  
dill| 0.2.6  
docopt| 0.6.2  
enum34| 1.1.6  
fastavro| 0.19.7  
fasteners| 0.14.1  
funcsigs| 1.0.2  
future| 0.16.0  
futures| 3.1.1  
gapic-google-cloud-pubsub-v1| 0.15.4  
gast| 0.2.0  
grpcio| 1.10.0  
google-apitools| 0.5.20  
google-cloud-bigquery| 0.25.0  
google-cloud-pubsub| 0.26.0  
google-python-cloud-debugger| 1.9.1  
googledatastore| 7.0.1  
guppy| 0.1.10  
hdfs| 2.1.0  
httplib2| 0.9.2  
idna| 2.6  
Markdown| 2.6.11  
mock| 2.0.0  
monotonic| 1.5  
nltk| 3.2.1  
nose| 1.3.7  
numpy| 1.13.3  
oauth2client| 4.1.2  
pandas| 0.18.1  
pbr| 4.1.0  
pillow| 3.4.1  
pip| 10.0.1  
ply| 3.8  
proto-google-cloud-datastore-v1| 0.90.4  
proto-google-cloud-pubsub-v1| 0.15.4  
proto-google-cloud-datastore-v1| 0.90.4  
proto-google-cloud-pubsub-v1| 0.15.4  
protobuf| 3.5.1  
protorpc| 0.11.1  
pyasn1| 0.4.3  
pyasn1-modules| 0.2.2  
pydot| 1.2.4  
pyparsing| 2.2.0  
python-dateutil| 2.7.3  
python-gflags| 3.0.6  
python-snappy| 0.5.1  
pytz| 2018.4  
pyvcf| 0.6.8  
pyyaml| 3.12  
requests| 2.18.4  
rsa| 3.4.2  
scikit-learn| 0.19.1  
scipy| 1.1.0  
setuptools| 39.1.0  
six| 1.10.0  
tensorboard| 1.9.0  
tensorflow| 1.10.0  
termcolor| 1.1.0  
typing| 3.6.1  
uritemplate| 3.0.0  
urllib3| 1.22  
Werkzeug| 0.14.1  
wheel| 0.29.0  
  
#### Version 2.6.0

Dataflow workers have the following packages already installed.

Package| Version  
---|---  
  
avro| 1.8.2  
beautifulsoup4| 4.5.1  
bs4| 0.0.1  
crcmod| 1.7  
cython| 0.28.1  
dill| 0.2.8.2  
fastavro| 0.21.4  
futures| 3.2.0  
future| 0.16.0  
google-apitools| 0.5.20  
google-cloud-bigquery| 0.25.0  
google-cloud-pubsub| 0.26.0  
googledatastore| 7.0.1  
google-python-cloud-debugger| 1.9.1  
grpcio| 1.15.0  
guppy| 0.1.10  
hdfs| 2.1.0  
httplib2| 0.9.2  
mock| 2.0.0  
nltk| 3.2.1  
nose| 1.3.7  
numpy| 1.14.5  
oauth2client| 4.1.2  
pandas| 0.23.3  
pillow| 3.4.1  
protobuf| 3.6.1  
proto-google-cloud-datastore-v1| 0.90.4  
proto-google-cloud-pubsub-v1| 0.15.4  
protorpc| 0.11.1  
pydot| 1.2.4  
python-gflags| 3.0.6  
python-snappy| 0.5.3  
pytz| 2018.4  
pyvcf| 0.6.8  
pyyaml| 3.12  
requests| 2.18.4  
scikit-learn| 0.19.1  
scipy| 1.1.0  
six| 1.10.0  
tensorflow| 1.10.0  
typing| 3.6.1  
wheel| 0.29.0  
  
## Dataflow 2.x SDKs

### SDK for Java

To determine if your JAR is using a conflicting version, inspect the dependency tree of your project. You can generate the dependency tree with various tools, such as [Maven](https://maven.apache.org/plugins/maven-dependency-plugin/tree-mojo.html).

Avoid specifying "latest" in your `pom.xml` for the libraries in the following table.

#### Version 2.5.0

Dataflow SDK 2.5.0 for Java has the following compile and runtime dependencies.

GroupId| ArtifactId| Version  
---|---|---  
  
args4j | args4j | 2.33  
ca.coglinc | javacc-gradle-plugin | 2.4.0  
com.datastax.cassandra | cassandra-driver-core | 3.5.0  
com.datastax.cassandra | cassandra-driver-mapping | 3.5.0  
com.fasterxml.jackson.core | jackson-annotations | 2.9.5  
com.fasterxml.jackson.core | jackson-core | 2.9.5  
com.fasterxml.jackson.core | jackson-databind | 2.9.5  
com.fasterxml.jackson.dataformat | jackson-dataformat-cbor | 2.9.5  
com.fasterxml.jackson.dataformat | jackson-dataformat-yaml | 2.9.5  
com.fasterxml.jackson.datatype | jackson-datatype-joda | 2.9.5  
com.fasterxml.jackson.module | jackson-module-scala_2.11 | 2.9.5  
com.github.ben-manes | gradle-versions-plugin | 0.20.0  
com.github.jengelman.gradle.plugins | shadow | 2.0.4  
com.github.kstyrc | embedded-redis | 0.6  
com.github.stephenc.findbugs | findbugs-annotations | 1.3.9-1  
com.google.api | gax-grpc | 0.20.0  
com.google.api-client | google-api-client | 1.23.0  
com.google.api.grpc | grpc-google-cloud-pubsub-v1 | 0.1.18  
com.google.api.grpc | proto-google-cloud-pubsub-v1 | 0.1.18  
com.google.api.grpc | proto-google-cloud-spanner-admin-database-v1 | 0.1.9  
com.google.api.grpc | proto-google-common-protos | 0.1.9  
com.google.apis | google-api-services-bigquery | v2-rev374-1.23.0  
com.google.apis | google-api-services-clouddebugger | v2-rev233-1.23.0  
com.google.apis | google-api-services-cloudresourcemanager | v1-rev477-1.23.0  
com.google.apis | google-api-services-dataflow | v1b3-rev221-1.23.0  
com.google.apis | google-api-services-pubsub | v1-rev382-1.23.0  
com.google.apis | google-api-services-storage | v1-rev124-1.23.0  
com.google.auth | google-auth-library-credentials | 0.7.1  
com.google.auth | google-auth-library-oauth2-http | 0.7.1  
com.google.cloud | google-cloud-core | 1.0.2  
com.google.cloud | google-cloud-core-grpc | 1.2.0  
com.google.cloud | google-cloud-spanner | 0.20.0b-beta  
com.google.cloud.bigdataoss | gcsio | 1.4.5  
com.google.cloud.bigdataoss | util | 1.4.5  
com.google.cloud.bigtable | bigtable-client-core | 1.0.0  
com.google.cloud.bigtable | bigtable-protos | 1.0.0-pre3  
com.google.cloud.dataflow | google-cloud-dataflow-java-proto-library-all | 0.5.160304  
com.google.cloud.datastore | datastore-v1-proto-client | 1.4.0  
com.google.cloud.datastore | datastore-v1-protos | 1.3.0  
com.google.code.findbugs | jsr305 | 3.0.1  
com.google.errorprone | error_prone_annotations | 2.0.15  
com.google.guava | guava | 20.0  
com.google.guava | guava-testlib | 20.0  
com.google.http-client | google-http-client | 1.23.0  
com.google.http-client | google-http-client-jackson2 | 1.23.0  
com.google.protobuf | protobuf-gradle-plugin | 0.8.5  
com.google.protobuf | protobuf-java | 3.2.0  
com.google.protobuf | protobuf-java-util | 3.2.0  
com.googlecode.fmpp-maven-plugin | fmpp-maven-plugin | 1.0  
com.pholser | junit-quickcheck-core | 0.8  
com.tdunning | t-digest | 3.2  
commons-io | commons-io | 2.5  
commons-lang | commons-lang | 2.6  
cz.malohlava | visteg | 1.0.3  
gradle.plugin.org.nosphere.apache | creadur-rat-gradle | 0.3.1  
io.grpc | grpc-all | 1.2.0  
io.grpc | grpc-auth | 1.2.0  
io.grpc | grpc-core | 1.2.0  
io.grpc | grpc-netty | 1.2.0  
io.grpc | grpc-protobuf | 1.2.0  
io.grpc | grpc-stub | 1.2.0  
io.netty | netty-handler | 4.1.8.Final  
io.netty | netty-tcnative-boringssl-static | 1.1.33.Fork26  
io.netty | netty-transport-native-epoll | 4.1.8.Final  
javax.xml.bind | jaxb-api | 2.2.12  
joda-time | joda-time | 2.4  
junit | junit | 4.12  
net.bytebuddy | byte-buddy | 1.8.11  
org.apache.activemq | activemq-amqp | 5.13.1  
org.apache.activemq | activemq-broker | 5.13.1  
org.apache.activemq | activemq-client | 5.13.1  
org.apache.activemq | activemq-jaas | 5.13.1  
org.apache.activemq | activemq-kahadb-store | 5.13.1  
org.apache.activemq | activemq-mqtt | 5.13.1  
org.apache.activemq.tooling | activemq-junit | 5.13.1  
org.apache.apex | apex-common | 3.7.0  
org.apache.apex | apex-engine | 3.7.0  
org.apache.apex | malhar-library | 3.4.0  
org.apache.avro | avro | 1.8.2  
org.apache.calcite | calcite-core | 1.16.0  
org.apache.calcite | calcite-linq4j | 1.16.0  
org.apache.calcite.avatica | avatica-core | 1.11.0  
org.apache.commons | commons-compress | 1.16.1  
org.apache.commons | commons-csv | 1.4  
org.apache.commons | commons-lang3 | 3.6  
org.apache.flink | flink-clients_2.11 | 1.5.0  
org.apache.flink | flink-core | 1.5.0  
org.apache.flink | flink-java | 1.5.0  
org.apache.flink | flink-metrics-core | 1.5.0  
org.apache.flink | flink-runtime_2.11 | 1.5.0  
org.apache.flink | flink-streaming-java_2.11 | 1.5.0  
org.apache.flink | flink-test-utils_2.11 | 1.5.0  
org.apache.gearpump | gearpump-core_2.11 | 0.8.4  
org.apache.gearpump | gearpump-streaming_2.11 | 0.8.4  
org.apache.geronimo.specs | geronimo-jms_1.1_spec | 1.1.1  
org.apache.hadoop | hadoop-client | 2.7.3  
org.apache.hadoop | hadoop-common | 2.7.3  
org.apache.hadoop | hadoop-hdfs | 2.7.3  
org.apache.hadoop | hadoop-mapreduce-client-core | 2.7.3  
org.apache.hadoop | hadoop-minicluster | 2.7.3  
org.apache.kafka | kafka-clients | 1.0.0  
org.apache.kafka | kafka_2.11 | 1.0.0  
org.apache.logging.log4j | log4j-api | 2.6.2  
org.apache.logging.log4j | log4j-core | 2.6.2  
org.apache.parquet | parquet-avro | 1.10.0  
org.apache.parquet | parquet-common | 1.10.0  
org.apache.parquet | parquet-hadoop | 1.10.0  
org.apache.rat | apache-rat-tasks | 0.12  
org.apache.spark | spark-core_2.11 | 2.3.1  
org.apache.spark | spark-network-common_2.11 | 2.3.1  
org.apache.spark | spark-streaming_2.11 | 2.3.1  
org.apache.tika | tika-core | 1.18  
org.apache.tika | tika-parsers | 1.18  
org.codehaus.woodstox | stax2-api | 3.1.4  
org.codehaus.woodstox | woodstox-core-asl | 4.4.1  
org.fusesource.hawtbuf | hawtbuf | 1.11  
org.fusesource.mqtt-client | mqtt-client | 1.14  
org.hamcrest | hamcrest-core | 1.3  
org.hamcrest | hamcrest-library | 1.3  
org.mockito | mockito-core | 1.9.5  
org.postgresql | postgresql | 42.2.2  
org.slf4j | slf4j-simple | 1.7.25  
org.xerial.snappy | snappy-java | 1.1.4  
redis.clients | jedis | 2.9.0  
biz.aQute | bndlib | 1.43.0  
com.alibaba | fastjson | 1.2.12  
com.amazonaws | amazon-kinesis-client | 1.8.8  
com.amazonaws | amazon-kinesis-producer | 0.12.8  
com.amazonaws | aws-java-sdk-cloudwatch | 1.11.255  
com.amazonaws | aws-java-sdk-core | 1.11.319  
com.amazonaws | aws-java-sdk-kinesis | 1.11.255  
com.amazonaws | aws-java-sdk-s3 | 1.11.319  
com.carrotsearch.randomizedtesting | randomizedtesting-runner | 2.5.0  
com.clearspring.analytics | stream | 2.9.5  
com.commercehub.gradle.plugin | gradle-avro-plugin | 0.11.0  
com.datastax.cassandra | cassandra-driver-core | 3.2.0  
com.datastax.cassandra | cassandra-driver-mapping | 3.2.0  
com.diffplug.spotless | spotless-plugin-gradle | 3.6.0  
com.esotericsoftware.kryo | kryo | 2.21  
com.google.auto.service | auto-service | 1.0-rc2  
com.google.auto.value | auto-value | 1.5.3  
com.google.protobuf | protoc | 3.2.0  
com.gradle | build-scan-plugin | 1.13.1  
com.typesafe | config | 1.3.0  
commons-cli | commons-cli | 1.2  
commons-codec | commons-codec | 1.9  
de.flapdoodle.embed | de.flapdoodle.embed.mongo | 1.50.1  
de.flapdoodle.embed | de.flapdoodle.embed.process | 1.50.1  
gradle.plugin.com.github.blindpirate | gogradle | 0.9  
gradle.plugin.com.palantir.gradle.docker | gradle-docker | 0.13.0  
gradle.plugin.io.pry.gradle.offline_dependencies | gradle-offline-dependencies-plugin | 0.3  
io.dropwizard.metrics | metrics-core | 3.1.2  
io.grpc | protoc-gen-grpc-java | 1.2.0  
io.netty | netty-all | 4.1.17.Final  
io.spring.gradle | propdeps-plugin | 0.0.9.RELEASE  
jline | jline | 2.14.6  
net.java.dev.javacc | javacc | 4.0  
net.java.dev.jna | jna | 4.1.0  
net.ltgt.gradle | gradle-apt-plugin | 0.13  
net.ltgt.gradle | gradle-errorprone-plugin | 0.0.13  
net.researchgate | gradle-release | 2.6.0  
org.apache.cassandra | cassandra-all | 3.9  
org.apache.commons | commons-dbcp2 | 2.1.1  
org.apache.derby | derby | 10.12.1.1  
org.apache.derby | derbyclient | 10.12.1.1  
org.apache.derby | derbynet | 10.12.1.1  
org.apache.hbase | hbase-common | 1.2.6  
org.apache.hbase | hbase-hadoop-compat | 1.2.6  
org.apache.hbase | hbase-hadoop2-compat | 1.2.6  
org.apache.hbase | hbase-server | 1.2.6  
org.apache.hbase | hbase-shaded-client | 1.2.6  
org.apache.hbase | hbase-shaded-server | 1.2.6  
org.apache.hive | hive-cli | 2.1.0  
org.apache.hive | hive-common | 2.1.0  
org.apache.hive | hive-exec | 2.1.0  
org.apache.hive.hcatalog | hive-hcatalog-core | 2.1.0  
org.apache.httpcomponents | httpasyncclient | 4.1.2  
org.apache.httpcomponents | httpclient | 4.5.2  
org.apache.httpcomponents | httpcore | 4.4.5  
org.apache.httpcomponents | httpcore-nio | 4.4.5  
org.apache.qpid | proton-j | 0.13.1  
org.apache.solr | solr-core | 5.5.4  
org.apache.solr | solr-solrj | 5.5.4  
org.apache.solr | solr-test-framework | 5.5.4  
org.apache.zookeeper | zookeeper | 3.4.11  
org.assertj | assertj-core | 2.5.0  
org.codehaus.groovy | groovy-all | 2.4.13  
org.elasticsearch | elasticsearch | 5.6.3  
org.elasticsearch | elasticsearch-hadoop | 5.0.0  
org.elasticsearch.client | elasticsearch-rest-client | 5.6.3  
org.elasticsearch.client | transport | 5.0.0  
org.elasticsearch.plugin | transport-netty4-client | 5.6.3  
org.elasticsearch.test | framework | 5.6.3  
org.freemarker | freemarker | 2.3.25-incubating  
org.mongodb | mongo-java-driver | 3.2.2  
org.scala-lang | scala-library | 2.11.8  
org.slf4j | slf4j-api | 1.7.25  
org.slf4j | slf4j-jdk14 | 1.7.25  
org.springframework | spring-expression | 4.3.5.RELEASE  
org.tukaani | xz | 1.5  
sqlline | sqlline | 1.3.0  
  
Dataflow workers have the following packages already installed.

GroupId| ArtifactId| Version  
---|---|---  
  
org.apache.logging.log4j| log4j-to-slf4j| 2.5  
org.slf4j| jcl-over-slf4j| 1.7.14  
org.slf4j| log4j-over-slf4j| 1.7.14  
org.slf4j| slf4j-api| 1.7.14  
org.slf4j| slf4j-jdk14| 1.7.14  
  
#### Version 2.4.0

Dataflow SDK 2.4.0 for Java has the following compile and runtime dependencies.

GroupId| ArtifactId| Version  
---|---|---  
  
com.fasterxml.jackson.core| jackson-annotations| 2.8.9  
com.fasterxml.jackson.core| jackson-core| 2.8.9  
com.fasterxml.jackson.core| jackson-databind| 2.8.9  
com.github.stephenc.findbugs| findbugs-annotations| 1.3.9-1  
com.google.api| api-common| 1.1.0  
com.google.api-client| google-api-client| 1.22.0  
com.google.api-client| google-api-client-jackson2| 1.20.0  
com.google.api-client| google-api-client-java6| 1.20.0  
com.google.api| gax| 1.3.1  
com.google.api| gax-grpc| 0.20.0  
com.google.api.grpc| grpc-google-cloud-pubsub-v1| 0.1.18  
com.google.api.grpc| grpc-google-cloud-spanner-admin-database-v1| 0.1.11  
com.google.api.grpc| grpc-google-cloud-spanner-admin-instance-v1| 0.1.11  
com.google.api.grpc| grpc-google-cloud-spanner-v1| 0.1.11b  
com.google.api.grpc| grpc-google-common-protos| 0.1.0  
com.google.api.grpc| grpc-google-longrunning-v1| 0.1.11  
com.google.api.grpc| proto-google-cloud-pubsub-v1| 0.1.18  
com.google.api.grpc| proto-google-cloud-spanner-admin-database-v1| 0.1.9  
com.google.api.grpc| proto-google-cloud-spanner-admin-instance-v1| 0.1.11  
com.google.api.grpc| proto-google-cloud-spanner-v1| 0.1.11b  
com.google.api.grpc| proto-google-common-protos| 0.1.9  
com.google.api.grpc| proto-google-iam-v1| 0.1.18  
com.google.api.grpc| proto-google-longrunning-v1| 0.1.11  
com.google.apis| google-api-services-bigquery| v2-rev374-1.22.0  
com.google.apis| google-api-services-clouddebugger| v2-rev8-1.22.0  
com.google.apis| google-api-services-cloudresourcemanager| v1-rev6-1.22.0  
com.google.apis| google-api-services-dataflow| v1b3-rev221-1.22.0  
com.google.apis| google-api-services-pubsub| v1-rev10-1.22.0  
com.google.apis| google-api-services-storage| v1-rev71-1.22.0  
com.google.auth| google-auth-library-appengine| 0.7.0  
com.google.auth| google-auth-library-credentials| 0.7.1  
com.google.auth| google-auth-library-oauth2-http| 0.7.1  
com.google.auto| auto-common| 0.3  
com.google.auto.service| auto-service| 1.0-rc2  
com.google.cloud.bigdataoss| gcsio| 1.4.5  
com.google.cloud.bigdataoss| util| 1.4.5  
com.google.cloud.bigtable| bigtable-client-core| 1.0.0  
com.google.cloud.bigtable| bigtable-protos| 1.0.0-pre3  
com.google.cloud.datastore| datastore-v1-proto-client| 1.4.0  
com.google.cloud.datastore| datastore-v1-protos| 1.3.0  
com.google.cloud| google-cloud-core| 1.0.2  
com.google.cloud| google-cloud-core-grpc| 1.2.0  
com.google.cloud| google-cloud-spanner| 0.20.0b-beta  
com.google.code.findbugs| jsr305| 3.0.1  
com.google.code.gson| gson| 2.7  
com.google.guava| guava| 20.0  
com.google.http-client| google-http-client| 1.22.0  
com.google.http-client| google-http-client-jackson| 1.22.0  
com.google.http-client| google-http-client-jackson2| 1.22.0  
com.google.http-client| google-http-client-protobuf| 1.20.0  
com.google.instrumentation| instrumentation-api| 0.3.0  
com.google.oauth-client| google-oauth-client| 1.22.0  
com.google.oauth-client| google-oauth-client-java6| 1.20.0  
com.google.protobuf.nano| protobuf-javanano| 3.0.0-alpha-5  
com.google.protobuf| protobuf-java| 3.2.0  
com.google.protobuf| protobuf-java-util| 3.2.0  
commons-codec| commons-codec| 1.3  
commons-logging| commons-logging| 1.2  
com.squareup.okhttp| okhttp| 2.5.0  
com.squareup.okio| okio| 1.6.0  
com.thoughtworks.paranamer| paranamer| 2.7  
io.dropwizard.metrics| metrics-core| 3.1.2  
io.grpc| grpc-all| 1.2.0  
io.grpc| grpc-auth| 1.2.0  
io.grpc| grpc-context| 1.2.0  
io.grpc| grpc-core| 1.2.0  
io.grpc| grpc-netty| 1.2.0  
io.grpc| grpc-okhttp| 1.2.0  
io.grpc| grpc-protobuf| 1.2.0  
io.grpc| grpc-protobuf-lite| 1.2.0  
io.grpc| grpc-protobuf-nano| 1.2.0  
io.grpc| grpc-stub| 1.2.0  
io.netty| netty-buffer| 4.1.8.Final  
io.netty| netty-codec| 4.1.8.Final  
io.netty| netty-codec-http2| 4.1.8.Final  
io.netty| netty-codec-http| 4.1.8.Final  
io.netty| netty-codec-socks| 4.1.8.Final  
io.netty| netty-common| 4.1.8.Final  
io.netty| netty-handler| 4.1.8.Final  
io.netty| netty-handler-proxy| 4.1.8.Final  
io.netty| netty-resolver| 4.1.8.Final  
io.netty| netty-tcnative-boringssl-static| 1.1.33.Fork18  
io.netty| netty-transport| 4.1.8.Final  
io.netty| netty-transport-native-epoll| linux-x86_64  
io.opencensus| opencensus-api| 0.7.0  
io.opencensus| opencensus-contrib-grpc-util| 0.7.0  
javax.servlet| javax.servlet-api| 3.1.0  
joda-time| joda-time| 2.4  
org.apache.avro| avro| 1.8.2  
org.apache.beam| beam-model-fn-execution| 2.4.0  
org.apache.beam| beam-model-job-management| 2.4.0  
org.apache.beam| beam-model-pipeline| 2.4.0  
org.apache.beam| beam-runners-core-construction-java| 2.4.0  
org.apache.beam| beam-runners-core-java| 2.4.0  
org.apache.beam| beam-runners-google-cloud-dataflow-java| 2.4.0  
org.apache.beam| beam-runners-java-fn-execution| 2.4.0  
org.apache.beam| beam-sdks-java-core| 2.4.0  
org.apache.beam| beam-sdks-java-extensions-google-cloud-platform-core| 2.4.0  
org.apache.beam| beam-sdks-java-extensions-protobuf| 2.4.0  
org.apache.beam| beam-sdks-java-io-google-cloud-platform| 2.4.0  
org.apache.commons| commons-compress| 1.8.1  
org.apache.httpcomponents| httpclient| 4.0.1  
org.apache.httpcomponents| httpcore| 4.0.1  
org.codehaus.jackson| jackson-core-asl| 1.9.13  
org.codehaus.jackson| jackson-mapper-asl| 1.9.13  
org.eclipse.jetty| jetty-http| 9.2.10.v20150310  
org.eclipse.jetty| jetty-io| 9.2.10.v20150310  
org.eclipse.jetty| jetty-security| 9.2.10.v20150310  
org.eclipse.jetty| jetty-server| 9.2.10.v20150310  
org.eclipse.jetty| jetty-servlet| 9.2.10.v20150310  
org.eclipse.jetty| jetty-util| 9.2.10.v20150310  
org.json| json| 20160810  
org.slf4j| slf4j-api| 1.7.25  
org.slf4j| slf4j-jdk14| 1.7.25  
org.threeten| threetenbp| 1.3.3  
org.tukaani| xz| 1.5  
org.xerial.snappy| snappy-java| 1.1.4  
  
Additionally, a Dataflow worker starts with the following logging JARs prepended to the classpath.

GroupId| ArtifactId| Version  
---|---|---  
  
org.apache.logging.log4j| log4j-to-slf4j| 2.5  
org.slf4j| jcl-over-slf4j| 1.7.14  
org.slf4j| log4j-over-slf4j| 1.7.14  
org.slf4j| slf4j-api| 1.7.14  
org.slf4j| slf4j-jdk14| 1.7.14  
  
#### Version 2.3.0

Dataflow SDK 2.3.0 for Java has the following compile and runtime dependencies.

GroupId| ArtifactId| Version  
---|---|---  
  
com.fasterxml.jackson.core| jackson-annotations| 2.8.9  
com.fasterxml.jackson.core| jackson-core| 2.8.9  
com.fasterxml.jackson.core| jackson-databind| 2.8.9  
com.github.stephenc.findbugs| findbugs-annotations| 1.3.9-1  
com.google.api| api-common| 1.1.0  
com.google.api-client| google-api-client| 1.22.0  
com.google.api-client| google-api-client-jackson2| 1.20.0  
com.google.api-client| google-api-client-java6| 1.20.0  
com.google.api| gax| 1.3.1  
com.google.api| gax-grpc| 0.20.0  
com.google.api.grpc| grpc-google-cloud-pubsub-v1| 0.1.18  
com.google.api.grpc| grpc-google-cloud-spanner-admin-database-v1| 0.1.11  
com.google.api.grpc| grpc-google-cloud-spanner-admin-instance-v1| 0.1.11  
com.google.api.grpc| grpc-google-cloud-spanner-v1| 0.1.11  
com.google.api.grpc| grpc-google-common-protos| 0.1.0  
com.google.api.grpc| grpc-google-longrunning-v1| 0.1.11  
com.google.api.grpc| proto-google-cloud-pubsub-v1| 0.1.18  
com.google.api.grpc| proto-google-cloud-spanner-admin-database-v1| 0.1.9  
com.google.api.grpc| proto-google-cloud-spanner-admin-instance-v1| 0.1.11  
com.google.api.grpc| proto-google-cloud-spanner-v1| 0.1.11  
com.google.api.grpc| proto-google-common-protos| 0.1.9  
com.google.api.grpc| proto-google-iam-v1| 0.1.18  
com.google.api.grpc| proto-google-longrunning-v1| 0.1.11  
com.google.apis| google-api-services-bigquery| v2-rev355-1.22.0  
com.google.apis| google-api-services-clouddebugger| v2-rev8-1.22.0  
com.google.apis| google-api-services-cloudresourcemanager| v1-rev6-1.22.0  
com.google.apis| google-api-services-dataflow| v1b3-rev221-1.22.0  
com.google.apis| google-api-services-pubsub| v1-rev10-1.22.0  
com.google.apis| google-api-services-storage| v1-rev71-1.22.0  
com.google.auth| google-auth-library-appengine| 0.7.0  
com.google.auth| google-auth-library-credentials| 0.7.1  
com.google.auth| google-auth-library-oauth2-http| 0.7.1  
com.google.auto| auto-common| 0.3  
com.google.auto.service| auto-service| 1.0-rc2  
com.google.cloud.bigdataoss| gcsio| 1.4.5  
com.google.cloud.bigdataoss| util| 1.4.5  
com.google.cloud.bigtable| bigtable-client-core| 1.0.0  
com.google.cloud.bigtable| bigtable-protos| 1.0.0-pre3  
com.google.cloud.datastore| datastore-v1-proto-client| 1.4.0  
com.google.cloud.datastore| datastore-v1-protos| 1.3.0  
com.google.cloud| google-cloud-core| 1.0.2  
com.google.cloud| google-cloud-core-grpc| 1.2.0  
com.google.cloud| google-cloud-spanner| 0.20.0-beta  
com.google.code.findbugs| jsr305| 3.0.1  
com.google.code.gson| gson| 2.7  
com.google.guava| guava| 20.0  
com.google.http-client| google-http-client| 1.22.0  
com.google.http-client| google-http-client-jackson| 1.22.0  
com.google.http-client| google-http-client-jackson2| 1.22.0  
com.google.http-client| google-http-client-protobuf| 1.20.0  
com.google.instrumentation| instrumentation-api| 0.3.0  
com.google.oauth-client| google-oauth-client| 1.22.0  
com.google.oauth-client| google-oauth-client-java6| 1.20.0  
com.google.protobuf.nano| protobuf-javanano| 3.0.0-alpha-5  
com.google.protobuf| protobuf-java| 3.2.0  
com.google.protobuf| protobuf-java-util| 3.2.0  
commons-codec| commons-codec| 1.3  
commons-logging| commons-logging| 1.2  
com.squareup.okhttp| okhttp| 2.5.0  
com.squareup.okio| okio| 1.6.0  
com.thoughtworks.paranamer| paranamer| 2.7  
io.dropwizard.metrics| metrics-core| 3.1.2  
io.grpc| grpc-all| 1.2.0  
io.grpc| grpc-auth| 1.2.0  
io.grpc| grpc-context| 1.2.0  
io.grpc| grpc-core| 1.2.0  
io.grpc| grpc-netty| 1.2.0  
io.grpc| grpc-okhttp| 1.2.0  
io.grpc| grpc-protobuf| 1.2.0  
io.grpc| grpc-protobuf-lite| 1.2.0  
io.grpc| grpc-protobuf-nano| 1.2.0  
io.grpc| grpc-stub| 1.2.0  
io.netty| netty-buffer| 4.1.8.Final  
io.netty| netty-codec| 4.1.8.Final  
io.netty| netty-codec-http2| 4.1.8.Final  
io.netty| netty-codec-http| 4.1.8.Final  
io.netty| netty-codec-socks| 4.1.8.Final  
io.netty| netty-common| 4.1.8.Final  
io.netty| netty-handler| 4.1.8.Final  
io.netty| netty-handler-proxy| 4.1.8.Final  
io.netty| netty-resolver| 4.1.8.Final  
io.netty| netty-tcnative-boringssl-static| 1.1.33.Fork18  
io.netty| netty-transport| 4.1.8.Final  
io.netty| netty-transport-native-epoll| linux-x86_64  
io.opencensus| opencensus-api| 0.7.0  
io.opencensus| opencensus-contrib-grpc-util| 0.7.0  
javax.servlet| javax.servlet-api| 3.1.0  
joda-time| joda-time| 2.4  
org.apache.avro| avro| 1.8.2  
org.apache.beam| beam-model-fn-execution| 2.3.0  
org.apache.beam| beam-model-job-management| 2.3.0  
org.apache.beam| beam-model-pipeline| 2.3.0  
org.apache.beam| beam-runners-core-construction-java| 2.3.0  
org.apache.beam| beam-runners-core-java| 2.3.0  
org.apache.beam| beam-runners-google-cloud-dataflow-java| 2.3.0  
org.apache.beam| beam-runners-java-fn-execution| 2.3.0  
org.apache.beam| beam-sdks-java-core| 2.3.0  
org.apache.beam| beam-sdks-java-extensions-google-cloud-platform-core| 2.3.0  
org.apache.beam| beam-sdks-java-extensions-protobuf| 2.3.0  
org.apache.beam| beam-sdks-java-io-google-cloud-platform| 2.3.0  
org.apache.commons| commons-compress| 1.8.1  
org.apache.httpcomponents| httpclient| 4.0.1  
org.apache.httpcomponents| httpcore| 4.0.1  
org.codehaus.jackson| jackson-core-asl| 1.9.13  
org.codehaus.jackson| jackson-mapper-asl| 1.9.13  
org.eclipse.jetty| jetty-http| 9.2.10.v20150310  
org.eclipse.jetty| jetty-io| 9.2.10.v20150310  
org.eclipse.jetty| jetty-security| 9.2.10.v20150310  
org.eclipse.jetty| jetty-server| 9.2.10.v20150310  
org.eclipse.jetty| jetty-servlet| 9.2.10.v20150310  
org.eclipse.jetty| jetty-util| 9.2.10.v20150310  
org.json| json| 20160810  
org.slf4j| slf4j-api| 1.7.25  
org.slf4j| slf4j-jdk14| 1.7.25  
org.threeten| threetenbp| 1.3.3  
org.tukaani| xz| 1.5  
org.xerial.snappy| snappy-java| 1.1.4  
  
Additionally, a Dataflow worker starts with the following logging JARs prepended to the classpath.

GroupId| ArtifactId| Version  
---|---|---  
  
org.apache.logging.log4j| log4j-to-slf4j| 2.5  
org.slf4j| jcl-over-slf4j| 1.7.14  
org.slf4j| log4j-over-slf4j| 1.7.14  
org.slf4j| slf4j-api| 1.7.14  
org.slf4j| slf4j-jdk14| 1.7.14  
  
#### Version 2.2.0

Dataflow SDK 2.2.0 for Java has the following compile and runtime dependencies.

GroupId| ArtifactId| Version  
---|---|---  
  
com.fasterxml.jackson.core| jackson-annotations| 2.8.9  
com.fasterxml.jackson.core| jackson-core| 2.8.9  
com.fasterxml.jackson.core| jackson-databind| 2.8.9  
com.google.api-client| google-api-client| 1.22.0  
com.google.api-client| google-api-client-jackson2| 1.22.0  
com.google.api-client| google-api-client-java6| 1.22.0  
com.google.api.grpc| grpc-google-cloud-pubsub-v1| 0.1.18  
com.google.api.grpc| grpc-google-cloud-spanner-admin-database-v1| 0.1.11  
com.google.api.grpc| grpc-google-cloud-spanner-admin-instance-v1| 0.1.11  
com.google.api.grpc| grpc-google-cloud-spanner-v1| 0.1.11  
com.google.api.grpc| grpc-google-common-protos| 0.1.9  
com.google.api.grpc| grpc-google-longrunning-v1| 0.1.11  
com.google.api.grpc| proto-google-cloud-pubsub-v1| 0.1.18  
com.google.api.grpc| proto-google-cloud-spanner-admin-database-v1| 0.1.9  
com.google.api.grpc| proto-google-cloud-spanner-admin-instance-v1| 0.1.11  
com.google.api.grpc| proto-google-cloud-spanner-v1| 0.1.11  
com.google.api.grpc| proto-google-common-protos| 0.1.9  
com.google.api.grpc| proto-google-iam-v1| 0.1.18  
com.google.api.grpc| proto-google-longrunning-v1| 0.1.11  
com.google.apis| google-api-services-bigquery| v2-rev355-1.22.0  
com.google.apis| google-api-services-clouddebugger| v2-rev8-1.22.0  
com.google.apis| google-api-services-cloudresourcemanager| v1-rev6-1.22.0  
com.google.apis| google-api-services-dataflow| v1b3-rev213-1.22.0  
com.google.apis| google-api-services-pubsub| v1-rev10-1.22.0  
com.google.apis| google-api-services-storage| v1-rev71-1.22.0  
com.google.api| api-common| 1.0.0-rc2  
com.google.api| gax| 1.3.1  
com.google.api| gax-grpc| 0.20.0  
com.google.auth| google-auth-library-appengine| 0.7.0  
com.google.auth| google-auth-library-credentials| 0.7.1  
com.google.auth| google-auth-library-oauth2-http| 0.7.1  
com.google.auto.service| auto-service| 1.0-rc2  
com.google.auto| auto-common| 0.3  
com.google.cloud.bigdataoss| gcsio| 1.4.5  
com.google.cloud.bigdataoss| util| 1.4.5  
com.google.cloud.bigtable| bigtable-client-core| 1.0.0-pre3  
com.google.cloud.bigtable| bigtable-protos| 1.0.0-pre3  
com.google.cloud.datastore| datastore-v1-proto-client| 1.4.0  
com.google.cloud| google-cloud-core| 1.0.2  
com.google.cloud| google-cloud-core-grpc| 1.2.0  
com.google.cloud| google-cloud-spanner| 0.20.0-beta  
com.google.code.findbugs| jsr305| 3.0.1  
com.google.code.gson| gson| 2.7  
com.google.errorprone| error_prone_annotations| 2.0.15  
com.google.guava| guava| 20.0  
com.google.http-client| google-http-client| 1.22.0  
com.google.http-client| google-http-client-jackson| 1.22.0  
com.google.http-client| google-http-client-jackson2| 1.22.0  
com.google.http-client| google-http-client-protobuf| 1.22.0  
com.google.instrumentation| instrumentation-api| 0.3.0  
com.google.oauth-client| google-oauth-client| 1.22.0  
com.google.oauth-client| google-oauth-client-java6| 1.22.0  
com.google.protobuf.nano| protobuf-javanano| 3.0.0-alpha-5  
com.google.protobuf| protobuf-java| 3.2.0  
com.google.protobuf| protobuf-java-util| 3.2.0  
commons-codec| commons-codec| 1.3  
commons-logging| commons-logging| 1.2  
com.squareup.okhttp| okhttp| 2.5.0  
com.squareup.okio| okio| 1.6.0  
com.thoughtworks.paranamer| paranamer| 2.7  
io.dropwizard.metrics| metrics-core| 3.1.2  
io.grpc| grpc-all| 1.2.0  
io.grpc| grpc-auth| 1.2.0  
io.grpc| grpc-context| 1.2.0  
io.grpc| grpc-core| 1.2.0  
io.grpc| grpc-netty| 1.2.0  
io.grpc| grpc-okhttp| 1.2.0  
io.grpc| grpc-protobuf| 1.2.0  
io.grpc| grpc-protobuf-lite| 1.2.0  
io.grpc| grpc-protobuf-nano| 1.2.0  
io.grpc| grpc-stub| 1.2.0  
io.netty| netty-buffer| 4.1.8.Final  
io.netty| netty-codec| 4.1.8.Final  
io.netty| netty-codec-http2| 4.1.8.Final  
io.netty| netty-codec-http| 4.1.8.Final  
io.netty| netty-codec-socks| 4.1.8.Final  
io.netty| netty-common| 4.1.8.Final  
io.netty| netty-handler| 4.1.8.Final  
io.netty| netty-handler-proxy| 4.1.8.Final  
io.netty| netty-resolver| 4.1.8.Final  
io.netty| netty-tcnative-boringssl-static| 1.1.33.Fork26  
io.netty| netty-transport| 4.1.8.Final  
joda-time| joda-time| 2.4  
org.apache.avro| avro| 1.8.2  
org.apache.beam| beam-sdks-common-runner-api| 2.2.0  
org.apache.beam| beam-sdks-java-core| 2.2.0  
org.apache.beam| beam-sdks-java-extensions-google-cloud-platform-core| 2.2.0  
org.apache.beam| beam-sdks-java-extensions-protobuf| 2.2.0  
org.apache.beam| beam-sdks-java-io-google-cloud-platform| 2.2.0  
org.apache.commons| commons-compress| 1.14  
org.apache.httpcomponents| httpclient| 4.0.1  
org.apache.httpcomponents| httpcore| 4.0.1  
org.codehaus.jackson| jackson-core-asl| 1.9.13  
org.codehaus.jackson| jackson-mapper-asl| 1.9.13  
org.json| json| 20160810  
org.slf4j| slf4j-api| 1.7.25  
org.threeten| threetenbp| 1.3.3  
org.tukaani| xz| 1.5  
org.xerial.snappy| snappy-java| 1.1.4  
  
Additionally, a Dataflow worker starts with the following logging JARs prepended to the classpath.

GroupId| ArtifactId| Version  
---|---|---  
  
org.apache.logging.log4j| log4j-to-slf4j| 2.5  
org.slf4j| jcl-over-slf4j| 1.7.14  
org.slf4j| log4j-over-slf4j| 1.7.14  
org.slf4j| slf4j-api| 1.7.14  
org.slf4j| slf4j-jdk14| 1.7.14  
  
#### Version 2.1.0

Dataflow SDK 2.1.0 for Java has the following compile and runtime dependencies.

GroupId| ArtifactId| Version  
---|---|---  
  
com.fasterxml.jackson.core| jackson-annotations| 2.8.8  
com.fasterxml.jackson.core| jackson-core| 2.8.8  
com.fasterxml.jackson.core| jackson-databind| 2.8.8  
com.google.api-client| google-api-client| 1.22.0  
com.google.api-client| google-api-client-jackson2| 1.20.0  
com.google.api-client| google-api-client-java6| 1.20.0  
com.google.api.grpc| grpc-google-cloud-spanner-admin-database-v1| 0.1.11  
com.google.api.grpc| grpc-google-cloud-spanner-admin-instance-v1| 0.1.11  
com.google.api.grpc| grpc-google-cloud-spanner-v1| 0.1.11  
com.google.api.grpc| grpc-google-common-protos| 0.1.0  
com.google.api.grpc| grpc-google-iam-v1| 0.1.0  
com.google.api.grpc| grpc-google-longrunning-v1| 0.1.11  
com.google.api.grpc| grpc-google-pubsub-v1| 0.1.0  
com.google.api.grpc| proto-google-cloud-spanner-admin-database-v1| 0.1.9  
com.google.api.grpc| proto-google-cloud-spanner-admin-instance-v1| 0.1.11  
com.google.api.grpc| proto-google-cloud-spanner-v1| 0.1.11  
com.google.api.grpc| proto-google-common-protos| 0.1.9  
com.google.api.grpc| proto-google-iam-v1| 0.1.11  
com.google.api.grpc| proto-google-longrunning-v1| 0.1.11  
com.google.apis| google-api-services-bigquery| v2-rev295-1.22.0  
com.google.apis| google-api-services-clouddebugger| v2-rev8-1.22.0  
com.google.apis| google-api-services-cloudresourcemanager| v1-rev6-1.22.0  
com.google.apis| google-api-services-dataflow| v1b3-rev196-1.22.0  
com.google.apis| google-api-services-pubsub| v1-rev10-1.22.0  
com.google.apis| google-api-services-storage| v1-rev71-1.22.0  
com.google.api| api-common| 1.1.0  
com.google.api| gax| 1.3.1  
com.google.api| gax-grpc| 0.20.0  
com.google.auth| google-auth-library-appengine| 0.6.1  
com.google.auth| google-auth-library-credentials| 0.7.1  
com.google.auth| google-auth-library-oauth2-http| 0.7.1  
com.google.auto.service| auto-service| 1.0-rc2  
com.google.auto| auto-common| 0.3  
com.google.cloud.bigdataoss| gcsio| 1.4.5  
com.google.cloud.bigdataoss| util| 1.4.5  
com.google.cloud.bigtable| bigtable-client-core| 0.9.7.1  
com.google.cloud.bigtable| bigtable-protos| 0.9.7.1  
com.google.cloud.datastore| datastore-v1-proto-client| 1.4.0  
com.google.cloud.datastore| datastore-v1-protos| 1.3.0  
com.google.cloud| google-cloud-core| 1.0.2  
com.google.cloud| google-cloud-core-grpc| 1.2.0  
com.google.cloud| google-cloud-spanner| 0.20.0-beta  
com.google.code.findbugs| jsr305| 3.0.1  
com.google.code.gson| gson| 2.7  
com.google.guava| guava| 20.0  
com.google.http-client| google-http-client| 1.22.0  
com.google.http-client| google-http-client-jackson| 1.22.0  
com.google.http-client| google-http-client-jackson2| 1.22.0  
com.google.http-client| google-http-client-protobuf| 1.20.0  
com.google.instrumentation| instrumentation-api| 0.3.0  
com.google.oauth-client| google-oauth-client| 1.22.0  
com.google.oauth-client| google-oauth-client-java6| 1.20.0  
com.google.protobuf.nano| protobuf-javanano| 3.0.0-alpha-5  
com.google.protobuf| protobuf-java| 3.2.0  
com.google.protobuf| protobuf-java-util| 3.2.0  
commons-codec| commons-codec| 1.3  
commons-logging| commons-logging| 1.2  
com.squareup.okhttp| okhttp| 2.5.0  
com.squareup.okio| okio| 1.6.0  
com.thoughtworks.paranamer| paranamer| 2.7  
io.dropwizard.metrics| metrics-core| 3.1.2  
io.grpc| grpc-all| 1.2.0  
io.grpc| grpc-auth| 1.2.0  
io.grpc| grpc-context| 1.2.0  
io.grpc| grpc-core| 1.2.0  
io.grpc| grpc-netty| 1.2.0  
io.grpc| grpc-okhttp| 1.2.0  
io.grpc| grpc-protobuf| 1.2.0  
io.grpc| grpc-protobuf-lite| 1.2.0  
io.grpc| grpc-protobuf-nano| 1.2.0  
io.grpc| grpc-stub| 1.2.0  
io.netty| netty-buffer| 4.1.8.Final  
io.netty| netty-codec| 4.1.8.Final  
io.netty| netty-codec-http2| 4.1.8.Final  
io.netty| netty-codec-http| 4.1.8.Final  
io.netty| netty-codec-socks| 4.1.8.Final  
io.netty| netty-common| 4.1.8.Final  
io.netty| netty-handler| 4.1.8.Final  
io.netty| netty-handler-proxy| 4.1.8.Final  
io.netty| netty-resolver| 4.1.8.Final  
io.netty| netty-tcnative-boringssl-static| 1.1.33.Fork18  
io.netty| netty-transport| 4.1.8.Final  
io.netty| netty-transport-native-epoll| linux-x86_64:4.1.8.Final  
javax.servlet| javax.servlet-api| 3.1.0  
joda-time| joda-time| 2.4  
org.apache.avro| avro| 1.8.1  
org.apache.beam| beam-runners-core-construction-java| 2.1.0  
org.apache.beam| beam-runners-core-java| 2.1.0  
org.apache.beam| beam-runners-google-cloud-dataflow-java| 2.1.0  
org.apache.beam| beam-sdks-common-fn-api| 2.1.0  
org.apache.beam| beam-sdks-common-runner-api| 2.1.0  
org.apache.beam| beam-sdks-java-core| 2.1.0  
org.apache.beam| beam-sdks-java-extensions-google-cloud-platform-core| 2.1.0  
org.apache.beam| beam-sdks-java-extensions-protobuf| 2.1.0  
org.apache.beam| beam-sdks-java-harness| 2.1.0  
org.apache.beam| beam-sdks-java-io-google-cloud-platform| 2.1.0  
org.apache.commons| commons-compress| 1.8.1  
org.apache.httpcomponents| httpclient| 4.0.1  
org.apache.httpcomponents| httpcore| 4.0.1  
org.codehaus.jackson| jackson-core-asl| 1.9.13  
org.codehaus.jackson| jackson-mapper-asl| 1.9.13  
org.eclipse.jetty| jetty-http| 9.2.10.v20150310  
org.eclipse.jetty| jetty-io| 9.2.10.v20150310  
org.eclipse.jetty| jetty-security| 9.2.10.v20150310  
org.eclipse.jetty| jetty-server| 9.2.10.v20150310  
org.eclipse.jetty| jetty-servlet| 9.2.10.v20150310  
org.eclipse.jetty| jetty-util| 9.2.10.v20150310  
org.json| json| 20160810  
org.slf4j| slf4j-api| 1.7.14  
org.slf4j| slf4j-jdk14| 1.7.14  
org.threeten| threetenbp| 1.3.3  
org.tukaani| xz| 1.5  
org.xerial.snappy| snappy-java| 1.1.4-M3  
  
Additionally, a Dataflow worker starts with the following logging JARs prepended to the classpath.

GroupId| ArtifactId| Version  
---|---|---  
  
org.apache.logging.log4j| log4j-to-slf4j| 2.5  
org.slf4j| jcl-over-slf4j| 1.7.14  
org.slf4j| log4j-over-slf4j| 1.7.14  
org.slf4j| slf4j-api| 1.7.14  
org.slf4j| slf4j-jdk14| 1.7.14  
  
### SDK for Python

#### Version 2.5.0

Dataflow SDK 2.5.0 for Python has the following dependencies.

Package| Version  
---|---  
  
avro| >=1.8.1, <2.0.0  
crcmod| >=1.7, <2.0  
dill| 0.2.6  
future| >=0.16.0, <1.0.0  
futures| >=3.1.1, <4.0.0  
google-apitools| >=0.5.18, <=0.5.20  
google-cloud-pubsub| 0.26.0  
google-cloud-bigquery| 0.25.0  
googledatastore| 7.0.1  
grpcio| >=1.8, <2.0  
hdfs| >=2.1.0, <3.0.0  
httplib2| >=0.8, <0.10  
mock| >=1.0.1, <3.0.0  
nose| >=1.3.7  
oauth2client| >=2.0.1, <5.0.0  
proto-google-cloud-datastore-v1| >=0.90.0, <=0.90.4  
proto-google-cloud-pubsub-v1| 0.15.4  
protobuf| >=3.5.0.post1, <4  
pyhamcrest| >=1.9, <2.0  
pytz| >=2018.3  
pyvcf| >=0.6.8, <0.7.0  
pyyaml| >=3.12, <4.0.0  
six| >=1.9, <1.12  
typing| >=3.6.0, <3.7.0  
  
Dataflow workers have the following packages already installed.

Package| Version  
---|---  
  
avro| 1.8.2  
beautifulsoup4| 4.5.1  
bs4| 0.0.1  
crcmod| 1.7  
cython| 0.28.1  
dill| 0.2.6  
future| 0.16.0  
futures| 3.1.1  
grpcio| 1.10.0  
google-apitools| 0.5.20  
google-cloud-bigquery| 0.25.0  
google-cloud-pubsub| 0.26.0  
google-python-cloud-debugger| 1.9.1  
googledatastore| 7.0.1  
guppy| 0.1.10  
hdfs| 2.1.0  
httplib2| 0.9.2  
mock| 2.0.0  
nltk| 3.2.1  
nose| 1.3.7  
numpy| 1.13.3  
oauth2client| 4.1.2  
pandas| 0.18.1  
pillow| 3.4.1  
proto-google-cloud-datastore-v1| 0.90.4  
proto-google-cloud-pubsub-v1| 0.15.4  
protobuf| 3.5.1  
protorpc| 0.11.1  
python-gflags| 3.0.6  
python-snappy| 0.5.1  
pytz| 2018.4  
pyvcf| 0.6.8  
pyyaml| 3.12  
requests| 2.18.4  
scikit-learn| 0.19.1  
scipy| 1.0.0  
six| 1.10.0  
tensorflow| 1.8.0  
typing| 3.6.1  
wheel| 0.29.0  
  
#### Version 2.4.0

Dataflow SDK 2.4.0 for Python has the following dependencies.

Package| Version  
---|---  
  
avro| >=1.8.1, <2.0.0  
crcmod| >=1.7, <2.0  
dill| 0.2.6  
futures| >=3.1.1, <4.0.0  
google-apitools| >=0.5.18, <=0.5.20  
google-cloud-pubsub| 0.26.0  
google-cloud-bigquery| 0.25.0  
googledatastore| 7.0.1  
grpcio| >=1.0, <2.0  
hdfs| >=2.1.0, <3.0.0  
httplib2| >=0.8, <0.10  
mock| >=1.0.1, <3.0.0  
nose| >=1.0  
oauth2client| >=2.0.1, <5.0.0  
proto-google-cloud-datastore-v1| >=0.90.0, <=0.90.4  
protobuf| >=3.5.0.post1, <4  
pyhamcrest| >=1.9, <2.0  
pyvcf| >=0.6.8, <0.7.0  
pyyaml| >=3.12, <4.0.0  
six| >=1.9, <1.12  
typing| >=3.6.0, <3.7.0  
  
Dataflow workers have the following packages already installed.

Package| Version  
---|---  
  
avro| 1.8.2  
beautifulsoup4| 4.5.1  
bs4| 0.0.1  
crcmod| 1.7  
cython| 0.27.3  
dill| 0.2.6  
futures| 3.1.1  
grpcio| 1.3.0  
google-apitools| 0.5.20  
google-cloud-bigquery| 0.25.0  
google-cloud-pubsub| 0.26.0  
google-python-cloud-debugger| 1.9.1  
googledatastore| 7.0.1  
guppy| 0.1.10  
hdfs3| 0.3.0  
httplib2| 0.9.2  
mock| 2.0.0  
nltk| 3.2.1  
nose| 1.3.7  
numpy| 1.13.3  
oauth2client| 4.1.2  
pandas| 0.18.1  
pillow| 3.4.1  
proto-google-cloud-datastore-v1| 0.90.4  
protobuf| 3.5.1  
protorpc| 0.11.1  
python-gflags| 3.0.6  
python-snappy| 0.5.1  
pyvcf| 0.6.8  
pyyaml| 3.12  
requests| 2.18.4  
scikit-learn| 0.19.1  
scipy| 1.0.0  
six| 1.10.0  
tensorflow| 1.6.0  
typing| 3.6.1  
wheel| 0.29.0  
  
#### Version 2.3.0

Dataflow SDK 2.3.0 for Python has the following dependencies.

Package| Version  
---|---  
  
avro| >=1.8.1, <2.0.0  
crcmod| >=1.7, <2.0  
dill| 0.2.6  
futures| >=3.1.1, <4.0.0  
google-apitools| >=0.5.18, <=0.5.20  
google-cloud-pubsub| 0.26.0  
google-cloud-bigquery| 0.25.0  
googledatastore| 7.0.1  
grpcio| >=1.0, <2.0  
hdfs2| >=0.3.0, <4.0.0  
httplib2| >=0.8, <0.10  
mock| >=1.0.1, <3.0.0  
nose| >=1.0  
oauth2client| >=2.0.1, <5.0.0  
proto-google-cloud-datastore-v1| >=0.90.0, <=0.90.4  
protobuf| >=3.5.0.post1, <4  
pyhamcrest| >=1.9, <2.0  
pyvcf| >=0.6.8, <0.7.0  
pyyaml| >=3.12, <4.0.0  
six| >=1.9, <1.11  
typing| >=3.6.0, <3.7.0  
  
Dataflow workers have the following packages already installed. Note: The Dataflow worker container OS was upgraded from Debian 8 to Debian 9 in this version.

Package| Version  
---|---  
  
avro| 1.8.2  
beautifulsoup4| 4.5.1  
bs4| 0.0.1  
crcmod| 1.7  
cython| 0.27.3  
dill| 0.2.6  
futures| 3.1.1  
grpcio| 1.3.0  
google-apitools| 0.5.20  
google-cloud-bigquery| 0.25.0  
google-cloud-pubsub| 0.26.0  
google-python-cloud-debugger| 1.9.1  
googledatastore| 7.0.1  
guppy| 0.1.10  
hdfs3| 0.3.0  
httplib2| 0.9.2  
mock| 2.0.0  
nltk| 3.2.1  
nose| 1.3.7  
numpy| 1.13.3  
oauth2client| 4.1.2  
pandas| 0.18.1  
pillow| 3.4.1  
proto-google-cloud-datastore-v1| 0.90.4  
protobuf| 3.5.1  
protorpc| 0.11.1  
python-gflags| 3.0.6  
python-snappy| 0.5.1  
pyvcf| 0.6.8  
pyyaml| 3.12  
requests| 2.18.4  
scikit-learn| 0.19.1  
scipy| 1.0.0  
six| 1.10.0  
tensorflow| 1.5.0  
typing| 3.6.1  
wheel| 0.29.0  
  
#### Version 2.2.0

Dataflow SDK 2.2.0 for Python has the following dependencies.

Package| Version  
---|---  
  
avro| >=1.8.1, <2.0.0  
crcmod| >=1.7, <2.0  
dill| 0.2.6  
google-apitools| >=0.5.10, <=0.5.11  
google-cloud-pubsub| 0.26.0  
google-cloud-bigquery| 0.25.0  
googledatastore| 7.0.1  
grpcio| >=1.0, <2.0  
httplib2| >=0.8, <0.10  
mock| >=1.0.1, <3.0.0  
nose| >=1.0  
oauth2client| >=2.0.1, <4.0.0  
proto-google-cloud-datastore-v1| >=0.90.0, <=0.90.4  
protobuf| >=3.2.0, <=3.3.0  
pyhamcrest| >=1.9, <2.0  
pyyaml| >=3.12, <4.0.0  
six| >=1.9, <1.11  
typing| >=3.6.0, <3.7.0  
  
Dataflow workers have the following packages already installed.

Package| Version  
---|---  
  
avro| 1.8.2  
beautifulsoup4| 4.5.1  
bs4| 0.0.1  
crcmod| 1.7  
cython| 0.27.2  
dill| 0.2.6  
grpcio| 0.3.0  
google-apitools| 0.5.11  
google-cloud-bigquery| 0.25.0  
google-cloud-pubsub| 0.26.0  
google-python-cloud-debugger| 1.9.1  
googledatastore| 7.0.1  
guppy| 0.1.10  
httplib2| 0.9.2  
mock| 2.0.0  
nltk| 3.2.1  
nose| 1.3.7  
numpy| 1.13.3  
oauth2client| 3.0.0  
pandas| 0.18.1  
pillow| 3.4.1  
proto-google-cloud-datastore-v1| 0.90.4  
protobuf| 3.3.0  
protorpc| 0.11.1  
python-gflags| 3.0.6  
python-snappy| 0.5.1  
pyyaml| 3.12  
requests| 2.18.4  
scikit-learn| 0.17.1  
scipy| 1.0.0  
six| 1.10.0  
tensorflow| 1.4.0  
typing| 3.6.1  
wheel| 0.29.0  
  
## Dataflow 1.x SDKs

### SDK for Java

#### Version 1.9.1

Dataflow SDK 1.9.1 for Java has the following compile and runtime dependencies.

GroupId| ArtifactId| Version  
---|---|---  
  
com.fasterxml.jackson.core| jackson-annotations| 2.7.0  
com.fasterxml.jackson.core| jackson-core| 2.7.0  
com.fasterxml.jackson.core| jackson-databind| 2.7.0  
com.google.api-client| google-api-client-jackson2| 1.22.0  
com.google.api-client| google-api-client-java6| 1.22.0  
com.google.api-client| google-api-client| 1.22.0  
com.google.api.grpc| grpc-core-proto| 0.0.3  
com.google.api.grpc| grpc-pubsub-v1| 0.0.2  
com.google.apis| google-api-services-bigquery| v2-rev295-1.22.0  
com.google.apis| google-api-services-clouddebugger| v2-rev8-1.22.0  
com.google.apis| google-api-services-dataflow| v1b3-rev36-1.22.0  
com.google.apis| google-api-services-datastore-protobuf| v1beta2-rev1-4.0.0  
com.google.apis| google-api-services-pubsub| v1-rev10-1.22.0  
com.google.apis| google-api-services-storage| v1-rev71-1.22.0  
com.google.auth| google-auth-library-credentials| 0.4.0  
com.google.auth| google-auth-library-oauth2-http| 0.4.0  
com.google.auto.service| auto-service| 1.0-rc2  
com.google.auto| auto-common| 0.3  
com.google.cloud.bigdataoss| gcsio| 1.4.5  
com.google.cloud.bigdataoss| util| 1.4.5  
com.google.cloud.bigtable| bigtable-protos| 0.3.0  
com.google.cloud.datastore| datastore-v1-proto-client| 1.1.0  
com.google.cloud.datastore| datastore-v1-protos| 1.0.1  
com.google.code.findbugs| jsr305| 3.0.1  
com.google.http-client| google-http-client-jackson| 1.22.0  
com.google.http-client| google-http-client-jackson2| 1.22.0  
com.google.http-client| google-http-client-protobuf| 1.22.0  
com.google.oauth-client| google-oauth-client-java6| 1.22.0  
com.google.oauth-client| google-oauth-client| 1.22.0  
com.google.protobuf.nano| protobuf-javanano| 3.0.0-alpha-5  
com.google.protobuf| protobuf-java| 3.0.0-beta-1  
com.squareup.okhttp| okhttp| 2.5.0  
com.squareup.okio| okio| 1.6.0  
com.thoughtworks.paranamer| paranamer| 2.3  
commons-codec| commons-codec| 1.3  
commons-logging| commons-logging| 1.1.1  
io.grpc| grpc-all| 0.13.1  
io.grpc| grpc-auth| 0.13.1  
io.grpc| grpc-core| 0.13.1  
io.grpc| grpc-netty| 0.13.1  
io.grpc| grpc-okhttp| 0.13.1  
io.grpc| grpc-protobuf-nano| 0.13.1  
io.grpc| grpc-protobuf| 0.13.1  
io.grpc| grpc-stub| 0.13.1  
io.netty| netty-buffer| 4.1.0.CR1  
io.netty| netty-codec-http| 4.1.0.CR1  
io.netty| netty-codec-http2| 4.1.0.CR1  
io.netty| netty-codec| 4.1.0.CR1  
io.netty| netty-common| 4.1.0.CR1  
io.netty| netty-handler| 4.1.0.CR1  
io.netty| netty-resolver| 4.1.0.CR1  
io.netty| netty-transport| 4.1.0.CR1  
joda-time| joda-time| 2.4  
org.apache.avro| avro| 1.7.7  
org.apache.commons| commons-compress| 1.9  
org.apache.httpcomponents| httpclient| 4.0.1  
org.apache.httpcomponents| httpcore| 4.0.1  
org.codehaus.jackson| jackson-core-asl| 1.9.13  
org.codehaus.jackson| jackson-mapper-asl| 1.9.13  
org.codehaus.woodstox| stax2-api| 3.1.4  
org.codehaus.woodstox| woodstox-core-asl| 4.4.1  
org.slf4j| slf4j-api| 1.7.14  
org.tukaani| xz| 1.5  
org.xerial.snappy| snappy-java| 1.1.2.1  
  
Additionally, a Dataflow worker starts with the following logging JARs prepended to the classpath.

GroupId| ArtifactId| Version  
---|---|---  
  
org.apache.logging.log4j| log4j-to-slf4j| 2.5  
org.slf4j| jcl-over-slf4j| 1.7.14  
org.slf4j| log4j-over-slf4j| 1.7.14  
org.slf4j| slf4j-api| 1.7.14  
org.slf4j| slf4j-jdk14| 1.7.14  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
