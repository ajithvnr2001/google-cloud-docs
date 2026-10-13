---
url: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.identityMappingStores
title: REST Resource: projects.locations.identityMappingStores \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:33:19.254544+00:00
---

# REST Resource: projects.locations.identityMappingStores  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.identityMappingStores

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Reference ](https://docs.cloud.google.com/gemini/enterprise/docs/apis)



Send feedback 

#  REST Resource: projects.locations.identityMappingStores Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: IdentityMappingStore
    * JSON representation
  * Methods



## Resource: IdentityMappingStore

Identity Mapping Store which contains Identity Mapping Entries.

JSON representation  
---  
      
    
    {
      "name": string,
      "kmsKeyName": string,
      "cmekConfig": {
        object ([CmekConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.cmekConfigs#CmekConfig))
      }
    }  
  
Fields  
---  
`name` |  `string` Immutable. The full resource name of the identity mapping store. Format: `projects/{project}/locations/{location}/identityMappingStores/{identityMappingStore}`. This field must be a UTF-8 encoded string with a length limit of 1024 characters.  
`kmsKeyName` |  `string` Input only. The KMS key to be used to protect this Identity Mapping Store at creation time.Must be set for requests that need to comply with CMEK Org Policy protections.If this field is set and processed successfully, the Identity Mapping Store will be protected by the KMS key, as indicated in the cmekConfig field.  
`cmekConfig` |  `object (`[CmekConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.cmekConfigs#CmekConfig)`)` Output only. CMEK-related information for the Identity Mapping Store.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.identityMappingStores/create)`

|  Creates a new Identity Mapping Store.  
  
### `[delete](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.identityMappingStores/delete)`

|  Deletes the Identity Mapping Store.  
  
### `[get](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.identityMappingStores/get)`

|  Gets the Identity Mapping Store.  
  
### `[importIdentityMappings](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.identityMappingStores/importIdentityMappings)`

|  Imports a list of Identity Mapping Entries to an Identity Mapping Store.  
  
### `[list](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.identityMappingStores/list)`

|  Lists all Identity Mapping Stores.  
  
### `[listIdentityMappings](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.identityMappingStores/listIdentityMappings)`

|  Lists Identity Mappings in an Identity Mapping Store.  
  
### `[purgeIdentityMappings](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.identityMappingStores/purgeIdentityMappings)`

|  Purges specified or all Identity Mapping Entries from an Identity Mapping Store.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-08 UTC."],[],[]] 
