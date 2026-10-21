---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_stub_util/ValueRange/
title: google.appengine.datastore.datastore_stub_util.ValueRange \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:49:58.868712+00:00
---

# google.appengine.datastore.datastore_stub_util.ValueRange  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_stub_util/ValueRange/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.datastore.datastore_stub_util.ValueRange Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L764-L844) A range of values defined by its two extremes (inclusive or exclusive). Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.datastore.datastore_stub_util.ValueRange()
    

## Methods

### `Contains`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L803-L817)
    
    
    Contains(
        value
    )
    

Check if the range contains a specific value. | Args  
---  
  
`value` |  the value to check.   
  
Returns  
---  
True iff value is contained in this range.   
  
### `MapExtremes`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L831-L844)
    
    
    MapExtremes(
        mapper
    )
    

Evaluate a function on the range extremes.

Args  
---  
  
`mapper` |  function to apply to the range extremes.   
  
Returns  
---  
(x, y) where x = None if the range has no start, mapper(start, start_inclusive, False) otherwise y = None if the range has no end, mapper(end, end_inclusive, True) otherwise   
  
### `Remap`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L819-L829)
    
    
    Remap(
        mapper
    )
    

Transforms the range extremes with a function.

The function mapper must preserve order, i.e. x rel_op y iff mapper(x) rel_op y

Args  
---  
  
`mapper` |  function to apply to the range extremes.   
  
### `Update`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L775-L801)
    
    
    Update(
        rel_op, limit
    )
    

Filter the range by 'rel_op limit'.

Args  
---  
  
`rel_op` |  relational operator from datastore_pb.Query.Filter.   
`limit` |  the value to limit the range by.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
