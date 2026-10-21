---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/LoadSingleAppInfo/
title: google.appengine.api.appinfo.LoadSingleAppInfo \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:41:46.707321+00:00
---

# google.appengine.api.appinfo.LoadSingleAppInfo  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/LoadSingleAppInfo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.appinfo.LoadSingleAppInfo Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/appinfo.py#L2686-L2740) Loads a single `AppInfo` object where one and only one is expected.
    
    
    google.appengine.api.appinfo.LoadSingleAppInfo(
        app_info
    )
    

This method validates that the values in the `AppInfo` match the validators that are defined in this file, in particular, [`AppInfoExternal.ATTRIBUTES`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/AppInfoExternal#ATTRIBUTES). | 

## Args  
  
---  
  
`app_info` |  A file-like object or string. If the argument is a string, the argument is parsed as a configuration file. If the argument is a file-like object, the data is read, then parsed.   
  
## Returns  
  
---  
An instance of `AppInfoExternal` as loaded from a YAML file.   
  
## Raises  
  
---  
  
`ValueError` |  If a specified service is not valid.   
`EmptyConfigurationFile` |  If there are no documents in YAML file.   
`MultipleConfigurationFile` |  If more than one document exists in the YAML file.   
`DuplicateBackend` |  If a backend is found more than once in the `backends` directive.   
`yaml_errors.EventError` |  If the `app.yaml` file fails validation.   
`appinfo_errors.MultipleProjectNames` |  If the `app.yaml` file has both an `application` directive and a `project` directive.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
