---
url: https://docs.cloud.google.com/gemini/data-agents/reference/rest/
title: Data Analytics API with Gemini \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:51:54.605566+00:00
---

# Data Analytics API with Gemini  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Reference ](https://docs.cloud.google.com/gemini/data-agents/reference/rest)



Send feedback 

#  Data Analytics API with Gemini Stay organized with collections  Save and categorize content based on your preferences. 

The Data Analytics API with Gemini (`geminidataanalytics.googleapis.com`) provides methods to query and analyze data by using natural language, and to create and manage the data agents that interact with your data in supported data sources. Developers should select the appropriate endpoint path based on their stability requirements.

  * **v1:** Recommended for generally available features that can be integrated into production environments.
  * **v1beta:** Recommended for integrating new features into production environments during their Preview period.
  * **v1alpha:** Intended for testing new and upcoming features. These features are subject to change or removal, potentially requiring updates to your code.



Learn more about [Google Cloud product launch stages](https://cloud.google.com/products#product-launch-stages).

For detailed implementation guides, see the [Conversational Analytics API overview](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview).

  * REST Resource: v1beta.a2a.projects.locations.dataAgents.v1
  * REST Resource: v1beta.a2a.projects.locations.dataAgents.v1.message
  * REST Resource: v1beta.projects.locations
  * REST Resource: v1beta.projects.locations.conversations
  * REST Resource: v1beta.projects.locations.conversations.messages
  * REST Resource: v1beta.projects.locations.dataAgents
  * REST Resource: v1beta.projects.locations.operations
  * REST Resource: v1alpha.projects.locations
  * REST Resource: v1alpha.projects.locations.conversations
  * REST Resource: v1alpha.projects.locations.conversations.messages
  * REST Resource: v1alpha.projects.locations.dataAgents
  * REST Resource: v1alpha.projects.locations.operations
  * REST Resource: v1.a2a.projects.locations.agents.v1
  * REST Resource: v1.a2a.projects.locations.agents.v1.message
  * REST Resource: v1.a2a.projects.locations.dataAgents.v1
  * REST Resource: v1.a2a.projects.locations.dataAgents.v1.message
  * REST Resource: v1.projects.locations
  * REST Resource: v1.projects.locations.conversations
  * REST Resource: v1.projects.locations.conversations.messages
  * REST Resource: v1.projects.locations.dataAgents
  * REST Resource: v1.projects.locations.operations



## Service: geminidataanalytics.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery documents:

  * <https://geminidataanalytics.googleapis.com/$discovery/rest?version=v1>
  * <https://geminidataanalytics.googleapis.com/$discovery/rest?version=v1beta>
  * <https://geminidataanalytics.googleapis.com/$discovery/rest?version=v1alpha>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://geminidataanalytics.googleapis.com`



## REST Resource: [v1beta.a2a.projects.locations.dataAgents.v1](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/a2a.projects.locations.dataAgents.v1)

Methods  
---  
`[getCard](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/a2a.projects.locations.dataAgents.v1/getCard)` |  `GET /v1beta/a2a/{tenant=projects/*/locations/*/dataAgents/*}/v1/card`   
GetAgentCard returns the agent card for the agent.  
  
## REST Resource: [v1beta.a2a.projects.locations.dataAgents.v1.message](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/a2a.projects.locations.dataAgents.v1.message)

Methods  
---  
`[send](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/a2a.projects.locations.dataAgents.v1.message/send)` |  `POST /v1beta/a2a/{tenant=projects/*/locations/*/dataAgents/*}/v1/message:send`   
Send a message to the agent.  
`[stream](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/a2a.projects.locations.dataAgents.v1.message/stream)` |  `POST /v1beta/a2a/{tenant=projects/*/locations/*/dataAgents/*}/v1/message:stream`   
SendStreamingMessage is a streaming call that will return a stream of task update events until the Task is in an interrupted or terminal state.  
  
## REST Resource: [v1beta.projects.locations](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations)

Methods  
---  
`[chat](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations/chat)` |  `POST /v1beta/{parent=projects/*/locations/*}:chat`   
Answers a data question by generating a stream of `[Message](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/Message)` objects.  
`[get](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations/get)` |  `GET /v1beta/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations/list)` |  `GET /v1beta/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
`[queryData](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations/queryData)` |  `POST /v1beta/{parent=projects/*/locations/*}:queryData`   
Queries data from a natural language user query.  
  
## REST Resource: [v1beta.projects.locations.conversations](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.conversations)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.conversations/create)` |  `POST /v1beta/{parent=projects/*/locations/*}/conversations`   
Creates a new conversation to persist the conversation history.  
`[delete](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.conversations/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/conversations/*}`   
Deletes a conversation.  
`[get](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.conversations/get)` |  `GET /v1beta/{name=projects/*/locations/*/conversations/*}`   
Gets details of a single conversation by using conversation id and parent.  
`[list](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.conversations/list)` |  `GET /v1beta/{parent=projects/*/locations/*}/conversations`   
Lists all conversations for a given parent.  
  
## REST Resource: [v1beta.projects.locations.conversations.messages](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.conversations.messages)

Methods  
---  
`[list](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.conversations.messages/list)` |  `GET /v1beta/{parent=projects/*/locations/*/conversations/*}/messages`   
Lists all messages for a given conversation.  
  
## REST Resource: [v1beta.projects.locations.dataAgents](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents/create)` |  `POST /v1beta/{parent=projects/*/locations/*}/dataAgents`   
Creates a new DataAgent in a given project and location.  
`[createSync](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents/createSync)` |  `POST /v1beta/{parent=projects/*/locations/*}/dataAgents:createSync`   
Creates a new DataAgent in a given project and location synchronously.  
`[delete](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/dataAgents/*}`   
Deletes a single DataAgent.  
`[deleteSync](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents/deleteSync)` |  `DELETE /v1beta/{name=projects/*/locations/*/dataAgents/*}:deleteSync`   
Deletes a single DataAgent synchronously.  
`[get](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents/get)` |  `GET /v1beta/{name=projects/*/locations/*/dataAgents/*}`   
Gets details of a single DataAgent.  
`[getIamPolicy](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents/getIamPolicy)` |  `POST /v1beta/{resource=projects/*/locations/*/dataAgents/*}:getIamPolicy`   
Gets the IAM policy for DataAgent  
`[list](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents/list)` |  `GET /v1beta/{parent=projects/*/locations/*}/dataAgents`   
Lists DataAgents in a given project and location.  
`[listAccessible](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents/listAccessible)` |  `GET /v1beta/{parent=projects/*/locations/*}/dataAgents:listAccessible`   
Lists DataAgents that are accessible to the caller in a given project and location.  
`[patch](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents/patch)` |  `PATCH /v1beta/{dataAgent.name=projects/*/locations/*/dataAgents/*}`   
Updates the parameters of a single DataAgent.  
`[setIamPolicy](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents/setIamPolicy)` |  `POST /v1beta/{resource=projects/*/locations/*/dataAgents/*}:setIamPolicy`   
Sets the IAM policy for a DataAgent.  
`[updateSync](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents/updateSync)` |  `PATCH /v1beta/{dataAgent.name=projects/*/locations/*/dataAgents/*}:updateSync`   
Updates the parameters of a single DataAgent synchronously.  
  
## REST Resource: [v1beta.projects.locations.operations](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.operations/cancel)` |  `POST /v1beta/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.operations/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.operations/get)` |  `GET /v1beta/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.operations/list)` |  `GET /v1beta/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1alpha.projects.locations](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations)

Methods  
---  
`[chat](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations/chat)` |  `POST /v1alpha/{parent=projects/*/locations/*}:chat`   
Answers a data question by generating a stream of `[Message](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/Message)` objects.  
`[get](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations/get)` |  `GET /v1alpha/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations/list)` |  `GET /v1alpha/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
`[queryData](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations/queryData)` |  `POST /v1alpha/{parent=projects/*/locations/*}:queryData`   
Queries data from a natural language user query.  
  
## REST Resource: [v1alpha.projects.locations.conversations](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.conversations)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.conversations/create)` |  `POST /v1alpha/{parent=projects/*/locations/*}/conversations`   
Creates a new conversation to persist the conversation history.  
`[delete](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.conversations/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/conversations/*}`   
Deletes a conversation.  
`[get](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.conversations/get)` |  `GET /v1alpha/{name=projects/*/locations/*/conversations/*}`   
Gets details of a single conversation by using conversation id and parent.  
`[list](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.conversations/list)` |  `GET /v1alpha/{parent=projects/*/locations/*}/conversations`   
Lists all conversations for a given parent.  
  
## REST Resource: [v1alpha.projects.locations.conversations.messages](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.conversations.messages)

Methods  
---  
`[list](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.conversations.messages/list)` |  `GET /v1alpha/{parent=projects/*/locations/*/conversations/*}/messages`   
Lists all messages for a given conversation.  
  
## REST Resource: [v1alpha.projects.locations.dataAgents](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents/create)` |  `POST /v1alpha/{parent=projects/*/locations/*}/dataAgents`   
Creates a new DataAgent in a given project and location.  
`[createSync](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents/createSync)` |  `POST /v1alpha/{parent=projects/*/locations/*}/dataAgents:createSync`   
Creates a new DataAgent in a given project and location synchronously.  
`[delete](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/dataAgents/*}`   
Deletes a single DataAgent.  
`[deleteSync](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents/deleteSync)` |  `DELETE /v1alpha/{name=projects/*/locations/*/dataAgents/*}:deleteSync`   
Deletes a single DataAgent synchronously.  
`[get](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents/get)` |  `GET /v1alpha/{name=projects/*/locations/*/dataAgents/*}`   
Gets details of a single DataAgent.  
`[getIamPolicy](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents/getIamPolicy)` |  `POST /v1alpha/{resource=projects/*/locations/*/dataAgents/*}:getIamPolicy`   
Gets the IAM policy for DataAgent  
`[list](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents/list)` |  `GET /v1alpha/{parent=projects/*/locations/*}/dataAgents`   
Lists DataAgents in a given project and location.  
`[listAccessible](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents/listAccessible)` |  `GET /v1alpha/{parent=projects/*/locations/*}/dataAgents:listAccessible`   
Lists DataAgents that are accessible to the caller in a given project and location.  
`[patch](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents/patch)` |  `PATCH /v1alpha/{dataAgent.name=projects/*/locations/*/dataAgents/*}`   
Updates the parameters of a single DataAgent.  
`[setIamPolicy](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents/setIamPolicy)` |  `POST /v1alpha/{resource=projects/*/locations/*/dataAgents/*}:setIamPolicy`   
Sets the IAM policy for a DataAgent.  
`[updateSync](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents/updateSync)` |  `PATCH /v1alpha/{dataAgent.name=projects/*/locations/*/dataAgents/*}:updateSync`   
Updates the parameters of a single DataAgent synchronously.  
  
## REST Resource: [v1alpha.projects.locations.operations](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.operations/cancel)` |  `POST /v1alpha/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.operations/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.operations/get)` |  `GET /v1alpha/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.operations/list)` |  `GET /v1alpha/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1.a2a.projects.locations.agents.v1](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/a2a.projects.locations.agents.v1)

Methods  
---  
`[getCard](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/a2a.projects.locations.agents.v1/getCard)` |  `GET /v1/a2a/{tenant=projects/*/locations/*/agents/*}/v1/card`   
GetAgentCard returns the agent card for the agent.  
  
## REST Resource: [v1.a2a.projects.locations.agents.v1.message](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/a2a.projects.locations.agents.v1.message)

Methods  
---  
`[send](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/a2a.projects.locations.agents.v1.message/send)` |  `POST /v1/a2a/{tenant=projects/*/locations/*/agents/*}/v1/message:send`   
Send a message to the agent.  
`[stream](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/a2a.projects.locations.agents.v1.message/stream)` |  `POST /v1/a2a/{tenant=projects/*/locations/*/agents/*}/v1/message:stream`   
SendStreamingMessage is a streaming call that will return a stream of task update events until the Task is in an interrupted or terminal state.  
  
## REST Resource: [v1.a2a.projects.locations.dataAgents.v1](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/a2a.projects.locations.dataAgents.v1)

Methods  
---  
`[getCard](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/a2a.projects.locations.dataAgents.v1/getCard)` |  `GET /v1/a2a/{tenant=projects/*/locations/*/dataAgents/*}/v1/card`   
GetAgentCard returns the agent card for the agent.  
  
## REST Resource: [v1.a2a.projects.locations.dataAgents.v1.message](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/a2a.projects.locations.dataAgents.v1.message)

Methods  
---  
`[send](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/a2a.projects.locations.dataAgents.v1.message/send)` |  `POST /v1/a2a/{tenant=projects/*/locations/*/dataAgents/*}/v1/message:send`   
Send a message to the agent.  
`[stream](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/a2a.projects.locations.dataAgents.v1.message/stream)` |  `POST /v1/a2a/{tenant=projects/*/locations/*/dataAgents/*}/v1/message:stream`   
SendStreamingMessage is a streaming call that will return a stream of task update events until the Task is in an interrupted or terminal state.  
  
## REST Resource: [v1.projects.locations](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations)

Methods  
---  
`[chat](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/chat)` |  `POST /v1/{parent=projects/*/locations/*}:chat`   
Answers a data question by generating a stream of `[Message](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message)` objects.  
`[get](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/get)` |  `GET /v1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/list)` |  `GET /v1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1.projects.locations.conversations](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.conversations)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.conversations/create)` |  `POST /v1/{parent=projects/*/locations/*}/conversations`   
Creates a new conversation to persist the conversation history.  
`[delete](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.conversations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/conversations/*}`   
Deletes a conversation.  
`[get](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.conversations/get)` |  `GET /v1/{name=projects/*/locations/*/conversations/*}`   
Gets details of a single conversation by using conversation id and parent.  
`[list](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.conversations/list)` |  `GET /v1/{parent=projects/*/locations/*}/conversations`   
Lists all conversations for a given parent.  
  
## REST Resource: [v1.projects.locations.conversations.messages](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.conversations.messages)

Methods  
---  
`[list](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.conversations.messages/list)` |  `GET /v1/{parent=projects/*/locations/*/conversations/*}/messages`   
Lists all messages for a given conversation.  
  
## REST Resource: [v1.projects.locations.dataAgents](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents/create)` |  `POST /v1/{parent=projects/*/locations/*}/dataAgents`   
Creates a new DataAgent in a given project and location.  
`[createSync](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents/createSync)` |  `POST /v1/{parent=projects/*/locations/*}/dataAgents:createSync`   
Creates a new DataAgent in a given project and location synchronously.  
`[delete](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents/delete)` |  `DELETE /v1/{name=projects/*/locations/*/dataAgents/*}`   
Deletes a single DataAgent.  
`[deleteSync](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents/deleteSync)` |  `DELETE /v1/{name=projects/*/locations/*/dataAgents/*}:deleteSync`   
Deletes a single DataAgent synchronously.  
`[get](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents/get)` |  `GET /v1/{name=projects/*/locations/*/dataAgents/*}`   
Gets details of a single DataAgent.  
`[getIamPolicy](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents/getIamPolicy)` |  `POST /v1/{resource=projects/*/locations/*/dataAgents/*}:getIamPolicy`   
Gets the IAM policy for DataAgent  
`[list](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents/list)` |  `GET /v1/{parent=projects/*/locations/*}/dataAgents`   
Lists DataAgents in a given project and location.  
`[listAccessible](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents/listAccessible)` |  `GET /v1/{parent=projects/*/locations/*}/dataAgents:listAccessible`   
Lists DataAgents that are accessible to the caller in a given project and location.  
`[patch](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents/patch)` |  `PATCH /v1/{dataAgent.name=projects/*/locations/*/dataAgents/*}`   
Updates the parameters of a single DataAgent.  
`[setIamPolicy](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents/setIamPolicy)` |  `POST /v1/{resource=projects/*/locations/*/dataAgents/*}:setIamPolicy`   
Sets the IAM policy for a DataAgent.  
`[updateSync](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents/updateSync)` |  `PATCH /v1/{dataAgent.name=projects/*/locations/*/dataAgents/*}:updateSync`   
Updates the parameters of a single DataAgent synchronously.  
  
## REST Resource: [v1.projects.locations.operations](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.operations/cancel)` |  `POST /v1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.operations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.operations/get)` |  `GET /v1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.operations/list)` |  `GET /v1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
