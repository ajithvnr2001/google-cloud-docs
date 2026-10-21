---
url: https://docs.cloud.google.com/agent-registry/reference/rest/
title: Agent Registry API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:06:30.984699+00:00
---

# Agent Registry API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Reference ](https://docs.cloud.google.com/agent-registry/apis)



Send feedback 

#  Agent Registry API Stay organized with collections  Save and categorize content based on your preferences. 

Agent Registry is a centralized, unified catalog that lets you store, discover, and govern Model Context Protocol (MCP) servers, tools, and AI agents within Google Cloud.

  * REST Resource: v1alpha.projects.locations
  * REST Resource: v1alpha.projects.locations.agents
  * REST Resource: v1alpha.projects.locations.aiApplications
  * REST Resource: v1alpha.projects.locations.bindings
  * REST Resource: v1alpha.projects.locations.endpoints
  * REST Resource: v1alpha.projects.locations.mcpServers
  * REST Resource: v1alpha.projects.locations.operations
  * REST Resource: v1alpha.projects.locations.publishers
  * REST Resource: v1alpha.projects.locations.services
  * REST Resource: v1alpha.projects.locations.skills
  * REST Resource: v1alpha.projects.locations.skills.revisions
  * REST Resource: v1.projects.locations
  * REST Resource: v1.projects.locations.agents
  * REST Resource: v1.projects.locations.aiApplications
  * REST Resource: v1.projects.locations.bindings
  * REST Resource: v1.projects.locations.endpoints
  * REST Resource: v1.projects.locations.mcpServers
  * REST Resource: v1.projects.locations.operations
  * REST Resource: v1.projects.locations.services



## Service: agentregistry.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery documents:

  * <https://agentregistry.googleapis.com/$discovery/rest?version=v1>
  * <https://agentregistry.googleapis.com/$discovery/rest?version=v1alpha>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://agentregistry.googleapis.com`



## REST Resource: [v1alpha.projects.locations](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations/get)` |  `GET /v1alpha/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations/list)` |  `GET /v1alpha/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1alpha.projects.locations.agents](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.agents)

Methods  
---  
`[get](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.agents/get)` |  `GET /v1alpha/{name=projects/*/locations/*/agents/*}`   
Gets details of a single Agent.  
`[list](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.agents/list)` |  `GET /v1alpha/{parent=projects/*/locations/*}/agents`   
Lists Agents in a given project and location.  
`[search](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.agents/search)` |  `POST /v1alpha/{parent=projects/*/locations/*}/agents:search`   
Searches Agents in a given project and location.  
  
## REST Resource: [v1alpha.projects.locations.aiApplications](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.aiApplications)

Methods  
---  
`[getIamPolicy](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.aiApplications/getIamPolicy)` |  `GET /v1alpha/{resource=projects/*/locations/*/aiApplications/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[setIamPolicy](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.aiApplications/setIamPolicy)` |  `POST /v1alpha/{resource=projects/*/locations/*/aiApplications/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.aiApplications/testIamPermissions)` |  `POST /v1alpha/{resource=projects/*/locations/*/aiApplications/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1alpha.projects.locations.bindings](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.bindings)

Methods  
---  
`[create](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.bindings/create)` |  `POST /v1alpha/{parent=projects/*/locations/*}/bindings`   
Creates a new Binding in a given project and location.  
`[delete](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.bindings/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/bindings/*}`   
Deletes a single Binding.  
`[fetchAvailable](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.bindings/fetchAvailable)` |  `GET /v1alpha/{parent=projects/*/locations/*}/bindings:fetchAvailable`   
Fetches available Bindings.  
`[get](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.bindings/get)` |  `GET /v1alpha/{name=projects/*/locations/*/bindings/*}`   
Gets details of a single Binding.  
`[list](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.bindings/list)` |  `GET /v1alpha/{parent=projects/*/locations/*}/bindings`   
Lists Bindings in a given project and location.  
`[patch](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.bindings/patch)` |  `PATCH /v1alpha/{binding.name=projects/*/locations/*/bindings/*}`   
Updates the parameters of a single Binding.  
  
## REST Resource: [v1alpha.projects.locations.endpoints](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.endpoints)

Methods  
---  
`[get](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.endpoints/get)` |  `GET /v1alpha/{name=projects/*/locations/*/endpoints/*}`   
Gets details of a single Endpoint.  
`[list](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.endpoints/list)` |  `GET /v1alpha/{parent=projects/*/locations/*}/endpoints`   
Lists Endpoints in a given project and location.  
  
## REST Resource: [v1alpha.projects.locations.mcpServers](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.mcpServers)

Methods  
---  
`[get](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.mcpServers/get)` |  `GET /v1alpha/{name=projects/*/locations/*/mcpServers/*}`   
Gets details of a single McpServer.  
`[list](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.mcpServers/list)` |  `GET /v1alpha/{parent=projects/*/locations/*}/mcpServers`   
Lists McpServers in a given project and location.  
`[search](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.mcpServers/search)` |  `POST /v1alpha/{parent=projects/*/locations/*}/mcpServers:search`   
Searches McpServers in a given project and location.  
  
## REST Resource: [v1alpha.projects.locations.operations](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.operations/cancel)` |  `POST /v1alpha/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.operations/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.operations/get)` |  `GET /v1alpha/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.operations/list)` |  `GET /v1alpha/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1alpha.projects.locations.publishers](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.publishers)

Methods  
---  
`[get](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.publishers/get)` |  `GET /v1alpha/{name=projects/*/locations/*/publishers/*}`   
Fetches details of a specific Publisher.  
`[list](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.publishers/list)` |  `GET /v1alpha/{parent=projects/*/locations/*}/publishers`   
Lists all Publishers in a location.  
  
## REST Resource: [v1alpha.projects.locations.services](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.services)

Methods  
---  
`[create](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.services/create)` |  `POST /v1alpha/{parent=projects/*/locations/*}/services`   
Creates a new Service in a given project and location.  
`[delete](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.services/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/services/*}`   
Deletes a single Service.  
`[get](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.services/get)` |  `GET /v1alpha/{name=projects/*/locations/*/services/*}`   
Gets details of a single Service.  
`[list](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.services/list)` |  `GET /v1alpha/{parent=projects/*/locations/*}/services`   
Lists Services in a given project and location.  
`[patch](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.services/patch)` |  `PATCH /v1alpha/{service.name=projects/*/locations/*/services/*}`   
Updates the parameters of a single Service.  
  
## REST Resource: [v1alpha.projects.locations.skills](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills)

Methods  
---  
`[create](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills/create)` |  `POST /v1alpha/{parent=projects/*/locations/*}/skills`   
=========================================================================

# Skills Collection APIs

Creates a Skill resource container, optionally publishing the initial SkillRevision inline in a single, atomic CRUD roundtrip.  
`[delete](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/skills/*}`   
Deletes a Skill container along with all its revisions.  
`[get](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills/get)` |  `GET /v1alpha/{name=projects/*/locations/*/skills/*}`   
Fetches the active configuration and metadata of a Skill.  
`[getIamPolicy](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills/getIamPolicy)` |  `GET /v1alpha/{resource=projects/*/locations/*/skills/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills/list)` |  `GET /v1alpha/{parent=projects/*/locations/*}/skills`   
Lists logical Skills available in a project.  
`[patch](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills/patch)` |  `PATCH /v1alpha/{skill.name=projects/*/locations/*/skills/*}`   
Updates Skill metadata or overrides active pointers/state using REST standard PATCH.  
`[search](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills/search)` |  `GET /v1alpha/{parent=projects/*/locations/*}/skills:search`   
Custom deep-search method to filter by frontmatter or query SKILL.md text blobs.  
`[setIamPolicy](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills/setIamPolicy)` |  `POST /v1alpha/{resource=projects/*/locations/*/skills/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills/testIamPermissions)` |  `POST /v1alpha/{resource=projects/*/locations/*/skills/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1alpha.projects.locations.skills.revisions](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills.revisions)

Methods  
---  
`[create](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills.revisions/create)` |  `POST /v1alpha/{parent=projects/*/locations/*/skills/*}/revisions`   
Creates a new immutable revision and triggers validation pipelines.  
`[delete](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills.revisions/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/skills/*/revisions/*}`   
Deletes a specific revision (restricted to admins to purge accidentally committed secrets).  
`[get](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills.revisions/get)` |  `GET /v1alpha/{name=projects/*/locations/*/skills/*/revisions/*}`   
Gets details of a single immutable Revision.  
`[list](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills.revisions/list)` |  `GET /v1alpha/{parent=projects/*/locations/*/skills/*}/revisions`   
Lists all revisions belonging to a parent Skill.  
  
## REST Resource: [v1.projects.locations](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations/get)` |  `GET /v1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations/list)` |  `GET /v1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1.projects.locations.agents](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.agents)

Methods  
---  
`[get](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.agents/get)` |  `GET /v1/{name=projects/*/locations/*/agents/*}`   
Gets details of a single Agent.  
`[list](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.agents/list)` |  `GET /v1/{parent=projects/*/locations/*}/agents`   
Lists Agents in a given project and location.  
`[search](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.agents/search)` |  `POST /v1/{parent=projects/*/locations/*}/agents:search`   
Searches Agents in a given project and location.  
  
## REST Resource: [v1.projects.locations.aiApplications](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.aiApplications)

Methods  
---  
`[getIamPolicy](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.aiApplications/getIamPolicy)` |  `GET /v1/{resource=projects/*/locations/*/aiApplications/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[setIamPolicy](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.aiApplications/setIamPolicy)` |  `POST /v1/{resource=projects/*/locations/*/aiApplications/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.aiApplications/testIamPermissions)` |  `POST /v1/{resource=projects/*/locations/*/aiApplications/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1.projects.locations.bindings](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.bindings)

Methods  
---  
`[create](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.bindings/create)` |  `POST /v1/{parent=projects/*/locations/*}/bindings`   
Creates a new Binding in a given project and location.  
`[delete](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.bindings/delete)` |  `DELETE /v1/{name=projects/*/locations/*/bindings/*}`   
Deletes a single Binding.  
`[fetchAvailable](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.bindings/fetchAvailable)` |  `GET /v1/{parent=projects/*/locations/*}/bindings:fetchAvailable`   
Fetches available Bindings.  
`[get](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.bindings/get)` |  `GET /v1/{name=projects/*/locations/*/bindings/*}`   
Gets details of a single Binding.  
`[list](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.bindings/list)` |  `GET /v1/{parent=projects/*/locations/*}/bindings`   
Lists Bindings in a given project and location.  
`[patch](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.bindings/patch)` |  `PATCH /v1/{binding.name=projects/*/locations/*/bindings/*}`   
Updates the parameters of a single Binding.  
  
## REST Resource: [v1.projects.locations.endpoints](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.endpoints)

Methods  
---  
`[get](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.endpoints/get)` |  `GET /v1/{name=projects/*/locations/*/endpoints/*}`   
Gets details of a single Endpoint.  
`[list](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.endpoints/list)` |  `GET /v1/{parent=projects/*/locations/*}/endpoints`   
Lists Endpoints in a given project and location.  
  
## REST Resource: [v1.projects.locations.mcpServers](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.mcpServers)

Methods  
---  
`[get](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.mcpServers/get)` |  `GET /v1/{name=projects/*/locations/*/mcpServers/*}`   
Gets details of a single McpServer.  
`[list](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.mcpServers/list)` |  `GET /v1/{parent=projects/*/locations/*}/mcpServers`   
Lists McpServers in a given project and location.  
`[search](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.mcpServers/search)` |  `POST /v1/{parent=projects/*/locations/*}/mcpServers:search`   
Searches McpServers in a given project and location.  
  
## REST Resource: [v1.projects.locations.operations](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.operations/cancel)` |  `POST /v1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.operations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.operations/get)` |  `GET /v1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.operations/list)` |  `GET /v1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1.projects.locations.services](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.services)

Methods  
---  
`[create](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.services/create)` |  `POST /v1/{parent=projects/*/locations/*}/services`   
Creates a new Service in a given project and location.  
`[delete](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.services/delete)` |  `DELETE /v1/{name=projects/*/locations/*/services/*}`   
Deletes a single Service.  
`[get](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.services/get)` |  `GET /v1/{name=projects/*/locations/*/services/*}`   
Gets details of a single Service.  
`[list](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.services/list)` |  `GET /v1/{parent=projects/*/locations/*}/services`   
Lists Services in a given project and location.  
`[patch](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.services/patch)` |  `PATCH /v1/{service.name=projects/*/locations/*/services/*}`   
Updates the parameters of a single Service.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
