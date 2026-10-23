---
url: https://docs.cloud.google.com/agent-registry/json-schemas/
title: JSON schemas \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:55:17.472749+00:00
---

# JSON schemas  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/json-schemas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Reference ](https://docs.cloud.google.com/agent-registry/apis)



Send feedback 

#  JSON schemas Stay organized with collections  Save and categorize content based on your preferences. 

When you manually register agents or Model Context Protocol (MCP) servers in Agent Registry by creating a `Service` resource, you provide JSON configuration files that declare their capabilities. Agent Registry validates these files against open source specifications before indexing them so that consumers can discover agent [A2A skills](https://docs.cloud.google.com/agent-registry/skills-architecture#standalone-vs-a2a) and MCP tools. Use the following JSON structures and examples to format your Agent Cards and MCP tool specifications.

## Agent Card schema

When registering an A2A-compliant agent, your `agent-card.json` payload must adhere to the official [Agent2Agent (A2A) specification](https://a2a-protocol.org/latest/specification/). The maximum file size for the specification file is 10 KB. The `skills` array fields support the keyword search index.

Agent Registry supports versions `1.0` and `0.3` of the A2A [Agent Card](https://agent2agent.info/docs/concepts/agentcard/). Select a version to view its JSON schema and field definitions:

###  Version 1.0 (recommended) 

For version `1.0` of A2A Agent Cards, the payload must adhere to the official A2A [v1.0 specification](https://github.com/a2aproject/A2A/blob/v1.0.1/specification/json/README.md). In this specification, you declare transport endpoints within a `supportedInterfaces` array:
    
    
    {
      "name": "string",
      "description": "string",
      "version": "string",
      "supportedInterfaces": [
        {
          "url": "string",
          "protocolBinding": "string",
          "protocolVersion": "string",
          "tenant": "string"
        }
      ],
      "capabilities": {
        "streaming": false,
        "pushNotifications": false,
        "extendedAgentCard": false
      },
      "defaultInputModes": [
        "text/plain"
      ],
      "defaultOutputModes": [
        "text/plain"
      ],
      "skills": [
        {
          "id": "string",
          "name": "string",
          "description": "string",
          "tags": [
            "string"
          ],
          "examples": [
            "string"
          ]
        }
      ]
    }
    

**Field definitions**

  * `name`: the human-readable name of the agent.
  * `description`: a high-level summary of the agent's purpose.
  * `version`: the version of the agent, for example, `1.0.0`.
  * `supportedInterfaces`: an array of supported transport and URL combinations. Each interface contains the following: 
    * `url`: the endpoint URL where this interface is reached.
    * `protocolBinding`: the protocol binding supported at this URL, for example, `HTTP+JSON`, `JSONRPC`, or `GRPC`.
    * `protocolVersion`: the A2A protocol version this interface exposes, for example, `1.0.0`.
    * `tenant` (optional): the identifier of the agent owner.
  * `capabilities` (optional): specifies supported operational capabilities such as the following: 
    * `extensions` (optional): an array of protocol extensions.
    * `streaming` (optional): a boolean indicating if the agent supports streaming responses.
    * `pushNotifications` (optional): a boolean indicating if push notifications are supported for task updates.
    * `extendedAgentCard` (optional): a boolean indicating if the agent provides an extended Agent Card when authenticated.
  * `defaultInputModes` (optional): an array of MIME types accepted as input.
  * `defaultOutputModes` (optional): an array of MIME types produced as output.
  * `skills`: an array of descriptive A2A skills the agent possesses: 
    * `id`: a unique programmatic identifier for the A2A skill.
    * `name`: a human-readable name for the A2A skill.
    * `description`: a detailed explanation of what the A2A skill does.
    * `tags`: an array of keyword strings used to categorize the A2A skill.
    * `examples`: an array of example prompts or scenarios this A2A skill handles.



###  Version 0.3 

For version `0.3` of A2A Agent Cards, the payload must adhere to the [v0.3.0 specification](https://github.com/a2aproject/A2A/blob/v0.3.0/specification/json/a2a.json). In this specification, the primary inference URL and protocol version are declared as top-level fields:
    
    
    {
      "name": "string",
      "description": "string",
      "version": "string",
      "protocolVersion": "string",
      "url": "string",
      "skills": [
        {
          "id": "string",
          "name": "string",
          "description": "string",
          "tags": [
            "string"
          ],
          "examples": [
            "string"
          ]
        }
      ],
      "capabilities": {
        "streaming": false,
        "pushNotifications": false,
        "stateTransitionHistory": false
      },
      "defaultInputModes": [
        "text/plain"
      ],
      "defaultOutputModes": [
        "text/plain"
      ]
    }
    

**Field definitions**

  * `name`: the human-readable name of the agent.
  * `description`: a high-level summary of the agent's purpose.
  * `version`: the version of the agent, for example, `1.0.2`.
  * `protocolVersion`: the version of the A2A protocol the agent implements. Because version `1.0` deprecates this top-level field, the value must be `0.3` or any `0.3` patch version, such as `0.3.1`, for this schema.
  * `url`: the endpoint URL where the agent can be reached.
  * `capabilities` (optional): an object specifying the agent's supported operational capabilities, such as `streaming`, `pushNotifications`, or `stateTransitionHistory`.
  * `defaultInputModes` (optional): an array of strings defining the default MIME types the agent accepts as input, for example, `["text/plain"]`.
  * `defaultOutputModes` (optional): an array of strings defining the default MIME types the agent produces as output, for example, `["text/plain"]`.
  * `skills`: an array of descriptive A2A skills the agent possesses: 
    * `id`: a unique programmatic identifier for the A2A skill.
    * `name`: a human-readable name for the A2A skill.
    * `description`: a detailed explanation of what the A2A skill does.
    * `tags`: an array of keyword strings used to categorize the A2A skill.
    * `examples`: an array of example prompts or scenarios this A2A skill handles.



## MCP tool schema

When registering an MCP server, your `toolspec.json` payload must include a list of tools that adhere to the [MCP `Tool` object schema](https://modelcontextprotocol.io/specification/2025-06-18/schema#tool).

The expected payload is a JSON object with a single `tools` field, exactly as it is returned by [the standard MCP tools or list request](https://modelcontextprotocol.io/specification/2025-06-18/schema#listtoolsresult). The maximum file size for this specification file is 10 KB.
    
    
    {
      "tools": [
        {
          "name": "string",
          "description": "string",
          "inputSchema": {
            "type": "object",
            "properties": {}
          },
          "annotations": {
            "title": "string",
            "readOnlyHint": false,
            "destructiveHint": true,
            "idempotentHint": false,
            "openWorldHint": true
          }
        }
      ]
    }
    

### Field definitions

  * `tools`: an array of tools provided by the server:

    * `name`: the programmatic identifier for the tool.
    * `description`: a human-readable explanation of the tool's purpose.
    * `inputSchema`: a JSON Schema object defining the expected parameters for the tool.
    * `annotations`: behavioral hints that guide how orchestrator agents interact with the tool:

      * `title`: a human-readable title for the tool.
      * `readOnlyHint`: if `true`, the tool only retrieves data and doesn't modify its environment. Default is `false`.
      * `destructiveHint`: if `true`, the tool performs operations that might cause permanent changes. Default is `true`.
      * `idempotentHint`: if `true`, calling the tool repeatedly has no additional effect. Default is `false`.
      * `openWorldHint`: if `true`, the tool interacts with external systems. Default is `true`.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
