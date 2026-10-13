---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.entityTypes
title: REST Resource: projects.locations.agents.entityTypes \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:37:59.555047+00:00
---

# REST Resource: projects.locations.agents.entityTypes  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.entityTypes

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  REST Resource: projects.locations.agents.entityTypes Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: EntityType
    * JSON representation
  * Kind
  * AutoExpansionMode
  * ExcludedPhrase
    * JSON representation
  * Methods



## Resource: EntityType

Entities are extracted from user input and represent parameters that are meaningful to your application. For example, a date range, a proper name such as a geographic location or landmark, and so on. Entities represent actionable data for your application.

When you define an entity, you can also include synonyms that all map to that entity. For example, "soft drink", "soda", "pop", and so on.

There are three types of entities:

  * **System** \- entities that are defined by the Dialogflow API for common data types such as date, time, currency, and so on. A system entity is represented by the `EntityType` type.

  * **Custom** \- entities that are defined by you that represent actionable data that is meaningful to your application. For example, you could define a `pizza.sauce` entity for red or white pizza sauce, a `pizza.cheese` entity for the different types of cheese on a pizza, a `pizza.topping` entity for different toppings, and so on. A custom entity is represented by the `EntityType` type.

  * **User** \- entities that are built for an individual user such as favorites, preferences, playlists, and so on. A user entity is represented by the `[SessionEntityType](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.environments.sessions.entityTypes#SessionEntityType)` type.




For more information about entity types, see the [Dialogflow documentation](https://cloud.google.com/dialogflow/docs/entities-overview).

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "kind": enum ([Kind](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.entityTypes#Kind)),
      "autoExpansionMode": enum ([AutoExpansionMode](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.entityTypes#AutoExpansionMode)),
      "entities": [
        {
          object ([Entity](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/Entity))
        }
      ],
      "excludedPhrases": [
        {
          object ([ExcludedPhrase](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.entityTypes#ExcludedPhrase))
        }
      ],
      "enableFuzzyExtraction": boolean,
      "redact": boolean
    }  
  
Fields  
---  
`name` |  `string` The unique identifier of the entity type. Required for `[EntityTypes.UpdateEntityType](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.entityTypes/patch#google.cloud.dialogflow.cx.v3beta1.EntityTypes.UpdateEntityType)`. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/entityTypes/<EntityTypeID>`.  
`displayName` |  `string` Required. The human-readable name of the entity type, unique within the agent.  
`kind` |  `enum (`[Kind](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.entityTypes#Kind)`)` Required. Indicates the kind of entity type.  
`autoExpansionMode` |  `enum (`[AutoExpansionMode](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.entityTypes#AutoExpansionMode)`)` Indicates whether the entity type can be automatically expanded.  
`entities[]` |  `object (`[Entity](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/Entity)`)` The collection of entity entries associated with the entity type.  
`excludedPhrases[]` |  `object (`[ExcludedPhrase](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.entityTypes#ExcludedPhrase)`)` Collection of exceptional words and phrases that shouldn't be matched. For example, if you have a size entity type with entry `giant`(an adjective), you might consider adding `giants`(a noun) as an exclusion. If the kind of entity type is `KIND_MAP`, then the phrases specified by entities and excluded phrases should be mutually exclusive.  
`enableFuzzyExtraction` |  `boolean` Enables fuzzy entity extraction during classification.  
`redact` |  `boolean` Indicates whether parameters of the entity type should be redacted in log. If redaction is enabled, page parameters and intent parameters referring to the entity type will be replaced by parameter name during logging.  
  
## Kind

Represents kinds of entities.

Enums  
---  
`KIND_UNSPECIFIED` | Not specified. This value should be never used.  
`KIND_MAP` | Map entity types allow mapping of a group of synonyms to a canonical value.  
`KIND_LIST` | List entity types contain a set of entries that do not map to canonical values. However, list entity types can contain references to other entity types (with or without aliases).  
`KIND_REGEXP` | Regexp entity types allow to specify regular expressions in entries values.  
  
## AutoExpansionMode

Represents different entity type expansion modes. Automated expansion allows an agent to recognize values that have not been explicitly listed in the entity (for example, new kinds of shopping list items).

Enums  
---  
`AUTO_EXPANSION_MODE_UNSPECIFIED` | Auto expansion disabled for the entity.  
`AUTO_EXPANSION_MODE_DEFAULT` | Allows an agent to recognize values that have not been explicitly listed in the entity.  
  
## ExcludedPhrase

An excluded entity phrase that should not be matched.

JSON representation  
---  
      
    
    {
      "value": string
    }  
  
Fields  
---  
`value` |  `string` Required. The word or phrase to be excluded.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.entityTypes/create)`

|  Creates an entity type in the specified agent.  
  
### `[delete](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.entityTypes/delete)`

|  Deletes the specified entity type.  
  
### `[export](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.entityTypes/export)`

|  Exports the selected entity types.  
  
### `[get](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.entityTypes/get)`

|  Retrieves the specified entity type.  
  
### `[import](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.entityTypes/import)`

|  Imports the specified entitytypes into the agent.  
  
### `[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.entityTypes/list)`

|  Returns the list of all entity types in the specified agent.  
  
### `[patch](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.entityTypes/patch)`

|  Updates the specified entity type.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
