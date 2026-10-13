---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts.involvedEntities
title: REST Resource: projects.locations.instances.cases.caseAlerts.involvedEntities \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:37:19.663513+00:00
---

# REST Resource: projects.locations.instances.cases.caseAlerts.involvedEntities  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts.involvedEntities

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  REST Resource: projects.locations.instances.cases.caseAlerts.involvedEntities Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: InvolvedEntity
    * JSON representation
  * ContextGroup
    * JSON representation
  * ContextGroupItem
    * JSON representation
  * Methods



## Resource: InvolvedEntity

This service is available for customers who migrated SOAR to a customer managed project and have the Chronicle API enabled. This resource represents entities that are associated with both cases and caseAlerts, or with all caseAlerts related to a specific case. These entities are uniquely identified by their entityIdentifier and type. Additionally, we have another entity resource in our system that is not connected to cases and caseAlerts - 'Unique Entity' and represents every unique entity in the system. Unique entities is a separate collection of all distinct entities in the system, not in the context of case/alert. Unique entities get updated (if needed) during ingestion when new entities arrive.

JSON representation  
---  
      
    
    {
      "name": string,
      "id": string,
      "type": string,
      "threatSource": string,
      "operatingSystem": string,
      "networkTitle": string,
      "environment": string,
      "additionalProperties": string,
      "sourceSystemUri": string,
      "entityUri": string,
      "fields": [
        {
          object ([ContextGroup](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts.involvedEntities#ContextGroup))
        }
      ],
      "alertIdentifier": string,
      "caseId": integer,
      "identifier": string,
      "suspicious": boolean,
      "internal": boolean,
      "networkPriority": integer,
      "attacker": boolean,
      "pivot": boolean,
      "manuallyCreated": boolean,
      "enriched": boolean,
      "artifact": boolean,
      "vulnerable": boolean
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique name(ID) of the InvolvedEntity. Format: projects/{project}/locations/{location}/instances/{instance}/cases/{case}/caseAlerts/{caseAlert}/involvedEntities/{involvedEntity}  
`id` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. Immutable. The id of the entity.  
`type` |  `string` Required. Immutable. The type of the entity. Could be: HOSTNAME, USB, PROCESS, ADDRESS, …  
`threatSource` |  `string` Optional. Threat source of the entity.  
`operatingSystem` |  `string` Optional. Operating system related to the entity.  
`networkTitle` |  `string` Optional. Network name related to the entity.  
`environment` |  `string` Output only. Immutable. The environment the entity belongs to. Derived from the case and alert.  
`additionalProperties` |  `string` Optional. Stores additional properties, as a JSON format.  
`sourceSystemUri` |  `string` Optional. Output only. Immutable. Link to the source system.  
`entityUri` |  `string` Optional. Output only. The full url of the entity, calculated using the sourceSystemUri and the entity data. Optional if the sourceSystemUri is not defined.  
`fields[]` |  `object (`[ContextGroup](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts.involvedEntities#ContextGroup)`)` Output only. A list of context group items, which are calculated based on the entity's properties.  
`alertIdentifier` |  `string` Output only. The alert identifier of the alert that the involved entity is associated with.  
`caseId` |  `integer` Output only. The id of the case that the involved entity is associated with.  
`identifier` |  `string` Output only. The identifier name of the involved entity.  
`suspicious` |  `boolean` Required. Describes if the entity is suspicious or not.  
`internal` |  `boolean` Required. Indicates whether this entity is internal. This setting is configured in the application's settings, and any entity type can be designated as internal.  
`networkPriority` |  `integer` Optional. Network priority of a related network.  
`attacker` |  `boolean` Optional. Describes if the entity represents an attacker or not.  
`pivot` |  `boolean` Optional. Describes if the entity is a pivot or not. A pivot entity is an entity which is common to two or more cases. In the case graph, it is connected to other entities by a dotted line.  
`manuallyCreated` |  `boolean` Output only. Immutable. Describes if the entity was created by the system (as part of the ingestion flow), or manually by the user.  
`enriched` |  `boolean` Output only. Indicates whether the entity has been enriched. An entity is enriched when an action adds information from an external system.  
`artifact` |  `boolean` Output only. Describes if the entity is an artifact or not.  
`vulnerable` |  `boolean` Output only. Describes if the entity is vulnerable or not.  
  
## ContextGroup

A group of context items.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "items": [
        {
          object ([ContextGroupItem](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts.involvedEntities#ContextGroupItem))
        }
      ],
      "highlighted": boolean,
      "hidden": boolean
    }  
  
Fields  
---  
`displayName` |  `string` Output only. The name of the context group. Default context group is called "Default".  
`items[]` |  `object (`[ContextGroupItem](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts.involvedEntities#ContextGroupItem)`)` Output only. A list of items in the group.  
`highlighted` |  `boolean` Output only. Is the context group highlighted.  
`hidden` |  `boolean` Output only. Is the context group hidden.  
  
## ContextGroupItem

A single item in the context group.

JSON representation  
---  
      
    
    {
      "name": string,
      "originalName": string,
      "value": string
    }  
  
Fields  
---  
`name` |  `string` Output only. The name of the property  
`originalName` |  `string` Output only. The original name of the property.  
`value` |  `string` Output only. The property's value.  
  
## Methods  
  
---  
  
### `[addProperty](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts.involvedEntities/addProperty)`

|  Adds a new custom property to an InvolvedEntity.  
  
### `[create](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts.involvedEntities/create)`

|  Manually adds a new InvolvedEntity to a case and alert.  
  
### `[fetchCards](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts.involvedEntities/fetchCards)`

|  Returns metadate of each involved entity in a specific alert, including their connectivity and high-level status.  
  
### `[get](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts.involvedEntities/get)`

|  Gets a single InvolvedEntity by its resource name.  
  
### `[list](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts.involvedEntities/list)`

|  Lists all InvolvedEntities associated with a specific case and alert.  
  
### `[patch](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts.involvedEntities/patch)`

|  Updates an existing InvolvedEntity.  
  
### `[updateProperty](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts.involvedEntities/updateProperty)`

|  Updates the value of an existing custom property on an InvolvedEntity.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-18 UTC."],[],[]] 
