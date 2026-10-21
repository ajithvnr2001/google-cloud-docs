---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/images_blob_stub/ImagesBlobStub/
title: google.appengine.api.images.images_blob_stub.ImagesBlobStub \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:50:48.065179+00:00
---

# google.appengine.api.images.images_blob_stub.ImagesBlobStub  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/images_blob_stub/ImagesBlobStub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.images.images_blob_stub.ImagesBlobStub Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/images/images_blob_stub.py#L34-L73) Stub version of the blob-related parts of the images API. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.api.images.images_blob_stub.ImagesBlobStub(
        host_prefix
    )
    

| 

## Args  
  
---  
  
`host_prefix` |  string - The URL prefix (protocol://host:port) to prepend to image URLs on a call to GetUrlBase.   
  
## Methods

### `DeleteUrlBase`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/images/images_blob_stub.py#L64-L73)
    
    
    DeleteUrlBase(
        request, unused_response
    )
    

Trivial implementation of an API call.

Args  
---  
  
`request` |  ImagesDeleteUrlBaseRequest - Contains a blobkey to an image.   
`unused_response` |  ImagesDeleteUrlBaseResponse - Unused.   
  
### `GetUrlBase`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/images/images_blob_stub.py#L46-L62)
    
    
    GetUrlBase(
        request, response
    )
    

Trivial implementation of an API call.

Args  
---  
  
`request` |  ImagesGetUrlBaseRequest - Contains a blobkey to an image.   
`response` |  ImagesGetUrlBaseResponse - Contains a URL to serve the image.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
