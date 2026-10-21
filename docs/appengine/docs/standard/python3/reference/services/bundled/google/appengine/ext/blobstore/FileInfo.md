---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/blobstore/FileInfo/
title: google.appengine.ext.blobstore.FileInfo \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:04:24.888385+00:00
---

# google.appengine.ext.blobstore.FileInfo  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/blobstore/FileInfo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.ext.blobstore.FileInfo Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/blobstore/blobstore.py#L607-L690) Details information about uploaded files. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)

#### View aliases

**Main aliases** `google.appengine.ext.blobstore.blobstore.FileInfo`
    
    
    google.appengine.ext.blobstore.FileInfo(
        filename=None,
        content_type=None,
        creation=None,
        size=None,
        md5_hash=None,
        gs_object_name=None
    )
    

This class contains information about blobs stored by an application. This class is similar to `BlobInfo`; however, this method does not make use of a key, and the information is not persisted in the datastore.

#### Properties:

  * content_type: The content type of the uploaded file.
  * creation: The creation date of the uploaded file, or when it was uploaded.
  * filename: The file name that the user selected from their machine.
  * size: The size of the uncompressed file.
  * md5_hash: The MD5 hash value of the uploaded file.
  * gs_object_name: The name of the file that was written to Google Cloud Storage, or `None` if the file was not uploaded to Google Cloud Storage.

All properties are read-only. Attempting to assign a value to a property will raise an `AttributeError`. | 

## Attributes  
  
---  
  
`content_type` |  Returns the content type of the uploaded file.   
`creation` |  Returns the creation date or upload time of the file.   
`filename` |  Returns the file name that the user selected.   
`gs_object_name` |  Returns the name of the file that was written to Cloud Storage.   
`md5_hash` |  Returns the MD5 hash of the uploaded file.   
`size` |  Returns the size of the uncompressed file.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
