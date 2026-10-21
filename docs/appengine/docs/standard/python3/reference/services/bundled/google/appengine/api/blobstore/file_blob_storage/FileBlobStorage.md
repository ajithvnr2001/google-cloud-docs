---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/blobstore/file_blob_storage/FileBlobStorage/
title: google.appengine.api.blobstore.file_blob_storage.FileBlobStorage \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:30:48.412400+00:00
---

# google.appengine.api.blobstore.file_blob_storage.FileBlobStorage  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/blobstore/file_blob_storage/FileBlobStorage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.blobstore.file_blob_storage.FileBlobStorage Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/blobstore/file_blob_storage.py#L51-L166) The storage mechanism that stores blob data on a local disk. Inherits From: [`BlobStorage`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/blobstore/blob_storage/BlobStorage), [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.api.blobstore.file_blob_storage.FileBlobStorage(
        storage_directory, app_id
    )
    

| 

## Args  
  
---  
  
`storage_directory` |  Directory within which to store blobs.   
`app_id` |  The application ID on whose behalf to store blobs.   
  
## Methods

### `DeleteBlob`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/blobstore/file_blob_storage.py#L154-L166)
    
    
    DeleteBlob(
        blob_key
    )
    

Deletes blob data.

Deleting an unknown blob will not raise an error.

Args  
---  
  
`blob_key` |  The blob key of an existing blob that you want to delete.   
  
### `OpenBlob`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/blobstore/file_blob_storage.py#L143-L152)
    
    
    OpenBlob(
        blob_key
    )
    

Opens a blob file for streaming.

Args  
---  
  
`blob_key` |  The blob key of an existing blob that you want to open.   
  
Returns  
---  
An open file stream to read the blob.   
  
### `StoreBlob`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/blobstore/file_blob_storage.py#L117-L141)
    
    
    StoreBlob(
        blob_key, blob_stream
    )
    

Stores a blob stream .

Args  
---  
  
`blob_key` |  The blob key of the blob that you want to store.   
`blob_stream` |  A stream or a stream-like object that will generate blob content.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
