---
url: https://docs.cloud.google.com/profiler/docs/reference/v2/rest/
title: Cloud Profiler API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:10:49.234627+00:00
---

# Cloud Profiler API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/profiler/docs/reference/v2/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Profiler ](https://docs.cloud.google.com/profiler/docs)
  * [ Reference ](https://docs.cloud.google.com/profiler/docs/reference/v2)



Send feedback 

#  Cloud Profiler API Stay organized with collections  Save and categorize content based on your preferences. 

Manages continuous profiling information.

  * REST Resource: v2.projects.profiles



## Service: cloudprofiler.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

  * <https://cloudprofiler.googleapis.com/$discovery/rest?version=v2>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://cloudprofiler.googleapis.com`



## REST Resource: [v2.projects.profiles](https://docs.cloud.google.com/profiler/docs/reference/v2/rest/v2/projects.profiles)

Methods  
---  
`[create](https://docs.cloud.google.com/profiler/docs/reference/v2/rest/v2/projects.profiles/create)` |  `POST /v2/{parent=projects/*}/profiles`   
CreateProfile creates a new profile resource in the online mode.  
`[createOffline](https://docs.cloud.google.com/profiler/docs/reference/v2/rest/v2/projects.profiles/createOffline)` |  `POST /v2/{parent=projects/*}/profiles:createOffline`   
CreateOfflineProfile creates a new profile resource in the offline mode.  
`[list](https://docs.cloud.google.com/profiler/docs/reference/v2/rest/v2/projects.profiles/list)` |  `GET /v2/{parent=projects/*}/profiles`   
Lists profiles which have been collected so far and for which the caller has permission to view.  
`[patch](https://docs.cloud.google.com/profiler/docs/reference/v2/rest/v2/projects.profiles/patch)` |  `PATCH /v2/{profile.name=projects/*/profiles/*}`   
UpdateProfile updates the profile bytes and labels on the profile resource created in the online mode.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-09 UTC."],[],[]] 
