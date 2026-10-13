---
url: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.entityTypes
title: REST Resource: projects.agent.entityTypes \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:32:02.909988+00:00
---

# REST Resource: projects.agent.entityTypes  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.entityTypes

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/es/docs/reference)



Send feedback 

#  REST Resource: projects.agent.entityTypes Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: EntityType
    * JSON representation
    * Kind
    * AutoExpansionMode
  * Methods



## Resource: EntityType

Each intent parameter has a type, called the entity type, which dictates exactly how data from an end-user expression is extracted.

Dialogflow provides predefined system entities that can match many common types of data. For example, there are system entities for matching dates, times, colors, email addresses, and so on. You can also create your own custom entities for matching custom data. For example, you could define a vegetable entity that can match the types of vegetables available for purchase with a grocery store agent.

For more information, see the [Entity guide](https://cloud.google.com/dialogflow/docs/entities-overview).

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "kind": enum ([Kind](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.entityTypes#EntityType.Kind)),
      "autoExpansionMode": enum ([AutoExpansionMode](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.entityTypes#EntityType.AutoExpansionMode)),
      "entities": [
        {
          object ([Entity](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/Entity))
        }
      ],
      "enableFuzzyExtraction": boolean
    }  
  
Fields  
---  
`name` |  `string` The unique identifier of the entity type. Required for `[EntityTypes.UpdateEntityType](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.entityTypes/patch#google.cloud.dialogflow.v2.EntityTypes.UpdateEntityType)` and `[EntityTypes.BatchUpdateEntityTypes](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.entityTypes/batchUpdate#google.cloud.dialogflow.v2.EntityTypes.BatchUpdateEntityTypes)` methods. Format: `projects/<Project ID>/agent/entityTypes/<Entity Type ID>`.  
`displayName` |  `string` Required. The name of the entity type.  
`kind` |  `enum (`[Kind](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.entityTypes#EntityType.Kind)`)` Required. Indicates the kind of entity type.  
`autoExpansionMode` |  `enum (`[AutoExpansionMode](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.entityTypes#EntityType.AutoExpansionMode)`)` Optional. Indicates whether the entity type can be automatically expanded.  
`entities[]` |  `object (`[Entity](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/Entity)`)` Optional. The collection of entity entries associated with the entity type.  
`enableFuzzyExtraction` |  `boolean` Optional. Enables fuzzy entity extraction during classification.  
  
### Kind

Represents kinds of entities.

Enums  
---  
`KIND_UNSPECIFIED` | Not specified. This value should be never used.  
`KIND_MAP` | Map entity types allow mapping of a group of synonyms to a reference value.  
`KIND_LIST` | List entity types contain a set of entries that do not map to reference values. However, list entity types can contain references to other entity types (with or without aliases).  
`KIND_REGEXP` | Regexp entity types allow to specify regular expressions in entries values.  
  
### AutoExpansionMode

Represents different entity type expansion modes. Automated expansion allows an agent to recognize values that have not been explicitly listed in the entity (for example, new kinds of shopping list items).

Enums  
---  
`AUTO_EXPANSION_MODE_UNSPECIFIED` | Auto expansion disabled for the entity.  
`AUTO_EXPANSION_MODE_DEFAULT` | Allows an agent to recognize values that have not been explicitly listed in the entity.  
  
## Methods  
  
---  
  
### `[batchDelete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.entityTypes/batchDelete)`

|  Deletes entity types in the specified agent.  
  
### `[batchUpdate](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.entityTypes/batchUpdate)`

|  Updates/Creates multiple entity types in the specified agent.  
  
### `[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.entityTypes/create)`

|  Creates an entity type in the specified agent.  
  
### `[delete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.entityTypes/delete)`

|  Deletes the specified entity type.  
  
### `[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.entityTypes/get)`

|  Retrieves the specified entity type.  
  
### `[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.entityTypes/list)`

|  Returns the list of all entity types in the specified agent.  
  
### `[patch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.entityTypes/patch)`

|  Updates the specified entity type.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
