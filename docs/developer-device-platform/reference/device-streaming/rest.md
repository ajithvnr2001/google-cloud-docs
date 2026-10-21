---
url: https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/
title: Device Streaming API \u00a0|\u00a0 Developer Device Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:59:57.686109+00:00
---

# Device Streaming API  |  Developer Device Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Device Platform ](https://docs.cloud.google.com/developer-device-platform)
  * [ API Reference ](https://docs.cloud.google.com/developer-device-platform/apis)



Send feedback 

#  Device Streaming API Stay organized with collections  Save and categorize content based on your preferences. 

The Cloud API for device streaming usage.

  * REST Resource: v1.projects.deviceSessions



## Service: devicestreaming.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

  * <https://devicestreaming.googleapis.com/$discovery/rest?version=v1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://devicestreaming.googleapis.com`



## REST Resource: [v1.projects.deviceSessions](https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/projects.deviceSessions)

Methods  
---  
`[cancel](https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/projects.deviceSessions/cancel)` |  `POST /v1/{name=projects/*/deviceSessions/*}:cancel`   
Cancel a DeviceSession.  
`[create](https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/projects.deviceSessions/create)` |  `POST /v1/{parent=projects/*}/deviceSessions`   
Creates a DeviceSession.  
`[get](https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/projects.deviceSessions/get)` |  `GET /v1/{name=projects/*/deviceSessions/*}`   
Gets a DeviceSession, which documents the allocation status and whether the device is allocated.  
`[list](https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/projects.deviceSessions/list)` |  `GET /v1/{parent=projects/*}/deviceSessions`   
Lists DeviceSessions owned by the project user.  
`[patch](https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/projects.deviceSessions/patch)` |  `PATCH /v1/{deviceSession.name=projects/*/deviceSessions/*}`   
Updates the current DeviceSession to the fields described by the update_mask.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
