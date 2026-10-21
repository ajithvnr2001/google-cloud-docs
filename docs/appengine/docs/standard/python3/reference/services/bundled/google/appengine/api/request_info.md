---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/request_info/
title: Module: google.appengine.api.request_info \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:58:27.653157+00:00
---

# Module: google.appengine.api.request_info  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/request_info/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Module: google.appengine.api.request_info Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/request_info.py) Allows API stubs to access request and system state when handling calls. Certain API stubs require access to information about the request that triggered the API call (e.g., `user_service_stub` needs to know the host name of the request to generate continuation URLs) or system state (e.g., `modules_stub`). Other stubs (e.g., `taskqueue_stub`, `channel_stub`) need to be able to dispatch requests within the system. An instance of a `RequestInfo` subclass is passed to stubs that require these capabilities.

## Classes

[`class BackgroundThreadLimitReachedError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/request_info/BackgroundThreadLimitReachedError): The instance is at its background thread capacity. [`class Dispatcher`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/request_info/Dispatcher): Provides information about and dispatches requests to modules. [`class Error`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/request_info/Error): Common base class for all non-exit exceptions. [`class InvalidInstanceIdError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/request_info/InvalidInstanceIdError): The provided instance ID is invalid. [`class ModuleDoesNotExistError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/request_info/ModuleDoesNotExistError): The provided module does not exist. [`class NotSupportedWithAutoScalingError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/request_info/NotSupportedWithAutoScalingError): The requested operation is not supported for auto-scaling modules. [`class VersionAlreadyStartedError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/request_info/VersionAlreadyStartedError): The version is already started. [`class VersionAlreadyStoppedError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/request_info/VersionAlreadyStoppedError): The version is already stopped. [`class VersionDoesNotExistError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/request_info/VersionDoesNotExistError): The provided version does not exist. Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2025-06-16 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
