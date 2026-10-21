---
url: https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders.capabilities
title: REST Resource: folders.capabilities \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:08:28.307606+00:00
---

# REST Resource: folders.capabilities  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders.capabilities

  * [ Home ](https://docs.cloud.google.com/)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager)
  * [ Reference ](https://docs.cloud.google.com/resource-manager/reference/rest)



Send feedback 

#  REST Resource: folders.capabilities Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Capability
    * JSON representation
  * Methods



## Resource: Capability

Representation of a Capability.

JSON representation  
---  
      
    
    {
      "name": string,
      "value": boolean
    }  
  
Fields  
---  
`name` |  `string` Immutable. Identifier. The resource name of the capability. Must be in the following form: * `folders/{folder_id}/capabilities/{capability_name}`For example, `folders/123/capabilities/app-management`Following are the allowed {capability_name} values: * `app-management`  
`value` |  `boolean` Required. The configured value of the capability at the given parent resource.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders.capabilities/get)`

|  Retrieves the Capability identified by the supplied resource name.  
  
### `[patch](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders.capabilities/patch)`

|  Updates the Capability.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-11 UTC."],[],[]] 
