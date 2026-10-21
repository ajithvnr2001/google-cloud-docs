---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_pbs/
title: Module: google.appengine.datastore.datastore_pbs \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:57:16.240385+00:00
---

# Module: google.appengine.datastore.datastore_pbs  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_pbs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Module: google.appengine.datastore.datastore_pbs Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_pbs.py) Utilities for converting between v3 and v1 datastore protocol buffers. This module is internal and should not be used by client applications.

## Classes

[`class IdResolver`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_pbs/IdResolver): A class that can handle project id <\--> application id transformations. [`class InvalidConversionError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_pbs/InvalidConversionError): Raised when conversion fails.

## Functions

[`check_conversion(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_pbs/check_conversion): Asserts a conversion condition and raises an error if it's not met. [`copy_path_element(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_pbs/copy_path_element) [`get_entity_converter(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_pbs/get_entity_converter): Returns a converter for v3 and v1 entities and keys. [`get_v1_mutation_key_and_entity(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_pbs/get_v1_mutation_key_and_entity): Returns the v1 key and entity for a v1 mutation proto, if applicable. [`is_complete_v1_key(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_pbs/is_complete_v1_key): Returns `True` if a key specifies an ID or name, `False` otherwise. [`is_complete_v3_key(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_pbs/is_complete_v3_key): Returns `True` if a key specifies an ID or name, `False` otherwise. [`is_complete_v4_key(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_pbs/is_complete_v4_key): Returns True if a key specifies an ID or name, False otherwise. [`is_in_rfc_3339_bounds(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_pbs/is_in_rfc_3339_bounds) [`is_valid_utf8(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_pbs/is_valid_utf8) [`v1_key_to_string(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_pbs/v1_key_to_string): Generates a string representing a key's path. [`v4_key_to_string(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_pbs/v4_key_to_string): Generates a string representing a key's path. | 

## Other Members  
  
---  
  
DEFAULT_GAIA_ID |  `0`  
MAX_DATASET_ID_LENGTH |  `302`  
MAX_DATASET_ID_SECTION_LENGTH |  `100`  
MAX_INDEXED_BLOB_BYTES |  `500`  
MAX_INDEXED_STRING_CHARS |  `500`  
MAX_KEY_PATH_LENGTH |  `100`  
MAX_PARTITION_ID_LENGTH |  `100`  
MAX_URL_CHARS |  `2083`  
MEANING_ATOM_AUTHOR |  `6`  
MEANING_ATOM_CATEGORY |  `1`  
MEANING_ATOM_CONTENT |  `4`  
MEANING_ATOM_SUMMARY |  `5`  
MEANING_ATOM_TITLE |  `3`  
MEANING_BLOBKEY |  `17`  
MEANING_BYTESTRING |  `16`  
MEANING_EMPTY_LIST |  `24`  
MEANING_GD_EMAIL |  `8`  
MEANING_GD_IM |  `10`  
MEANING_GD_PHONENUMBER |  `11`  
MEANING_GD_POSTALADDRESS |  `12`  
MEANING_GEORSS_POINT |  `9`  
MEANING_INDEX_ONLY |  `18`  
MEANING_NON_RFC_3339_TIMESTAMP |  `7`  
MEANING_PERCENT |  `13`  
MEANING_POINT_WITHOUT_V3_MEANING |  `23`  
MEANING_PREDEFINED_ENTITY_POINT |  `21`  
MEANING_PREDEFINED_ENTITY_USER |  `20`  
MEANING_TEXT |  `15`  
MEANING_URL |  `2`  
MEANING_ZLIB |  `22`  
MISSING_CLOUD_DATASTORE_MESSAGE |  `('Could not import googledatastore. This library must be installed with ' 'version >= 6.0.0 to use the Cloud Datastore API.')`  
PROPERTY_NAME_AUTH_DOMAIN |  `'auth_domain'`  
PROPERTY_NAME_EMAIL |  `'email'`  
PROPERTY_NAME_FEDERATED_IDENTITY |  `'federated_identity'`  
PROPERTY_NAME_FEDERATED_PROVIDER |  `'federated_provider'`  
PROPERTY_NAME_INTERNAL_ID |  `'internal_id'`  
PROPERTY_NAME_KEY |  `'__key__'`  
PROPERTY_NAME_USER_ID |  `'user_id'`  
PROPERTY_NAME_X |  `'x'`  
PROPERTY_NAME_Y |  `'y'`  
RFC_3339_MAX_MICROSECONDS_INCLUSIVE |  `253402300799999999`  
RFC_3339_MIN_MICROSECONDS_INCLUSIVE |  `-62135596800000000`  
URI_MEANING_ZLIB |  `'ZLIB'`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
