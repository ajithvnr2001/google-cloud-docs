---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore/RunInReadOnlyTransaction/
title: google.appengine.api.datastore.RunInReadOnlyTransaction \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:54:57.191467+00:00
---

# google.appengine.api.datastore.RunInReadOnlyTransaction  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore/RunInReadOnlyTransaction/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.datastore.RunInReadOnlyTransaction Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L2533-L2554) Runs a function inside a read-only datastore transaction.
    
    
    google.appengine.api.datastore.RunInReadOnlyTransaction(
        function, *args, **kwargs
    )
    

A read-only transaction cannot perform writes, but may be able to execute more efficiently. Runs the user-provided function inside a read-only transaction, retries default number of times. | 

## Args  
  
---  
  
`function` |  a function to be run inside the transaction on all remaining arguments   
`*args` |  positional arguments for function.   
`**kwargs` |  keyword arguments for function.   
  
## Returns  
  
---  
the function's return value, if any   
  
## Raises  
  
---  
`TransactionFailedError`, if the transaction could not be committed.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
