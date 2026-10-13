---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Memory
title: Vertex AI v1beta1 API - Class Memory (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:17:52.504526+00:00
---

# Vertex AI v1beta1 API - Class Memory (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Memory

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class Memory (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public sealed class Memory : IMessage<Memory>, IEquatable<Memory>, IDeepCloneable<Memory>, IBufferMessage, IMessage

Reference documentation and code samples for the Vertex AI v1beta1 API class Memory.

A memory.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Memory

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Memory](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Memory), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Memory](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Memory), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Memory](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Memory), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Constructors 

### Memory()
    
    
    public Memory()

### Memory(Memory)
    
    
    public Memory(Memory other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Memory](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Memory)`  
  
  
## Properties 

### Context
    
    
    public string Context { get; set; }

Optional. Represents the context of the memory.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. Represents the timestamp when this Memory was created.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### Description
    
    
    public string Description { get; set; }

Optional. Represents the description of the Memory.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DisableMemoryRevisions
    
    
    public bool DisableMemoryRevisions { get; set; }

Optional. Input only. Indicates whether no revision will be created for this request.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### DisplayName
    
    
    public string DisplayName { get; set; }

Optional. Represents the display name of the Memory.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ExpirationCase
    
    
    public Memory.ExpirationOneofCase ExpirationCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[Memory](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Memory)[ExpirationOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Memory.ExpirationOneofCase)` |   
  
### ExpireTime
    
    
    public Timestamp ExpireTime { get; set; }

Optional. Represents the timestamp of when this resource is considered expired. This is _always_ provided on output when `expiration` is set on input, regardless of whether `expire_time` or `ttl` was provided.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### Fact
    
    
    public string Fact { get; set; }

Optional. Represents semantic knowledge extracted from the source content.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### HasDisableMemoryRevisions
    
    
    public bool HasDisableMemoryRevisions { get; }

Gets whether the "disable_memory_revisions" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### MemoryName
    
    
    public MemoryName MemoryName { get; set; }

[MemoryName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MemoryName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Memory#Google_Cloud_AIPlatform_V1Beta1_Memory_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[MemoryName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MemoryName)` |   
  
### MemoryType
    
    
    public MemoryType MemoryType { get; set; }

Optional. Represents the type of the memory. If not set, the `NATURAL_LANGUAGE_COLLECTION` type is used. If `STRUCTURED_COLLECTION` or `STRUCTURED_PROFILE` is used, then `structured_data` must be provided.

**Property Value**  
---  
**Type** | **Description**  
`[MemoryType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MemoryType)` |   
  
### Metadata
    
    
    public MapField<string, MemoryMetadataValue> Metadata { get; }

Optional. Represents user-provided metadata for the Memory. This information was provided when creating, updating, or generating the Memory. It was not generated by Memory Bank.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[MemoryMetadataValue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MemoryMetadataValue)` |   
  
### Name
    
    
    public string Name { get; set; }

Identifier. Represents the resource name of the Memory. Format: `projects/{project}/locations/{location}/reasoningEngines/{reasoning_engine}/memories/{memory}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### RevisionExpirationCase
    
    
    public Memory.RevisionExpirationOneofCase RevisionExpirationCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[Memory](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Memory)[RevisionExpirationOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Memory.RevisionExpirationOneofCase)` |   
  
### RevisionExpireTime
    
    
    public Timestamp RevisionExpireTime { get; set; }

Optional. Input only. Represents the timestamp of when the revision is considered expired. If not set, the memory revision will be kept until manually deleted.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### RevisionLabels
    
    
    public MapField<string, string> RevisionLabels { get; }

Optional. Input only. Represents the labels to apply to the Memory Revision created as a result of this request.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### RevisionTtl
    
    
    public Duration RevisionTtl { get; set; }

Optional. Input only. Represents the TTL for the revision. The expiration time is computed: now + TTL.

**Property Value**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)` |   
  
### Scope
    
    
    public MapField<string, string> Scope { get; }

Required. Immutable. Represents the scope of the Memory. Memories are isolated within their scope. The scope is defined when creating or generating memories. Scope values cannot contain the wildcard character '*'.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### StructuredContent
    
    
    public Memory.Types.StructuredContent StructuredContent { get; set; }

Optional. Represents the structured content of the memory.

**Property Value**  
---  
**Type** | **Description**  
`[Memory](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Memory)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Memory.Types)[StructuredContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Memory.Types.StructuredContent)` |   
  
### Topics
    
    
    public RepeatedField<MemoryTopicId> Topics { get; }

Optional. Represents the Topics of the Memory.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[MemoryTopicId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MemoryTopicId)` |   
  
### Ttl
    
    
    public Duration Ttl { get; set; }

Optional. Input only. Represents the TTL for this resource. The expiration time is computed: now + TTL.

**Property Value**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)` |   
  
### UpdateTime
    
    
    public Timestamp UpdateTime { get; set; }

Output only. Represents the timestamp when this Memory was most recently updated.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
