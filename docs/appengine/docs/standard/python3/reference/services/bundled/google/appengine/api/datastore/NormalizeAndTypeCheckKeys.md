---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore/NormalizeAndTypeCheckKeys/
title: google.appengine.api.datastore.NormalizeAndTypeCheckKeys \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:53:12.012392+00:00
---

# google.appengine.api.datastore.NormalizeAndTypeCheckKeys  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore/NormalizeAndTypeCheckKeys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.datastore.NormalizeAndTypeCheckKeys Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L162-L182) Normalizes and type checks that the given argument is a valid key or keys.
    
    
    google.appengine.api.datastore.NormalizeAndTypeCheckKeys(
        keys
    )
    

A wrapper around `NormalizeAndTypeCheck()` that accepts strings, Keys, and Entities, and normalizes to Keys. | 

## Args  
  
---  
  
`keys` |  a Key or sequence of Keys   
  
## Returns  
  
---  
A `(list of Keys, bool)` tuple. See `NormalizeAndTypeCheck`.   
  
## Raises  
  
---  
  
`BadArgumentError` |  arg is not an instance or sequence of one of the given types.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
