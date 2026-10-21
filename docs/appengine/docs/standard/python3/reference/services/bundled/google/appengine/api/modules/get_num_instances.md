---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/modules/get_num_instances/
title: google.appengine.api.modules.get_num_instances \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:59:35.436097+00:00
---

# google.appengine.api.modules.get_num_instances  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/modules/get_num_instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.modules.get_num_instances Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/modules/modules.py#L249-L285) Return the number of instances that are set for the given module version.

#### View aliases

**Main aliases** `google.appengine.api.modules.modules.get_num_instances`
    
    
    google.appengine.api.modules.get_num_instances(
        module=None, version=None
    )
    

This is only valid for fixed modules, an error will be raised for automatically-scaled modules. Support for automatically-scaled modules may be supported in the future. | 

## Args  
  
---  
  
`module` |  String containing the name of the module to fetch this info for, if `None` the module of the current instance will be used.   
`version` |  String containing the name of the version to fetch this info for, if `None` the version of the current instance will be used. If that version does not exist in the other module, then an `InvalidVersionError` is raised.   
  
## Returns  
  
---  
The number of instances that are set for the given module version.   
  
## Raises  
  
---  
`InvalidVersionError` on invalid input.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
