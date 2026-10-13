---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.Example
title: Gemini Enterprise for Customer Experience v1 API - Class Example (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:24:40.954484+00:00
---

# Gemini Enterprise for Customer Experience v1 API - Class Example (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.Example

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Gemini Enterprise for Customer Experience v1 API - Class Example (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta04 
    
    
    public sealed class Example : IMessage<Example>, IEquatable<Example>, IDeepCloneable<Example>, IBufferMessage, IMessage

Reference documentation and code samples for the Gemini Enterprise for Customer Experience v1 API class Example.

An example represents a sample conversation between the user and the agent(s).

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Example

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.Example), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.Example), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.Example), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Ces.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1)

## Assembly

Google.Cloud.Ces.V1.dll

## Constructors 

### Example()
    
    
    public Example()

### Example(Example)
    
    
    public Example(Example other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.Example)`  
  
  
## Properties 

### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. Timestamp when the example was created.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### Description
    
    
    public string Description { get; set; }

Optional. Human-readable description of the example.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DisplayName
    
    
    public string DisplayName { get; set; }

Required. Display name of the example.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### EntryAgent
    
    
    public string EntryAgent { get; set; }

Optional. The agent that initially handles the conversation. If not specified, the example represents a conversation that is handled by the root agent. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### EntryAgentAsAgentName
    
    
    public AgentName EntryAgentAsAgentName { get; set; }

[AgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.AgentName)-typed view over the [EntryAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.Example#Google_Cloud_Ces_V1_Example_EntryAgent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[AgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.AgentName)` |   
  
### Etag
    
    
    public string Etag { get; set; }

Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ExampleName
    
    
    public ExampleName ExampleName { get; set; }

[ExampleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.ExampleName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.Example#Google_Cloud_Ces_V1_Example_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ExampleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.ExampleName)` |   
  
### Invalid
    
    
    public bool Invalid { get; set; }

Output only. The example may become invalid if referencing resources are deleted. Invalid examples will not be used as few-shot examples.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Messages
    
    
    public RepeatedField<Message> Messages { get; }

Optional. The collection of messages that make up the conversation.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Message](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.Message)` |   
  
### Name
    
    
    public string Name { get; set; }

Identifier. The unique identifier of the example. Format: `projects/{project}/locations/{location}/apps/{app}/examples/{example}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### UpdateTime
    
    
    public Timestamp UpdateTime { get; set; }

Output only. Timestamp when the example was last updated.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
