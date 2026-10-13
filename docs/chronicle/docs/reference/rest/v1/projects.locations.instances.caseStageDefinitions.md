---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseStageDefinitions
title: REST Resource: projects.locations.instances.caseStageDefinitions \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:36:48.039163+00:00
---

# REST Resource: projects.locations.instances.caseStageDefinitions  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseStageDefinitions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  REST Resource: projects.locations.instances.caseStageDefinitions Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: CaseStageDefinition
    * JSON representation
  * Methods



## Resource: CaseStageDefinition

This service is available for customers who migrated SOAR to a customer managed project and have the Chronicle API enabled. CaseStageDefinitions represents a stage in the lifecycle of a case.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "order": integer
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the CaseStageDefinition. Format: projects/{project}/locations/{location}/instances/{instance}/caseStageDefinitions/{caseStageDefinition}  
`displayName` |  `string` Required. Immutable. The display name of the new stage to create. The display name must be unique within the instance. The display name must not contain special characters.  
`order` |  `integer` Required. Immutable. Defines the case stage order in the lifetime of a case.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseStageDefinitions/create)`

|  Creates a new CaseStageDefinition.  
  
### `[delete](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseStageDefinitions/delete)`

|  Deletes a CaseStageDefinition.  
  
### `[get](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseStageDefinitions/get)`

|  Gets a single CaseStageDefinition by its resource name.  
  
### `[list](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseStageDefinitions/list)`

|  Lists all CaseStageDefinitions available in the instance.  
  
### `[patch](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseStageDefinitions/patch)`

|  Updates an existing CaseStageDefinition.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-18 UTC."],[],[]] 
