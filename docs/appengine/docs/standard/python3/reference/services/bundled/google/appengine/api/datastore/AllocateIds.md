---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore/AllocateIds/
title: google.appengine.api.datastore.AllocateIds \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:52:53.257884+00:00
---

# google.appengine.api.datastore.AllocateIds  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore/AllocateIds/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.datastore.AllocateIds Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L2008-L2035) Allocates a range of `IDs` of size or with max for the given key.
    
    
    google.appengine.api.datastore.AllocateIds(
        model_key, size=None, **kwargs
    )
    

Allocates a range of `IDs` in the datastore such that those `IDs` will not be automatically assigned to new entities. You can only allocate `IDs` for model keys from your app. If there is an error, raises a subclass of datastore_errors.Error. Either size or max must be provided but not both. If size is provided then a range of the given size is returned. If max is provided then the largest range of ids that are safe to use with an upper bound of max is returned (can be an empty range). Max should only be provided if you have an existing numeric id range that you want to reserve, e.g. bulk loading entities that already have `IDs`. If you don't care about which `IDs` you receive, use size instead. | 

## Args  
  
---  
  
`model_key` |  Key or string to serve as a model specifying the `ID` sequence in which to allocate `IDs`  
`size` |  integer, number of `IDs` to allocate.   
`max` |  integer, upper bound of the range of `IDs` to allocate.   
`config` |  Optional Configuration to use for this request.   
  
## Returns  
  
---  
`(start, end)` of the allocated range, inclusive.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
