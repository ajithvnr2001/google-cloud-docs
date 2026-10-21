---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1-overview/
title: Gemini Enterprise for Customer Experience API \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:22:27.751408+00:00
---

# Gemini Enterprise for Customer Experience API  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Gemini Enterprise for Customer Experience API Stay organized with collections  Save and categorize content based on your preferences. 

  * REST Resource: tasks
  * REST Resource: tasks.pushNotificationConfigs
  * REST Resource: v1.projects.locations
  * REST Resource: v1.projects.locations.apps
  * REST Resource: v1.projects.locations.apps.agents
  * REST Resource: v1.projects.locations.apps.changelogs
  * REST Resource: v1.projects.locations.apps.conversations
  * REST Resource: v1.projects.locations.apps.deployments
  * REST Resource: v1.projects.locations.apps.deployments.message
  * REST Resource: v1.projects.locations.apps.examples
  * REST Resource: v1.projects.locations.apps.guardrails
  * REST Resource: v1.projects.locations.apps.message
  * REST Resource: v1.projects.locations.apps.sessions
  * REST Resource: v1.projects.locations.apps.tools
  * REST Resource: v1.projects.locations.apps.toolsets
  * REST Resource: v1.projects.locations.apps.versions
  * REST Resource: v1.projects.locations.apps.versions.message
  * REST Resource: v1.projects.locations.operations



## Service: ces.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

  * <https://ces.googleapis.com/$discovery/rest?version=v1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://ces.googleapis.com`



## REST Resource: [tasks](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/tasks)

Methods  
---  
`[cancel](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/tasks/cancel)` |  `POST /tasks/{id}:cancel`   
Cancels a task in progress.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/tasks/get)` |  `GET /tasks/{id}`   
Gets the latest state of a task.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/tasks/list)` |  `GET /tasks`   
Lists tasks that match the specified filter.  
`[subscribe](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/tasks/subscribe)` |  `GET /tasks/{id}:subscribe`   
Subscribes to task updates for tasks not in a terminal state.  
  
## REST Resource: [tasks.pushNotificationConfigs](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/tasks.pushNotificationConfigs)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/tasks.pushNotificationConfigs/create)` |  `POST /tasks/{taskId}/pushNotificationConfigs`   
Creates a push notification config for a task.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/tasks.pushNotificationConfigs/delete)` |  `DELETE /tasks/{taskId}/pushNotificationConfigs/{id}`   
Deletes a push notification config for a task.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/tasks.pushNotificationConfigs/get)` |  `GET /tasks/{taskId}/pushNotificationConfigs/{id}`   
Gets a push notification config for a task.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/tasks.pushNotificationConfigs/list)` |  `GET /tasks/{taskId}/pushNotificationConfigs`   
Get a list of push notifications configured for a task.  
  
## REST Resource: [v1.projects.locations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations/get)` |  `GET /v1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations/list)` |  `GET /v1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1.projects.locations.apps](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps/create)` |  `POST /v1/{parent=projects/*/locations/*}/apps`   
Creates a new app in the given project and location.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps/delete)` |  `DELETE /v1/{name=projects/*/locations/*/apps/*}`   
Deletes the specified app.  
`[executeTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps/executeTool)` |  `POST /v1/{parent=projects/*/locations/*/apps/*}:executeTool`   
Executes the given tool with the given arguments.  
`[exportApp](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps/exportApp)` |  `POST /v1/{name=projects/*/locations/*/apps/*}:exportApp`   
Exports the specified app.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps/get)` |  `GET /v1/{name=projects/*/locations/*/apps/*}`   
Gets details of the specified app.  
`[getExtendedAgentCard](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps/getExtendedAgentCard)` |  `GET /v1/{tenant=projects/*/locations/*/apps/*}/extendedAgentCard`   
Gets the extended agent card for the authenticated agent.  
`[importApp](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps/importApp)` |  `POST /v1/{parent=projects/*/locations/*}/apps:importApp`   
Imports the specified app.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps/list)` |  `GET /v1/{parent=projects/*/locations/*}/apps`   
Lists apps in the given project and location.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps/patch)` |  `PATCH /v1/{app.name=projects/*/locations/*/apps/*}`   
Updates the specified app.  
`[retrieveToolSchema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps/retrieveToolSchema)` |  `POST /v1/{parent=projects/*/locations/*/apps/*}:retrieveToolSchema`   
Retrieve the schema of the given tool.  
  
## REST Resource: [v1.projects.locations.apps.agents](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.agents)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.agents/create)` |  `POST /v1/{parent=projects/*/locations/*/apps/*}/agents`   
Creates a new agent in the given app.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.agents/delete)` |  `DELETE /v1/{name=projects/*/locations/*/apps/*/agents/*}`   
Deletes the specified agent.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.agents/get)` |  `GET /v1/{name=projects/*/locations/*/apps/*/agents/*}`   
Gets details of the specified agent.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.agents/list)` |  `GET /v1/{parent=projects/*/locations/*/apps/*}/agents`   
Lists agents in the given app.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.agents/patch)` |  `PATCH /v1/{agent.name=projects/*/locations/*/apps/*/agents/*}`   
Updates the specified agent.  
  
## REST Resource: [v1.projects.locations.apps.changelogs](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.changelogs)

Methods  
---  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.changelogs/get)` |  `GET /v1/{name=projects/*/locations/*/apps/*/changelogs/*}`   
Gets the specified changelog.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.changelogs/list)` |  `GET /v1/{parent=projects/*/locations/*/apps/*}/changelogs`   
Lists the changelogs of the specified app.  
  
## REST Resource: [v1.projects.locations.apps.conversations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.conversations)

Methods  
---  
`[batchDelete](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.conversations/batchDelete)` |  `POST /v1/{parent=projects/*/locations/*/apps/*}/conversations:batchDelete`   
Batch deletes the specified conversations.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.conversations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/apps/*/conversations/*}`   
Deletes the specified conversation.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.conversations/get)` |  `GET /v1/{name=projects/*/locations/*/apps/*/conversations/*}`   
Gets details of the specified conversation.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.conversations/list)` |  `GET /v1/{parent=projects/*/locations/*/apps/*}/conversations`   
Lists conversations in the given app.  
  
## REST Resource: [v1.projects.locations.apps.deployments](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.deployments)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.deployments/create)` |  `POST /v1/{parent=projects/*/locations/*/apps/*}/deployments`   
Creates a new deployment in the given app.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.deployments/delete)` |  `DELETE /v1/{name=projects/*/locations/*/apps/*/deployments/*}`   
Deletes the specified deployment.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.deployments/get)` |  `GET /v1/{name=projects/*/locations/*/apps/*/deployments/*}`   
Gets details of the specified deployment.  
`[getExtendedAgentCard](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.deployments/getExtendedAgentCard)` |  `GET /v1/{tenant=projects/*/locations/*/apps/*/deployments/*}/extendedAgentCard`   
Gets the extended agent card for the authenticated agent.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.deployments/list)` |  `GET /v1/{parent=projects/*/locations/*/apps/*}/deployments`   
Lists deployments in the given app.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.deployments/patch)` |  `PATCH /v1/{deployment.name=projects/*/locations/*/apps/*/deployments/*}`   
Updates the specified deployment.  
  
## REST Resource: [v1.projects.locations.apps.deployments.message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.deployments.message)

Methods  
---  
`[send](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.deployments.message/send)` |  `POST /v1/{tenant=projects/*/locations/*/apps/*/deployments/*}/message:send`   
Sends a message to an agent.  
`[stream](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.deployments.message/stream)` |  `POST /v1/{tenant=projects/*/locations/*/apps/*/deployments/*}/message:stream`   
Sends a streaming message to an agent, allowing for real-time interaction and status updates.  
  
## REST Resource: [v1.projects.locations.apps.examples](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.examples)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.examples/create)` |  `POST /v1/{parent=projects/*/locations/*/apps/*}/examples`   
Creates a new example in the given app.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.examples/delete)` |  `DELETE /v1/{name=projects/*/locations/*/apps/*/examples/*}`   
Deletes the specified example.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.examples/get)` |  `GET /v1/{name=projects/*/locations/*/apps/*/examples/*}`   
Gets details of the specified example.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.examples/list)` |  `GET /v1/{parent=projects/*/locations/*/apps/*}/examples`   
Lists examples in the given app.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.examples/patch)` |  `PATCH /v1/{example.name=projects/*/locations/*/apps/*/examples/*}`   
Updates the specified example.  
  
## REST Resource: [v1.projects.locations.apps.guardrails](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails/create)` |  `POST /v1/{parent=projects/*/locations/*/apps/*}/guardrails`   
Creates a new guardrail in the given app.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails/delete)` |  `DELETE /v1/{name=projects/*/locations/*/apps/*/guardrails/*}`   
Deletes the specified guardrail.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails/get)` |  `GET /v1/{name=projects/*/locations/*/apps/*/guardrails/*}`   
Gets details of the specified guardrail.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails/list)` |  `GET /v1/{parent=projects/*/locations/*/apps/*}/guardrails`   
Lists guardrails in the given app.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails/patch)` |  `PATCH /v1/{guardrail.name=projects/*/locations/*/apps/*/guardrails/*}`   
Updates the specified guardrail.  
  
## REST Resource: [v1.projects.locations.apps.message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.message)

Methods  
---  
`[send](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.message/send)` |  `POST /v1/{tenant=projects/*/locations/*/apps/*}/message:send`   
Sends a message to an agent.  
`[stream](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.message/stream)` |  `POST /v1/{tenant=projects/*/locations/*/apps/*}/message:stream`   
Sends a streaming message to an agent, allowing for real-time interaction and status updates.  
  
## REST Resource: [v1.projects.locations.apps.sessions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.sessions)

Methods  
---  
`[generateChatToken](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.sessions/generateChatToken)` |  `POST /v1/{name=projects/*/locations/*/apps/*/sessions/*}:generateChatToken`   
Generates a session scoped token for chat widget to authenticate with Session APIs.  
`[runSession](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.sessions/runSession)` |  `POST /v1/{config.session=projects/*/locations/*/apps/*/sessions/*}:runSession`   
Initiates a single-turn interaction with the CES agent within a session.  
`[streamRunSession](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.sessions/streamRunSession)` |  `POST /v1/{config.session=projects/*/locations/*/apps/*/sessions/*}:streamRunSession`   
Initiates a single-turn interaction with the CES agent.  
  
## REST Resource: [v1.projects.locations.apps.tools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.tools)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.tools/create)` |  `POST /v1/{parent=projects/*/locations/*/apps/*}/tools`   
Creates a new tool in the given app.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.tools/delete)` |  `DELETE /v1/{name=projects/*/locations/*/apps/*/tools/*}`   
Deletes the specified tool.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.tools/get)` |  `GET /v1/{name=projects/*/locations/*/apps/*/tools/*}`   
Gets details of the specified tool.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.tools/list)` |  `GET /v1/{parent=projects/*/locations/*/apps/*}/tools`   
Lists tools in the given app.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.tools/patch)` |  `PATCH /v1/{tool.name=projects/*/locations/*/apps/*/tools/*}`   
Updates the specified tool.  
  
## REST Resource: [v1.projects.locations.apps.toolsets](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.toolsets)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.toolsets/create)` |  `POST /v1/{parent=projects/*/locations/*/apps/*}/toolsets`   
Creates a new toolset in the given app.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.toolsets/delete)` |  `DELETE /v1/{name=projects/*/locations/*/apps/*/toolsets/*}`   
Deletes the specified toolset.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.toolsets/get)` |  `GET /v1/{name=projects/*/locations/*/apps/*/toolsets/*}`   
Gets details of the specified toolset.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.toolsets/list)` |  `GET /v1/{parent=projects/*/locations/*/apps/*}/toolsets`   
Lists toolsets in the given app.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.toolsets/patch)` |  `PATCH /v1/{toolset.name=projects/*/locations/*/apps/*/toolsets/*}`   
Updates the specified toolset.  
`[retrieveTools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.toolsets/retrieveTools)` |  `POST /v1/{toolset=projects/*/locations/*/apps/*/toolsets/*}:retrieveTools`   
Retrieve the list of tools included in the specified toolset.  
  
## REST Resource: [v1.projects.locations.apps.versions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.versions)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.versions/create)` |  `POST /v1/{parent=projects/*/locations/*/apps/*}/versions`   
Creates a new app version in the given app.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.versions/delete)` |  `DELETE /v1/{name=projects/*/locations/*/apps/*/versions/*}`   
Deletes the specified app version.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.versions/get)` |  `GET /v1/{name=projects/*/locations/*/apps/*/versions/*}`   
Gets details of the specified app version.  
`[getExtendedAgentCard](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.versions/getExtendedAgentCard)` |  `GET /v1/{tenant=projects/*/locations/*/apps/*/versions/*}/extendedAgentCard`   
Gets the extended agent card for the authenticated agent.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.versions/list)` |  `GET /v1/{parent=projects/*/locations/*/apps/*}/versions`   
Lists all app versions in the given app.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.versions/patch)` |  `PATCH /v1/{appVersion.name=projects/*/locations/*/apps/*/versions/*}`   
Updates the specified app version.  
`[restore](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.versions/restore)` |  `POST /v1/{name=projects/*/locations/*/apps/*/versions/*}:restore`   
Restores the specified app version.  
  
## REST Resource: [v1.projects.locations.apps.versions.message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.versions.message)

Methods  
---  
`[send](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.versions.message/send)` |  `POST /v1/{tenant=projects/*/locations/*/apps/*/versions/*}/message:send`   
Sends a message to an agent.  
`[stream](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.versions.message/stream)` |  `POST /v1/{tenant=projects/*/locations/*/apps/*/versions/*}/message:stream`   
Sends a streaming message to an agent, allowing for real-time interaction and status updates.  
  
## REST Resource: [v1.projects.locations.operations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.operations/cancel)` |  `POST /v1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.operations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.operations/get)` |  `GET /v1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.operations/list)` |  `GET /v1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
