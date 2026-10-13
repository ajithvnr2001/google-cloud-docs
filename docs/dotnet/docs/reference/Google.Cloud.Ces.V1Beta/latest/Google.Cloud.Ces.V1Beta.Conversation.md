---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation
title: Gemini Enterprise for Customer Experience v1beta API - Class Conversation (1.0.0-beta09) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:01.032554+00:00
---

# Gemini Enterprise for Customer Experience v1beta API - Class Conversation (1.0.0-beta09)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Gemini Enterprise for Customer Experience v1beta API - Class Conversation (1.0.0-beta09) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta09 (latest)  1.0.0-beta08 
    
    
    public sealed class Conversation : IMessage<Conversation>, IEquatable<Conversation>, IDeepCloneable<Conversation>, IBufferMessage, IMessage

Reference documentation and code samples for the Gemini Enterprise for Customer Experience v1beta API class Conversation.

A conversation represents an interaction between an end user and the CES app.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Conversation

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Ces.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta)

## Assembly

Google.Cloud.Ces.V1Beta.dll

## Constructors 

### Conversation()
    
    
    public Conversation()

### Conversation(Conversation)
    
    
    public Conversation(Conversation other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation)`  
  
  
## Properties 

### AppVersion
    
    
    public string AppVersion { get; set; }

Output only. The version of the app used for processing the conversation. Format: `projects/{project}/locations/{location}/apps/{app}/versions/{version}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### AppVersionAsAppVersionName
    
    
    public AppVersionName AppVersionAsAppVersionName { get; set; }

[AppVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersionName)-typed view over the [AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation#Google_Cloud_Ces_V1Beta_Conversation_AppVersion) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[AppVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersionName)` |   
  
### ChannelType
    
    
    [Obsolete]
    public Conversation.Types.ChannelType ChannelType { get; set; }

DEPRECATED. Please use [input_types][google.cloud.ces.v1beta.Conversation.input_types] instead.

**Property Value**  
---  
**Type** | **Description**  
`[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation.Types)[ChannelType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation.Types.ChannelType)` |   
  
### ConversationName
    
    
    public ConversationName ConversationName { get; set; }

[ConversationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ConversationName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation#Google_Cloud_Ces_V1Beta_Conversation_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ConversationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ConversationName)` |   
  
### Deployment
    
    
    public string Deployment { get; set; }

Output only. The deployment of the app used for processing the conversation. Format: `projects/{project}/locations/{location}/apps/{app}/deployments/{deployment}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DeploymentAsDeploymentName
    
    
    public DeploymentName DeploymentAsDeploymentName { get; set; }

[DeploymentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeploymentName)-typed view over the [Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation#Google_Cloud_Ces_V1Beta_Conversation_Deployment) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[DeploymentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeploymentName)` |   
  
### EndTime
    
    
    public Timestamp EndTime { get; set; }

Output only. Timestamp when the conversation was completed.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### EntryAgent
    
    
    public string EntryAgent { get; set; }

Output only. The agent that initially handles the conversation. If not specified, the conversation is handled by the root agent. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### EntryAgentAsAgentName
    
    
    public AgentName EntryAgentAsAgentName { get; set; }

[AgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentName)-typed view over the [EntryAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation#Google_Cloud_Ces_V1Beta_Conversation_EntryAgent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[AgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentName)` |   
  
### InputTypes
    
    
    public RepeatedField<Conversation.Types.InputType> InputTypes { get; }

Output only. The input types of the conversation.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation.Types)[InputType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation.Types.InputType)` |   
  
### LanguageCode
    
    
    public string LanguageCode { get; set; }

Output only. The language code of the conversation.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Messages
    
    
    [Obsolete]
    public RepeatedField<Message> Messages { get; }

Deprecated. Use turns instead.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Message](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Message)` |   
  
### Name
    
    
    public string Name { get; set; }

Identifier. The unique identifier of the conversation. Format: `projects/{project}/locations/{location}/apps/{app}/conversations/{conversation}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Source
    
    
    public Conversation.Types.Source Source { get; set; }

Output only. Indicate the source of the conversation.

**Property Value**  
---  
**Type** | **Description**  
`[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation.Types)[Source](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation.Types.Source)` |   
  
### StartTime
    
    
    public Timestamp StartTime { get; set; }

Output only. Timestamp when the conversation was created.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### TurnCount
    
    
    public int TurnCount { get; set; }

Output only. The number of turns in the conversation.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### Turns
    
    
    public RepeatedField<Conversation.Types.Turn> Turns { get; }

Required. The turns in the conversation.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation.Types)[Turn](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation.Types.Turn)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
