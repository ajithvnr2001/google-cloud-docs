---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/blobstore/blobstore/
title: Module: google.appengine.ext.blobstore.blobstore \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:42:01.314591+00:00
---

# Module: google.appengine.ext.blobstore.blobstore  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/blobstore/blobstore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Module: google.appengine.ext.blobstore.blobstore Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/blobstore/blobstore.py) A Python blobstore API used by app developers. This module contains methods that are used to interface with Blobstore API. The module includes a [`db.Model`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/Model)-like class that represents a reference to a very large blob. The module imports a `db.Key`-like class that represents a blob key.

## Classes

[`class BlobInfo`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/blobstore/BlobInfo): Information about blobs in Blobstore. [`class BlobInfoParseError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/blobstore/BlobInfoParseError): The CGI parameter does not contain a valid `BlobInfo` record. [`class BlobMigrationRecord`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/blobstore/BlobMigrationRecord): Defines a model that records the result of a blob migration. [`class BlobReader`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/blobstore/BlobReader): Provides a read-only file-like interface to a blobstore blob. [`class BlobReferenceProperty`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/blobstore/BlobReferenceProperty): Property compatible with [`db.Model`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/Model) classes. [`class BlobstoreDownloadHandler`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/blobstore/BlobstoreDownloadHandler): Base class for creating handlers that may send blobs to users. [`class BlobstoreUploadHandler`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/blobstore/BlobstoreUploadHandler): Base class for creation blob upload handlers. [`class FileInfo`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/blobstore/FileInfo): Details information about uploaded files. [`class FileInfoParseError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/blobstore/FileInfoParseError): The CGI parameter does not contain a valid `FileInfo` record. [`class RangeFormatError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/blobstore/RangeFormatError): Raised when Range header incorrectly formatted. [`class UnsupportedRangeFormatError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/blobstore/UnsupportedRangeFormatError): Raised when Range format is correct, but not supported.

## Functions

[`fetch_data(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/blobstore/fetch_data): Fetches data for a blob. [`fetch_data_async(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/blobstore/fetch_data_async): Asynchronously fetches data for a blob. [`get(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/blobstore/get): Gets a `BlobInfo` record from blobstore. [`parse_blob_info(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/blobstore/parse_blob_info): Parses a `BlobInfo` record from file upload `field_storage`. [`parse_file_info(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/blobstore/parse_file_info): Parses a `FileInfo` record from file upload `field_storage`. | 

## Other Members  
  
---  
  
BLOB_INFO_KIND |  `'__BlobInfo__'`  
BLOB_KEY_HEADER |  `'X-AppEngine-BlobKey'`  
BLOB_MIGRATION_KIND |  `'__BlobMigration__'`  
BLOB_RANGE_HEADER |  `'X-AppEngine-BlobRange'`  
CLOUD_STORAGE_OBJECT_HEADER |  `'X-AppEngine-Cloud-Storage-Object'`  
GS_PREFIX |  `'/gs/'`  
MAX_BLOB_FETCH_SIZE |  `1015808`  
UPLOAD_INFO_CREATION_HEADER |  `'X-AppEngine-Upload-Creation'`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
