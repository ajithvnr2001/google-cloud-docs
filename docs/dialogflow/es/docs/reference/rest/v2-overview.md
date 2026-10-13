---
url: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2-overview/
title: Dialogflow API \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:32:00.182586+00:00
---

# Dialogflow API  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/es/docs/reference)



Send feedback 

#  Dialogflow API Stay organized with collections  Save and categorize content based on your preferences. 

Builds conversational interfaces (for example, chatbots, and voice-powered apps and devices).

  * REST Resource: v2.projects
  * REST Resource: v2.projects.agent
  * REST Resource: v2.projects.agent.entityTypes
  * REST Resource: v2.projects.agent.entityTypes.entities
  * REST Resource: v2.projects.agent.environments
  * REST Resource: v2.projects.agent.environments.intents
  * REST Resource: v2.projects.agent.environments.users.sessions
  * REST Resource: v2.projects.agent.environments.users.sessions.contexts
  * REST Resource: v2.projects.agent.environments.users.sessions.entityTypes
  * REST Resource: v2.projects.agent.intents
  * REST Resource: v2.projects.agent.knowledgeBases
  * REST Resource: v2.projects.agent.knowledgeBases.documents
  * REST Resource: v2.projects.agent.sessions
  * REST Resource: v2.projects.agent.sessions.contexts
  * REST Resource: v2.projects.agent.sessions.entityTypes
  * REST Resource: v2.projects.agent.versions
  * REST Resource: v2.projects.answerRecords
  * REST Resource: v2.projects.conversationDatasets
  * REST Resource: v2.projects.conversationModels
  * REST Resource: v2.projects.conversationModels.evaluations
  * REST Resource: v2.projects.conversationProfiles
  * REST Resource: v2.projects.conversations
  * REST Resource: v2.projects.conversations.messages
  * REST Resource: v2.projects.conversations.participants
  * REST Resource: v2.projects.conversations.participants.suggestions
  * REST Resource: v2.projects.conversations.suggestions
  * REST Resource: v2.projects.generators
  * REST Resource: v2.projects.knowledgeBases
  * REST Resource: v2.projects.knowledgeBases.documents
  * REST Resource: v2.projects.locations
  * REST Resource: v2.projects.locations.agent
  * REST Resource: v2.projects.locations.agent.entityTypes
  * REST Resource: v2.projects.locations.agent.entityTypes.entities
  * REST Resource: v2.projects.locations.agent.environments
  * REST Resource: v2.projects.locations.agent.environments.intents
  * REST Resource: v2.projects.locations.agent.environments.users.sessions
  * REST Resource: v2.projects.locations.agent.environments.users.sessions.contexts
  * REST Resource: v2.projects.locations.agent.environments.users.sessions.entityTypes
  * REST Resource: v2.projects.locations.agent.intents
  * REST Resource: v2.projects.locations.agent.sessions
  * REST Resource: v2.projects.locations.agent.sessions.contexts
  * REST Resource: v2.projects.locations.agent.sessions.entityTypes
  * REST Resource: v2.projects.locations.agent.versions
  * REST Resource: v2.projects.locations.answerRecords
  * REST Resource: v2.projects.locations.companionAgents
  * REST Resource: v2.projects.locations.conversationDatasets
  * REST Resource: v2.projects.locations.conversationModels
  * REST Resource: v2.projects.locations.conversationModels.evaluations
  * REST Resource: v2.projects.locations.conversationProfiles
  * REST Resource: v2.projects.locations.conversations
  * REST Resource: v2.projects.locations.conversations.messages
  * REST Resource: v2.projects.locations.conversations.participants
  * REST Resource: v2.projects.locations.conversations.participants.suggestions
  * REST Resource: v2.projects.locations.conversations.suggestions
  * REST Resource: v2.projects.locations.encryptionSpec
  * REST Resource: v2.projects.locations.generators
  * REST Resource: v2.projects.locations.generators.evaluations
  * REST Resource: v2.projects.locations.knowledgeBases
  * REST Resource: v2.projects.locations.knowledgeBases.documents
  * REST Resource: v2.projects.locations.operations
  * REST Resource: v2.projects.locations.sipTrunks
  * REST Resource: v2.projects.locations.statelessSuggestion
  * REST Resource: v2.projects.locations.suggestions
  * REST Resource: v2.projects.locations.tools
  * REST Resource: v2.projects.operations
  * REST Resource: v2.projects.suggestions



## Service: dialogflow.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

  * <https://dialogflow.googleapis.com/$discovery/rest?version=v2>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoints and all URIs below are relative to these service endpoints:

  * `https://dialogflow.googleapis.com`
  * `https://asia-northeast1-dialogflow.googleapis.com`
  * `https://australia-southeast1-dialogflow.googleapis.com`
  * `https://europe-west1-dialogflow.googleapis.com`
  * `https://europe-west2-dialogflow.googleapis.com`



## REST Resource: [v2.projects](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects)

Methods  
---  
`[deleteAgent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects/deleteAgent)` |  `DELETE /v2/{parent=projects/*}/agent`   
Deletes the specified agent.  
`[getAgent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects/getAgent)` |  `GET /v2/{parent=projects/*}/agent`   
Retrieves the specified agent.  
`[setAgent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects/setAgent)` |  `POST /v2/{agent.parent=projects/*}/agent`   
Creates/updates the specified agent.  
  
## REST Resource: [v2.projects.agent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent)

Methods  
---  
`[export](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent/export)` |  `POST /v2/{parent=projects/*}/agent:export`   
Exports the specified agent to a ZIP file.  
`[getFulfillment](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent/getFulfillment)` |  `GET /v2/{name=projects/*/agent/fulfillment}`   
Retrieves the fulfillment.  
`[getValidationResult](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent/getValidationResult)` |  `GET /v2/{parent=projects/*}/agent/validationResult`   
Gets agent validation result.  
`[import](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent/import)` |  `POST /v2/{parent=projects/*}/agent:import`   
Imports the specified agent from a ZIP file.  
`[restore](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent/restore)` |  `POST /v2/{parent=projects/*}/agent:restore`   
Restores the specified agent from a ZIP file.  
`[search](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent/search)` |  `GET /v2/{parent=projects/*}/agent:search`   
Returns the list of agents.  
`[train](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent/train)` |  `POST /v2/{parent=projects/*}/agent:train`   
Trains the specified agent.  
`[updateFulfillment](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent/updateFulfillment)` |  `PATCH /v2/{fulfillment.name=projects/*/agent/fulfillment}`   
Updates the fulfillment.  
  
## REST Resource: [v2.projects.agent.entityTypes](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.entityTypes)

Methods  
---  
`[batchDelete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.entityTypes/batchDelete)` |  `POST /v2/{parent=projects/*/agent}/entityTypes:batchDelete`   
Deletes entity types in the specified agent.  
`[batchUpdate](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.entityTypes/batchUpdate)` |  `POST /v2/{parent=projects/*/agent}/entityTypes:batchUpdate`   
Updates/Creates multiple entity types in the specified agent.  
`[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.entityTypes/create)` |  `POST /v2/{parent=projects/*/agent}/entityTypes`   
Creates an entity type in the specified agent.  
`[delete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.entityTypes/delete)` |  `DELETE /v2/{name=projects/*/agent/entityTypes/*}`   
Deletes the specified entity type.  
`[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.entityTypes/get)` |  `GET /v2/{name=projects/*/agent/entityTypes/*}`   
Retrieves the specified entity type.  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.entityTypes/list)` |  `GET /v2/{parent=projects/*/agent}/entityTypes`   
Returns the list of all entity types in the specified agent.  
`[patch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.entityTypes/patch)` |  `PATCH /v2/{entityType.name=projects/*/agent/entityTypes/*}`   
Updates the specified entity type.  
  
## REST Resource: [v2.projects.agent.entityTypes.entities](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.entityTypes.entities)

Methods  
---  
`[batchCreate](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.entityTypes.entities/batchCreate)` |  `POST /v2/{parent=projects/*/agent/entityTypes/*}/entities:batchCreate`   
Creates multiple new entities in the specified entity type.  
`[batchDelete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.entityTypes.entities/batchDelete)` |  `POST /v2/{parent=projects/*/agent/entityTypes/*}/entities:batchDelete`   
Deletes entities in the specified entity type.  
`[batchUpdate](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.entityTypes.entities/batchUpdate)` |  `POST /v2/{parent=projects/*/agent/entityTypes/*}/entities:batchUpdate`   
Updates or creates multiple entities in the specified entity type.  
  
## REST Resource: [v2.projects.agent.environments](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments/create)` |  `POST /v2/{parent=projects/*/agent}/environments`   
Creates an agent environment.  
`[delete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments/delete)` |  `DELETE /v2/{name=projects/*/agent/environments/*}`   
Deletes the specified agent environment.  
`[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments/get)` |  `GET /v2/{name=projects/*/agent/environments/*}`   
Retrieves the specified agent environment.  
`[getHistory](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments/getHistory)` |  `GET /v2/{parent=projects/*/agent/environments/*}/history`   
Gets the history of the specified environment.  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments/list)` |  `GET /v2/{parent=projects/*/agent}/environments`   
Returns the list of all non-default environments of the specified agent.  
`[patch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments/patch)` |  `PATCH /v2/{environment.name=projects/*/agent/environments/*}`   
Updates the specified agent environment.  
  
## REST Resource: [v2.projects.agent.environments.intents](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments.intents)

Methods  
---  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments.intents/list)` |  `GET /v2/{parent=projects/*/agent/environments/*}/intents`   
Returns the list of all intents in the specified agent.  
  
## REST Resource: [v2.projects.agent.environments.users.sessions](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments.users.sessions)

Methods  
---  
`[deleteContexts](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments.users.sessions/deleteContexts)` |  `DELETE /v2/{parent=projects/*/agent/environments/*/users/*/sessions/*}/contexts`   
Deletes all active contexts in the specified session.  
`[detectIntent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments.users.sessions/detectIntent)` |  `POST /v2/{session=projects/*/agent/environments/*/users/*/sessions/*}:detectIntent`   
Processes a natural language query and returns structured, actionable data as a result.  
  
## REST Resource: [v2.projects.agent.environments.users.sessions.contexts](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments.users.sessions.contexts)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments.users.sessions.contexts/create)` |  `POST /v2/{parent=projects/*/agent/environments/*/users/*/sessions/*}/contexts`   
Creates a context.  
`[delete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments.users.sessions.contexts/delete)` |  `DELETE /v2/{name=projects/*/agent/environments/*/users/*/sessions/*/contexts/*}`   
Deletes the specified context.  
`[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments.users.sessions.contexts/get)` |  `GET /v2/{name=projects/*/agent/environments/*/users/*/sessions/*/contexts/*}`   
Retrieves the specified context.  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments.users.sessions.contexts/list)` |  `GET /v2/{parent=projects/*/agent/environments/*/users/*/sessions/*}/contexts`   
Returns the list of all contexts in the specified session.  
`[patch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments.users.sessions.contexts/patch)` |  `PATCH /v2/{context.name=projects/*/agent/environments/*/users/*/sessions/*/contexts/*}`   
Updates the specified context.  
  
## REST Resource: [v2.projects.agent.environments.users.sessions.entityTypes](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments.users.sessions.entityTypes)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments.users.sessions.entityTypes/create)` |  `POST /v2/{parent=projects/*/agent/environments/*/users/*/sessions/*}/entityTypes`   
Creates a session entity type.  
`[delete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments.users.sessions.entityTypes/delete)` |  `DELETE /v2/{name=projects/*/agent/environments/*/users/*/sessions/*/entityTypes/*}`   
Deletes the specified session entity type.  
`[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments.users.sessions.entityTypes/get)` |  `GET /v2/{name=projects/*/agent/environments/*/users/*/sessions/*/entityTypes/*}`   
Retrieves the specified session entity type.  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments.users.sessions.entityTypes/list)` |  `GET /v2/{parent=projects/*/agent/environments/*/users/*/sessions/*}/entityTypes`   
Returns the list of all session entity types in the specified session.  
`[patch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments.users.sessions.entityTypes/patch)` |  `PATCH /v2/{sessionEntityType.name=projects/*/agent/environments/*/users/*/sessions/*/entityTypes/*}`   
Updates the specified session entity type.  
  
## REST Resource: [v2.projects.agent.intents](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents)

Methods  
---  
`[batchDelete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents/batchDelete)` |  `POST /v2/{parent=projects/*/agent}/intents:batchDelete`   
Deletes intents in the specified agent.  
`[batchUpdate](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents/batchUpdate)` |  `POST /v2/{parent=projects/*/agent}/intents:batchUpdate`   
Updates/Creates multiple intents in the specified agent.  
`[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents/create)` |  `POST /v2/{parent=projects/*/agent}/intents`   
Creates an intent in the specified agent.  
`[delete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents/delete)` |  `DELETE /v2/{name=projects/*/agent/intents/*}`   
Deletes the specified intent and its direct or indirect followup intents.  
`[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents/get)` |  `GET /v2/{name=projects/*/agent/intents/*}`   
Retrieves the specified intent.  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents/list)` |  `GET /v2/{parent=projects/*/agent}/intents`   
Returns the list of all intents in the specified agent.  
`[patch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents/patch)` |  `PATCH /v2/{intent.name=projects/*/agent/intents/*}`   
Updates the specified intent.  
  
## REST Resource: [v2.projects.agent.knowledgeBases](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.knowledgeBases)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.knowledgeBases/create)` |  `POST /v2/{parent=projects/*/agent}/knowledgeBases`   
Creates a knowledge base.  
`[delete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.knowledgeBases/delete)` |  `DELETE /v2/{name=projects/*/agent/knowledgeBases/*}`   
Deletes the specified knowledge base.  
`[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.knowledgeBases/get)` |  `GET /v2/{name=projects/*/agent/knowledgeBases/*}`   
Retrieves the specified knowledge base.  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.knowledgeBases/list)` |  `GET /v2/{parent=projects/*/agent}/knowledgeBases`   
Returns the list of all knowledge bases of the specified agent.  
`[patch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.knowledgeBases/patch)` |  `PATCH /v2/{knowledgeBase.name=projects/*/agent/knowledgeBases/*}`   
Updates the specified knowledge base.  
  
## REST Resource: [v2.projects.agent.knowledgeBases.documents](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.knowledgeBases.documents)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.knowledgeBases.documents/create)` |  `POST /v2/{parent=projects/*/agent/knowledgeBases/*}/documents`   
Creates a new document.  
`[delete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.knowledgeBases.documents/delete)` |  `DELETE /v2/{name=projects/*/agent/knowledgeBases/*/documents/*}`   
Deletes the specified document.  
`[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.knowledgeBases.documents/get)` |  `GET /v2/{name=projects/*/agent/knowledgeBases/*/documents/*}`   
Retrieves the specified document.  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.knowledgeBases.documents/list)` |  `GET /v2/{parent=projects/*/agent/knowledgeBases/*}/documents`   
Returns the list of all documents of the knowledge base.  
`[patch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.knowledgeBases.documents/patch)` |  `PATCH /v2/{document.name=projects/*/agent/knowledgeBases/*/documents/*}`   
Updates the specified document.  
`[reload](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.knowledgeBases.documents/reload)` |  `POST /v2/{name=projects/*/agent/knowledgeBases/*/documents/*}:reload`   
Reloads the specified document from its specified source, content_uri or content.  
  
## REST Resource: [v2.projects.agent.sessions](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.sessions)

Methods  
---  
`[deleteContexts](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.sessions/deleteContexts)` |  `DELETE /v2/{parent=projects/*/agent/sessions/*}/contexts`   
Deletes all active contexts in the specified session.  
`[detectIntent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.sessions/detectIntent)` |  `POST /v2/{session=projects/*/agent/sessions/*}:detectIntent`   
Processes a natural language query and returns structured, actionable data as a result.  
  
## REST Resource: [v2.projects.agent.sessions.contexts](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.sessions.contexts)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.sessions.contexts/create)` |  `POST /v2/{parent=projects/*/agent/sessions/*}/contexts`   
Creates a context.  
`[delete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.sessions.contexts/delete)` |  `DELETE /v2/{name=projects/*/agent/sessions/*/contexts/*}`   
Deletes the specified context.  
`[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.sessions.contexts/get)` |  `GET /v2/{name=projects/*/agent/sessions/*/contexts/*}`   
Retrieves the specified context.  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.sessions.contexts/list)` |  `GET /v2/{parent=projects/*/agent/sessions/*}/contexts`   
Returns the list of all contexts in the specified session.  
`[patch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.sessions.contexts/patch)` |  `PATCH /v2/{context.name=projects/*/agent/sessions/*/contexts/*}`   
Updates the specified context.  
  
## REST Resource: [v2.projects.agent.sessions.entityTypes](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.sessions.entityTypes)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.sessions.entityTypes/create)` |  `POST /v2/{parent=projects/*/agent/sessions/*}/entityTypes`   
Creates a session entity type.  
`[delete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.sessions.entityTypes/delete)` |  `DELETE /v2/{name=projects/*/agent/sessions/*/entityTypes/*}`   
Deletes the specified session entity type.  
`[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.sessions.entityTypes/get)` |  `GET /v2/{name=projects/*/agent/sessions/*/entityTypes/*}`   
Retrieves the specified session entity type.  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.sessions.entityTypes/list)` |  `GET /v2/{parent=projects/*/agent/sessions/*}/entityTypes`   
Returns the list of all session entity types in the specified session.  
`[patch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.sessions.entityTypes/patch)` |  `PATCH /v2/{sessionEntityType.name=projects/*/agent/sessions/*/entityTypes/*}`   
Updates the specified session entity type.  
  
## REST Resource: [v2.projects.agent.versions](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.versions)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.versions/create)` |  `POST /v2/{parent=projects/*/agent}/versions`   
Creates an agent version.  
`[delete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.versions/delete)` |  `DELETE /v2/{name=projects/*/agent/versions/*}`   
Delete the specified agent version.  
`[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.versions/get)` |  `GET /v2/{name=projects/*/agent/versions/*}`   
Retrieves the specified agent version.  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.versions/list)` |  `GET /v2/{parent=projects/*/agent}/versions`   
Returns the list of all versions of the specified agent.  
`[patch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.versions/patch)` |  `PATCH /v2/{version.name=projects/*/agent/versions/*}`   
Updates the specified agent version.  
  
## REST Resource: [v2.projects.answerRecords](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.answerRecords)

Methods  
---  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.answerRecords/list)` |  `GET /v2/{parent=projects/*}/answerRecords`   
Returns the list of all answer records in the specified project in reverse chronological order.  
`[patch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.answerRecords/patch)` |  `PATCH /v2/{answerRecord.name=projects/*/answerRecords/*}`   
Updates the specified answer record.  
  
## REST Resource: [v2.projects.conversationDatasets](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationDatasets)

Methods  
---  
`[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationDatasets/get)` |  `GET /v2/{name=projects/*/conversationDatasets/*}`   
Retrieves the specified conversation dataset.  
`[importConversationData](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationDatasets/importConversationData)` |  `POST /v2/{name=projects/*/conversationDatasets/*}:importConversationData`   
Import data into the specified conversation dataset.  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationDatasets/list)` |  `GET /v2/{parent=projects/*}/conversationDatasets`   
Returns the list of all conversation datasets in the specified project and location.  
  
## REST Resource: [v2.projects.conversationModels](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationModels)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationModels/create)` |  `POST /v2/{parent=projects/*}/conversationModels`   
Creates a model.  
`[delete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationModels/delete)` |  `DELETE /v2/{name=projects/*/conversationModels/*}`   
Deletes a model.  
`[deploy](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationModels/deploy)` |  `POST /v2/{name=projects/*/conversationModels/*}:deploy`   
Deploys a model.  
`[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationModels/get)` |  `GET /v2/{name=projects/*/conversationModels/*}`   
Gets conversation model.  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationModels/list)` |  `GET /v2/{parent=projects/*}/conversationModels`   
Lists conversation models.  
`[undeploy](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationModels/undeploy)` |  `POST /v2/{name=projects/*/conversationModels/*}:undeploy`   
Undeploys a model.  
  
## REST Resource: [v2.projects.conversationModels.evaluations](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationModels.evaluations)

Methods  
---  
`[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationModels.evaluations/get)` |  `GET /v2/{name=projects/*/conversationModels/*/evaluations/*}`   
Gets an evaluation of conversation model.  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationModels.evaluations/list)` |  `GET /v2/{parent=projects/*/conversationModels/*}/evaluations`   
Lists evaluations of a conversation model.  
  
## REST Resource: [v2.projects.conversationProfiles](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles)

Methods  
---  
`[clearSuggestionFeatureConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles/clearSuggestionFeatureConfig)` |  `POST /v2/{conversationProfile=projects/*/conversationProfiles/*}:clearSuggestionFeatureConfig`   
Clears a suggestion feature from a conversation profile for the given participant role.  
`[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles/create)` |  `POST /v2/{parent=projects/*}/conversationProfiles`   
Creates a conversation profile in the specified project.  
`[delete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles/delete)` |  `DELETE /v2/{name=projects/*/conversationProfiles/*}`   
Deletes the specified conversation profile.  
`[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles/get)` |  `GET /v2/{name=projects/*/conversationProfiles/*}`   
Retrieves the specified conversation profile.  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles/list)` |  `GET /v2/{parent=projects/*}/conversationProfiles`   
Returns the list of all conversation profiles in the specified project.  
`[patch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles/patch)` |  `PATCH /v2/{conversationProfile.name=projects/*/conversationProfiles/*}`   
Updates the specified conversation profile.  
`[setSuggestionFeatureConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles/setSuggestionFeatureConfig)` |  `POST /v2/{conversationProfile=projects/*/conversationProfiles/*}:setSuggestionFeatureConfig`   
Adds or updates a suggestion feature in a conversation profile.  
  
## REST Resource: [v2.projects.conversations](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations)

Methods  
---  
`[complete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations/complete)` |  `POST /v2/{name=projects/*/conversations/*}:complete`   
Completes the specified conversation.  
`[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations/create)` |  `POST /v2/{parent=projects/*}/conversations`   
Creates a new conversation.  
`[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations/get)` |  `GET /v2/{name=projects/*/conversations/*}`   
Retrieves the specific conversation.  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations/list)` |  `GET /v2/{parent=projects/*}/conversations`   
Returns the list of all conversations in the specified project.  
  
## REST Resource: [v2.projects.conversations.messages](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.messages)

Methods  
---  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.messages/list)` |  `GET /v2/{parent=projects/*/conversations/*}/messages`   
Lists messages that belong to a given conversation.  
  
## REST Resource: [v2.projects.conversations.participants](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants)

Methods  
---  
`[analyzeContent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants/analyzeContent)` |  `POST /v2/{participant=projects/*/conversations/*/participants/*}:analyzeContent`   
Adds a text (chat, for example), or audio (phone recording, for example) message from a participant into the conversation.  
`[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants/create)` |  `POST /v2/{parent=projects/*/conversations/*}/participants`   
Creates a new participant in a conversation.  
`[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants/get)` |  `GET /v2/{name=projects/*/conversations/*/participants/*}`   
Retrieves a conversation participant.  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants/list)` |  `GET /v2/{parent=projects/*/conversations/*}/participants`   
Returns the list of all participants in the specified conversation.  
`[patch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants/patch)` |  `PATCH /v2/{participant.name=projects/*/conversations/*/participants/*}`   
Updates the specified participant.  
  
## REST Resource: [v2.projects.conversations.participants.suggestions](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants.suggestions)

Methods  
---  
`[suggestArticles](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants.suggestions/suggestArticles)` |  `POST /v2/{parent=projects/*/conversations/*/participants/*}/suggestions:suggestArticles`   
Gets suggested articles for a participant based on specific historical messages.  
`[suggestFaqAnswers](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants.suggestions/suggestFaqAnswers)` |  `POST /v2/{parent=projects/*/conversations/*/participants/*}/suggestions:suggestFaqAnswers`   
Gets suggested faq answers for a participant based on specific historical messages.  
`[suggestKnowledgeAssist](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants.suggestions/suggestKnowledgeAssist)` |  `POST /v2/{parent=projects/*/conversations/*/participants/*}/suggestions:suggestKnowledgeAssist`   
Gets knowledge assist suggestions based on historical messages.  
`[suggestSmartReplies](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants.suggestions/suggestSmartReplies)` |  `POST /v2/{parent=projects/*/conversations/*/participants/*}/suggestions:suggestSmartReplies`   
Gets smart replies for a participant based on specific historical messages.  
  
## REST Resource: [v2.projects.conversations.suggestions](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.suggestions)

Methods  
---  
`[generate](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.suggestions/generate)` |  `POST /v2/{conversation=projects/*/conversations/*}/suggestions:generate`   
Generates all the suggestions using generators configured in the conversation profile.  
`[searchKnowledge](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.suggestions/searchKnowledge)` |  `POST /v2/{conversation=projects/*/conversations/*}/suggestions:searchKnowledge`   
Get answers for the given query based on knowledge documents.  
`[suggestConversationSummary](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.suggestions/suggestConversationSummary)` |  `POST /v2/{conversation=projects/*/conversations/*}/suggestions:suggestConversationSummary`   
Suggests summary for a conversation based on specific historical messages.  
  
## REST Resource: [v2.projects.generators](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators/create)` |  `POST /v2/{parent=projects/*}/generators`   
Creates a generator.  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators/list)` |  `GET /v2/{parent=projects/*}/generators`   
Lists generators.  
  
## REST Resource: [v2.projects.knowledgeBases](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.knowledgeBases)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.knowledgeBases/create)` |  `POST /v2/{parent=projects/*}/knowledgeBases`   
Creates a knowledge base.  
`[delete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.knowledgeBases/delete)` |  `DELETE /v2/{name=projects/*/knowledgeBases/*}`   
Deletes the specified knowledge base.  
`[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.knowledgeBases/get)` |  `GET /v2/{name=projects/*/knowledgeBases/*}`   
Retrieves the specified knowledge base.  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.knowledgeBases/list)` |  `GET /v2/{parent=projects/*}/knowledgeBases`   
Returns the list of all knowledge bases of the specified agent.  
`[patch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.knowledgeBases/patch)` |  `PATCH /v2/{knowledgeBase.name=projects/*/knowledgeBases/*}`   
Updates the specified knowledge base.  
  
## REST Resource: [v2.projects.knowledgeBases.documents](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.knowledgeBases.documents)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.knowledgeBases.documents/create)` |  `POST /v2/{parent=projects/*/knowledgeBases/*}/documents`   
Creates a new document.  
`[delete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.knowledgeBases.documents/delete)` |  `DELETE /v2/{name=projects/*/knowledgeBases/*/documents/*}`   
Deletes the specified document.  
`[export](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.knowledgeBases.documents/export)` |  `POST /v2/{name=projects/*/knowledgeBases/*/documents/*}:export`   
Exports a smart messaging candidate document into the specified destination.  
`[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.knowledgeBases.documents/get)` |  `GET /v2/{name=projects/*/knowledgeBases/*/documents/*}`   
Retrieves the specified document.  
`[import](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.knowledgeBases.documents/import)` |  `POST /v2/{parent=projects/*/knowledgeBases/*}/documents:import`   
Creates documents by importing data from external sources.  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.knowledgeBases.documents/list)` |  `GET /v2/{parent=projects/*/knowledgeBases/*}/documents`   
Returns the list of all documents of the knowledge base.  
`[patch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.knowledgeBases.documents/patch)` |  `PATCH /v2/{document.name=projects/*/knowledgeBases/*/documents/*}`   
Updates the specified document.  
`[reload](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.knowledgeBases.documents/reload)` |  `POST /v2/{name=projects/*/knowledgeBases/*/documents/*}:reload`   
Reloads the specified document from its specified source, content_uri or content.  
  
## REST Resource: [v2.projects.locations](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations)

Methods  
---  
`[deleteAgent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations/deleteAgent)` |  `DELETE /v2/{parent=projects/*/locations/*}/agent`   
Deletes the specified agent.  
`[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations/get)` |  `GET /v2/{name=projects/*/locations/*}`   
Gets information about a location.  
`[getAgent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations/getAgent)` |  `GET /v2/{parent=projects/*/locations/*}/agent`   
Retrieves the specified agent.  
`[getEncryptionSpec](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations/getEncryptionSpec)` |  `GET /v2/{name=projects/*/locations/*/encryptionSpec}`   
Gets location-level encryption key specification.  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations/list)` |  `GET /v2/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
`[setAgent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations/setAgent)` |  `POST /v2/{agent.parent=projects/*/locations/*}/agent`   
Creates/updates the specified agent.  
  
## REST Resource: [v2.projects.locations.agent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent)

Methods  
---  
`[export](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent/export)` |  `POST /v2/{parent=projects/*/locations/*}/agent:export`   
Exports the specified agent to a ZIP file.  
`[getFulfillment](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent/getFulfillment)` |  `GET /v2/{name=projects/*/locations/*/agent/fulfillment}`   
Retrieves the fulfillment.  
`[getValidationResult](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent/getValidationResult)` |  `GET /v2/{parent=projects/*/locations/*}/agent/validationResult`   
Gets agent validation result.  
`[import](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent/import)` |  `POST /v2/{parent=projects/*/locations/*}/agent:import`   
Imports the specified agent from a ZIP file.  
`[restore](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent/restore)` |  `POST /v2/{parent=projects/*/locations/*}/agent:restore`   
Restores the specified agent from a ZIP file.  
`[search](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent/search)` |  `GET /v2/{parent=projects/*/locations/*}/agent:search`   
Returns the list of agents.  
`[train](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent/train)` |  `POST /v2/{parent=projects/*/locations/*}/agent:train`   
Trains the specified agent.  
`[updateFulfillment](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent/updateFulfillment)` |  `PATCH /v2/{fulfillment.name=projects/*/locations/*/agent/fulfillment}`   
Updates the fulfillment.  
  
## REST Resource: [v2.projects.locations.agent.entityTypes](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.entityTypes)

Methods  
---  
`[batchDelete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.entityTypes/batchDelete)` |  `POST /v2/{parent=projects/*/locations/*/agent}/entityTypes:batchDelete`   
Deletes entity types in the specified agent.  
`[batchUpdate](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.entityTypes/batchUpdate)` |  `POST /v2/{parent=projects/*/locations/*/agent}/entityTypes:batchUpdate`   
Updates/Creates multiple entity types in the specified agent.  
`[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.entityTypes/create)` |  `POST /v2/{parent=projects/*/locations/*/agent}/entityTypes`   
Creates an entity type in the specified agent.  
`[delete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.entityTypes/delete)` |  `DELETE /v2/{name=projects/*/locations/*/agent/entityTypes/*}`   
Deletes the specified entity type.  
`[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.entityTypes/get)` |  `GET /v2/{name=projects/*/locations/*/agent/entityTypes/*}`   
Retrieves the specified entity type.  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.entityTypes/list)` |  `GET /v2/{parent=projects/*/locations/*/agent}/entityTypes`   
Returns the list of all entity types in the specified agent.  
`[patch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.entityTypes/patch)` |  `PATCH /v2/{entityType.name=projects/*/locations/*/agent/entityTypes/*}`   
Updates the specified entity type.  
  
## REST Resource: [v2.projects.locations.agent.entityTypes.entities](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.entityTypes.entities)

Methods  
---  
`[batchCreate](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.entityTypes.entities/batchCreate)` |  `POST /v2/{parent=projects/*/locations/*/agent/entityTypes/*}/entities:batchCreate`   
Creates multiple new entities in the specified entity type.  
`[batchDelete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.entityTypes.entities/batchDelete)` |  `POST /v2/{parent=projects/*/locations/*/agent/entityTypes/*}/entities:batchDelete`   
Deletes entities in the specified entity type.  
`[batchUpdate](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.entityTypes.entities/batchUpdate)` |  `POST /v2/{parent=projects/*/locations/*/agent/entityTypes/*}/entities:batchUpdate`   
Updates or creates multiple entities in the specified entity type.  
  
## REST Resource: [v2.projects.locations.agent.environments](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.environments)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.environments/create)` |  `POST /v2/{parent=projects/*/locations/*/agent}/environments`   
Creates an agent environment.  
`[delete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.environments/delete)` |  `DELETE /v2/{name=projects/*/locations/*/agent/environments/*}`   
Deletes the specified agent environment.  
`[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.environments/get)` |  `GET /v2/{name=projects/*/locations/*/agent/environments/*}`   
Retrieves the specified agent environment.  
`[getHistory](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.environments/getHistory)` |  `GET /v2/{parent=projects/*/locations/*/agent/environments/*}/history`   
Gets the history of the specified environment.  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.environments/list)` |  `GET /v2/{parent=projects/*/locations/*/agent}/environments`   
Returns the list of all non-default environments of the specified agent.  
`[patch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.environments/patch)` |  `PATCH /v2/{environment.name=projects/*/locations/*/agent/environments/*}`   
Updates the specified agent environment.  
  
## REST Resource: [v2.projects.locations.agent.environments.intents](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.environments.intents)

Methods  
---  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.environments.intents/list)` |  `GET /v2/{parent=projects/*/locations/*/agent/environments/*}/intents`   
Returns the list of all intents in the specified agent.  
  
## REST Resource: [v2.projects.locations.agent.environments.users.sessions](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.environments.users.sessions)

Methods  
---  
`[deleteContexts](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.environments.users.sessions/deleteContexts)` |  `DELETE /v2/{parent=projects/*/locations/*/agent/environments/*/users/*/sessions/*}/contexts`   
Deletes all active contexts in the specified session.  
`[detectIntent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.environments.users.sessions/detectIntent)` |  `POST /v2/{session=projects/*/locations/*/agent/environments/*/users/*/sessions/*}:detectIntent`   
Processes a natural language query and returns structured, actionable data as a result.  
  
## REST Resource: [v2.projects.locations.agent.environments.users.sessions.contexts](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.environments.users.sessions.contexts)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.environments.users.sessions.contexts/create)` |  `POST /v2/{parent=projects/*/locations/*/agent/environments/*/users/*/sessions/*}/contexts`   
Creates a context.  
`[delete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.environments.users.sessions.contexts/delete)` |  `DELETE /v2/{name=projects/*/locations/*/agent/environments/*/users/*/sessions/*/contexts/*}`   
Deletes the specified context.  
`[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.environments.users.sessions.contexts/get)` |  `GET /v2/{name=projects/*/locations/*/agent/environments/*/users/*/sessions/*/contexts/*}`   
Retrieves the specified context.  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.environments.users.sessions.contexts/list)` |  `GET /v2/{parent=projects/*/locations/*/agent/environments/*/users/*/sessions/*}/contexts`   
Returns the list of all contexts in the specified session.  
`[patch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.environments.users.sessions.contexts/patch)` |  `PATCH /v2/{context.name=projects/*/locations/*/agent/environments/*/users/*/sessions/*/contexts/*}`   
Updates the specified context.  
  
## REST Resource: [v2.projects.locations.agent.environments.users.sessions.entityTypes](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.environments.users.sessions.entityTypes)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.environments.users.sessions.entityTypes/create)` |  `POST /v2/{parent=projects/*/locations/*/agent/environments/*/users/*/sessions/*}/entityTypes`   
Creates a session entity type.  
`[delete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.environments.users.sessions.entityTypes/delete)` |  `DELETE /v2/{name=projects/*/locations/*/agent/environments/*/users/*/sessions/*/entityTypes/*}`   
Deletes the specified session entity type.  
`[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.environments.users.sessions.entityTypes/get)` |  `GET /v2/{name=projects/*/locations/*/agent/environments/*/users/*/sessions/*/entityTypes/*}`   
Retrieves the specified session entity type.  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.environments.users.sessions.entityTypes/list)` |  `GET /v2/{parent=projects/*/locations/*/agent/environments/*/users/*/sessions/*}/entityTypes`   
Returns the list of all session entity types in the specified session.  
`[patch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.environments.users.sessions.entityTypes/patch)` |  `PATCH /v2/{sessionEntityType.name=projects/*/locations/*/agent/environments/*/users/*/sessions/*/entityTypes/*}`   
Updates the specified session entity type.  
  
## REST Resource: [v2.projects.locations.agent.intents](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.intents)

Methods  
---  
`[batchDelete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.intents/batchDelete)` |  `POST /v2/{parent=projects/*/locations/*/agent}/intents:batchDelete`   
Deletes intents in the specified agent.  
`[batchUpdate](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.intents/batchUpdate)` |  `POST /v2/{parent=projects/*/locations/*/agent}/intents:batchUpdate`   
Updates/Creates multiple intents in the specified agent.  
`[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.intents/create)` |  `POST /v2/{parent=projects/*/locations/*/agent}/intents`   
Creates an intent in the specified agent.  
`[delete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.intents/delete)` |  `DELETE /v2/{name=projects/*/locations/*/agent/intents/*}`   
Deletes the specified intent and its direct or indirect followup intents.  
`[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.intents/get)` |  `GET /v2/{name=projects/*/locations/*/agent/intents/*}`   
Retrieves the specified intent.  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.intents/list)` |  `GET /v2/{parent=projects/*/locations/*/agent}/intents`   
Returns the list of all intents in the specified agent.  
`[patch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.intents/patch)` |  `PATCH /v2/{intent.name=projects/*/locations/*/agent/intents/*}`   
Updates the specified intent.  
  
## REST Resource: [v2.projects.locations.agent.sessions](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.sessions)

Methods  
---  
`[deleteContexts](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.sessions/deleteContexts)` |  `DELETE /v2/{parent=projects/*/locations/*/agent/sessions/*}/contexts`   
Deletes all active contexts in the specified session.  
`[detectIntent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.sessions/detectIntent)` |  `POST /v2/{session=projects/*/locations/*/agent/sessions/*}:detectIntent`   
Processes a natural language query and returns structured, actionable data as a result.  
  
## REST Resource: [v2.projects.locations.agent.sessions.contexts](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.sessions.contexts)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.sessions.contexts/create)` |  `POST /v2/{parent=projects/*/locations/*/agent/sessions/*}/contexts`   
Creates a context.  
`[delete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.sessions.contexts/delete)` |  `DELETE /v2/{name=projects/*/locations/*/agent/sessions/*/contexts/*}`   
Deletes the specified context.  
`[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.sessions.contexts/get)` |  `GET /v2/{name=projects/*/locations/*/agent/sessions/*/contexts/*}`   
Retrieves the specified context.  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.sessions.contexts/list)` |  `GET /v2/{parent=projects/*/locations/*/agent/sessions/*}/contexts`   
Returns the list of all contexts in the specified session.  
`[patch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.sessions.contexts/patch)` |  `PATCH /v2/{context.name=projects/*/locations/*/agent/sessions/*/contexts/*}`   
Updates the specified context.  
  
## REST Resource: [v2.projects.locations.agent.sessions.entityTypes](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.sessions.entityTypes)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.sessions.entityTypes/create)` |  `POST /v2/{parent=projects/*/locations/*/agent/sessions/*}/entityTypes`   
Creates a session entity type.  
`[delete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.sessions.entityTypes/delete)` |  `DELETE /v2/{name=projects/*/locations/*/agent/sessions/*/entityTypes/*}`   
Deletes the specified session entity type.  
`[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.sessions.entityTypes/get)` |  `GET /v2/{name=projects/*/locations/*/agent/sessions/*/entityTypes/*}`   
Retrieves the specified session entity type.  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.sessions.entityTypes/list)` |  `GET /v2/{parent=projects/*/locations/*/agent/sessions/*}/entityTypes`   
Returns the list of all session entity types in the specified session.  
`[patch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.sessions.entityTypes/patch)` |  `PATCH /v2/{sessionEntityType.name=projects/*/locations/*/agent/sessions/*/entityTypes/*}`   
Updates the specified session entity type.  
  
## REST Resource: [v2.projects.locations.agent.versions](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.versions)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.versions/create)` |  `POST /v2/{parent=projects/*/locations/*/agent}/versions`   
Creates an agent version.  
`[delete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.versions/delete)` |  `DELETE /v2/{name=projects/*/locations/*/agent/versions/*}`   
Delete the specified agent version.  
`[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.versions/get)` |  `GET /v2/{name=projects/*/locations/*/agent/versions/*}`   
Retrieves the specified agent version.  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.versions/list)` |  `GET /v2/{parent=projects/*/locations/*/agent}/versions`   
Returns the list of all versions of the specified agent.  
`[patch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.versions/patch)` |  `PATCH /v2/{version.name=projects/*/locations/*/agent/versions/*}`   
Updates the specified agent version.  
  
## REST Resource: [v2.projects.locations.answerRecords](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.answerRecords)

Methods  
---  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.answerRecords/list)` |  `GET /v2/{parent=projects/*/locations/*}/answerRecords`   
Returns the list of all answer records in the specified project in reverse chronological order.  
`[patch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.answerRecords/patch)` |  `PATCH /v2/{answerRecord.name=projects/*/locations/*/answerRecords/*}`   
Updates the specified answer record.  
  
## REST Resource: [v2.projects.locations.companionAgents](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.companionAgents)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.companionAgents/create)` |  `POST /v2/{parent=projects/*/locations/*}/companionAgents`   
Creates a companion agent.  
`[delete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.companionAgents/delete)` |  `DELETE /v2/{name=projects/*/locations/*/companionAgents/*}`   
Deletes a companion agent.  
`[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.companionAgents/get)` |  `GET /v2/{name=projects/*/locations/*/companionAgents/*}`   
Gets a companion agent.  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.companionAgents/list)` |  `GET /v2/{parent=projects/*/locations/*}/companionAgents`   
Lists companion agents.  
`[patch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.companionAgents/patch)` |  `PATCH /v2/{companionAgent.name=projects/*/locations/*/companionAgents/*}`   
Updates a companion agent.  
  
## REST Resource: [v2.projects.locations.conversationDatasets](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversationDatasets)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversationDatasets/create)` |  `POST /v2/{parent=projects/*/locations/*}/conversationDatasets`   
Creates a new conversation dataset.  
`[delete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversationDatasets/delete)` |  `DELETE /v2/{name=projects/*/locations/*/conversationDatasets/*}`   
Deletes the specified conversation dataset.  
`[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversationDatasets/get)` |  `GET /v2/{name=projects/*/locations/*/conversationDatasets/*}`   
Retrieves the specified conversation dataset.  
`[importConversationData](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversationDatasets/importConversationData)` |  `POST /v2/{name=projects/*/locations/*/conversationDatasets/*}:importConversationData`   
Import data into the specified conversation dataset.  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversationDatasets/list)` |  `GET /v2/{parent=projects/*/locations/*}/conversationDatasets`   
Returns the list of all conversation datasets in the specified project and location.  
  
## REST Resource: [v2.projects.locations.conversationModels](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversationModels)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversationModels/create)` |  `POST /v2/{parent=projects/*/locations/*}/conversationModels`   
Creates a model.  
`[delete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversationModels/delete)` |  `DELETE /v2/{name=projects/*/locations/*/conversationModels/*}`   
Deletes a model.  
`[deploy](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversationModels/deploy)` |  `POST /v2/{name=projects/*/locations/*/conversationModels/*}:deploy`   
Deploys a model.  
`[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversationModels/get)` |  `GET /v2/{name=projects/*/locations/*/conversationModels/*}`   
Gets conversation model.  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversationModels/list)` |  `GET /v2/{parent=projects/*/locations/*}/conversationModels`   
Lists conversation models.  
`[undeploy](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversationModels/undeploy)` |  `POST /v2/{name=projects/*/locations/*/conversationModels/*}:undeploy`   
Undeploys a model.  
  
## REST Resource: [v2.projects.locations.conversationModels.evaluations](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversationModels.evaluations)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversationModels.evaluations/create)` |  `POST /v2/{parent=projects/*/locations/*/conversationModels/*}/evaluations`   
Creates evaluation of a conversation model.  
`[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversationModels.evaluations/get)` |  `GET /v2/{name=projects/*/locations/*/conversationModels/*/evaluations/*}`   
Gets an evaluation of conversation model.  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversationModels.evaluations/list)` |  `GET /v2/{parent=projects/*/locations/*/conversationModels/*}/evaluations`   
Lists evaluations of a conversation model.  
  
## REST Resource: [v2.projects.locations.conversationProfiles](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversationProfiles)

Methods  
---  
`[clearSuggestionFeatureConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversationProfiles/clearSuggestionFeatureConfig)` |  `POST /v2/{conversationProfile=projects/*/locations/*/conversationProfiles/*}:clearSuggestionFeatureConfig`   
Clears a suggestion feature from a conversation profile for the given participant role.  
`[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversationProfiles/create)` |  `POST /v2/{parent=projects/*/locations/*}/conversationProfiles`   
Creates a conversation profile in the specified project.  
`[delete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversationProfiles/delete)` |  `DELETE /v2/{name=projects/*/locations/*/conversationProfiles/*}`   
Deletes the specified conversation profile.  
`[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversationProfiles/get)` |  `GET /v2/{name=projects/*/locations/*/conversationProfiles/*}`   
Retrieves the specified conversation profile.  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversationProfiles/list)` |  `GET /v2/{parent=projects/*/locations/*}/conversationProfiles`   
Returns the list of all conversation profiles in the specified project.  
`[patch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversationProfiles/patch)` |  `PATCH /v2/{conversationProfile.name=projects/*/locations/*/conversationProfiles/*}`   
Updates the specified conversation profile.  
`[setSuggestionFeatureConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversationProfiles/setSuggestionFeatureConfig)` |  `POST /v2/{conversationProfile=projects/*/locations/*/conversationProfiles/*}:setSuggestionFeatureConfig`   
Adds or updates a suggestion feature in a conversation profile.  
  
## REST Resource: [v2.projects.locations.conversations](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversations)

Methods  
---  
`[complete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversations/complete)` |  `POST /v2/{name=projects/*/locations/*/conversations/*}:complete`   
Completes the specified conversation.  
`[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversations/create)` |  `POST /v2/{parent=projects/*/locations/*}/conversations`   
Creates a new conversation.  
`[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversations/get)` |  `GET /v2/{name=projects/*/locations/*/conversations/*}`   
Retrieves the specific conversation.  
`[ingestContextReferences](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversations/ingestContextReferences)` |  `POST /v2/{conversation=projects/*/locations/*/conversations/*}:ingestContextReferences`   
Data ingestion API.  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversations/list)` |  `GET /v2/{parent=projects/*/locations/*}/conversations`   
Returns the list of all conversations in the specified project.  
  
## REST Resource: [v2.projects.locations.conversations.messages](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversations.messages)

Methods  
---  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversations.messages/list)` |  `GET /v2/{parent=projects/*/locations/*/conversations/*}/messages`   
Lists messages that belong to a given conversation.  
  
## REST Resource: [v2.projects.locations.conversations.participants](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversations.participants)

Methods  
---  
`[analyzeContent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversations.participants/analyzeContent)` |  `POST /v2/{participant=projects/*/locations/*/conversations/*/participants/*}:analyzeContent`   
Adds a text (chat, for example), or audio (phone recording, for example) message from a participant into the conversation.  
`[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversations.participants/create)` |  `POST /v2/{parent=projects/*/locations/*/conversations/*}/participants`   
Creates a new participant in a conversation.  
`[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversations.participants/get)` |  `GET /v2/{name=projects/*/locations/*/conversations/*/participants/*}`   
Retrieves a conversation participant.  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversations.participants/list)` |  `GET /v2/{parent=projects/*/locations/*/conversations/*}/participants`   
Returns the list of all participants in the specified conversation.  
`[patch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversations.participants/patch)` |  `PATCH /v2/{participant.name=projects/*/locations/*/conversations/*/participants/*}`   
Updates the specified participant.  
  
## REST Resource: [v2.projects.locations.conversations.participants.suggestions](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversations.participants.suggestions)

Methods  
---  
`[suggestArticles](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversations.participants.suggestions/suggestArticles)` |  `POST /v2/{parent=projects/*/locations/*/conversations/*/participants/*}/suggestions:suggestArticles`   
Gets suggested articles for a participant based on specific historical messages.  
`[suggestFaqAnswers](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversations.participants.suggestions/suggestFaqAnswers)` |  `POST /v2/{parent=projects/*/locations/*/conversations/*/participants/*}/suggestions:suggestFaqAnswers`   
Gets suggested faq answers for a participant based on specific historical messages.  
`[suggestKnowledgeAssist](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversations.participants.suggestions/suggestKnowledgeAssist)` |  `POST /v2/{parent=projects/*/locations/*/conversations/*/participants/*}/suggestions:suggestKnowledgeAssist`   
Gets knowledge assist suggestions based on historical messages.  
`[suggestSmartReplies](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversations.participants.suggestions/suggestSmartReplies)` |  `POST /v2/{parent=projects/*/locations/*/conversations/*/participants/*}/suggestions:suggestSmartReplies`   
Gets smart replies for a participant based on specific historical messages.  
  
## REST Resource: [v2.projects.locations.conversations.suggestions](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversations.suggestions)

Methods  
---  
`[generate](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversations.suggestions/generate)` |  `POST /v2/{conversation=projects/*/locations/*/conversations/*}/suggestions:generate`   
Generates all the suggestions using generators configured in the conversation profile.  
`[searchKnowledge](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversations.suggestions/searchKnowledge)` |  `POST /v2/{conversation=projects/*/locations/*/conversations/*}/suggestions:searchKnowledge`   
Get answers for the given query based on knowledge documents.  
`[suggestConversationSummary](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversations.suggestions/suggestConversationSummary)` |  `POST /v2/{conversation=projects/*/locations/*/conversations/*}/suggestions:suggestConversationSummary`   
Suggests summary for a conversation based on specific historical messages.  
  
## REST Resource: [v2.projects.locations.encryptionSpec](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.encryptionSpec)

Methods  
---  
`[initialize](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.encryptionSpec/initialize)` |  `POST /v2/{encryptionSpec.name=projects/*/locations/*/encryptionSpec}:initialize`   
Initializes a location-level encryption key specification.  
  
## REST Resource: [v2.projects.locations.generators](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.generators)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.generators/create)` |  `POST /v2/{parent=projects/*/locations/*}/generators`   
Creates a generator.  
`[delete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.generators/delete)` |  `DELETE /v2/{name=projects/*/locations/*/generators/*}`   
Deletes a generator.  
`[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.generators/get)` |  `GET /v2/{name=projects/*/locations/*/generators/*}`   
Retrieves a generator.  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.generators/list)` |  `GET /v2/{parent=projects/*/locations/*}/generators`   
Lists generators.  
`[patch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.generators/patch)` |  `PATCH /v2/{generator.name=projects/*/locations/*/generators/*}`   
Updates a generator.  
  
## REST Resource: [v2.projects.locations.generators.evaluations](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.generators.evaluations)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.generators.evaluations/create)` |  `POST /v2/{parent=projects/*/locations/*/generators/*}/evaluations`   
Creates evaluation of a generator.  
`[delete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.generators.evaluations/delete)` |  `DELETE /v2/{name=projects/*/locations/*/generators/*/evaluations/*}`   
Deletes an evaluation of generator.  
`[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.generators.evaluations/get)` |  `GET /v2/{name=projects/*/locations/*/generators/*/evaluations/*}`   
Gets an evaluation of generator.  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.generators.evaluations/list)` |  `GET /v2/{parent=projects/*/locations/*/generators/*}/evaluations`   
Lists evaluations of generator.  
  
## REST Resource: [v2.projects.locations.knowledgeBases](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.knowledgeBases)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.knowledgeBases/create)` |  `POST /v2/{parent=projects/*/locations/*}/knowledgeBases`   
Creates a knowledge base.  
`[delete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.knowledgeBases/delete)` |  `DELETE /v2/{name=projects/*/locations/*/knowledgeBases/*}`   
Deletes the specified knowledge base.  
`[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.knowledgeBases/get)` |  `GET /v2/{name=projects/*/locations/*/knowledgeBases/*}`   
Retrieves the specified knowledge base.  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.knowledgeBases/list)` |  `GET /v2/{parent=projects/*/locations/*}/knowledgeBases`   
Returns the list of all knowledge bases of the specified agent.  
`[patch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.knowledgeBases/patch)` |  `PATCH /v2/{knowledgeBase.name=projects/*/locations/*/knowledgeBases/*}`   
Updates the specified knowledge base.  
  
## REST Resource: [v2.projects.locations.knowledgeBases.documents](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.knowledgeBases.documents)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.knowledgeBases.documents/create)` |  `POST /v2/{parent=projects/*/locations/*/knowledgeBases/*}/documents`   
Creates a new document.  
`[delete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.knowledgeBases.documents/delete)` |  `DELETE /v2/{name=projects/*/locations/*/knowledgeBases/*/documents/*}`   
Deletes the specified document.  
`[export](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.knowledgeBases.documents/export)` |  `POST /v2/{name=projects/*/locations/*/knowledgeBases/*/documents/*}:export`   
Exports a smart messaging candidate document into the specified destination.  
`[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.knowledgeBases.documents/get)` |  `GET /v2/{name=projects/*/locations/*/knowledgeBases/*/documents/*}`   
Retrieves the specified document.  
`[import](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.knowledgeBases.documents/import)` |  `POST /v2/{parent=projects/*/locations/*/knowledgeBases/*}/documents:import`   
Creates documents by importing data from external sources.  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.knowledgeBases.documents/list)` |  `GET /v2/{parent=projects/*/locations/*/knowledgeBases/*}/documents`   
Returns the list of all documents of the knowledge base.  
`[patch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.knowledgeBases.documents/patch)` |  `PATCH /v2/{document.name=projects/*/locations/*/knowledgeBases/*/documents/*}`   
Updates the specified document.  
`[reload](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.knowledgeBases.documents/reload)` |  `POST /v2/{name=projects/*/locations/*/knowledgeBases/*/documents/*}:reload`   
Reloads the specified document from its specified source, content_uri or content.  
  
## REST Resource: [v2.projects.locations.operations](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.operations/cancel)` |  `POST /v2/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.operations/get)` |  `GET /v2/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.operations/list)` |  `GET /v2/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v2.projects.locations.sipTrunks](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.sipTrunks)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.sipTrunks/create)` |  `POST /v2/{parent=projects/*/locations/*}/sipTrunks`   
Creates a SipTrunk for a specified location.  
`[delete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.sipTrunks/delete)` |  `DELETE /v2/{name=projects/*/locations/*/sipTrunks/*}`   
Deletes a specified SipTrunk.  
`[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.sipTrunks/get)` |  `GET /v2/{name=projects/*/locations/*/sipTrunks/*}`   
Retrieves the specified SipTrunk.  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.sipTrunks/list)` |  `GET /v2/{parent=projects/*/locations/*}/sipTrunks`   
Returns a list of SipTrunks in the specified location.  
`[patch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.sipTrunks/patch)` |  `PATCH /v2/{sipTrunk.name=projects/*/locations/*/sipTrunks/*}`   
Updates the specified SipTrunk.  
  
## REST Resource: [v2.projects.locations.statelessSuggestion](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.statelessSuggestion)

Methods  
---  
`[generate](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.statelessSuggestion/generate)` |  `POST /v2/{parent=projects/*/locations/*}/statelessSuggestion:generate`   
Generates and returns a suggestion for a conversation that does not have a resource created for it.  
  
## REST Resource: [v2.projects.locations.suggestions](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.suggestions)

Methods  
---  
`[generateStatelessSummary](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.suggestions/generateStatelessSummary)` |  `POST /v2/{statelessConversation.parent=projects/*/locations/*}/suggestions:generateStatelessSummary`   
Generates and returns a summary for a conversation that does not have a resource created for it.  
`[searchKnowledge](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.suggestions/searchKnowledge)` |  `POST /v2/{parent=projects/*/locations/*}/suggestions:searchKnowledge`   
Get answers for the given query based on knowledge documents.  
  
## REST Resource: [v2.projects.locations.tools](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.tools)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.tools/create)` |  `POST /v2/{parent=projects/*/locations/*}/tools`   
Creates a tool.  
`[delete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.tools/delete)` |  `DELETE /v2/{name=projects/*/locations/*/tools/*}`   
Deletes a tool.  
`[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.tools/get)` |  `GET /v2/{name=projects/*/locations/*/tools/*}`   
Retrieves a tool.  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.tools/list)` |  `GET /v2/{parent=projects/*/locations/*}/tools`   
Lists tools.  
`[patch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.tools/patch)` |  `PATCH /v2/{tool.name=projects/*/locations/*/tools/*}`   
Updates a tool.  
  
## REST Resource: [v2.projects.operations](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.operations/cancel)` |  `POST /v2/{name=projects/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.operations/get)` |  `GET /v2/{name=projects/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.operations/list)` |  `GET /v2/{name=projects/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v2.projects.suggestions](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.suggestions)

Methods  
---  
`[generateStatelessSummary](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.suggestions/generateStatelessSummary)` |  `POST /v2/{statelessConversation.parent=projects/*}/suggestions:generateStatelessSummary`   
Generates and returns a summary for a conversation that does not have a resource created for it.  
`[searchKnowledge](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.suggestions/searchKnowledge)` |  `POST /v2/{parent=projects/*}/suggestions:searchKnowledge`   
Get answers for the given query based on knowledge documents.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
