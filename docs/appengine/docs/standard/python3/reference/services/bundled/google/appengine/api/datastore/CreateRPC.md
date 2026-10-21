---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore/CreateRPC/
title: google.appengine.api.datastore.CreateRPC \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:06:00.221718+00:00
---

# google.appengine.api.datastore.CreateRPC  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore/CreateRPC/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.datastore.CreateRPC Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L472-L505) Create an rpc for use in configuring datastore calls.
    
    
    google.appengine.api.datastore.CreateRPC(
        service='datastore_v3',
        deadline=None,
        callback=None,
        read_policy=None
    )
    

NOTE: This functions exists for backwards compatibility. Please use `CreateConfig()` instead. NOTE: the latter uses 'on_completion', which is a function taking an argument, wherease `CreateRPC` uses 'callback' which is a function without arguments. | 

## Args  
  
---  
  
`service` |  Optional string; for backwards compatibility, must be 'datastore_v3'.   
`deadline` |  Optional int or float, deadline for calls in seconds.   
`callback` |  Optional callable, a callback triggered when this rpc completes; takes no arguments.   
`read_policy` |  Optional read policy; set to EVENTUAL_CONSISTENCY to enable eventually consistent reads (i.e. reads that may be satisfied from an older version of the datastore in some cases). The default read policy may have to wait until in-flight transactions are committed.   
  
## Returns  
  
---  
A `UserRPC` instance.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
