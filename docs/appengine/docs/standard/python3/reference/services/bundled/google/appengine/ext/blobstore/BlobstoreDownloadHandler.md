---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/blobstore/BlobstoreDownloadHandler/
title: google.appengine.ext.blobstore.BlobstoreDownloadHandler \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:45:32.476084+00:00
---

# google.appengine.ext.blobstore.BlobstoreDownloadHandler  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/blobstore/BlobstoreDownloadHandler/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.ext.blobstore.BlobstoreDownloadHandler Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/blobstore/blobstore.py#L1363-L1529) Base class for creating handlers that may send blobs to users. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)

#### View aliases

**Main aliases** `google.appengine.ext.blobstore.blobstore.BlobstoreDownloadHandler`

## Methods

### `get`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/blobstore/blobstore.py#L1507-L1521)
    
    
    get(
        environ
    )
    

Override this method to handle GET requests to this WSGI handler. This method is called internally by **call** if an instance of this class is used as a WSGI callable app, and the HTTP request being handled is a GET request. | Args  
---  
  
`environ` |  a WSGI dict describing the HTTP request (See PEP 333).   
  
Returns  
---  
  
`response` |  a string containing body of the response   
`status` |  HTTP status code of enum type http.HTTPStatus   
`headers` |  a list of 2-tuples containing Response headers   
  
### `get_range`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/blobstore/blobstore.py#L1471-L1505)
    
    
    get_range(
        environ
    )
    

Get range from header if it exists.

A range header of "bytes: 0-100" would return (0, 100). Args: environ: a WSGI dict describing the HTTP request (See PEP 333). Returns: Tuple (start, end): start: Start index. None if there is None. end: End index (inclusive). None if there is None. None if there is no request header.

Raises  
---  
  
`UnsupportedRangeFormatError` |  If the range format in the header is valid, but not supported.   
`RangeFormatError` |  If the range format in the header is not valid.   
  
### `send_blob`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/blobstore/blobstore.py#L1368-L1469)
    
    
    send_blob(
        environ,
        blob_key_or_info,
        content_type=None,
        save_as=None,
        start=None,
        end=None,
        **kwargs
    )
    

Send a blob-response based on a blob_key.

Returns the correct response headers for serving a blob. If BlobInfo is provided and no content_type specified, will set request content type to BlobInfo's content type.

Args  
---  
  
`environ` |  a WSGI dict describing the HTTP request (See PEP 333).   
`blob_key_or_info` |  BlobKey or BlobInfo record to serve.   
`content_type` |  Content-type header to override when known. If not set, this header is not included in the returned headers. Web frameworks might set the 'content-type' header to a default type, which prevents GAE from setting a guessed 'content-type'. This behavior can be bypassed by setting headers['content-type'] to None or an empty string explicitly after this function call.   
`save_as` |  If True, and BlobInfo record is provided, use BlobInfos filename to save-as. If string is provided, use string as filename. If None or False, do not send as attachment.   
`start` |  Start index of content-range to send.   
`end` |  End index of content-range to send. End index is inclusive.   
`**kwargs` |  The `use_range` keyworded argument provides content range from the requests' Range header.   
  
Raises  
---  
ValueError on invalid save_as parameter.   
  
Returns  
---  
  
`headers` |  a `dict` containing response headers   
  
### `__call__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/blobstore/blobstore.py#L1523-L1529)
    
    
    __call__(
        environ, start_response
    )
    

Call self as a function.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
