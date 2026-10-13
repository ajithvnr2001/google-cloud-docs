---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.propertySchemaDefinitions
title: REST Resource: projects.locations.instances.propertySchemaDefinitions \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:29:32.349002+00:00
---

# REST Resource: projects.locations.instances.propertySchemaDefinitions  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.propertySchemaDefinitions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  REST Resource: projects.locations.instances.propertySchemaDefinitions Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: PropertySchemaDefinition
    * JSON representation
  * Methods



## Resource: PropertySchemaDefinition

This service is available for customers who migrated SOAR to a customer managed project and have the Chronicle API enabled. The properties metadata enable customers to rewrite how event fields will be presented and under what category they appear such as case overview – event fields and entity screen – enrichment fields. So for example, I can create a properties metadata in the platform so that all the events or enrichment fields that start with the VT_ prefix will be grouped under the VirusTotal category.

JSON representation  
---  
      
    
    {
      "name": string,
      "rawFieldName": string,
      "displayName": string,
      "groupName": string,
      "prefix": string,
      "trimPrefix": boolean,
      "system": boolean,
      "highlighted": boolean
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique name(ID) of the PropertySchemaDefinition. Format: projects/{project}/locations/{location}/instances/{instance}/propertySchemaDefinitions/{propertySchemaDefinition}  
`rawFieldName` |  `string` Required. Title of the raw field - the system name. Limited to 100 characters.  
`displayName` |  `string` Required. How to display the raw_field_title on the case overview screen.  
`groupName` |  `string` Required. Title of the group/category.  
`prefix` |  `string` Optional. Used for grouping multiple fields together. Limited to 256 characters.  
`trimPrefix` |  `boolean` Optional. Whether to display the prefix as part of the field name. Example – "VTdepartment" will be presented as "department" in case you defined "VT" prefix and trimmed it. Default value: false  
`system` |  `boolean` Output only. Indicates if the field is in the system category or not. Also inidicates if the field should be displayed in the UI screen or not.  
`highlighted` |  `boolean` Optional. To display the field in the Highlighted section of the cases overview screen or not. Default value: false  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.propertySchemaDefinitions/create)`

|  Creates a new PropertySchemaDefinition.  
  
### `[delete](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.propertySchemaDefinitions/delete)`

|  Deletes a PropertySchemaDefinition.  
  
### `[get](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.propertySchemaDefinitions/get)`

|  Gets a single PropertySchemaDefinition.  
  
### `[list](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.propertySchemaDefinitions/list)`

|  Lists PropertySchemaDefinitions.  
  
### `[patch](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.propertySchemaDefinitions/patch)`

|  Updates an existing PropertySchemaDefinition.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-20 UTC."],[],[]] 
