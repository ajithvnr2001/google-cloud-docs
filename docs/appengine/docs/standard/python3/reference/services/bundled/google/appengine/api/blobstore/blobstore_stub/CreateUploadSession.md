---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/blobstore/blobstore_stub/CreateUploadSession/
title: google.appengine.api.blobstore.blobstore_stub.CreateUploadSession \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:27:54.924069+00:00
---

# google.appengine.api.blobstore.blobstore_stub.CreateUploadSession  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/blobstore/blobstore_stub/CreateUploadSession/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.blobstore.blobstore_stub.CreateUploadSession Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/blobstore/blobstore_stub.py#L76-L110) Create upload session in datastore.
    
    
    google.appengine.api.blobstore.blobstore_stub.CreateUploadSession(
        creation,
        success_path,
        user,
        max_bytes_per_blob,
        max_bytes_total,
        bucket_name=None
    )
    

Creates an upload session and puts it in Datastore to be referenced by upload handler later. | 

## Args  
  
---  
  
`creation` |  Creation timestamp.   
`success_path` |  Path in users application to call upon success.   
`user` |  User that initiated this upload, if any.   
`max_bytes_per_blob` |  Maximum number of bytes for any blob in the upload.   
`max_bytes_total` |  Maximum aggregate bytes for all blobs in the upload.   
`bucket_name` |  Name of the Google Storage bucket tio upload the files.   
  
## Returns  
  
---  
String encoded key of new Datastore entity.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
