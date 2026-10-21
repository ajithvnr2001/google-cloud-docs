---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services/
title: REST Resource: services \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:26.163999+00:00
---

# REST Resource: services  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  REST Resource: services Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ManagedService
    * JSON representation
  * Methods



## Resource: ManagedService

The full representation of a Service that is managed by Google Service Management.

JSON representation  
---  
      
    
    {
      "serviceName": string,
      "producerProjectId": string
    }  
  
Fields  
---  
`serviceName` |  `string` The name of the service. See the [overview](https://cloud.google.com/service-infrastructure/docs/overview) for naming requirements.  
`producerProjectId` |  `string` ID of the project that produces and owns this service.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services/create)`

|  Creates a new managed service.  
  
### `[delete](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services/delete)`

|  Deletes a managed service.  
  
### `[disable](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services/disable)   
**(deprecated)**`

|  Disables a `[service](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services#ManagedService)` for a project, so it can no longer be be used for the project.  
  
### `[enable](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services/enable)   
**(deprecated)**`

|  Enables a `[service](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services#ManagedService)` for a project, so it can be used for the project.  
  
### `[generateConfigReport](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services/generateConfigReport)`

|  Generates and returns a report (errors, warnings and changes from existing configurations) associated with GenerateConfigReportRequest.new_valueIf GenerateConfigReportRequest.old_value is specified, GenerateConfigReportRequest will contain a single ChangeReport based on the comparison between GenerateConfigReportRequest.new_value and GenerateConfigReportRequest.old_value.  
  
### `[get](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services/get)`

|  Gets a managed service.  
  
### `[getConfig](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services/getConfig)`

|  Gets a service configuration (version) for a managed service.  
  
### `[getIamPolicy](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services/list)`

|  Lists managed services.  
  
### `[setIamPolicy](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
### `[undelete](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services/undelete)`

|  Revives a previously deleted managed service.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
