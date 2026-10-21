---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore_types/PropertyValueFromString/
title: google.appengine.api.datastore_types.PropertyValueFromString \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T06:35:01.815699+00:00
---

# google.appengine.api.datastore_types.PropertyValueFromString  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore_types/PropertyValueFromString/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.datastore_types.PropertyValueFromString Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore_types.py#L2090-L2145) Returns an instance of a property value given a type and string value.

#### View aliases

**Main aliases** `google.appengine.api.datastore.datastore_types.PropertyValueFromString`
    
    
    google.appengine.api.datastore_types.PropertyValueFromString(
        type_, value_string, _auth_domain=None
    )
    

The reverse of this method is just `str()` and `type()` of the Python value. Note that this does _not_ support non-UTC offsets in ISO 8601-formatted datetime strings, e.g., the `-08:00` suffix in `2002-12-25 00:00:00-08:00`. It only supports `-00:00` and `+00:00` suffixes, which are UTC. | 

## Args  
  
---  
  
`type_` |  A Python class.   
`value_string` |  A string representation of the value of the property.   
  
## Returns  
  
---  
An instance of `type`.   
  
## Raises  
  
---  
`ValueError` if `type_` is datetime and `value_string` has a timezone offset.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
