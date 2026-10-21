---
url: https://docs.cloud.google.com/cloud-assist/reference/rest/
title: Gemini Cloud Assist API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:06:57.388476+00:00
---

# Gemini Cloud Assist API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-assist/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Cloud Assist ](https://docs.cloud.google.com/cloud-assist)
  * [ API and references ](https://docs.cloud.google.com/cloud-assist/api-and-reference)



Send feedback 

#  Gemini Cloud Assist API Stay organized with collections  Save and categorize content based on your preferences. 

The AI-powered assistant for Google Cloud.

  * REST Resource: v1alpha.projects.locations
  * REST Resource: v1alpha.projects.locations.investigations
  * REST Resource: v1alpha.projects.locations.investigations.revisions
  * REST Resource: v1alpha.projects.locations.operations



## Service: geminicloudassist.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

  * <https://geminicloudassist.googleapis.com/$discovery/rest?version=v1alpha>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://geminicloudassist.googleapis.com`



## REST Resource: [v1alpha.projects.locations](https://docs.cloud.google.com/cloud-assist/reference/rest/v1alpha/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/cloud-assist/reference/rest/v1alpha/projects.locations/get)` |  `GET /v1alpha/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/cloud-assist/reference/rest/v1alpha/projects.locations/list)` |  `GET /v1alpha/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1alpha.projects.locations.investigations](https://docs.cloud.google.com/cloud-assist/reference/rest/v1alpha/projects.locations.investigations)

Methods  
---  
`[create](https://docs.cloud.google.com/cloud-assist/reference/rest/v1alpha/projects.locations.investigations/create)   
**(deprecated)**` |  `POST /v1alpha/{parent=projects/*/locations/*}/investigations`   
Deprecated: Investigations should only be created by the agent.  
`[delete](https://docs.cloud.google.com/cloud-assist/reference/rest/v1alpha/projects.locations.investigations/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/investigations/*}`   
Deletes a single Investigation.  
`[get](https://docs.cloud.google.com/cloud-assist/reference/rest/v1alpha/projects.locations.investigations/get)` |  `GET /v1alpha/{name=projects/*/locations/*/investigations/*}`   
Gets details of a single Investigation.  
`[getIamPolicy](https://docs.cloud.google.com/cloud-assist/reference/rest/v1alpha/projects.locations.investigations/getIamPolicy)` |  `GET /v1alpha/{resource=projects/*/locations/*/investigations/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/cloud-assist/reference/rest/v1alpha/projects.locations.investigations/list)` |  `GET /v1alpha/{parent=projects/*/locations/*}/investigations`   
Lists Investigations in a given project and location.  
`[patch](https://docs.cloud.google.com/cloud-assist/reference/rest/v1alpha/projects.locations.investigations/patch)   
**(deprecated)**` |  `PATCH /v1alpha/{investigation.name=projects/*/locations/*/investigations/*}`   
Deprecated: Investigations should only be modified by the agent.  
`[setIamPolicy](https://docs.cloud.google.com/cloud-assist/reference/rest/v1alpha/projects.locations.investigations/setIamPolicy)` |  `POST /v1alpha/{resource=projects/*/locations/*/investigations/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/cloud-assist/reference/rest/v1alpha/projects.locations.investigations/testIamPermissions)` |  `POST /v1alpha/{resource=projects/*/locations/*/investigations/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1alpha.projects.locations.investigations.revisions](https://docs.cloud.google.com/cloud-assist/reference/rest/v1alpha/projects.locations.investigations.revisions)

Methods  
---  
`[create](https://docs.cloud.google.com/cloud-assist/reference/rest/v1alpha/projects.locations.investigations.revisions/create)   
**(deprecated)**` |  `POST /v1alpha/{parent=projects/*/locations/*/investigations/*}/revisions`   
Deprecated: Investigations should only be modified by the agent.  
`[delete](https://docs.cloud.google.com/cloud-assist/reference/rest/v1alpha/projects.locations.investigations.revisions/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/investigations/*/revisions/*}`   
Deletes a single revision of an Investigation.  
`[get](https://docs.cloud.google.com/cloud-assist/reference/rest/v1alpha/projects.locations.investigations.revisions/get)` |  `GET /v1alpha/{name=projects/*/locations/*/investigations/*/revisions/*}`   
Gets details of a single revision of an Investigation.  
`[list](https://docs.cloud.google.com/cloud-assist/reference/rest/v1alpha/projects.locations.investigations.revisions/list)` |  `GET /v1alpha/{parent=projects/*/locations/*/investigations/*}/revisions`   
Lists Investigations in a given project.  
`[run](https://docs.cloud.google.com/cloud-assist/reference/rest/v1alpha/projects.locations.investigations.revisions/run)   
**(deprecated)**` |  `POST /v1alpha/{name=projects/*/locations/*/investigations/*/revisions/*}:run`   
Deprecated: Investigations should only be run by the agent.  
  
## REST Resource: [v1alpha.projects.locations.operations](https://docs.cloud.google.com/cloud-assist/reference/rest/v1alpha/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/cloud-assist/reference/rest/v1alpha/projects.locations.operations/cancel)` |  `POST /v1alpha/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/cloud-assist/reference/rest/v1alpha/projects.locations.operations/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/cloud-assist/reference/rest/v1alpha/projects.locations.operations/get)` |  `GET /v1alpha/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/cloud-assist/reference/rest/v1alpha/projects.locations.operations/list)` |  `GET /v1alpha/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-21 UTC."],[],[]] 
