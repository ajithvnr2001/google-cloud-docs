---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/dispatchinfo/LoadSingleDispatch/
title: google.appengine.api.dispatchinfo.LoadSingleDispatch \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:03:16.336409+00:00
---

# google.appengine.api.dispatchinfo.LoadSingleDispatch  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/dispatchinfo/LoadSingleDispatch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.dispatchinfo.LoadSingleDispatch Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/dispatchinfo.py#L187-L222) Load a dispatch.yaml file or string and return a DispatchInfoExternal.
    
    
    google.appengine.api.dispatchinfo.LoadSingleDispatch(
        dispatch_info, open_fn=None
    )
    

| 

## Args  
  
---  
  
`dispatch_info` |  The contents of a dispatch.yaml file as a string, or an open file object.   
`open_fn` |  Function for opening files. Unused here, needed to provide a polymorphic API used by appcfg.py yaml parsing.   
  
## Returns  
  
---  
A DispatchInfoExternal instance which represents the contents of the parsed yaml file.   
  
## Raises  
  
---  
  
`MalformedDispatchConfigurationError` |  The yaml file contains multiple dispatch sections or is missing a required value.   
`yaml_errors.EventError` |  An error occured while parsing the yaml file.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
