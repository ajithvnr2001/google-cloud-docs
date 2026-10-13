---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RubricBasedInstructionFollowingInstance
title: Vertex AI v1beta1 API - Class RubricBasedInstructionFollowingInstance (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:10:10.595568+00:00
---

# Vertex AI v1beta1 API - Class RubricBasedInstructionFollowingInstance (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RubricBasedInstructionFollowingInstance

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class RubricBasedInstructionFollowingInstance (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public sealed class RubricBasedInstructionFollowingInstance : IMessage<RubricBasedInstructionFollowingInstance>, IEquatable<RubricBasedInstructionFollowingInstance>, IDeepCloneable<RubricBasedInstructionFollowingInstance>, IBufferMessage, IMessage

Reference documentation and code samples for the Vertex AI v1beta1 API class RubricBasedInstructionFollowingInstance.

Instance for RubricBasedInstructionFollowing metric - one instance corresponds to one row in an evaluation dataset.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > RubricBasedInstructionFollowingInstance

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[RubricBasedInstructionFollowingInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RubricBasedInstructionFollowingInstance), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[RubricBasedInstructionFollowingInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RubricBasedInstructionFollowingInstance), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[RubricBasedInstructionFollowingInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RubricBasedInstructionFollowingInstance), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Constructors 

### RubricBasedInstructionFollowingInstance()
    
    
    public RubricBasedInstructionFollowingInstance()

### RubricBasedInstructionFollowingInstance(RubricBasedInstructionFollowingInstance)
    
    
    public RubricBasedInstructionFollowingInstance(RubricBasedInstructionFollowingInstance other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[RubricBasedInstructionFollowingInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RubricBasedInstructionFollowingInstance)`  
  
  
## Properties 

### HasJsonInstance
    
    
    public bool HasJsonInstance { get; }

Gets whether the "json_instance" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### InstanceCase
    
    
    public RubricBasedInstructionFollowingInstance.InstanceOneofCase InstanceCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[RubricBasedInstructionFollowingInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RubricBasedInstructionFollowingInstance)[InstanceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RubricBasedInstructionFollowingInstance.InstanceOneofCase)` |   
  
### JsonInstance
    
    
    public string JsonInstance { get; set; }

Required. Instance specified as a json string. String key-value pairs are expected in the json_instance to render RubricBasedInstructionFollowing prompt templates.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
