---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.backends
title: Package com.google.appengine.api.backends (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:07:12.604656+00:00
---

# Package com.google.appengine.api.backends (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.backends

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Package com.google.appengine.api.backends (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 

Provides access to long-running, addressable servers. See Also: [com.google.appengine.api.backends.BackendService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.backends.BackendService), [Backends (Java) in the _Google App Engine Developer's Guide_](http://cloud.google.com/appengine/docs/java/backends/).

## Classes 

### [BackendServiceFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.backends.BackendServiceFactory)

Factory for getting the Backends API implementation for the current environment.

### [IBackendServiceFactoryProvider](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.backends.IBackendServiceFactoryProvider)

Factory provider for [IBackendServiceFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.backends.IBackendServiceFactory).

**Note:** This class is not intended for end users.

## Interfaces 

### [BackendService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.backends.BackendService)

[BackendService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.backends.BackendService) allows you to retrieve information about backend servers. Backend servers are long running addressable servers that can be used for applications that need to keep persistent state in ram between requests. 

This API is deprecated and has been replaced by [com.google.appengine.api.modules.ModulesService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesService). Please update your code as soon as possible. See the modules documentation for more information: <https://developers.google.com/appengine/docs/java/modules/converting>

This API allows you to retrieve information about the backend handling the current request. It also allows you to to get the address of a specific backend instance in such a way that a local server is used during development and a production server is used in production.

### [IBackendServiceFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.backends.IBackendServiceFactory)

Factory for getting the Backends API implementation for the current environment.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
