---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1Alpha/latest/Google.Cloud.Batch.V1Alpha.Runnable.Types.Barrier
title: Batch v1alpha API - Class Runnable.Types.Barrier (1.0.0-alpha35) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:59:27.267537+00:00
---

# Batch v1alpha API - Class Runnable.Types.Barrier (1.0.0-alpha35)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1Alpha/latest/Google.Cloud.Batch.V1Alpha.Runnable.Types.Barrier

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Batch v1alpha API - Class Runnable.Types.Barrier (1.0.0-alpha35) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-alpha35 (latest)  1.0.0-alpha34 
    
    
    public sealed class Runnable.Types.Barrier : IMessage<Runnable.Types.Barrier>, IEquatable<Runnable.Types.Barrier>, IDeepCloneable<Runnable.Types.Barrier>, IBufferMessage, IMessage

Reference documentation and code samples for the Batch v1alpha API class Runnable.Types.Barrier.

A barrier runnable automatically blocks the execution of subsequent runnables until all the tasks in the task group reach the barrier.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Runnable.Types.Barrier

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Runnable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1Alpha/latest/Google.Cloud.Batch.V1Alpha.Runnable)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1Alpha/latest/Google.Cloud.Batch.V1Alpha.Runnable.Types)[Barrier](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1Alpha/latest/Google.Cloud.Batch.V1Alpha.Runnable.Types.Barrier), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Runnable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1Alpha/latest/Google.Cloud.Batch.V1Alpha.Runnable)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1Alpha/latest/Google.Cloud.Batch.V1Alpha.Runnable.Types)[Barrier](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1Alpha/latest/Google.Cloud.Batch.V1Alpha.Runnable.Types.Barrier), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Runnable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1Alpha/latest/Google.Cloud.Batch.V1Alpha.Runnable)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1Alpha/latest/Google.Cloud.Batch.V1Alpha.Runnable.Types)[Barrier](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1Alpha/latest/Google.Cloud.Batch.V1Alpha.Runnable.Types.Barrier), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Batch.V1Alpha](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1Alpha/latest/Google.Cloud.Batch.V1Alpha)

## Assembly

Google.Cloud.Batch.V1Alpha.dll

## Constructors 

### Barrier()
    
    
    public Barrier()

### Barrier(Barrier)
    
    
    public Barrier(Runnable.Types.Barrier other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Runnable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1Alpha/latest/Google.Cloud.Batch.V1Alpha.Runnable)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1Alpha/latest/Google.Cloud.Batch.V1Alpha.Runnable.Types)[Barrier](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1Alpha/latest/Google.Cloud.Batch.V1Alpha.Runnable.Types.Barrier)`  
  
  
## Properties 

### Name
    
    
    public string Name { get; set; }

Barriers are identified by their index in runnable list. Names are not required, but if present should be an identifier.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
