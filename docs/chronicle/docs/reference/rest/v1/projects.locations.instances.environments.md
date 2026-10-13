---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.environments
title: REST Resource: projects.locations.instances.environments \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:11:08.045990+00:00
---

# REST Resource: projects.locations.instances.environments  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.environments

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  REST Resource: projects.locations.instances.environments Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Environment
    * JSON representation
  * EnvironmentDynamicParameter
    * JSON representation
  * Methods



## Resource: Environment

This service is available for customers who migrated SOAR to a customer managed project and have the Chronicle API enabled. An environment is simply another word for your different networks or customers that are managed by the SOC or MSSP. This is useful for SOCs who provide services to several different networks, customers or business units within the organization. The Platform comes with a predefined environment named Default Environment.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "contact": string,
      "contactEmails": string,
      "contactPhone": string,
      "base64Image": string,
      "retentionDuration": integer,
      "dynamicParameters": [
        {
          object ([EnvironmentDynamicParameter](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.environments#EnvironmentDynamicParameter))
        }
      ],
      "system": boolean,
      "aliasesJson": string,
      "instanceUri": string,
      "dataAccessScopesJson": string,
      "weight": integer,
      "instance": string,
      "environmentAllowedForAllUsers": boolean
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique name(ID) of the Environment. Format: projects/{project}/locations/{location}/instances/{instance}/environments/{environment}  
`displayName` |  `string` Required. Immutable. Replaces the "Name" prop with "ResourceName". MAX_NAME_LENGTH = 256  
`description` |  `string` Required. MAX_NAME_LENGTH = 256 Description of the environment.  
`contact` |  `string` Required. MAX_NAME_LENGTH = 256 Name of the contact for the environment.  
`contactEmails` |  `string` Required. MAX_NAME_LENGTH = 256 Email of the contact for the environment.  
`contactPhone` |  `string` Required. MAX_NAME_LENGTH = 256 Phone number of the contact for the environment.  
`base64Image` |  `string` Optional. MAX_NAME_LENGTH = 1024 Environment icon.  
`retentionDuration` |  `integer` Required. Environment data retention in months.  
`dynamicParameters[]` |  `object (`[EnvironmentDynamicParameter](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.environments#EnvironmentDynamicParameter)`)` Required. Additional custom properties for enriching the environment. For example: { "value": "value1", "dynamicParameterId": 123, "environmentId": 456 }  
`system` |  `boolean` Required. Output only. Whether the environment is a system environment.  
`aliasesJson` |  `string` Optional. Environment nicknames.  
`instanceUri` |  `string` Optional. URL of the environment. Used to route UI links to the correct SIEM instance when making cross-SecOps requests from SOAR. Format: https://.backstory.chronicle.security?myUrlParam=myValue  
`dataAccessScopesJson` |  `string` Optional. data access scopes.  
`weight` |  `integer` Optional. The weight of the environment, enabling customers to control distribution of resources between the separate environments in a single instance of Chronicle SOAR. Environments with higher weights get prioritized for processing in Chronicle SOAR via a lottery algorithm. Defaults to 1.  
`instance` |  `string` Optional. The optional parallel SIEM instance used as a data source. Used to route API requests to the correct SIEM instance when making cross-SecOps requests from SOAR. For most customers, this is not required, since the parent instance is used as the data source by default. Format: projects/{project}/locations/{location}/instances/{instance}  
`environmentAllowedForAllUsers` |  `boolean` Optional. Optional. If set to true, automatically assigns the new environment to all existing users and API keys.  
  
## EnvironmentDynamicParameter

Dynamic parameter for the environment.

JSON representation  
---  
      
    
    {
      "value": string,
      "dynamicParameterId": string,
      "environmentId": string
    }  
  
Fields  
---  
`value` |  `string` Required. The value of the dynamic parameter.  
`dynamicParameterId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. The ID of the dynamic parameter.  
`environmentId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. The ID of the environment.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.environments/create)`

|  Creates a new Environment.  
  
### `[delete](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.environments/delete)`

|  Deletes a specific Environment.  
  
### `[get](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.environments/get)`

|  Gets a single Environment by its resource name.  
  
### `[list](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.environments/list)`

|  Lists all Environments available in the instance.  
  
### `[patch](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.environments/patch)`

|  Updates an existing Environment.  
  
### `[resetWeights](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.environments/resetWeights)`

|  Resets the resource distribution weights for all environments.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
