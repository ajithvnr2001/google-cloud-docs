---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseCloseDefinitions
title: REST Resource: projects.locations.instances.caseCloseDefinitions \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:13:55.954324+00:00
---

# REST Resource: projects.locations.instances.caseCloseDefinitions  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseCloseDefinitions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  REST Resource: projects.locations.instances.caseCloseDefinitions Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: CaseCloseDefinition
    * JSON representation
  * CloseReason
  * Methods



## Resource: CaseCloseDefinition

This service is available for customers who migrated SOAR to a customer managed project and have the Chronicle API enabled. Provides the customers the ability to create root causes upon case closure.

JSON representation  
---  
      
    
    {
      "name": string,
      "closeReason": enum ([CloseReason](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseCloseDefinitions#CloseReason)),
      "rootCause": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique name(ID) of the CaseCloseDefinition. Format: projects/{project}/locations/{location}/instances/{instance}/caseCloseDefinitions/{caseCloseDefinition}  
`closeReason` |  `enum (`[CloseReason](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseCloseDefinitions#CloseReason)`)` Required. Specify why the case was closed.  
`rootCause` |  `string` Required. Provides detailed description about the specific root cause option.  
  
## CloseReason

The reason for closing the case.

Enums  
---  
`CLOSE_REASON_UNSPECIFIED` | Unspecified close reason.  
`MALICIOUS` | Malicious close reason.  
`NOT_MALICIOUS` | Not malicious close reason.  
`MAINTENANCE` | Maintenance close reason.  
`INCONCLUSIVE` | Inconclusive close reason.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseCloseDefinitions/create)`

|  Creates a new CaseCloseDefinition.  
  
### `[delete](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseCloseDefinitions/delete)`

|  Deletes a CaseCloseDefinition.  
  
### `[get](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseCloseDefinitions/get)`

|  Gets a single CaseCloseDefinition by its resource name.  
  
### `[list](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseCloseDefinitions/list)`

|  Lists all CaseCloseDefinitions.  
  
### `[patch](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseCloseDefinitions/patch)`

|  Updates an existing CaseCloseDefinition.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-18 UTC."],[],[]] 
