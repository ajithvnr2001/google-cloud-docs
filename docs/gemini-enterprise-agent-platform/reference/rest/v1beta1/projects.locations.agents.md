---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.agents
title: REST Resource: projects.locations.agents \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:33:51.475028+00:00
---

# REST Resource: projects.locations.agents  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.agents

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  REST Resource: projects.locations.agents Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: Agent

A Vertex agent contains instructions and configurations for the LLM to execute a certain task.

Fields  
  
`name` `string` Identifier. The resource name of the agent. Format: `projects/{project}/locations/{location}/agents/{agent}`. | `id` `string` Immutable. The user-specified id for the agent. This id becomes the final component of the agent resource name. If not provided, Agent Platform will generate a value for this id. The id can be up to 63 characters and must match the regular expression `[a-z]([a-z0-9-]{0,61}[a-z0-9])?`. | `created` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the agent was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `updated` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the agent was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `object` `string` Output only. The object type of the resource. For agents, the value is `agent`. | `base_agent` `string` Required. Immutable. The base agent for the agent. Supported values: * `antigravity-preview-05-2026`Immutable: `agents.patch` rejects a change, including clearing it. The kind of agent this is gets derived from this field when the agent is created and is recorded then; nothing recomputes it afterwards, so a later change would leave the agent described as one kind and behaving as another. Create a new agent instead. | `metadata` `map (key: string, value: string)` Optional. The metadata for the agent. | `description` `string` Optional. The description of the agent. | `system_instruction` `string` Optional. The instructions for the agent to follow. These instructions are passed to the LLM as a system instruction. | `tools[]` `object (`[AgentTool](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.agents#AgentTool)`)` Optional. The tools available to the agent. | `environment` `Union type`  
  
The environment configuration for the agent. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`base_environment` `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` Optional. The base environment configuration for the agent. Valid types:

  * A string value for the environment id, or `remote` for the default.
  * A struct value for the `environment_config`.

End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
      "name": string,
      "id": string,
      "created": string,
      "updated": string,
      "object": string,
      "base_agent": string,
      "metadata": {
        string: string,
        ...
      },
      "description": string,
      "system_instruction": string,
      "tools": [
        {
          object ([AgentTool](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.agents#AgentTool))
        }
      ],
    
      // environment
      "base_environment": value
      // Union type
    }  
  
## AgentTool

A tool provides a list of actions available to the `[Agent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.agents#Agent)` during the process of executing a task.

Example JSON for an MCP server tool: { "type": "mcpServer", "name": "my-mcp-server", "url": "https://api.example.com/mcp", "headers": { "Authorization": "Bearer token123" } }

Fields  
  
`type` `string` Required. The type of the tool. Supported types:

  * `code_execution`
  * `endpoint`
  * `filesystem`
  * `google_search`
  * `mcp_server`
  * `url_context`

| `name` `string` Optional. The tool's Google Cloud resource name, used to resolve the tool. Applicable when `type` is `mcp_server` or `endpoint` (a tool registered in Agent Registry), for example `projects/{project}/locations/{location}/.../mcpServers/{id}` or `projects/{project}/locations/{location}/.../endpoints/{id}`. | `url` `string` Optional. Fallback for the tool's runtime reference, consumed by `agents.create` to create the downstream AI App. Applicable when `type` is `mcp_server` or `endpoint`, and optional: the Agent service derives the runtime reference from `name` via Agent Registry (`GetMcpServer` / `GetEndpoint`), and reads this only when that lookup yields none. | `headers` `map (key: string, value: string)` Optional. The headers for the MCP server, such as for authentication. Only applicable when `type` is `mcp_server`. | JSON representation  
---  
      
    
    {
      "type": string,
      "name": string,
      "url": string,
      "headers": {
        string: string,
        ...
      }
    }  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.agents/create)`

|  Creates an agent.  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.agents/delete)`

|  Deletes an agent.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.agents/get)`

|  Retrieves an agent.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.agents/list)`

|  Lists the agents in a location that belong to the caller.  
  
### `[patch](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.agents/patch)`

|  Updates an agent.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-26 UTC."],[],[]] 
