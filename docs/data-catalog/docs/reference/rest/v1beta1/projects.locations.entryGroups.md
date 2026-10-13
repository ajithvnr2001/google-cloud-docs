---
url: https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1beta1/projects.locations.entryGroups
title: REST Resource: projects.locations.entryGroups \u00a0|\u00a0 Data Catalog Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:16:05.296884+00:00
---

# REST Resource: projects.locations.entryGroups  |  Data Catalog Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1beta1/projects.locations.entryGroups

Data Catalog API methods that are related to Data Catalog search and metadata are deprecated and will be discontinued on June 1, 2026. See [Transition from Data Catalog to Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/transition-to-dataplex-catalog). Methods that are related to policy tags and policy tag taxonomies are not deprecated. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Data Catalog ](https://docs.cloud.google.com/products)
  * [ Documentation ](https://docs.cloud.google.com/data-catalog/docs)
  * [ Reference ](https://docs.cloud.google.com/data-catalog/docs/reference)



Send feedback 

#  REST Resource: projects.locations.entryGroups Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: EntryGroup
    * JSON representation
  * Methods



## Resource: EntryGroup

EntryGroup Metadata. An EntryGroup resource represents a logical grouping of zero or more Data Catalog `[Entry](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1beta1/projects.locations.entryGroups.entries#Entry)` resources.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "dataCatalogTimestamps": {
        object ([SystemTimestamps](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1beta1/SystemTimestamps))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the entry group in URL format. Example:

  * projects/{projectId}/locations/{location}/entryGroups/{entryGroupId}

Note that this EntryGroup and its child resources may not actually be stored in the location in this name.  
`displayName` |  `string` A short name to identify the entry group, for example, "analytics data - jan 2011". Default value is an empty string.  
`description` |  `string` Entry group description, which can consist of several sentences or paragraphs that describe entry group contents. Default value is an empty string.  
`dataCatalogTimestamps` |  `object (`[SystemTimestamps](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1beta1/SystemTimestamps)`)` Output only. Timestamps about this EntryGroup. Default value is empty timestamps.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1beta1/projects.locations.entryGroups/create)   
**(deprecated)**`

|  A maximum of 10,000 entry groups may be created per organization across all locations.  
  
### `[delete](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1beta1/projects.locations.entryGroups/delete)   
**(deprecated)**`

|  Deletes an EntryGroup.  
  
### `[get](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1beta1/projects.locations.entryGroups/get)   
**(deprecated)**`

|  Gets an EntryGroup.  
  
### `[getIamPolicy](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1beta1/projects.locations.entryGroups/getIamPolicy)   
**(deprecated)**`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1beta1/projects.locations.entryGroups/list)   
**(deprecated)**`

|  Lists entry groups.  
  
### `[patch](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1beta1/projects.locations.entryGroups/patch)   
**(deprecated)**`

|  Updates an EntryGroup.  
  
### `[setIamPolicy](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1beta1/projects.locations.entryGroups/setIamPolicy)   
**(deprecated)**`

|  Sets the access control policy for a resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1beta1/projects.locations.entryGroups/testIamPermissions)   
**(deprecated)**`

|  Returns the caller's permissions on a resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-17 UTC."],[],[]] 
