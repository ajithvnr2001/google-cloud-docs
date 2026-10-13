---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent.Types.RemoteDialogflowAgent
title: Gemini Enterprise for Customer Experience v1beta API - Class Agent.Types.RemoteDialogflowAgent (1.0.0-beta09) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:19:31.938364+00:00
---

# Gemini Enterprise for Customer Experience v1beta API - Class Agent.Types.RemoteDialogflowAgent (1.0.0-beta09)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent.Types.RemoteDialogflowAgent

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Gemini Enterprise for Customer Experience v1beta API - Class Agent.Types.RemoteDialogflowAgent (1.0.0-beta09) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta09 (latest)  1.0.0-beta08 
    
    
    public sealed class Agent.Types.RemoteDialogflowAgent : IMessage<Agent.Types.RemoteDialogflowAgent>, IEquatable<Agent.Types.RemoteDialogflowAgent>, IDeepCloneable<Agent.Types.RemoteDialogflowAgent>, IBufferMessage, IMessage

Reference documentation and code samples for the Gemini Enterprise for Customer Experience v1beta API class Agent.Types.RemoteDialogflowAgent.

The agent which will transfer execution to a remote [Dialogflow CX](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent) agent. The Dialogflow agent will process subsequent user queries until the session ends or flow ends, and the control is transferred back to the parent CES agent.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Agent.Types.RemoteDialogflowAgent

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent.Types)[RemoteDialogflowAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent.Types.RemoteDialogflowAgent), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent.Types)[RemoteDialogflowAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent.Types.RemoteDialogflowAgent), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent.Types)[RemoteDialogflowAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent.Types.RemoteDialogflowAgent), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Ces.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta)

## Assembly

Google.Cloud.Ces.V1Beta.dll

## Constructors 

### RemoteDialogflowAgent()
    
    
    public RemoteDialogflowAgent()

### RemoteDialogflowAgent(RemoteDialogflowAgent)
    
    
    public RemoteDialogflowAgent(Agent.Types.RemoteDialogflowAgent other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent.Types)[RemoteDialogflowAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent.Types.RemoteDialogflowAgent)`  
  
  
## Properties 

### Agent
    
    
    public string Agent { get; set; }

Required. The [Dialogflow](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent) agent resource name. Format: `projects/{project}/locations/{location}/agents/{agent}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### AgentAsDialogflowAgentName
    
    
    public DialogflowAgentName AgentAsDialogflowAgentName { get; set; }

[DialogflowAgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DialogflowAgentName)-typed view over the [Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent.Types.RemoteDialogflowAgent#Google_Cloud_Ces_V1Beta_Agent_Types_RemoteDialogflowAgent_Agent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[DialogflowAgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DialogflowAgentName)` |   
  
### EnvironmentId
    
    
    public string EnvironmentId { get; set; }

Optional. The environment ID of the Dialogflow agent to be used for the agent execution. If not specified, the draft environment will be used.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### FlowId
    
    
    public string FlowId { get; set; }

Optional. The flow ID of the flow in the Dialogflow agent.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### InputVariableMapping
    
    
    public MapField<string, string> InputVariableMapping { get; }

Optional. The mapping of the app variables names to the Dialogflow session parameters names to be sent to the Dialogflow agent as input.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### LanguageCodeVariable
    
    
    public string LanguageCodeVariable { get; set; }

Optional. The name of the variable that contains the language code to be used for the Dialogflow session. If unspecified, the default language code of the Dialogflow agent will be used.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OutputVariableMapping
    
    
    public MapField<string, string> OutputVariableMapping { get; }

Optional. The mapping of the Dialogflow session parameters names to the app variables names to be sent back to the CES agent after the Dialogflow agent execution ends.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### RespectResponseInterruptionSettings
    
    
    public bool RespectResponseInterruptionSettings { get; set; }

Optional. Indicates whether to respect the message-level interruption settings configured in the Dialogflow agent.

  * If false: all response messages from the Dialogflow agent follow the app-level barge-in settings.
  * If true: only response messages with [`allow_playback_interruption`](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#text) set to true will be interruptable, all other messages follow the app-level barge-in settings.



**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
