---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.agents/list/
title: Method: agents.list \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T04:27:47.985320+00:00
---

# Method: agents.list  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.agents/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: agents.list Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.agents.list

Lists the agents in a location that belong to the caller.

An agent belongs to the end user recorded as its owner when it was created, so the response holds that caller's agents and no others. It is empty for a caller that is not an end user, and an agent with no recorded owner is listed for nobody.

### Endpoint

get  `https://{service-endpoint}/v1beta1/{parent}/agents`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`parent` `string` Required. The resource name of the location to list agents from. Format: `projects/{project}/locations/{location}`.

### Query parameters

| `pageSize` `integer` Optional. The maximum number of agents to return. The service may return fewer than this value. The maximum page size is 100; values above 100 will be coerced to 100. If unspecified, the default page size is 10. | `pageToken` `string` Optional. A page token, received from a previous `[AgentService.ListAgents](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.agents/list#google.cloud.aiplatform.v1beta1.AgentService.ListAgents)` call. Provide this to retrieve the subsequent page. | `filter` `string` Optional. An [AIP-160](https://google.aip.dev/160) filter over the returned agents. An empty filter returns the unfiltered collection.Supported fields, and the operators each accepts:

  * `created`
  * `updated`
  * `baseAgent`
  * `metadata.agent_type`

`created` and `updated` are timestamps and take an RFC-3339 value, for example `2026-08-01T00:00:00Z`. Supported operators: `=`, `!=`, `<`, `>`, `<=`, `>=`, `:`, `AND`, `OR`, `NOT` (equivalently `-`), and parentheses. Note that `OR` binds more tightly than `AND`, so `a AND b OR c` means `a AND (b OR c)`; parentheses are recommended, not required.`metadata.agent_type` accepts only the value `"default_agent"`, matched exactly: `metadata.agent_type:"default_agent"` selects the caller's default agent, of which there is at most one, and the negated form selects the rest. Any other value is `INVALID_ARGUMENT` rather than an empty page -- `metadata` is an opaque blob, so only this one marker is indexed, and the server cannot answer a question about the others. An agent designated before the server began recording the marker is not matched by the positive form; there is no backfill.`baseAgent` accepts `=` and `!=` against the value an agent was created with, and selects only among the agents you own: an agent that belongs to the project rather than to a user is never returned by a filter naming it, including the negated form. An agent created before the server began recording the value is not matched either.Example: `created > "2026-08-01T00:00:00Z" AND updated < "2026-08-09T00:00:00Z"`.IMPORTANT -- `baseAgent` and `metadata.agent_type` select only among the agents you own. An agent that belongs to the project rather than to a user is never returned by a filter naming either of them, including a negated one: `baseAgent != "some-value"` returns your matching agents and no project-owned agents at all. Filtering on `created` or `updated` alone is unaffected and still spans both. If you want every agent in the project, do not filter on these two fields.Not supported: any field other than those listed above, wildcards other than `field:*`, bare literals with no field name, functions, and the regular-expression operators `=~` and `!~`. A filter that names an unsupported field, exceeds 1000 characters, or nests parentheses more than 5 deep fails with `INVALID_ARGUMENT`. | `orderBy` `string` Optional. A comma-separated list of fields to order by. Supported fields:

  * `created`
  * `updated`

Use `desc` after a field name for descending order. Example: `created desc`.

### Request body

The request body must be empty.

### Response body

Response message for `[AgentService.ListAgents](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.agents/list#google.cloud.aiplatform.v1beta1.AgentService.ListAgents)`. If successful, the response body contains data with the following structure: | Fields  
  
`agents[]` `object (`[Agent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.agents#Agent)`)` The agents matching the request. | `nextPageToken` `string` A token to retrieve the next page of results. Pass this value as `[ListAgentsRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.agents/list#body.QUERY_PARAMETERS.page_token)` in a subsequent call. | JSON representation  
---  
      
    
    {
      "agents": [
        {
          object ([Agent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.agents#Agent))
        }
      ],
      "nextPageToken": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-02 UTC."],[],[]] 
