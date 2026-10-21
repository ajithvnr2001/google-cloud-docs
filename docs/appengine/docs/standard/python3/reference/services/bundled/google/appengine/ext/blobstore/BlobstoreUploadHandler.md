---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/blobstore/BlobstoreUploadHandler/
title: google.appengine.ext.blobstore.BlobstoreUploadHandler \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:58:46.157984+00:00
---

# google.appengine.ext.blobstore.BlobstoreUploadHandler  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/blobstore/BlobstoreUploadHandler/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.ext.blobstore.BlobstoreUploadHandler Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/blobstore/blobstore.py#L1532-L1618) Base class for creation blob upload handlers. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)

#### View aliases

**Main aliases** `google.appengine.ext.blobstore.blobstore.BlobstoreUploadHandler`
    
    
    google.appengine.ext.blobstore.BlobstoreUploadHandler()
    

## Methods

### `get_file_infos`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/blobstore/blobstore.py#L1567-L1594)
    
    
    get_file_infos(
        environ, field_name=None
    )
    

Get the file infos associated to the uploads sent to this handler. | Args  
---  
  
`environ` |  a WSGI dict describing the HTTP request (See PEP 333).   
`field_name` |  Only select uploads that were sent as a specific field. Specify None to select all the uploads.   
  
Returns  
---  
A list of FileInfo records corresponding to each upload. Empty list if there are no FileInfo records for field_name.   
  
### `get_uploads`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/blobstore/blobstore.py#L1539-L1565)
    
    
    get_uploads(
        environ, field_name=None
    )
    

Get uploads sent to this handler.

Args  
---  
  
`environ` |  a WSGI dict describing the HTTP request (See PEP 333).   
`field_name` |  Only select uploads that were sent as a specific field.   
  
Returns  
---  
A list of BlobInfo records corresponding to each upload. Empty list if there are no blob-info records for field_name.   
  
### `post`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/blobstore/blobstore.py#L1596-L1610)
    
    
    post(
        environ
    )
    

Override this method to handle POST requests to this WSGI handler.

This method is called internally by **call** if an instance of this class is used as a WSGI callable app, and the HTTP request being handled is a POST request.

Args  
---  
  
`environ` |  a WSGI dict describing the HTTP request (See PEP 333).   
  
Returns  
---  
  
`response` |  a string containing body of the response   
`status` |  HTTP status code of enum type http.HTTPStatus   
`headers` |  a list of 2-tuples containing Response headers   
  
### `__call__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/blobstore/blobstore.py#L1612-L1618)
    
    
    __call__(
        environ, start_response
    )
    

Call self as a function.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
