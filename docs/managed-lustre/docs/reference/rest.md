---
url: https://docs.cloud.google.com/managed-lustre/docs/reference/rest/
title: Google Cloud Managed Lustre API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:56:03.893513+00:00
---

# Google Cloud Managed Lustre API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-lustre/docs/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Managed Lustre ](https://docs.cloud.google.com/managed-lustre/docs/overview)
  * [ Reference ](https://docs.cloud.google.com/managed-lustre/docs/apis)



Send feedback 

#  Google Cloud Managed Lustre API Stay organized with collections  Save and categorize content based on your preferences. 

  * REST Resource: v1.projects.locations
  * REST Resource: v1.projects.locations.instances
  * REST Resource: v1.projects.locations.operations



## Service: lustre.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

  * <https://lustre.googleapis.com/$discovery/rest?version=v1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://lustre.googleapis.com`



## REST Resource: [v1.projects.locations](https://docs.cloud.google.com/managed-lustre/docs/reference/rest/v1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/managed-lustre/docs/reference/rest/v1/projects.locations/get)` |  `GET /v1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/managed-lustre/docs/reference/rest/v1/projects.locations/list)` |  `GET /v1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1.projects.locations.instances](https://docs.cloud.google.com/managed-lustre/docs/reference/rest/v1/projects.locations.instances)

Methods  
---  
`[create](https://docs.cloud.google.com/managed-lustre/docs/reference/rest/v1/projects.locations.instances/create)` |  `POST /v1/{parent=projects/*/locations/*}/instances`   
Creates a new instance in a given project and location.  
`[delete](https://docs.cloud.google.com/managed-lustre/docs/reference/rest/v1/projects.locations.instances/delete)` |  `DELETE /v1/{name=projects/*/locations/*/instances/*}`   
Deletes a single instance.  
`[exportData](https://docs.cloud.google.com/managed-lustre/docs/reference/rest/v1/projects.locations.instances/exportData)` |  `POST /v1/{name=projects/*/locations/*/instances/*}:exportData`   
Exports data from a Managed Lustre instance to Cloud Storage.  
`[get](https://docs.cloud.google.com/managed-lustre/docs/reference/rest/v1/projects.locations.instances/get)` |  `GET /v1/{name=projects/*/locations/*/instances/*}`   
Gets details of a single instance.  
`[importData](https://docs.cloud.google.com/managed-lustre/docs/reference/rest/v1/projects.locations.instances/importData)` |  `POST /v1/{name=projects/*/locations/*/instances/*}:importData`   
Imports data from Cloud Storage to a Managed Lustre instance.  
`[list](https://docs.cloud.google.com/managed-lustre/docs/reference/rest/v1/projects.locations.instances/list)` |  `GET /v1/{parent=projects/*/locations/*}/instances`   
Lists instances in a given project and location.  
`[patch](https://docs.cloud.google.com/managed-lustre/docs/reference/rest/v1/projects.locations.instances/patch)` |  `PATCH /v1/{instance.name=projects/*/locations/*/instances/*}`   
Updates the parameters of a single instance.  
`[rescheduleMaintenance](https://docs.cloud.google.com/managed-lustre/docs/reference/rest/v1/projects.locations.instances/rescheduleMaintenance)` |  `POST /v1/{name=projects/*/locations/*/instances/*}:rescheduleMaintenance`   
Reschedules a planned maintenance event for a specific instance.  
  
## REST Resource: [v1.projects.locations.operations](https://docs.cloud.google.com/managed-lustre/docs/reference/rest/v1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/managed-lustre/docs/reference/rest/v1/projects.locations.operations/cancel)` |  `POST /v1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/managed-lustre/docs/reference/rest/v1/projects.locations.operations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/managed-lustre/docs/reference/rest/v1/projects.locations.operations/get)` |  `GET /v1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/managed-lustre/docs/reference/rest/v1/projects.locations.operations/list)` |  `GET /v1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-04 UTC."],[],[]] 
