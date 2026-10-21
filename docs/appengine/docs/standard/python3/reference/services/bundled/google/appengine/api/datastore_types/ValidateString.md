---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore_types/ValidateString/
title: google.appengine.api.datastore_types.ValidateString \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:29:27.665380+00:00
---

# google.appengine.api.datastore_types.ValidateString  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore_types/ValidateString/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.datastore_types.ValidateString Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore_types.py#L174-L211) Raises an exception if the value is not a valid string or a subclass thereof.

#### View aliases

**Main aliases** `google.appengine.api.datastore.datastore_types.ValidateString`
    
    
    google.appengine.api.datastore_types.ValidateString(
        value,
        name='unused',
        exception=[google.appengine.api.datastore_errors.BadValueError](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore_errors/BadValueError),
        max_len=_MAX_STRING_LENGTH,
        empty_ok=False
    )
    

A string is valid if it's not empty, no more than `_MAX_STRING_LENGTH` bytes, and not a Blob. The exception type can be specified with the exception argument; it defaults to `BadValueError`. | 

## Args  
  
---  
  
`value` |  The value to validate.   
`name` |  The name of this value; used in the exception message.   
`exception` |  The type of exception to raise.   
`max_len` |  The maximum allowed length, in bytes.   
`empty_ok` |  Allow empty value.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
