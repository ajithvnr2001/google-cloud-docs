---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/put/
title: google.appengine.ext.db.put \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:52:44.984192+00:00
---

# google.appengine.ext.db.put  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/put/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.ext.db.put Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/db/__init__.py#L1572-L1587) Store one or more `Model` instances.

#### View aliases

**Main aliases** `google.appengine.ext.db.save`
    
    
    google.appengine.ext.db.put(
        models, **kwargs
    )
    

| 

## Args  
  
---  
  
`models` |  `Model` instance or list of `Model` instances.   
`config` |  [`datastore_rpc.Configuration`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_rpc/Configuration) to use for this request, must be specified as a keyword argument.   
  
## Returns  
  
---  
A `Key` if `models` is an instance, a list of `Key`s in the same order as `models` if `models` is a list.   
  
## Raises  
  
---  
`TransactionFailedError` if the data could not be committed.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
