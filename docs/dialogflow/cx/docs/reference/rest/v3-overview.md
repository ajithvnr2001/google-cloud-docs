---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3-overview/
title: Dialogflow API \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:22:57.910329+00:00
---

# Dialogflow API  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3-overview/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  Dialogflow API Stay organized with collections  Save and categorize content based on your preferences. 

Builds conversational interfaces (for example, chatbots, and voice-powered apps and devices).

  * REST Resource: v3.projects.locations
  * REST Resource: v3.projects.locations.agents
  * REST Resource: v3.projects.locations.agents.changelogs
  * REST Resource: v3.projects.locations.agents.entityTypes
  * REST Resource: v3.projects.locations.agents.environments
  * REST Resource: v3.projects.locations.agents.environments.continuousTestResults
  * REST Resource: v3.projects.locations.agents.environments.deployments
  * REST Resource: v3.projects.locations.agents.environments.experiments
  * REST Resource: v3.projects.locations.agents.environments.sessions
  * REST Resource: v3.projects.locations.agents.environments.sessions.entityTypes
  * REST Resource: v3.projects.locations.agents.flows
  * REST Resource: v3.projects.locations.agents.flows.pages
  * REST Resource: v3.projects.locations.agents.flows.transitionRouteGroups
  * REST Resource: v3.projects.locations.agents.flows.versions
  * REST Resource: v3.projects.locations.agents.generators
  * REST Resource: v3.projects.locations.agents.intents
  * REST Resource: v3.projects.locations.agents.playbooks
  * REST Resource: v3.projects.locations.agents.playbooks.examples
  * REST Resource: v3.projects.locations.agents.playbooks.versions
  * REST Resource: v3.projects.locations.agents.sessions
  * REST Resource: v3.projects.locations.agents.sessions.entityTypes
  * REST Resource: v3.projects.locations.agents.testCases
  * REST Resource: v3.projects.locations.agents.testCases.results
  * REST Resource: v3.projects.locations.agents.tools
  * REST Resource: v3.projects.locations.agents.tools.versions
  * REST Resource: v3.projects.locations.agents.transitionRouteGroups
  * REST Resource: v3.projects.locations.agents.webhooks
  * REST Resource: v3.projects.locations.operations
  * REST Resource: v3.projects.locations.securitySettings
  * REST Resource: v3.projects.operations



## Service: dialogflow.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

  * <https://dialogflow.googleapis.com/$discovery/rest?version=v3>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoints and all URIs below are relative to these service endpoints:

  * `https://dialogflow.googleapis.com`
  * `https://asia-northeast1-dialogflow.googleapis.com`
  * `https://asia-south1-dialogflow.googleapis.com`
  * `https://asia-southeast1-dialogflow.googleapis.com`
  * `https://asia-southeast2-dialogflow.googleapis.com`
  * `https://australia-southeast1-dialogflow.googleapis.com`
  * `https://europe-west1-dialogflow.googleapis.com`
  * `https://europe-west2-dialogflow.googleapis.com`
  * `https://europe-west3-dialogflow.googleapis.com`
  * `https://europe-west4-dialogflow.googleapis.com`
  * `https://europe-west6-dialogflow.googleapis.com`
  * `https://northamerica-northeast1-dialogflow.googleapis.com`
  * `https://us-central1-dialogflow.googleapis.com`
  * `https://us-east1-dialogflow.googleapis.com`
  * `https://us-west1-dialogflow.googleapis.com`



## REST Resource: [v3.projects.locations](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations/get)` |  `GET /v3/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations/list)` |  `GET /v3/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v3.projects.locations.agents](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents/create)` |  `POST /v3/{parent=projects/*/locations/*}/agents`   
Creates an agent in the specified location.  
`[delete](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents/delete)` |  `DELETE /v3/{name=projects/*/locations/*/agents/*}`   
Deletes the specified agent.  
`[export](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents/export)` |  `POST /v3/{name=projects/*/locations/*/agents/*}:export`   
Exports the specified agent to a binary file.  
`[get](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents/get)` |  `GET /v3/{name=projects/*/locations/*/agents/*}`   
Retrieves the specified agent.  
`[getGenerativeSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents/getGenerativeSettings)` |  `GET /v3/{name=projects/*/locations/*/agents/*/generativeSettings}`   
Gets the generative settings for the agent.  
`[getValidationResult](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents/getValidationResult)` |  `GET /v3/{name=projects/*/locations/*/agents/*/validationResult}`   
Gets the latest agent validation result.  
`[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents/list)` |  `GET /v3/{parent=projects/*/locations/*}/agents`   
Returns the list of all agents in the specified location.  
`[patch](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents/patch)` |  `PATCH /v3/{agent.name=projects/*/locations/*/agents/*}`   
Updates the specified agent.  
`[restore](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents/restore)` |  `POST /v3/{name=projects/*/locations/*/agents/*}:restore`   
Restores the specified agent from a binary file.  
`[updateGenerativeSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents/updateGenerativeSettings)` |  `PATCH /v3/{generativeSettings.name=projects/*/locations/*/agents/*/generativeSettings}`   
Updates the generative settings for the agent.  
`[validate](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents/validate)` |  `POST /v3/{name=projects/*/locations/*/agents/*}:validate`   
Validates the specified agent and creates or updates validation results.  
  
## REST Resource: [v3.projects.locations.agents.changelogs](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.changelogs)

Methods  
---  
`[get](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.changelogs/get)` |  `GET /v3/{name=projects/*/locations/*/agents/*/changelogs/*}`   
Retrieves the specified Changelog.  
`[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.changelogs/list)` |  `GET /v3/{parent=projects/*/locations/*/agents/*}/changelogs`   
Returns the list of Changelogs.  
  
## REST Resource: [v3.projects.locations.agents.entityTypes](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.entityTypes)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.entityTypes/create)` |  `POST /v3/{parent=projects/*/locations/*/agents/*}/entityTypes`   
Creates an entity type in the specified agent.  
`[delete](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.entityTypes/delete)` |  `DELETE /v3/{name=projects/*/locations/*/agents/*/entityTypes/*}`   
Deletes the specified entity type.  
`[export](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.entityTypes/export)` |  `POST /v3/{parent=projects/*/locations/*/agents/*}/entityTypes:export`   
Exports the selected entity types.  
`[get](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.entityTypes/get)` |  `GET /v3/{name=projects/*/locations/*/agents/*/entityTypes/*}`   
Retrieves the specified entity type.  
`[import](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.entityTypes/import)` |  `POST /v3/{parent=projects/*/locations/*/agents/*}/entityTypes:import`   
Imports the specified entitytypes into the agent.  
`[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.entityTypes/list)` |  `GET /v3/{parent=projects/*/locations/*/agents/*}/entityTypes`   
Returns the list of all entity types in the specified agent.  
`[patch](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.entityTypes/patch)` |  `PATCH /v3/{entityType.name=projects/*/locations/*/agents/*/entityTypes/*}`   
Updates the specified entity type.  
  
## REST Resource: [v3.projects.locations.agents.environments](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments/create)` |  `POST /v3/{parent=projects/*/locations/*/agents/*}/environments`   
Creates an `[Environment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments#Environment)` in the specified `[Agent](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents#Agent)`.  
`[delete](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments/delete)` |  `DELETE /v3/{name=projects/*/locations/*/agents/*/environments/*}`   
Deletes the specified `[Environment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments#Environment)`.  
`[deployFlow](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments/deployFlow)` |  `POST /v3/{environment=projects/*/locations/*/agents/*/environments/*}:deployFlow`   
Deploys a flow to the specified `[Environment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments#Environment)`.  
`[get](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments/get)` |  `GET /v3/{name=projects/*/locations/*/agents/*/environments/*}`   
Retrieves the specified `[Environment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments#Environment)`.  
`[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments/list)` |  `GET /v3/{parent=projects/*/locations/*/agents/*}/environments`   
Returns the list of all environments in the specified `[Agent](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents#Agent)`.  
`[lookupEnvironmentHistory](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments/lookupEnvironmentHistory)` |  `GET /v3/{name=projects/*/locations/*/agents/*/environments/*}:lookupEnvironmentHistory`   
Looks up the history of the specified `[Environment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments#Environment)`.  
`[patch](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments/patch)` |  `PATCH /v3/{environment.name=projects/*/locations/*/agents/*/environments/*}`   
Updates the specified `[Environment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments#Environment)`.  
`[runContinuousTest](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments/runContinuousTest)` |  `POST /v3/{environment=projects/*/locations/*/agents/*/environments/*}:runContinuousTest`   
Kicks off a continuous test under the specified `[Environment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments#Environment)`.  
  
## REST Resource: [v3.projects.locations.agents.environments.continuousTestResults](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.continuousTestResults)

Methods  
---  
`[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.continuousTestResults/list)` |  `GET /v3/{parent=projects/*/locations/*/agents/*/environments/*}/continuousTestResults`   
Fetches a list of continuous test results for a given environment.  
  
## REST Resource: [v3.projects.locations.agents.environments.deployments](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.deployments)

Methods  
---  
`[get](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.deployments/get)` |  `GET /v3/{name=projects/*/locations/*/agents/*/environments/*/deployments/*}`   
Retrieves the specified `[Deployment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.deployments#Deployment)`.  
`[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.deployments/list)` |  `GET /v3/{parent=projects/*/locations/*/agents/*/environments/*}/deployments`   
Returns the list of all deployments in the specified `[Environment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments#Environment)`.  
  
## REST Resource: [v3.projects.locations.agents.environments.experiments](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments/create)` |  `POST /v3/{parent=projects/*/locations/*/agents/*/environments/*}/experiments`   
Creates an `[Experiment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments#Experiment)` in the specified `[Environment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments#Environment)`.  
`[delete](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments/delete)` |  `DELETE /v3/{name=projects/*/locations/*/agents/*/environments/*/experiments/*}`   
Deletes the specified `[Experiment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments#Experiment)`.  
`[get](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments/get)` |  `GET /v3/{name=projects/*/locations/*/agents/*/environments/*/experiments/*}`   
Retrieves the specified `[Experiment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments#Experiment)`.  
`[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments/list)` |  `GET /v3/{parent=projects/*/locations/*/agents/*/environments/*}/experiments`   
Returns the list of all experiments in the specified `[Environment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments#Environment)`.  
`[patch](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments/patch)` |  `PATCH /v3/{experiment.name=projects/*/locations/*/agents/*/environments/*/experiments/*}`   
Updates the specified `[Experiment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments#Experiment)`.  
`[start](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments/start)` |  `POST /v3/{name=projects/*/locations/*/agents/*/environments/*/experiments/*}:start`   
Starts the specified `[Experiment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments#Experiment)`.  
`[stop](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments/stop)` |  `POST /v3/{name=projects/*/locations/*/agents/*/environments/*/experiments/*}:stop`   
Stops the specified `[Experiment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.experiments#Experiment)`.  
  
## REST Resource: [v3.projects.locations.agents.environments.sessions](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.sessions)

Methods  
---  
`[detectIntent](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.sessions/detectIntent)` |  `POST /v3/{session=projects/*/locations/*/agents/*/environments/*/sessions/*}:detectIntent`   
Processes a natural language query and returns structured, actionable data as a result.  
`[fulfillIntent](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.sessions/fulfillIntent)` |  `POST /v3/{matchIntentRequest.session=projects/*/locations/*/agents/*/environments/*/sessions/*}:fulfillIntent`   
Fulfills a matched intent returned by `[MatchIntent](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.sessions/matchIntent#google.cloud.dialogflow.cx.v3.Sessions.MatchIntent)`.  
`[matchIntent](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.sessions/matchIntent)` |  `POST /v3/{session=projects/*/locations/*/agents/*/environments/*/sessions/*}:matchIntent`   
Returns preliminary intent match results, doesn't change the session status.  
`[serverStreamingDetectIntent](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.sessions/serverStreamingDetectIntent)` |  `POST /v3/{session=projects/*/locations/*/agents/*/environments/*/sessions/*}:serverStreamingDetectIntent`   
Processes a natural language query and returns structured, actionable data as a result through server-side streaming.  
  
## REST Resource: [v3.projects.locations.agents.environments.sessions.entityTypes](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.sessions.entityTypes)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.sessions.entityTypes/create)` |  `POST /v3/{parent=projects/*/locations/*/agents/*/environments/*/sessions/*}/entityTypes`   
Creates a session entity type.  
`[delete](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.sessions.entityTypes/delete)` |  `DELETE /v3/{name=projects/*/locations/*/agents/*/environments/*/sessions/*/entityTypes/*}`   
Deletes the specified session entity type.  
`[get](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.sessions.entityTypes/get)` |  `GET /v3/{name=projects/*/locations/*/agents/*/environments/*/sessions/*/entityTypes/*}`   
Retrieves the specified session entity type.  
`[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.sessions.entityTypes/list)` |  `GET /v3/{parent=projects/*/locations/*/agents/*/environments/*/sessions/*}/entityTypes`   
Returns the list of all session entity types in the specified session.  
`[patch](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.sessions.entityTypes/patch)` |  `PATCH /v3/{sessionEntityType.name=projects/*/locations/*/agents/*/environments/*/sessions/*/entityTypes/*}`   
Updates the specified session entity type.  
  
## REST Resource: [v3.projects.locations.agents.flows](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows/create)` |  `POST /v3/{parent=projects/*/locations/*/agents/*}/flows`   
Creates a flow in the specified agent.  
`[delete](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows/delete)` |  `DELETE /v3/{name=projects/*/locations/*/agents/*/flows/*}`   
Deletes a specified flow.  
`[export](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows/export)` |  `POST /v3/{name=projects/*/locations/*/agents/*/flows/*}:export`   
Exports the specified flow to a binary file.  
`[get](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows/get)` |  `GET /v3/{name=projects/*/locations/*/agents/*/flows/*}`   
Retrieves the specified flow.  
`[getValidationResult](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows/getValidationResult)` |  `GET /v3/{name=projects/*/locations/*/agents/*/flows/*/validationResult}`   
Gets the latest flow validation result.  
`[import](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows/import)` |  `POST /v3/{parent=projects/*/locations/*/agents/*}/flows:import`   
Imports the specified flow to the specified agent from a binary file.  
`[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows/list)` |  `GET /v3/{parent=projects/*/locations/*/agents/*}/flows`   
Returns the list of all flows in the specified agent.  
`[patch](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows/patch)` |  `PATCH /v3/{flow.name=projects/*/locations/*/agents/*/flows/*}`   
Updates the specified flow.  
`[train](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows/train)` |  `POST /v3/{name=projects/*/locations/*/agents/*/flows/*}:train`   
Trains the specified flow.  
`[validate](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows/validate)` |  `POST /v3/{name=projects/*/locations/*/agents/*/flows/*}:validate`   
Validates the specified flow and creates or updates validation results.  
  
## REST Resource: [v3.projects.locations.agents.flows.pages](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages/create)` |  `POST /v3/{parent=projects/*/locations/*/agents/*/flows/*}/pages`   
Creates a page in the specified flow.  
`[delete](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages/delete)` |  `DELETE /v3/{name=projects/*/locations/*/agents/*/flows/*/pages/*}`   
Deletes the specified page.  
`[get](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages/get)` |  `GET /v3/{name=projects/*/locations/*/agents/*/flows/*/pages/*}`   
Retrieves the specified page.  
`[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages/list)` |  `GET /v3/{parent=projects/*/locations/*/agents/*/flows/*}/pages`   
Returns the list of all pages in the specified flow.  
`[patch](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages/patch)` |  `PATCH /v3/{page.name=projects/*/locations/*/agents/*/flows/*/pages/*}`   
Updates the specified page.  
  
## REST Resource: [v3.projects.locations.agents.flows.transitionRouteGroups](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.transitionRouteGroups)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.transitionRouteGroups/create)` |  `POST /v3/{parent=projects/*/locations/*/agents/*/flows/*}/transitionRouteGroups`   
Creates an `[TransitionRouteGroup](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.transitionRouteGroups#TransitionRouteGroup)` in the specified flow.  
`[delete](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.transitionRouteGroups/delete)` |  `DELETE /v3/{name=projects/*/locations/*/agents/*/flows/*/transitionRouteGroups/*}`   
Deletes the specified `[TransitionRouteGroup](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.transitionRouteGroups#TransitionRouteGroup)`.  
`[get](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.transitionRouteGroups/get)` |  `GET /v3/{name=projects/*/locations/*/agents/*/flows/*/transitionRouteGroups/*}`   
Retrieves the specified `[TransitionRouteGroup](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.transitionRouteGroups#TransitionRouteGroup)`.  
`[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.transitionRouteGroups/list)` |  `GET /v3/{parent=projects/*/locations/*/agents/*/flows/*}/transitionRouteGroups`   
Returns the list of all transition route groups in the specified flow.  
`[patch](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.transitionRouteGroups/patch)` |  `PATCH /v3/{transitionRouteGroup.name=projects/*/locations/*/agents/*/flows/*/transitionRouteGroups/*}`   
Updates the specified `[TransitionRouteGroup](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.transitionRouteGroups#TransitionRouteGroup)`.  
  
## REST Resource: [v3.projects.locations.agents.flows.versions](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.versions)

Methods  
---  
`[compareVersions](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.versions/compareVersions)` |  `POST /v3/{baseVersion=projects/*/locations/*/agents/*/flows/*/versions/*}:compareVersions`   
Compares the specified base version with target version.  
`[create](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.versions/create)` |  `POST /v3/{parent=projects/*/locations/*/agents/*/flows/*}/versions`   
Creates a `[Version](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.versions#Version)` in the specified `[Flow](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows#Flow)`.  
`[delete](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.versions/delete)` |  `DELETE /v3/{name=projects/*/locations/*/agents/*/flows/*/versions/*}`   
Deletes the specified `[Version](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.versions#Version)`.  
`[get](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.versions/get)` |  `GET /v3/{name=projects/*/locations/*/agents/*/flows/*/versions/*}`   
Retrieves the specified `[Version](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.versions#Version)`.  
`[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.versions/list)` |  `GET /v3/{parent=projects/*/locations/*/agents/*/flows/*}/versions`   
Returns the list of all versions in the specified `[Flow](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows#Flow)`.  
`[load](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.versions/load)` |  `POST /v3/{name=projects/*/locations/*/agents/*/flows/*/versions/*}:load`   
Loads resources in the specified version to the draft flow.  
`[patch](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.versions/patch)` |  `PATCH /v3/{version.name=projects/*/locations/*/agents/*/flows/*/versions/*}`   
Updates the specified `[Version](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.versions#Version)`.  
  
## REST Resource: [v3.projects.locations.agents.generators](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.generators)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.generators/create)` |  `POST /v3/{parent=projects/*/locations/*/agents/*}/generators`   
Creates a generator in the specified agent.  
`[delete](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.generators/delete)` |  `DELETE /v3/{name=projects/*/locations/*/agents/*/generators/*}`   
Deletes the specified generators.  
`[get](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.generators/get)` |  `GET /v3/{name=projects/*/locations/*/agents/*/generators/*}`   
Retrieves the specified generator.  
`[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.generators/list)` |  `GET /v3/{parent=projects/*/locations/*/agents/*}/generators`   
Returns the list of all generators in the specified agent.  
`[patch](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.generators/patch)` |  `PATCH /v3/{generator.name=projects/*/locations/*/agents/*/generators/*}`   
Update the specified generator.  
  
## REST Resource: [v3.projects.locations.agents.intents](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents/create)` |  `POST /v3/{parent=projects/*/locations/*/agents/*}/intents`   
Creates an intent in the specified agent.  
`[delete](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents/delete)` |  `DELETE /v3/{name=projects/*/locations/*/agents/*/intents/*}`   
Deletes the specified intent.  
`[export](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents/export)` |  `POST /v3/{parent=projects/*/locations/*/agents/*}/intents:export`   
Exports the selected intents.  
`[get](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents/get)` |  `GET /v3/{name=projects/*/locations/*/agents/*/intents/*}`   
Retrieves the specified intent.  
`[import](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents/import)` |  `POST /v3/{parent=projects/*/locations/*/agents/*}/intents:import`   
Imports the specified intents into the agent.  
`[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents/list)` |  `GET /v3/{parent=projects/*/locations/*/agents/*}/intents`   
Returns the list of all intents in the specified agent.  
`[patch](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents/patch)` |  `PATCH /v3/{intent.name=projects/*/locations/*/agents/*/intents/*}`   
Updates the specified intent.  
  
## REST Resource: [v3.projects.locations.agents.playbooks](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks/create)` |  `POST /v3/{parent=projects/*/locations/*/agents/*}/playbooks`   
Creates a playbook in a specified agent.  
`[delete](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks/delete)` |  `DELETE /v3/{name=projects/*/locations/*/agents/*/playbooks/*}`   
Deletes a specified playbook.  
`[export](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks/export)` |  `POST /v3/{name=projects/*/locations/*/agents/*/playbooks/*}:export`   
Exports the specified playbook to a binary file.  
`[get](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks/get)` |  `GET /v3/{name=projects/*/locations/*/agents/*/playbooks/*}`   
Retrieves the specified Playbook.  
`[import](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks/import)` |  `POST /v3/{parent=projects/*/locations/*/agents/*}/playbooks:import`   
Imports the specified playbook to the specified agent from a binary file.  
`[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks/list)` |  `GET /v3/{parent=projects/*/locations/*/agents/*}/playbooks`   
Returns a list of playbooks in the specified agent.  
`[patch](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks/patch)` |  `PATCH /v3/{playbook.name=projects/*/locations/*/agents/*/playbooks/*}`   
Updates the specified Playbook.  
  
## REST Resource: [v3.projects.locations.agents.playbooks.examples](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.examples)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.examples/create)` |  `POST /v3/{parent=projects/*/locations/*/agents/*/playbooks/*}/examples`   
Creates an example in the specified playbook.  
`[delete](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.examples/delete)` |  `DELETE /v3/{name=projects/*/locations/*/agents/*/playbooks/*/examples/*}`   
Deletes the specified example.  
`[get](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.examples/get)` |  `GET /v3/{name=projects/*/locations/*/agents/*/playbooks/*/examples/*}`   
Retrieves the specified example.  
`[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.examples/list)` |  `GET /v3/{parent=projects/*/locations/*/agents/*/playbooks/*}/examples`   
Returns a list of examples in the specified playbook.  
`[patch](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.examples/patch)` |  `PATCH /v3/{example.name=projects/*/locations/*/agents/*/playbooks/*/examples/*}`   
Update the specified example.  
  
## REST Resource: [v3.projects.locations.agents.playbooks.versions](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.versions)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.versions/create)` |  `POST /v3/{parent=projects/*/locations/*/agents/*/playbooks/*}/versions`   
Creates a version for the specified Playbook.  
`[delete](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.versions/delete)` |  `DELETE /v3/{name=projects/*/locations/*/agents/*/playbooks/*/versions/*}`   
Deletes the specified version of the Playbook.  
`[get](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.versions/get)` |  `GET /v3/{name=projects/*/locations/*/agents/*/playbooks/*/versions/*}`   
Retrieves the specified version of the Playbook.  
`[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.versions/list)` |  `GET /v3/{parent=projects/*/locations/*/agents/*/playbooks/*}/versions`   
Lists versions for the specified Playbook.  
`[restore](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.versions/restore)` |  `POST /v3/{name=projects/*/locations/*/agents/*/playbooks/*/versions/*}:restore`   
Retrieves the specified version of the Playbook and stores it as the current playbook draft, returning the playbook with resources updated.  
  
## REST Resource: [v3.projects.locations.agents.sessions](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.sessions)

Methods  
---  
`[detectIntent](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.sessions/detectIntent)` |  `POST /v3/{session=projects/*/locations/*/agents/*/sessions/*}:detectIntent`   
Processes a natural language query and returns structured, actionable data as a result.  
`[fulfillIntent](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.sessions/fulfillIntent)` |  `POST /v3/{matchIntentRequest.session=projects/*/locations/*/agents/*/sessions/*}:fulfillIntent`   
Fulfills a matched intent returned by `[MatchIntent](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.sessions/matchIntent#google.cloud.dialogflow.cx.v3.Sessions.MatchIntent)`.  
`[matchIntent](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.sessions/matchIntent)` |  `POST /v3/{session=projects/*/locations/*/agents/*/sessions/*}:matchIntent`   
Returns preliminary intent match results, doesn't change the session status.  
`[serverStreamingDetectIntent](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.sessions/serverStreamingDetectIntent)` |  `POST /v3/{session=projects/*/locations/*/agents/*/sessions/*}:serverStreamingDetectIntent`   
Processes a natural language query and returns structured, actionable data as a result through server-side streaming.  
`[submitAnswerFeedback](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.sessions/submitAnswerFeedback)` |  `POST /v3/{session=projects/*/locations/*/agents/*/sessions/*}:submitAnswerFeedback`   
Updates the feedback received from the user for a single turn of the bot response.  
  
## REST Resource: [v3.projects.locations.agents.sessions.entityTypes](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.sessions.entityTypes)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.sessions.entityTypes/create)` |  `POST /v3/{parent=projects/*/locations/*/agents/*/sessions/*}/entityTypes`   
Creates a session entity type.  
`[delete](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.sessions.entityTypes/delete)` |  `DELETE /v3/{name=projects/*/locations/*/agents/*/sessions/*/entityTypes/*}`   
Deletes the specified session entity type.  
`[get](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.sessions.entityTypes/get)` |  `GET /v3/{name=projects/*/locations/*/agents/*/sessions/*/entityTypes/*}`   
Retrieves the specified session entity type.  
`[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.sessions.entityTypes/list)` |  `GET /v3/{parent=projects/*/locations/*/agents/*/sessions/*}/entityTypes`   
Returns the list of all session entity types in the specified session.  
`[patch](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.sessions.entityTypes/patch)` |  `PATCH /v3/{sessionEntityType.name=projects/*/locations/*/agents/*/sessions/*/entityTypes/*}`   
Updates the specified session entity type.  
  
## REST Resource: [v3.projects.locations.agents.testCases](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases)

Methods  
---  
`[batchDelete](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/batchDelete)` |  `POST /v3/{parent=projects/*/locations/*/agents/*}/testCases:batchDelete`   
Batch deletes test cases.  
`[batchRun](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/batchRun)` |  `POST /v3/{parent=projects/*/locations/*/agents/*}/testCases:batchRun`   
Kicks off a batch run of test cases.  
`[calculateCoverage](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/calculateCoverage)` |  `GET /v3/{agent=projects/*/locations/*/agents/*}/testCases:calculateCoverage`   
Calculates the test coverage for an agent.  
`[create](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/create)` |  `POST /v3/{parent=projects/*/locations/*/agents/*}/testCases`   
Creates a test case for the given agent.  
`[export](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/export)` |  `POST /v3/{parent=projects/*/locations/*/agents/*}/testCases:export`   
Exports the test cases under the agent to a Cloud Storage bucket or a local file.  
`[get](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/get)` |  `GET /v3/{name=projects/*/locations/*/agents/*/testCases/*}`   
Gets a test case.  
`[import](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/import)` |  `POST /v3/{parent=projects/*/locations/*/agents/*}/testCases:import`   
Imports the test cases from a Cloud Storage bucket or a local file.  
`[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/list)` |  `GET /v3/{parent=projects/*/locations/*/agents/*}/testCases`   
Fetches a list of test cases for a given agent.  
`[patch](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/patch)` |  `PATCH /v3/{testCase.name=projects/*/locations/*/agents/*/testCases/*}`   
Updates the specified test case.  
`[run](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/run)` |  `POST /v3/{name=projects/*/locations/*/agents/*/testCases/*}:run`   
Kicks off a test case run.  
  
## REST Resource: [v3.projects.locations.agents.testCases.results](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases.results)

Methods  
---  
`[get](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases.results/get)` |  `GET /v3/{name=projects/*/locations/*/agents/*/testCases/*/results/*}`   
Gets a test case result.  
`[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases.results/list)` |  `GET /v3/{parent=projects/*/locations/*/agents/*/testCases/*}/results`   
Fetches the list of run results for the given test case.  
  
## REST Resource: [v3.projects.locations.agents.tools](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools/create)` |  `POST /v3/{parent=projects/*/locations/*/agents/*}/tools`   
Creates a `[Tool](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool)` in the specified agent.  
`[delete](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools/delete)` |  `DELETE /v3/{name=projects/*/locations/*/agents/*/tools/*}`   
Deletes a specified `[Tool](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool)`.  
`[get](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools/get)` |  `GET /v3/{name=projects/*/locations/*/agents/*/tools/*}`   
Retrieves the specified `[Tool](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool)`.  
`[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools/list)` |  `GET /v3/{parent=projects/*/locations/*/agents/*}/tools`   
Returns a list of `[Tools](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool)` in the specified agent.  
`[patch](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools/patch)` |  `PATCH /v3/{tool.name=projects/*/locations/*/agents/*/tools/*}`   
Update the specified `[Tool](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool)`.  
  
## REST Resource: [v3.projects.locations.agents.tools.versions](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools.versions)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools.versions/create)` |  `POST /v3/{parent=projects/*/locations/*/agents/*/tools/*}/versions`   
Creates a version for the specified `[Tool](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool)`.  
`[delete](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools.versions/delete)` |  `DELETE /v3/{name=projects/*/locations/*/agents/*/tools/*/versions/*}`   
Deletes the specified version of the `[Tool](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool)`.  
`[get](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools.versions/get)` |  `GET /v3/{name=projects/*/locations/*/agents/*/tools/*/versions/*}`   
Retrieves the specified version of the `[Tool](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool)`.  
`[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools.versions/list)` |  `GET /v3/{parent=projects/*/locations/*/agents/*/tools/*}/versions`   
List versions of the specified `[Tool](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool)`.  
`[restore](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools.versions/restore)` |  `POST /v3/{name=projects/*/locations/*/agents/*/tools/*/versions/*}:restore`   
Retrieves the specified version of the Tool and stores it as the current tool draft, returning the tool with resources updated.  
  
## REST Resource: [v3.projects.locations.agents.transitionRouteGroups](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.transitionRouteGroups)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.transitionRouteGroups/create)` |  `POST /v3/{parent=projects/*/locations/*/agents/*}/transitionRouteGroups`   
Creates an `[TransitionRouteGroup](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.transitionRouteGroups#TransitionRouteGroup)` in the specified flow.  
`[delete](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.transitionRouteGroups/delete)` |  `DELETE /v3/{name=projects/*/locations/*/agents/*/transitionRouteGroups/*}`   
Deletes the specified `[TransitionRouteGroup](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.transitionRouteGroups#TransitionRouteGroup)`.  
`[get](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.transitionRouteGroups/get)` |  `GET /v3/{name=projects/*/locations/*/agents/*/transitionRouteGroups/*}`   
Retrieves the specified `[TransitionRouteGroup](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.transitionRouteGroups#TransitionRouteGroup)`.  
`[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.transitionRouteGroups/list)` |  `GET /v3/{parent=projects/*/locations/*/agents/*}/transitionRouteGroups`   
Returns the list of all transition route groups in the specified flow.  
`[patch](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.transitionRouteGroups/patch)` |  `PATCH /v3/{transitionRouteGroup.name=projects/*/locations/*/agents/*/transitionRouteGroups/*}`   
Updates the specified `[TransitionRouteGroup](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.transitionRouteGroups#TransitionRouteGroup)`.  
  
## REST Resource: [v3.projects.locations.agents.webhooks](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.webhooks)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.webhooks/create)` |  `POST /v3/{parent=projects/*/locations/*/agents/*}/webhooks`   
Creates a webhook in the specified agent.  
`[delete](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.webhooks/delete)` |  `DELETE /v3/{name=projects/*/locations/*/agents/*/webhooks/*}`   
Deletes the specified webhook.  
`[get](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.webhooks/get)` |  `GET /v3/{name=projects/*/locations/*/agents/*/webhooks/*}`   
Retrieves the specified webhook.  
`[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.webhooks/list)` |  `GET /v3/{parent=projects/*/locations/*/agents/*}/webhooks`   
Returns the list of all webhooks in the specified agent.  
`[patch](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.webhooks/patch)` |  `PATCH /v3/{webhook.name=projects/*/locations/*/agents/*/webhooks/*}`   
Updates the specified webhook.  
  
## REST Resource: [v3.projects.locations.operations](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.operations/cancel)` |  `POST /v3/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[get](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.operations/get)` |  `GET /v3/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.operations/list)` |  `GET /v3/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v3.projects.locations.securitySettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings)

Methods  
---  
`[create](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings/create)` |  `POST /v3/{parent=projects/*/locations/*}/securitySettings`   
Create security settings in the specified location.  
`[delete](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings/delete)` |  `DELETE /v3/{name=projects/*/locations/*/securitySettings/*}`   
Deletes the specified `[SecuritySettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings#SecuritySettings)`.  
`[get](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings/get)` |  `GET /v3/{name=projects/*/locations/*/securitySettings/*}`   
Retrieves the specified `[SecuritySettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings#SecuritySettings)`.  
`[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings/list)` |  `GET /v3/{parent=projects/*/locations/*}/securitySettings`   
Returns the list of all security settings in the specified location.  
`[patch](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings/patch)` |  `PATCH /v3/{securitySettings.name=projects/*/locations/*/securitySettings/*}`   
Updates the specified `[SecuritySettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings#SecuritySettings)`.  
  
## REST Resource: [v3.projects.operations](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.operations/cancel)` |  `POST /v3/{name=projects/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[get](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.operations/get)` |  `GET /v3/{name=projects/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.operations/list)` |  `GET /v3/{name=projects/*}/operations`   
Lists operations that match the specified filter in the request.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
