---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AgentConfig
title: Vertex AI v1beta1 API - Class AgentConfig (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:30:04.364749+00:00
---

# Vertex AI v1beta1 API - Class AgentConfig (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AgentConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class AgentConfig (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public sealed class AgentConfig : IMessage<AgentConfig>, IEquatable<AgentConfig>, IDeepCloneable<AgentConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the Vertex AI v1beta1 API class AgentConfig.

Represents configuration for an Agent.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AgentConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AgentConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AgentConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AgentConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AgentConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AgentConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AgentConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Constructors 

### AgentConfig()
    
    
    public AgentConfig()

### AgentConfig(AgentConfig)
    
    
    public AgentConfig(AgentConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AgentConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AgentConfig)`  
  
  
## Properties 

### AgentId
    
    
    public string AgentId { get; set; }

Required. Unique identifier of the agent. This ID is used to refer to this agent, e.g., in AgentEvent.author, or in the `sub_agents` field. It must be unique within the `agents` map.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### AgentType
    
    
    public string AgentType { get; set; }

Optional. The type or class of the agent (e.g., "LlmAgent", "RouterAgent", "ToolUseAgent"). Useful for the autorater to understand the expected behavior of the agent.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Description
    
    
    public string Description { get; set; }

Optional. A high-level description of the agent's role and responsibilities. Critical for evaluating if the agent is routing tasks correctly.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### HasAgentId
    
    
    public bool HasAgentId { get; }

Gets whether the "agent_id" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Instruction
    
    
    public string Instruction { get; set; }

Optional. Provides instructions for the LLM model, guiding the agent's behavior. Can be static or dynamic. Dynamic instructions can contain placeholders like {variable_name} that will be resolved at runtime using the `AgentEvent.state_delta` field.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SubAgents
    
    
    public RepeatedField<string> SubAgents { get; }

Optional. The list of valid agent IDs that this agent can delegate to. This defines the directed edges in the multi-agent system graph topology.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Tools
    
    
    public RepeatedField<Tool> Tools { get; }

Optional. The list of tools available to this agent.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Tool)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
