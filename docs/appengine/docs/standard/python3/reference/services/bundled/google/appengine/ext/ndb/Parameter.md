---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/ndb/Parameter/
title: google.appengine.ext.ndb.Parameter \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:27:06.530845+00:00
---

# google.appengine.ext.ndb.Parameter  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/ndb/Parameter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.ext.ndb.Parameter Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/query.py#L300-L340) Represents a bound variable in a GQL query. Inherits From: [`ParameterizedThing`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/ndb/ParameterizedThing), [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.ext.ndb.Parameter(
        key
    )
    

Parameter(1) corresponds to a slot labeled ":1" in a GQL query. Parameter('xyz') corresponds to a slot labeled ":xyz". The value must be set (bound) separately by calling .set(value). | 

## Args  
  
---  
  
`key` |  The Parameter key, must be either an integer or a string.   
  
## Attributes  
  
---  
  
`key` |  Retrieve the key.   
  
## Methods

### `resolve`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/query.py#L333-L340)
    
    
    resolve(
        bindings, used
    )
    

### `__eq__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/query.py#L323-L326)
    
    
    __eq__(
        other
    )
    

Return self==value.

### `__ne__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/query.py#L293-L297)
    
    
    __ne__(
        other
    )
    

Return self!=value.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
