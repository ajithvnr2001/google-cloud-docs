---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/blobstore/fetch_data_async/
title: google.appengine.ext.blobstore.fetch_data_async \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:21:34.186659+00:00
---

# google.appengine.ext.blobstore.fetch_data_async  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/blobstore/fetch_data_async/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.ext.blobstore.fetch_data_async Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/blobstore/blobstore.py#L828-L863) Asynchronously fetches data for a blob.

#### View aliases

**Main aliases** `google.appengine.ext.blobstore.blobstore.fetch_data_async`
    
    
    google.appengine.ext.blobstore.fetch_data_async(
        blob, start_index, end_index, rpc=None
    )
    

Fetches a fragment of a blob up to `MAX_BLOB_FETCH_SIZE` in length. Attempting to fetch a fragment that extends beyond the boundaries of the blob will return the amount of data from `start_index` until the end of the blob, which will be a smaller size than requested. Requesting a fragment that is entirely outside the boundaries of the blob will return an empty string. Attempting to fetch a negative index will raise an exception. | 

## Args  
  
---  
  
`blob` |  A `BlobInfo`, `BlobKey`, string, or Unicode representation of the `BlobKey` of the blob from which you want to fetch data.   
`start_index` |  The start index of blob data to fetch. This value must not be negative.   
`end_index` |  The end index (inclusive) of the blob data to fetch. This value must be greater than or equal to `start_index`.   
`rpc` |  Optional UserRPC object.   
  
## Returns  
  
---  
A UserRPC whose result will be a string as returned by `fetch_data()`.   
  
## Raises  
  
---  
  
`TypeError` |  If `start_index` or `end_index` are not indexes, or if `blob` is not a string, `BlobKey` or `BlobInfo`.   
`DataIndexOutOfRangeError` |  If `start_index` is set to a value that is less than 0 or `end_index` is less than `start_index` when calling `rpc.get_result()`.   
`BlobFetchSizeTooLargeError` |  If the requested blob fragment is larger than `MAX_BLOB_FETCH_SIZE` when calling `rpc.get_result()`.   
`BlobNotFoundError` |  If the blob does not exist when calling `rpc.get_result()`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
