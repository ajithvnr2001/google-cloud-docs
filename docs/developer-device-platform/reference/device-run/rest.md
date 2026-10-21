---
url: https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/
title: Device Run API \u00a0|\u00a0 Developer Device Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:59:55.168512+00:00
---

# Device Run API  |  Developer Device Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Device Platform ](https://docs.cloud.google.com/developer-device-platform)
  * [ API Reference ](https://docs.cloud.google.com/developer-device-platform/apis)



Send feedback 

#  Device Run API Stay organized with collections  Save and categorize content based on your preferences. 

The Device Run API allows management, scheduling, and execution of automated sessions and workloads across device catalogs.

  * REST Resource: v1alpha.projects.locations
  * REST Resource: v1alpha.projects.locations.devices
  * REST Resource: v1alpha.projects.locations.operations
  * REST Resource: v1alpha.projects.locations.sessions
  * REST Resource: v1alpha.projects.locations.softwareVersions



## Service: devicerun.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://docs.cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

  * <https://devicerun.googleapis.com/$discovery/rest?version=v1alpha>



### Service endpoint

A [service endpoint](https://docs.cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://devicerun.googleapis.com`



## REST Resource: [v1alpha.projects.locations](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations/get)` |  `GET /v1alpha/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations/list)` |  `GET /v1alpha/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1alpha.projects.locations.devices](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.devices)

Methods  
---  
`[get](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.devices/get)` |  `GET /v1alpha/{name=projects/*/locations/*/devices/*}`   
Returns information about a specific device.  
`[list](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.devices/list)` |  `GET /v1alpha/{parent=projects/*/locations/*}/devices`   
Lists all devices.  
  
## REST Resource: [v1alpha.projects.locations.operations](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.operations/cancel)` |  `POST /v1alpha/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.operations/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.operations/get)` |  `GET /v1alpha/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.operations/list)` |  `GET /v1alpha/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1alpha.projects.locations.sessions](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions)

Methods  
---  
`[batchGet](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions/batchGet)` |  `GET /v1alpha/{parent=projects/*/locations/*}/sessions:batchGet`   
Retrieves multiple automation sessions in a single batch request.  
`[cancel](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions/cancel)` |  `POST /v1alpha/{name=projects/*/locations/*/sessions/*}:cancel`   
Cancels an in-progress automation session.  
`[create](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions/create)` |  `POST /v1alpha/{parent=projects/*/locations/*}/sessions`   
Starts an automation session with the specified configuration.  
`[delete](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/sessions/*}`   
Deletes a session.  
`[get](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions/get)` |  `GET /v1alpha/{name=projects/*/locations/*/sessions/*}`   
Returns information about a previously created automation session.  
`[list](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions/list)` |  `GET /v1alpha/{parent=projects/*/locations/*}/sessions`   
Lists previously created automation sessions.  
  
## REST Resource: [v1alpha.projects.locations.softwareVersions](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.softwareVersions)

Methods  
---  
`[get](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.softwareVersions/get)` |  `GET /v1alpha/{name=projects/*/locations/*/softwareVersions/*}`   
Returns information about a specific software version.  
`[list](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.softwareVersions/list)` |  `GET /v1alpha/{parent=projects/*/locations/*}/softwareVersions`   
Lists all software packages in lab and their versions.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
