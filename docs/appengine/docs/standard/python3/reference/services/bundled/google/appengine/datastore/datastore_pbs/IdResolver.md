---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_pbs/IdResolver/
title: google.appengine.datastore.datastore_pbs.IdResolver \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:42:49.267508+00:00
---

# google.appengine.datastore.datastore_pbs.IdResolver  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_pbs/IdResolver/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.datastore.datastore_pbs.IdResolver Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_pbs.py#L280-L319) A class that can handle project id <\--> application id transformations. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.datastore.datastore_pbs.IdResolver(
        app_ids=()
    )
    

| 

## Args  
  
---  
  
`app_ids` |  A list of application ids with application id shard set. i.e. s~my_app or e~my_app.   
  
## Methods

### `resolve_app_id`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_pbs.py#L305-L319)
    
    
    resolve_app_id(
        project_id
    )
    

Converts a project id to an application id.

Args  
---  
  
`project_id` |  The project id.   
  
Returns  
---  
The application id.   
  
Raises  
---  
  
`InvalidConversionError` |  if the application is unknown for the project id.   
  
### `resolve_project_id`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_pbs.py#L295-L303)
    
    
    resolve_project_id(
        app_id
    )
    

Converts an application id to a project id.

Args  
---  
  
`app_id` |  The application id.   
  
Returns  
---  
The project id.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
