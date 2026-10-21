---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/blobstore/blobstore/
title: Module: google.appengine.api.blobstore.blobstore \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:30:06.589713+00:00
---

# Module: google.appengine.api.blobstore.blobstore  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/blobstore/blobstore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Module: google.appengine.api.blobstore.blobstore Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/blobstore/blobstore.py) Blobstore API. This module contains methods that you can use to interface with the Blobstore API. The module defines a `db.Key`-like class that represents a blob key.

## Classes

[`class BlobFetchSizeTooLargeError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/blobstore/BlobFetchSizeTooLargeError): The block could not be fetched because it was too large. [`class BlobNotFoundError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/blobstore/BlobNotFoundError): The blob does not exist. [`class DataIndexOutOfRangeError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/blobstore/DataIndexOutOfRangeError): The indexes could not be accessed. [`class Error`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/blobstore/Error): Base blobstore error type. [`class InternalError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/blobstore/InternalError): An internal error occured. [`class PermissionDeniedError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/blobstore/PermissionDeniedError): The operation did not complete; review the permissions required.

## Functions

[`create_gs_key(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/blobstore/create_gs_key): Creates an encoded key for a Google Cloud Storage file. [`create_gs_key_async(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/blobstore/create_gs_key_async): Asynchronously creates an encoded key for a Google Cloud Storage file. [`create_rpc(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/blobstore/create_rpc): Creates an RPC object to use with the Blobstore API. [`create_upload_url(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/blobstore/create_upload_url): Creates the upload URL for a POST form. [`create_upload_url_async(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/blobstore/create_upload_url_async): Asynchronously creates the upload URL for a POST form. [`delete(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/blobstore/delete): Deletes a blob from Blobstore. [`delete_async(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/blobstore/delete_async): Asynchronously deletes a blob from Blobstore. [`fetch_data(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/blobstore/fetch_data): Fetches the data for a blob. [`fetch_data_async(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/blobstore/fetch_data_async): Asynchronously fetches the data for a blob. | 

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
