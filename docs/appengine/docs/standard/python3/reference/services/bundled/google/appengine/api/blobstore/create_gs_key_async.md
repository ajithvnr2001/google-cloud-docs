---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/blobstore/create_gs_key_async/
title: google.appengine.api.blobstore.create_gs_key_async \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T14:35:10.688064+00:00
---

# google.appengine.api.blobstore.create_gs_key_async  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/blobstore/create_gs_key_async/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.blobstore.create_gs_key_async Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/blobstore/blobstore.py#L495-L529) Asynchronously creates an encoded key for a Google Cloud Storage file.

#### View aliases

**Main aliases** `google.appengine.api.blobstore.blobstore.create_gs_key_async`
    
    
    google.appengine.api.blobstore.create_gs_key_async(
        filename, rpc=None
    )
    

It is safe to persist this key for future use. | 

## Args  
  
---  
  
`filename` |  The file name of the Google Cloud Storage object for which you want to create the key.   
`rpc` |  Optional UserRPC object.   
  
## Returns  
  
---  
A UserRPC whose result will be a string as returned by `create_gs_key()`.   
  
## Raises  
  
---  
  
`TypeError` |  If `filename` is not a string.   
`ValueError` |  If `filename` is not in the format `/gs/bucket_name/object_name`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
