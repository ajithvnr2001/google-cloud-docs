---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/get_serving_url_async/
title: google.appengine.api.images.get_serving_url_async \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:21:19.552313+00:00
---

# google.appengine.api.images.get_serving_url_async  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/get_serving_url_async/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.images.get_serving_url_async Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/images/__init__.py#L1914-L2027) Asynchronously obtains a URL that will serve the underlying image.
    
    
    google.appengine.api.images.get_serving_url_async(
        blob_key, size=None, crop=False, secure_url=None, filename=None, rpc=None
    )
    

This URL is served by a high-performance dynamic image serving infrastructure. This URL format also allows dynamic resizing and cropping with certain restrictions. To dynamically resize and crop, specify size and crop arguments, or simply append options to the end of the default URL obtained via this call. Example::
    
    
    get_serving_url -> "http://lh3.ggpht.com/SomeCharactersGoesHere"
    

To get a 32-pixel-sized version (aspect-ratio preserved), append `=s32` to the URL::
    
    
    http://lh3.ggpht.com/SomeCharactersGoesHere=s32
    

To get a 32-pixel cropped version, append `=s32-c`::
    
    
    http://lh3.ggpht.com/SomeCharactersGoesHere=s32-c
    

Available sizes are any integer in the range [0, 1600] and is available as `IMG_SERVING_SIZES_LIMIT`. | 

## Args  
  
---  
  
`blob_key` |  The `BlobKey`, `BlobInfo`, string, or Unicode representation of the `BlobKey` of blob whose URL you require.   
`size` |  Integer of the size of resulting images.   
`crop` |  Boolean value. `True` requests a cropped image, while `False` requests a resized image.   
`secure_url` |  Boolean value. `True` requests a `https` URL, while `False` requests a `http` URL.   
`filename` |  The file name of a Google Storage object whose URL you require.   
`rpc` |  Optional UserRPC object.   
  
## Returns  
  
---  
A UserRPC whose result will be a string that is the serving URL.   
  
## Raises  
  
---  
  
`BlobKeyRequiredError` |  If a blob key was not specified in the constructor.   
`UnsupportedSizeError` |  If you specified an invalid size parameter.   
`BadRequestError` |  If `crop` and `size` are present in the wrong combination, or if `blob_key` and `filename` are both specified.   
`TypeError` |  If `secure_url` is not a boolean type.   
`AccessDeniedError` |  If `blob_key` refers to a Google Storage object and the application does not have permission to access the object.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
