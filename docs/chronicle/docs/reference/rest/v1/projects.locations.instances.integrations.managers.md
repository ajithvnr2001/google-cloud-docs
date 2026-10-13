---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.integrations.managers
title: REST Resource: projects.locations.instances.integrations.managers \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:30:48.924196+00:00
---

# REST Resource: projects.locations.instances.integrations.managers  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.integrations.managers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  REST Resource: projects.locations.instances.integrations.managers Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: IntegrationManager
    * JSON representation
  * Methods



## Resource: IntegrationManager

This service is available for customers who migrated SOAR to a customer managed project and have the Chronicle API enabled. Integration Managers provide reusable code utilities (functions, classes, etc.) // that can be imported and leveraged across various components, including connectors, scheduled jobs, and actions. This promotes modularity, code reuse, and consistency throughout the integration.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "script": string,
      "integration": string,
      "description": string,
      "author": string,
      "custom": boolean
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique name(ID) of the manager. Format: projects/{project}/locations/{location}/instances/{instance}/integrations/{integration}/managers/{manager}  
`displayName` |  `string` Required. Manager's definition name, limited to a maximum of 150 characters  
`script` |  `string` Required. Manager's script. Limited to a maximum of 5MB.  
`integration` |  `string` Output only. Manager's integration.  
`description` |  `string` Optional. Manager's description, limited to a maximum of 400 characters.  
`author` |  `string` Output only. The user who saved the manager.  
`custom` |  `boolean` Output only. Determines whether the manager is custom or commercial.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.integrations.managers/create)`

|  Creates a new custom IntegrationManager.  
  
### `[delete](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.integrations.managers/delete)`

|  Deletes a specific custom IntegrationManager.  
  
### `[fetchTemplate](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.integrations.managers/fetchTemplate)`

|  Returns a default recommended Python script template for an integration manager.  
  
### `[get](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.integrations.managers/get)`

|  Gets a single `IntegrationManager` by its resource name.  
  
### `[list](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.integrations.managers/list)`

|  Lists all IntegrationManagers defined for a specific integration.  
  
### `[patch](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.integrations.managers/patch)`

|  Updates an existing custom IntegrationManager.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-18 UTC."],[],[]] 
