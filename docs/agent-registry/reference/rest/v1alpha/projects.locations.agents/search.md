---
url: https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.agents/search/
title: Method: projects.locations.agents.search \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:06:44.512636+00:00
---

# Method: projects.locations.agents.search  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.agents/search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Reference ](https://docs.cloud.google.com/agent-registry/apis)



Send feedback 

#  Method: projects.locations.agents.search Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Searches Agents in a given project and location.

### HTTP request

`POST https://agentregistry.googleapis.com/v1alpha/{parent=projects/*/locations/*}/agents:search`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Parent value for SearchAgentsRequest. Format: `projects/{project}/locations/{location}`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "searchString": string,
      "pageSize": integer,
      "pageToken": string
    }  
  
Fields  
---  
`searchString` |  `string` Optional. Search criteria used to select the Agents to return. If no search criteria is specified then all accessible Agents will be returned.Search expressions can be used to restrict results based upon searchable fields, where the operators can be used along with the suffix wildcard symbol `*`. See [instructions](https://docs.cloud.google.com/agent-registry/search-agents-and-tools) for more details.Allowed operators: `=`, `:`, `NOT`, `AND`, `OR`, and `()`.Searchable fields: | Field  | `=` | `:` | `*` | Keyword Search   
---|---|---|---|---  
agentId  | Yes  | Yes  | Yes  | Included   
name  | No  | Yes  | Yes  | Included   
displayName  | No  | Yes  | Yes  | Included   
description  | No  | Yes  | No  | Included   
skills  | No  | Yes  | No  | Included   
skills.id  | No  | Yes  | No  | Included   
skills.name  | No  | Yes  | No  | Included   
skills.description  | No  | Yes  | No  | Included   
skills.tags  | No  | Yes  | No  | Included   
skills.examples  | No  | Yes  | No  | Included   
  
Examples:

  * `agentId="urn:agent:projects-123:projects:123:locations:us-central1:aiplatform:reasoningEngines:1234"` to find the agent with the specified agent ID.
  * `name:important` to find agents whose name contains `important` as a word.
  * `displayName:works*` to find agents whose display name contains words that start with `works`.
  * `skills.tags:test` to find agents whose skills tags contain `test`.
  * `planner OR booking` to find agents whose metadata contains the words `planner` or `booking`.

  
`pageSize` |  `integer` Optional. The maximum number of search results to return per page. The page size is capped at `100`, even if a larger value is specified. A negative value will result in an `INVALID_ARGUMENT` error. If unspecified or set to `0`, a default value of `20` will be used. The server may return fewer results than requested.  
`pageToken` |  `string` Optional. If present, retrieve the next batch of results from the preceding call to this method. `pageToken` must be the value of `nextPageToken` from the previous response. The values of all other method parameters, must be identical to those in the previous call.  
  
### Response body

Message for response to searching Agents

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "agents": [
        {
          object ([Agent](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.agents#Agent))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`agents[]` |  `object (`[Agent](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.agents#Agent)`)` A list of Agents that match the `searchString`.  
`nextPageToken` |  `string` If there are more results than those appearing in this response, then `nextPageToken` is included. To get the next set of results, call this method again using the value of `nextPageToken` as `pageToken`.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/agentregistry.read-write`
  * `https://www.googleapis.com/auth/agentregistry.read-only`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `agentregistry.agents.search`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
