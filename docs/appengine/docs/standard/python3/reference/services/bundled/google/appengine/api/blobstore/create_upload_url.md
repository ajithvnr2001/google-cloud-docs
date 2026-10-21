---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/blobstore/create_upload_url/
title: google.appengine.api.blobstore.create_upload_url \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:59:17.284701+00:00
---

# google.appengine.api.blobstore.create_upload_url  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/blobstore/create_upload_url/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.blobstore.create_upload_url Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/blobstore/blobstore.py#L253-L288) Creates the upload URL for a POST form.

#### View aliases

**Main aliases** `google.appengine.api.blobstore.blobstore.create_upload_url`
    
    
    google.appengine.api.blobstore.create_upload_url(
        success_path,
        max_bytes_per_blob=None,
        max_bytes_total=None,
        rpc=None,
        gs_bucket_name=None
    )
    

| 

## Args  
  
---  
  
`success_path` |  Path within application to call when a `POST` call is successful and the upload is complete.   
`max_bytes_per_blob` |  The maximum size in bytes that any one blob in the upload can be, or `None` for no maximum size.   
`max_bytes_total` |  The maximum size in bytes that the aggregate sizes of all of the blobs in the upload can be, or `None` for no maximum size.   
`rpc` |  Optional UserRPC object.   
`gs_bucket_name` |  The Google Cloud Storage bucket name to which the blobs should be uploaded. The application's service account must have the correct permissions to write to this bucket. The bucket name can be of the format `bucket/path/`, in which case the included path will be prepended to the uploaded object name.   
  
## Returns  
  
---  
The upload URL.   
  
## Raises  
  
---  
  
`TypeError` |  If `max_bytes_per_blob` or `max_bytes_total` are not integral types.   
`ValueError` |  If `max_bytes_per_blob` or `max_bytes_total` are not positive values.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
