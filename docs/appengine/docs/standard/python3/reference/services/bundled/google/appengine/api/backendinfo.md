---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/backendinfo/
title: Module: google.appengine.api.backendinfo \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:47:52.941197+00:00
---

# Module: google.appengine.api.backendinfo  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/backendinfo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Module: google.appengine.api.backendinfo Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/backendinfo.py) A library for working with `BackendInfoExternal` records, describing backends configured for an application. Supports loading the records from `backend.yaml`.

## Classes

[`class BackendEntry`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/backendinfo/BackendEntry): A backend entry describes a single backend. [`class BackendInfoExternal`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/backendinfo/BackendInfoExternal): `BackendInfoExternal` describes all backend entries for an application. [`class BadConfig`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/backendinfo/BadConfig): An invalid configuration was provided.

## Functions

[`LoadBackendEntry(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/backendinfo/LoadBackendEntry): Parses a `BackendEntry` object from a string. [`LoadBackendInfo(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/backendinfo/LoadBackendInfo): Parses a `BackendInfoExternal` object from a string. | 

## Other Members  
  
---  
  
BACKENDS |  `'backends'`  
CLASS |  `'class'`  
CLASS_REGEX |  `'^[bB](1|2|4|8|4_1G)$'`  
DYNAMIC |  `'dynamic'`  
FAILFAST |  `'failfast'`  
FILE_REGEX |  `'(?!\\^).*(?!\\$).{1,256}'`  
INSTANCES |  `'instances'`  
MAX_CONCURRENT_REQUESTS |  `'max_concurrent_requests'`  
NAME |  `'name'`  
NAME_REGEX |  `'(?!-)[a-z\\d\\-]{1,100}'`  
OPTIONS |  `'options'`  
OPTIONS_REGEX |  `'^[a-z, ]*$'`  
PUBLIC |  `'public'`  
START |  `'start'`  
STATE |  `'state'`  
STATE_REGEX |  `'^(START|STOP|DISABLED)$'`  
VALID_OPTIONS | 
    
    
    {
     'dynamic',
     'failfast',
     'public'
    }
      
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
