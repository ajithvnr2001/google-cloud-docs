---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore_types/RestoreFromIndexValue/
title: google.appengine.api.datastore_types.RestoreFromIndexValue \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:49:35.093332+00:00
---

# google.appengine.api.datastore_types.RestoreFromIndexValue  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore_types/RestoreFromIndexValue/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.datastore_types.RestoreFromIndexValue Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore_types.py#L1967-L2021) Restores an index value to the correct datastore type.

#### View aliases

**Main aliases** `google.appengine.api.datastore.datastore_types.RestoreFromIndexValue`
    
    
    google.appengine.api.datastore_types.RestoreFromIndexValue(
        index_value, data_type
    )
    

Projection queries return property values directly from a datastore index. These values are the native datastore values that can be one of the following: `str`, `bool`, `long`, `float`, `GeoPt`, `Key`, or `User`. This function restores the original value when the original type is known. This function returns the value type returned when decoding a normal entity, not necessarily of type `data_type`. For example, `data_type=int` returns a `long` instance. | 

## Args  
  
---  
  
`index_value` |  The value returned by `FromPropertyPb` for the projected property.   
`data_type` |  The type of the value originally given to `ToPropertyPb`.   
  
## Returns  
  
---  
The restored property value.   
  
## Raises  
  
---  
[`datastore_errors.BadValueError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore_errors/BadValueError) if the value cannot be restored.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
