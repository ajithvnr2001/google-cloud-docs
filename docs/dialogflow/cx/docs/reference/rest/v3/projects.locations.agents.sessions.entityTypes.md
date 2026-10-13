---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.sessions.entityTypes
title: REST Resource: projects.locations.agents.sessions.entityTypes \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:18.366040+00:00
---

# REST Resource: projects.locations.agents.sessions.entityTypes  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.sessions.entityTypes

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  REST Resource: projects.locations.agents.sessions.entityTypes Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: SessionEntityType
    * JSON representation
  * Methods



## Resource: SessionEntityType

Session entity types are referred to as **User** entity types and are entities that are built for an individual user such as favorites, preferences, playlists, and so on.

You can redefine a session entity type at the session level to extend or replace a `[custom entity type](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.entityTypes#EntityType)` at the user session level (we refer to the entity types defined at the agent level as "custom entity types").

Note: session entity types apply to all queries, regardless of the language.

For more information about entity types, see the [Dialogflow documentation](https://cloud.google.com/dialogflow/docs/entities-overview).

JSON representation  
---  
      
    
    {
      "name": string,
      "entityOverrideMode": enum ([EntityOverrideMode](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.sessions.entityTypes#SessionEntityType.EntityOverrideMode)),
      "entities": [
        {
          object ([Entity](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Entity))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Required. The unique identifier of the session entity type. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/sessions/<SessionID>/entityTypes/<EntityTypeID>` or `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>/sessions/<SessionID>/entityTypes/<EntityTypeID>`. If `Environment ID` is not specified, we assume default 'draft' environment.  
`entityOverrideMode` |  `enum (`[EntityOverrideMode](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.sessions.entityTypes#SessionEntityType.EntityOverrideMode)`)` Required. Indicates whether the additional data should override or supplement the custom entity type definition.  
`entities[]` |  `object (`[Entity](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Entity)`)` Required. The collection of entities to override or supplement the custom entity type.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.sessions.entityTypes/create)`

|  Creates a session entity type.  
  
### `[delete](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.sessions.entityTypes/delete)`

|  Deletes the specified session entity type.  
  
### `[get](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.sessions.entityTypes/get)`

|  Retrieves the specified session entity type.  
  
### `[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.sessions.entityTypes/list)`

|  Returns the list of all session entity types in the specified session.  
  
### `[patch](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.sessions.entityTypes/patch)`

|  Updates the specified session entity type.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
