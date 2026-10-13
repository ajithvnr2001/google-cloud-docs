---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent
title: Google Cloud Dialogflow v2 API - Class CompanionAgent (4.33.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:58:17.445373+00:00
---

# Google Cloud Dialogflow v2 API - Class CompanionAgent (4.33.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Dialogflow v2 API - Class CompanionAgent (4.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.33.0 (latest)  4.32.0  4.31.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.16.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.0  4.8.0  4.7.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0 
    
    
    public sealed class CompanionAgent : IMessage<CompanionAgent>, IEquatable<CompanionAgent>, IDeepCloneable<CompanionAgent>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Dialogflow v2 API class CompanionAgent.

Companion agent.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CompanionAgent

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dialogflow.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2)

## Assembly

Google.Cloud.Dialogflow.V2.dll

## Constructors 

### CompanionAgent()
    
    
    public CompanionAgent()

### CompanionAgent(CompanionAgent)
    
    
    public CompanionAgent(CompanionAgent other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent)`  
  
  
## Properties 

### CesToolSpecs
    
    
    public RepeatedField<CesToolSpec> CesToolSpecs { get; }

Optional. List of CES tool specs that the companion agent can choose from.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[CesToolSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CesToolSpec)` |   
  
### CompanionAgentName
    
    
    public CompanionAgentName CompanionAgentName { get; set; }

[CompanionAgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgentName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent#Google_Cloud_Dialogflow_V2_CompanionAgent_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[CompanionAgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgentName)` |   
  
### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. Creation time of this companion agent.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### Description
    
    
    public string Description { get; set; }

Optional. Description for the companion agent.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DisplayName
    
    
    public string DisplayName { get; set; }

Optional. Display name for the companion agent. Character limit is 63.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Identifier. The unique identifier of the companion agent. Format: `projects/{project}/locations/{location}/companionAgents/{companion_agent}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SkillConfigs
    
    
    public RepeatedField<CompanionAgent.Types.SkillConfig> SkillConfigs { get; }

Optional. List of skill configs for the companion agent. Allows at most one instance of each [SkillConfig][google.cloud.dialogflow.v2.CompanionAgent.SkillConfig] type.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent.Types)[SkillConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent.Types.SkillConfig)` |   
  
### ToolsetTools
    
    
    public RepeatedField<ToolsetTool> ToolsetTools { get; }

Optional. List of CES toolset specs that the companion agent can choose from.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[ToolsetTool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ToolsetTool)` |   
  
### UpdateTime
    
    
    public Timestamp UpdateTime { get; set; }

Output only. Update time of this companion agent.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
