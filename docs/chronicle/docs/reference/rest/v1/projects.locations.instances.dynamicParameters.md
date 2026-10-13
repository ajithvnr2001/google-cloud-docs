---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.dynamicParameters
title: REST Resource: projects.locations.instances.dynamicParameters \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:39:32.691321+00:00
---

# REST Resource: projects.locations.instances.dynamicParameters  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.dynamicParameters

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  REST Resource: projects.locations.instances.dynamicParameters Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: DynamicParameter
    * JSON representation
  * DynamicParameterType
  * Methods



## Resource: DynamicParameter

This service is available for customers who migrated SOAR to a customer managed project and have the Chronicle API enabled. DynamicParameter - Chronicle SOAR Dynamic Parameter. Dynamic Parameters allows you to create "groups" or "categories" of environments to further help categorize and define environments. This can come in particularly useful when running Playbooks as you can use Custom Trigger/Actions or Conditions based on one of these new environment parameters. This provides greater customization for Playbooks and is useful for Enterprises or MSSPs with lots of tenants.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "parameterType": enum ([DynamicParameterType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.dynamicParameters#DynamicParameterType)),
      "defaultValue": string,
      "optionalValuesJson": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the DynamicParameter. Format: projects/{project}/locations/{location}/instances/{instance}/dynamicParameters/{dynamicParameter}  
`displayName` |  `string` Required. The display name of the new stage to create.  
`parameterType` |  `enum (`[DynamicParameterType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.dynamicParameters#DynamicParameterType)`)` Required. Defines the DynamicParameter's parameter type.  
`defaultValue` |  `string` Optional. Defines the DynamicParameter Default Value.  
`optionalValuesJson` |  `string` Optional. Defines the DynamicParameter optional values.  
  
## DynamicParameterType

The type of the DynamicParameter.

Enums  
---  
`DYNAMIC_PARAMETER_TYPE_UNSPECIFIED` | The default value.  
`STRING` | The parameter is a string.  
`LIST` | The parameter is a list of strings.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.dynamicParameters/create)`

|  Creates a new DynamicParameter.  
  
### `[delete](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.dynamicParameters/delete)`

|  Deletes a DynamicParameter.  
  
### `[export](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.dynamicParameters/export)`

|  Exports all DynamicParameters defined in the instance to a CSV file.  
  
### `[get](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.dynamicParameters/get)`

|  Gets a single DynamicParameter by its resource name.  
  
### `[import](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.dynamicParameters/import)`

|  Imports DynamicParameters from a CSV file.  
  
### `[list](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.dynamicParameters/list)`

|  Lists all DynamicParameters defined in the instance.  
  
### `[patch](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.dynamicParameters/patch)`

|  Updates an existing DynamicParameter.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-18 UTC."],[],[]] 
