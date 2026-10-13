---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.uniqueEntities
title: REST Resource: projects.locations.instances.uniqueEntities \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:27:32.441246+00:00
---

# REST Resource: projects.locations.instances.uniqueEntities  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.uniqueEntities

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  REST Resource: projects.locations.instances.uniqueEntities Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: UniqueEntity
    * JSON representation
  * PropertyValue
    * JSON representation
  * FetchFullUniqueEntityContextGroup
    * JSON representation
  * UniqueEntityContextGroupItem
    * JSON representation
  * Methods



## Resource: UniqueEntity

This service is available for customers who migrated SOAR to a customer managed project and have the Chronicle API enabled. This resource represents entities that are unique in the system and not associated with cases and alerts.

JSON representation  
---  
      
    
    {
      "name": string,
      "identifier": string,
      "type": string,
      "environment": string,
      "properties": [
        {
          object ([PropertyValue](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.uniqueEntities#PropertyValue))
        }
      ],
      "uniqueEntityId": integer,
      "fields": [
        {
          object ([FetchFullUniqueEntityContextGroup](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.uniqueEntities#FetchFullUniqueEntityContextGroup))
        }
      ],
      "dataAccessScopes": [
        string
      ],
      "suspicious": boolean,
      "enriched": boolean,
      "internalAsset": boolean,
      "artifact": boolean,
      "manuallyCreated": boolean,
      "network": string,
      "threatSource": string,
      "operatingSystem": string,
      "country": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique name of the entity.  
`identifier` |  `string` Output only. Identifier of the entity, contributing to its uniqueness.  
`type` |  `string` Output only. Type of the entity, contributing to its uniqueness.  
`environment` |  `string` Output only. The environment in which the entity exists, contributing to its uniqueness.  
`properties[]` |  `object (`[PropertyValue](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.uniqueEntities#PropertyValue)`)` Optional. Properties added by user or not part of this object properties.  
`uniqueEntityId` |  `integer` Output only. Unique Entity Id  
`fields[]` |  `object (`[FetchFullUniqueEntityContextGroup](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.uniqueEntities#FetchFullUniqueEntityContextGroup)`)` Optional. Context group for uniqueEntities.fetchFull.  
`dataAccessScopes[]` |  `string` Output only. Data Access Scopes, used to filter the data returned.  
`suspicious` |  `boolean` Optional. Describes if the entity is a suspicious or not.  
`enriched` |  `boolean` Output only. Describes if the entity is a enriched or not.  
`internalAsset` |  `boolean` Optional. Describes if the entity is an internal or not.  
`artifact` |  `boolean` Optional. Describes if the entity is an artifact or not.  
`manuallyCreated` |  `boolean` Output only. Describes if the entity is a manually created or not.  
`network` |  `string` Optional. Network name property.  
`threatSource` |  `string` Optional. Threat source of the entity.  
`operatingSystem` |  `string` Optional. The operating system related to the entity.  
`country` |  `string` Optional. The country related to the entity.  
  
## PropertyValue

A property key and value.

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string` Required. The property key.  
`value` |  `string` Required. The property value.  
  
## FetchFullUniqueEntityContextGroup

Context group for uniqueEntities.fetchFull.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "items": [
        {
          object ([UniqueEntityContextGroupItem](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.uniqueEntities#UniqueEntityContextGroupItem))
        }
      ],
      "highlighted": boolean,
      "hidden": boolean
    }  
  
Fields  
---  
`displayName` |  `string` Optional. Display name of the entity.  
`items[]` |  `object (`[UniqueEntityContextGroupItem](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.uniqueEntities#UniqueEntityContextGroupItem)`)` Optional. Context group items.  
`highlighted` |  `boolean` Optional. Highlighted property.  
`hidden` |  `boolean` Optional. Indicates if the entity is hidden property.  
  
## UniqueEntityContextGroupItem

Context group item.

JSON representation  
---  
      
    
    {
      "name": string,
      "originalName": string,
      "value": string
    }  
  
Fields  
---  
`name` |  `string` Optional. Name of the item.  
`originalName` |  `string` Optional. Original name of the item.  
`value` |  `string` Optional. Value of the item.  
  
## Methods  
  
---  
  
### `[addNote](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.uniqueEntities/addNote)`

|  Adds a comment or note to a unique entity.  
  
### `[download](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.uniqueEntities/download)`

|  Generates and downloads a report for a unique entity.  
  
### `[fetchFull](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.uniqueEntities/fetchFull)`

|  Fetches comprehensive information for a unique entity.  
  
### `[get](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.uniqueEntities/get)`

|  Gets a specific unique entity.  
  
### `[list](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.uniqueEntities/list)`

|  Lists unique entities within a specific instance.  
  
### `[patch](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.uniqueEntities/patch)`

|  Updates properties of a unique entity.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-13 UTC."],[],[]] 
