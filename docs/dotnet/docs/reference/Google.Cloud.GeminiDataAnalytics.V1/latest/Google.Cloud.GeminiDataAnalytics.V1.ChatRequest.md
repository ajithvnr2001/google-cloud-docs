---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.ChatRequest
title: Data Analytics API with Gemini v1 API - Class ChatRequest (2.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:46:37.785281+00:00
---

# Data Analytics API with Gemini v1 API - Class ChatRequest (2.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.ChatRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Data Analytics API with Gemini v1 API - Class ChatRequest (2.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.0.0 (latest)  1.1.0  1.0.0 
    
    
    public sealed class ChatRequest : IMessage<ChatRequest>, IEquatable<ChatRequest>, IDeepCloneable<ChatRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Data Analytics API with Gemini v1 API class ChatRequest.

Request for Chat.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ChatRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ChatRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.ChatRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ChatRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.ChatRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ChatRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.ChatRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.GeminiDataAnalytics.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1)

## Assembly

Google.Cloud.GeminiDataAnalytics.V1.dll

## Constructors 

### ChatRequest()
    
    
    public ChatRequest()

### ChatRequest(ChatRequest)
    
    
    public ChatRequest(ChatRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ChatRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.ChatRequest)`  
  
  
## Properties 

### ClientManagedResourceContext
    
    
    public ClientManagedResourceContext ClientManagedResourceContext { get; set; }

Optional. Context with client managed resources. Some clients may not use GDA managed resources including conversations and agents, instead they create and manage their own conversations and agents resources.

**Property Value**  
---  
**Type** | **Description**  
`[ClientManagedResourceContext](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.ClientManagedResourceContext)` |   
  
### ContextProviderCase
    
    
    public ChatRequest.ContextProviderOneofCase ContextProviderCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[ChatRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.ChatRequest)[ContextProviderOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.ChatRequest.ContextProviderOneofCase)` |   
  
### ConversationReference
    
    
    public ConversationReference ConversationReference { get; set; }

Optional. Reference to a persisted conversation and agent context. Use this to chat with an Agent using managed conversation persistence.

**Property Value**  
---  
**Type** | **Description**  
`[ConversationReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.ConversationReference)` |   
  
### Credentials
    
    
    public Credentials Credentials { get; set; }

Optional. The credentials to use when calling the data source(s) specified in the context.

This field can be used to provide credentials for various data sources. For example, when connecting to Looker, it currently supports both OAuth token and API key-based credentials, as described in [Authentication with an SDK](https://cloud.google.com/looker/docs/api-auth#authentication_with_an_sdk).

**Property Value**  
---  
**Type** | **Description**  
`[Credentials](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.Credentials)` |   
  
### DataAgentContext
    
    
    public DataAgentContext DataAgentContext { get; set; }

Optional. Context for the chat request. Use this to chat with an Agent statelessly, without managed conversation persistence.

**Property Value**  
---  
**Type** | **Description**  
`[DataAgentContext](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.DataAgentContext)` |   
  
### DatasourceSettingsCase
    
    
    public ChatRequest.DatasourceSettingsOneofCase DatasourceSettingsCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[ChatRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.ChatRequest)[DatasourceSettingsOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.ChatRequest.DatasourceSettingsOneofCase)` |   
  
### InlineContext
    
    
    public Context InlineContext { get; set; }

Optional. Inline context for the chat request. Use this to chat statelessly (without managed conversation persistence and without an Agent) by passing all context inline.

**Property Value**  
---  
**Type** | **Description**  
`[Context](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.Context)` |   
  
### LookerSettings
    
    
    public LookerSettings LookerSettings { get; set; }

Optional. Looker specific settings.

**Property Value**  
---  
**Type** | **Description**  
`[LookerSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.LookerSettings)` |   
  
### Messages
    
    
    public RepeatedField<Message> Messages { get; }

Required. Content of current conversation.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Message](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.Message)` |   
  
### Model
    
    
    public ChatRequest.Types.Model Model { get; set; }

Optional. The model to use for the agent loop when processing the request. This setting only has an effect when context.options.model is not set.

**Property Value**  
---  
**Type** | **Description**  
`[ChatRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.ChatRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.ChatRequest.Types)[Model](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.ChatRequest.Types.Model)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The parent value for chat request. Pattern: `projects/{project}/locations/{location}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ThinkingMode
    
    
    public ChatRequest.Types.ThinkingMode ThinkingMode { get; set; }

Optional. The thinking mode to use for the agent loop. Defaults to THINKING_MODE_UNSPECIFIED if not specified.

**Property Value**  
---  
**Type** | **Description**  
`[ChatRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.ChatRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.ChatRequest.Types)[ThinkingMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.ChatRequest.Types.ThinkingMode)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
