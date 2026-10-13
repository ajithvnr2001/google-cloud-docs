---
url: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.environments.users.sessions.entityTypes
title: REST Resource: projects.locations.agent.environments.users.sessions.entityTypes \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:32:39.521621+00:00
---

# REST Resource: projects.locations.agent.environments.users.sessions.entityTypes  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.environments.users.sessions.entityTypes

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/es/docs/reference)



Send feedback 

#  REST Resource: projects.locations.agent.environments.users.sessions.entityTypes Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: SessionEntityType
    * JSON representation
  * Methods



## Resource: SessionEntityType

A session represents a conversation between a Dialogflow agent and an end-user. You can create special entities, called session entities, during a session. Session entities can extend or replace custom entity types and only exist during the session that they were created for. All session data, including session entities, is stored by Dialogflow for 20 minutes.

For more information, see the [session entity guide](https://cloud.google.com/dialogflow/docs/entities-session).

JSON representation  
---  
      
    
    {
      "name": string,
      "entityOverrideMode": enum ([EntityOverrideMode](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments.users.sessions.entityTypes#SessionEntityType.EntityOverrideMode)),
      "entities": [
        {
          object ([Entity](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/Entity))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Required. The unique identifier of this session entity type. Format: `projects/<Project ID>/agent/sessions/<Session ID>/entityTypes/<Entity Type Display Name>`, or `projects/<Project ID>/agent/environments/<Environment ID>/users/<User ID>/sessions/<Session ID>/entityTypes/<Entity Type Display Name>`. If `Environment ID` is not specified, we assume default 'draft' environment. If `User ID` is not specified, we assume default '-' user.`<Entity Type Display Name>` must be the display name of an existing entity type in the same agent that will be overridden or supplemented.  
`entityOverrideMode` |  `enum (`[EntityOverrideMode](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments.users.sessions.entityTypes#SessionEntityType.EntityOverrideMode)`)` Required. Indicates whether the additional data should override or supplement the custom entity type definition.  
`entities[]` |  `object (`[Entity](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/Entity)`)` Required. The collection of entities associated with this session entity type.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.environments.users.sessions.entityTypes/create)`

|  Creates a session entity type.  
  
### `[delete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.environments.users.sessions.entityTypes/delete)`

|  Deletes the specified session entity type.  
  
### `[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.environments.users.sessions.entityTypes/get)`

|  Retrieves the specified session entity type.  
  
### `[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.environments.users.sessions.entityTypes/list)`

|  Returns the list of all session entity types in the specified session.  
  
### `[patch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.environments.users.sessions.entityTypes/patch)`

|  Updates the specified session entity type.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
