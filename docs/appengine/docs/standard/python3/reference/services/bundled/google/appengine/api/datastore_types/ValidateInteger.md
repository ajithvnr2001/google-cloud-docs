---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore_types/ValidateInteger/
title: google.appengine.api.datastore_types.ValidateInteger \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:55:57.701497+00:00
---

# google.appengine.api.datastore_types.ValidateInteger  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore_types/ValidateInteger/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.datastore_types.ValidateInteger Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore_types.py#L214-L242) Raises an exception if value is not a valid integer.

#### View aliases

**Main aliases** `google.appengine.api.datastore.datastore_types.ValidateInteger`
    
    
    google.appengine.api.datastore_types.ValidateInteger(
        value,
        name='unused',
        exception=[google.appengine.api.datastore_errors.BadValueError](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore_errors/BadValueError),
        empty_ok=False,
        zero_ok=False,
        negative_ok=False
    )
    

An integer is valid if it's not negative or empty and is an integer (either `int` or `long`). The exception type raised can be specified with the exception argument; it defaults to `BadValueError`. | 

## Args  
  
---  
  
`value` |  The value to validate.   
`name` |  The name of this value; used in the exception message.   
`exception` |  The type of exception to raise.   
`empty_ok` |  Allow `None` value.   
`zero_ok` |  Allow zero value.   
`negative_ok` |  Allow negative value.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
