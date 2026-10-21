---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/runtime/context/gae_headers/
title: Module: google.appengine.runtime.context.gae_headers \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:48:56.369761+00:00
---

# Module: google.appengine.runtime.context.gae_headers  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/runtime/context/gae_headers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Module: google.appengine.runtime.context.gae_headers Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/runtime/context/gae_headers.py) Save X-Appengine-* headers into request context.

## Functions

[`init_from_wsgi_environ(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/runtime/context/gae_headers/init_from_wsgi_environ): Init contextvars from matching X _APPENGINE_ headers if found. | 

## Other Members  
  
---  
  
API_TICKET |  Instance of `_contextvars.ContextVar`  
AUTH_DOMAIN |  Instance of `_contextvars.ContextVar`  
DEFAULT_NAMESPACE |  Instance of `_contextvars.ContextVar`  
DEFAULT_VERSION_HOSTNAME |  Instance of `_contextvars.ContextVar`  
DEV_REQUEST_ID |  Instance of `_contextvars.ContextVar`  
PREFIX |  `'HTTP_X_APPENGINE_'`  
REQUEST_LOG_ID |  Instance of `_contextvars.ContextVar`  
USER_EMAIL |  Instance of `_contextvars.ContextVar`  
USER_ID |  Instance of `_contextvars.ContextVar`  
USER_IS_ADMIN |  Instance of `_contextvars.ContextVar`  
USER_NICKNAME |  Instance of `_contextvars.ContextVar`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
