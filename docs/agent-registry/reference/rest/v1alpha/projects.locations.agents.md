---
url: https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.agents
title: REST Resource: projects.locations.agents \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:06:37.084313+00:00
---

# REST Resource: projects.locations.agents  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.agents

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Reference ](https://docs.cloud.google.com/agent-registry/apis)



Send feedback 

#  REST Resource: projects.locations.agents Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Agent
    * JSON representation
  * Protocol
    * JSON representation
  * Type
  * Skill
    * JSON representation
  * Card
    * JSON representation
  * Type
  * Methods



## Resource: Agent

Represents an Agent. "A2A" below refers to the Agent-to-Agent protocol.

JSON representation  
---  
      
    
    {
      "name": string,
      "agentId": string,
      "location": string,
      "displayName": string,
      "description": string,
      "version": string,
      "protocols": [
        {
          object ([Protocol](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.agents#Protocol))
        }
      ],
      "skills": [
        {
          object ([Skill](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.agents#Skill))
        }
      ],
      "uid": string,
      "createTime": string,
      "updateTime": string,
      "attributes": {
        string: {
          object
        },
        ...
      },
      "card": {
        object ([Card](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.agents#Card))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of an Agent. Format: `projects/{project}/locations/{location}/agents/{agent}`.  
`agentId` |  `string` Output only. A stable, globally unique identifier for agents.  
`location` |  `string` Output only. The location where agent is hosted. The value is defined by the hosting environment (i.e. cloud provider).  
`displayName` |  `string` Output only. The display name of the agent, often obtained from the A2A Agent Card.  
`description` |  `string` Output only. The description of the Agent, often obtained from the A2A Agent Card. Empty if Agent Card has no description.  
`version` |  `string` Output only. The version of the Agent, often obtained from the A2A Agent Card. Empty if Agent Card has no version or agent is not an A2A Agent.  
`protocols[]` |  `object (`[Protocol](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.agents#Protocol)`)` Output only. The connection details for the Agent.  
`skills[]` |  `object (`[Skill](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.agents#Skill)`)` Output only. Skills the agent possesses, often obtained from the A2A Agent Card.  
`uid` |  `string` Output only. A universally unique identifier for the Agent.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Create time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Update time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`attributes` |  `map (key: string, value: object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format))` Output only. Attributes of the Agent. Valid values:

  * `agentregistry.googleapis.com/system/Framework`: {"framework": "google-adk"} - the agent framework used to develop the Agent. Example values: "google-adk", "langchain", "custom".
  * `agentregistry.googleapis.com/system/RuntimeIdentity`: {"principal": "principal://..."} - the runtime identity associated with the Agent.
  * `agentregistry.googleapis.com/system/RuntimeReference`: {"uri": "//..."}
  * the URI of the underlying resource hosting the Agent, for example, the Reasoning Engine URI.

An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`card` |  `object (`[Card](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.agents#Card)`)` Output only. Full Agent Card payload, when available.  
  
## Protocol

Represents the protocol of an Agent.

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.agents#Type)),
      "protocolVersion": string,
      "interfaces": [
        {
          object ([Interface](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/Interface))
        }
      ]
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.agents#Type)`)` Output only. The type of the protocol.  
`protocolVersion` |  `string` Output only. The version of the protocol, for example, the A2A Agent Card version.  
`interfaces[]` |  `object (`[Interface](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/Interface)`)` Output only. The connection details for the Agent.  
  
## Type

The type of the protocol.

Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified type.  
`A2A_AGENT` | The interfaces point to an A2A Agent following the A2A specification.  
`CUSTOM` | Agent does not follow any standard protocol.  
  
## Skill

Represents the skills of an Agent.

JSON representation  
---  
      
    
    {
      "id": string,
      "name": string,
      "description": string,
      "tags": [
        string
      ],
      "examples": [
        string
      ]
    }  
  
Fields  
---  
`id` |  `string` Output only. A unique identifier for the agent's skill.  
`name` |  `string` Output only. A human-readable name for the agent's skill.  
`description` |  `string` Output only. A more detailed description of the skill.  
`tags[]` |  `string` Output only. Keywords describing the skill.  
`examples[]` |  `string` Output only. Example prompts or scenarios this skill can handle.  
  
## Card

Full Agent Card payload, often obtained from the A2A Agent Card.

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.agents#Type_1)),
      "content": {
        object
      }
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.agents#Type_1)`)` Output only. The type of agent card.  
`content` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Output only. The content of the agent card.  
  
## Type

Represents the type of the agent card.

Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified type.  
`A2A_AGENT_CARD` | Indicates that the card is an A2A Agent Card.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.agents/get)`

|  Gets details of a single Agent.  
  
### `[list](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.agents/list)`

|  Lists Agents in a given project and location.  
  
### `[search](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.agents/search)`

|  Searches Agents in a given project and location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
