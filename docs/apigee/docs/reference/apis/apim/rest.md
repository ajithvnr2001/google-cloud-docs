---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/
title: API Management API \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:10:59.336282+00:00
---

# API Management API  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  API Management API Stay organized with collections  Save and categorize content based on your preferences. 

Enables users to discover shadow APIs in existing Google Cloud infrastructure.

  * REST Resource: v1alpha.projects.locations
  * REST Resource: v1alpha.projects.locations.observationJobs
  * REST Resource: v1alpha.projects.locations.observationJobs.apiObservations
  * REST Resource: v1alpha.projects.locations.observationJobs.apiObservations.apiOperations
  * REST Resource: v1alpha.projects.locations.observationSources
  * REST Resource: v1alpha.projects.locations.operations



## Service: apim.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://apim.googleapis.com`



## REST Resource: [v1alpha.projects.locations](https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/v1alpha/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/v1alpha/projects.locations/get)` |  `GET /v1alpha/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/v1alpha/projects.locations/list)` |  `GET /v1alpha/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
`[listApiObservationTags](https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/v1alpha/projects.locations/listApiObservationTags)` |  `GET /v1alpha/{parent=projects/*/locations/*}:listApiObservationTags`   
ListApiObservationTags lists all extant tags on any observation in the given project.  
  
## REST Resource: [v1alpha.projects.locations.observationJobs](https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/v1alpha/projects.locations.observationJobs)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/v1alpha/projects.locations.observationJobs/create)` |  `POST /v1alpha/{parent=projects/*/locations/*}/observationJobs`   
CreateObservationJob creates a new ObservationJob but does not have any effecton its own.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/v1alpha/projects.locations.observationJobs/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/observationJobs/*}`   
DeleteObservationJob deletes an ObservationJob.  
`[disable](https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/v1alpha/projects.locations.observationJobs/disable)` |  `POST /v1alpha/{name=projects/*/locations/*/observationJobs/*}:disable`   
Disables the given ObservationJob.  
`[enable](https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/v1alpha/projects.locations.observationJobs/enable)` |  `POST /v1alpha/{name=projects/*/locations/*/observationJobs/*}:enable`   
Enables the given ObservationJob.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/v1alpha/projects.locations.observationJobs/get)` |  `GET /v1alpha/{name=projects/*/locations/*/observationJobs/*}`   
GetObservationJob retrieves a single ObservationJob by name.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/v1alpha/projects.locations.observationJobs/list)` |  `GET /v1alpha/{parent=projects/*/locations/*}/observationJobs`   
ListObservationJobs gets all ObservationJobs for a given project and location.  
  
## REST Resource: [v1alpha.projects.locations.observationJobs.apiObservations](https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/v1alpha/projects.locations.observationJobs.apiObservations)

Methods  
---  
`[batchEditTags](https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/v1alpha/projects.locations.observationJobs.apiObservations/batchEditTags)` |  `POST /v1alpha/{parent=projects/*/locations/*/observationJobs/*}/apiObservations:batchEditTags`   
BatchEditTagsApiObservations adds or removes Tags for ApiObservations.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/v1alpha/projects.locations.observationJobs.apiObservations/get)` |  `GET /v1alpha/{name=projects/*/locations/*/observationJobs/*/apiObservations/*}`   
GetApiObservation retrieves a single ApiObservation by name.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/v1alpha/projects.locations.observationJobs.apiObservations/list)` |  `GET /v1alpha/{parent=projects/*/locations/*/observationJobs/*}/apiObservations`   
ListApiObservations gets all ApiObservations for a given project and location and ObservationJob.  
  
## REST Resource: [v1alpha.projects.locations.observationJobs.apiObservations.apiOperations](https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/v1alpha/projects.locations.observationJobs.apiObservations.apiOperations)

Methods  
---  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/v1alpha/projects.locations.observationJobs.apiObservations.apiOperations/get)` |  `GET /v1alpha/{name=projects/*/locations/*/observationJobs/*/apiObservations/*/apiOperations/*}`   
GetApiOperation retrieves a single ApiOperation by name.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/v1alpha/projects.locations.observationJobs.apiObservations.apiOperations/list)` |  `GET /v1alpha/{parent=projects/*/locations/*/observationJobs/*/apiObservations/*}/apiOperations`   
ListApiOperations gets all ApiOperations for a given project and location and ObservationJob and ApiObservation.  
  
## REST Resource: [v1alpha.projects.locations.observationSources](https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/v1alpha/projects.locations.observationSources)

Methods  
---  
`[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/v1alpha/projects.locations.observationSources/create)` |  `POST /v1alpha/{parent=projects/*/locations/*}/observationSources`   
CreateObservationSource creates a new ObservationSource but does not affect any deployed infrastructure.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/v1alpha/projects.locations.observationSources/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/observationSources/*}`   
DeleteObservationSource deletes an observation source.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/v1alpha/projects.locations.observationSources/get)` |  `GET /v1alpha/{name=projects/*/locations/*/observationSources/*}`   
GetObservationSource retrieves a single ObservationSource by name.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/v1alpha/projects.locations.observationSources/list)` |  `GET /v1alpha/{parent=projects/*/locations/*}/observationSources`   
ListObservationSources gets all ObservationSources for a given project and location.  
  
## REST Resource: [v1alpha.projects.locations.operations](https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/v1alpha/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/v1alpha/projects.locations.operations/cancel)` |  `POST /v1alpha/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/v1alpha/projects.locations.operations/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/v1alpha/projects.locations.operations/get)` |  `GET /v1alpha/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apim/rest/v1alpha/projects.locations.operations/list)` |  `GET /v1alpha/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
