---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.cases.alerts.contextProperties
title: REST Resource: projects.locations.instances.cases.alerts.contextProperties \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:35:47.926314+00:00
---

# REST Resource: projects.locations.instances.cases.alerts.contextProperties  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.cases.alerts.contextProperties

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback 

#  REST Resource: projects.locations.instances.cases.alerts.contextProperties Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ContextProperty
    * JSON representation
  * Methods



## Resource: ContextProperty

This service is available for customers who migrated SOAR to a customer managed project and have the Chronicle API enabled. ContextProperty - Chronicle SOAR ContextProperty.

JSON representation  
---  
      
    
    {
      "name": string,
      "value": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique name of the ContextProperty - the property key This value should be 4-63 characters and valid characters are /[a-z][0-9]-/.  
`value` |  `string` Required. The property value  
  
## Methods  
  
---  
  
### `[clearAll](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.cases.alerts.contextProperties/clearAll)`

|  The method clears all context-properties set on a specific context.  
  
### `[create](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.cases.alerts.contextProperties/create)`

|  Create a context-property.  
  
### `[delete](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.cases.alerts.contextProperties/delete)`

|  Delete a context-property.  
  
### `[get](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.cases.alerts.contextProperties/get)`

|  Get a context-property.  
  
### `[list](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.cases.alerts.contextProperties/list)`

|  List context-properties.  
  
### `[patch](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.cases.alerts.contextProperties/patch)`

|  Update a context-property.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-25 UTC."],[],[]] 
