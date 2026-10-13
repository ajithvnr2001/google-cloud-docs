---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPICheckpointConfig.Types.IteratorStrategy
title: Chronicle v1 API - Class CustomAPICheckpointConfig.Types.IteratorStrategy (1.1.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:06:51.400927+00:00
---

# Chronicle v1 API - Class CustomAPICheckpointConfig.Types.IteratorStrategy (1.1.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPICheckpointConfig.Types.IteratorStrategy

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Chronicle v1 API - Class CustomAPICheckpointConfig.Types.IteratorStrategy (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0 
    
    
    public sealed class CustomAPICheckpointConfig.Types.IteratorStrategy : IMessage<CustomAPICheckpointConfig.Types.IteratorStrategy>, IEquatable<CustomAPICheckpointConfig.Types.IteratorStrategy>, IDeepCloneable<CustomAPICheckpointConfig.Types.IteratorStrategy>, IBufferMessage, IMessage

Reference documentation and code samples for the Chronicle v1 API class CustomAPICheckpointConfig.Types.IteratorStrategy.

Use progress tokens provided by the API.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CustomAPICheckpointConfig.Types.IteratorStrategy

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CustomAPICheckpointConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPICheckpointConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPICheckpointConfig.Types)[IteratorStrategy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPICheckpointConfig.Types.IteratorStrategy), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CustomAPICheckpointConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPICheckpointConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPICheckpointConfig.Types)[IteratorStrategy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPICheckpointConfig.Types.IteratorStrategy), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CustomAPICheckpointConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPICheckpointConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPICheckpointConfig.Types)[IteratorStrategy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPICheckpointConfig.Types.IteratorStrategy), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Chronicle.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1)

## Assembly

Google.Cloud.Chronicle.V1.dll

## Constructors 

### IteratorStrategy()
    
    
    public IteratorStrategy()

### IteratorStrategy(IteratorStrategy)
    
    
    public IteratorStrategy(CustomAPICheckpointConfig.Types.IteratorStrategy other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CustomAPICheckpointConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPICheckpointConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPICheckpointConfig.Types)[IteratorStrategy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPICheckpointConfig.Types.IteratorStrategy)`  
  
  
## Properties 

### CheckpointValuePath
    
    
    public string CheckpointValuePath { get; set; }

Required. Enter the exact location within a log record where the checkpoint value (like a timestamp or ID) is found.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### CheckpointVariable
    
    
    public string CheckpointVariable { get; set; }

Required. Specify a custom name you assign to store and reference the checkpoint value between polling cycles.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
