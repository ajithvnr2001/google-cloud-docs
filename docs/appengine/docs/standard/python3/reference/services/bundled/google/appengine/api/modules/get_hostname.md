---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/modules/get_hostname/
title: google.appengine.api.modules.get_hostname \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:45:04.508062+00:00
---

# google.appengine.api.modules.get_hostname  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/modules/get_hostname/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.modules.get_hostname Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/modules/modules.py#L446-L490) Returns a hostname to use to contact the module.

#### View aliases

**Main aliases** `google.appengine.api.modules.modules.get_hostname`
    
    
    google.appengine.api.modules.get_hostname(
        module=None, version=None, instance=None
    )
    

| 

## Args  
  
---  
  
`module` |  Name of module, if None, take module of the current instance.   
`version` |  Name of version, if version is `None` then either use the version of the current instance if that version exists for the target module, otherwise use the default version of the target module.   
`instance` |  Instance to construct a hostname for, if instance is None, a loadbalanced hostname for the module will be returned. If the target module is not a fixed module, then instance is not considered valid.   
  
## Returns  
  
---  
A valid canonical hostname that can be used to communicate with the given module/version/instance. For example: `0.v1.module5.myapp.appspot.com`  
  
## Raises  
  
---  
  
`InvalidModuleError` |  if the given module version is invalid.   
`InvalidInstancesError` |  if the given instance value is invalid.   
`TypeError` |  if the given instance type is invalid.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
