---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/blobstore/blob_storage/BlobStorage/
title: google.appengine.api.blobstore.blob_storage.BlobStorage \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:01:49.527362+00:00
---

# google.appengine.api.blobstore.blob_storage.BlobStorage  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/blobstore/blob_storage/BlobStorage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.blobstore.blob_storage.BlobStorage Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/blobstore/blob_storage.py#L20-L55) Base class for defining how blobs are stored. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type) This base class merely defines an interface that all stub blob-storage mechanisms must implement.

## Methods

### `DeleteBlob`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/blobstore/blob_storage.py#L49-L55)
    
    
    DeleteBlob(
        blob_key
    )
    

Delete blob data from storage. | Args  
---  
  
`blob_key` |  Blob-key of existing blob to delete.   
  
### `OpenBlob`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/blobstore/blob_storage.py#L38-L47)
    
    
    OpenBlob(
        blob_key
    )
    

Open blob for streaming.

Args  
---  
  
`blob_key` |  Blob-key of existing blob to open for reading.   
  
Returns  
---  
Open file stream for reading blob. Caller is responsible for closing file.   
  
### `StoreBlob`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/blobstore/blob_storage.py#L27-L36)
    
    
    StoreBlob(
        blob_key, blob_stream
    )
    

Store blob stream.

Implement this method to persist blob data.

Args  
---  
  
`blob_key` |  Blob key of blob to store.   
`blob_stream` |  Stream or stream-like object that will generate blob content.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
