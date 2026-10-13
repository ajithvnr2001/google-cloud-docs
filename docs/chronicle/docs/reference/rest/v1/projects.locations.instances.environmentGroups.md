---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.environmentGroups
title: REST Resource: projects.locations.instances.environmentGroups \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:08:54.150581+00:00
---

# REST Resource: projects.locations.instances.environmentGroups  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.environmentGroups

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  REST Resource: projects.locations.instances.environmentGroups Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: EnvironmentGroup
    * JSON representation
  * Methods



## Resource: EnvironmentGroup

This service is available for customers who migrated SOAR to a customer managed project and have the Chronicle API enabled. EnvironmentGroup - Chronicle SOAR EnvironmentGroup.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "environmentsIds": [
        string
      ],
      "description": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the environment group. Format: projects/{project}/locations/{location}/instances/{instance}/environmentGroups/{environmentGroup}  
`displayName` |  `string` Required. The group name.  
`environmentsIds[]` |  `string` Required. The environment IDs for the group.  
`description` |  `string` Optional. The EnvironmentGroup description. This value is optional. This value should be up to 250 characters, and valid characters are /[a-z][0-9]-/.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.environmentGroups/create)`

|  Creates a new EnvironmentGroup.  
  
### `[delete](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.environmentGroups/delete)`

|  Deletes a specific EnvironmentGroup.  
  
### `[get](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.environmentGroups/get)`

|  Gets a single EnvironmentGroup by its `name`.  
  
### `[list](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.environmentGroups/list)`

|  Lists all EnvironmentGroups available in the instance.  
  
### `[patch](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.environmentGroups/patch)`

|  Updates an existing EnvironmentGroup.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-13 UTC."],[],[]] 
