---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.SystemMessage
title: Data Analytics API with Gemini v1 API - Class SystemMessage (2.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:39:26.831450+00:00
---

# Data Analytics API with Gemini v1 API - Class SystemMessage (2.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.SystemMessage

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Data Analytics API with Gemini v1 API - Class SystemMessage (2.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.0.0 (latest)  1.1.0  1.0.0 
    
    
    public sealed class SystemMessage : IMessage<SystemMessage>, IEquatable<SystemMessage>, IDeepCloneable<SystemMessage>, IBufferMessage, IMessage

Reference documentation and code samples for the Data Analytics API with Gemini v1 API class SystemMessage.

A message from the system in response to the user. This message can also be a message from the user as historical context for multi-turn conversations with the system.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SystemMessage

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[SystemMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.SystemMessage), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[SystemMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.SystemMessage), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[SystemMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.SystemMessage), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.GeminiDataAnalytics.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1)

## Assembly

Google.Cloud.GeminiDataAnalytics.V1.dll

## Constructors 

### SystemMessage()
    
    
    public SystemMessage()

### SystemMessage(SystemMessage)
    
    
    public SystemMessage(SystemMessage other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[SystemMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.SystemMessage)`  
  
  
## Properties 

### Analysis
    
    
    public AnalysisMessage Analysis { get; set; }

A message produced during analysis.

**Property Value**  
---  
**Type** | **Description**  
`[AnalysisMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.AnalysisMessage)` |   
  
### Chart
    
    
    public ChartMessage Chart { get; set; }

A message produced during chart generation.

**Property Value**  
---  
**Type** | **Description**  
`[ChartMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.ChartMessage)` |   
  
### Citation
    
    
    public Citation Citation { get; set; }

Output only. Citation information for the system message.

**Property Value**  
---  
**Type** | **Description**  
`[Citation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.Citation)` |   
  
### Data
    
    
    public DataMessage Data { get; set; }

A message produced during data retrieval.

**Property Value**  
---  
**Type** | **Description**  
`[DataMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.DataMessage)` |   
  
### Error
    
    
    public ErrorMessage Error { get; set; }

An error message.

**Property Value**  
---  
**Type** | **Description**  
`[ErrorMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.ErrorMessage)` |   
  
### ExampleQueries
    
    
    public ExampleQueries ExampleQueries { get; set; }

Optional. A message containing example queries.

**Property Value**  
---  
**Type** | **Description**  
`[ExampleQueries](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.ExampleQueries)` |   
  
### GroupId
    
    
    public int GroupId { get; set; }

Identifies the group that the event belongs to. Similar events are deemed to be logically relevant to each other and should be shown together in the UI.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### HasGroupId
    
    
    public bool HasGroupId { get; }

Gets whether the "group_id" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### KindCase
    
    
    public SystemMessage.KindOneofCase KindCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[SystemMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.SystemMessage)[KindOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.SystemMessage.KindOneofCase)` |   
  
### Schema
    
    
    public SchemaMessage Schema { get; set; }

A message produced during schema resolution.

**Property Value**  
---  
**Type** | **Description**  
`[SchemaMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.SchemaMessage)` |   
  
### Text
    
    
    public TextMessage Text { get; set; }

A direct natural language response to the user message.

**Property Value**  
---  
**Type** | **Description**  
`[TextMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.TextMessage)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
