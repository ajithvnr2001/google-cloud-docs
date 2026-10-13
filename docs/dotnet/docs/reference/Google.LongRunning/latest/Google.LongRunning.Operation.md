---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation
title: Google.LongRunning - Class Operation (3.5.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:22:47.554367+00:00
---

# Google.LongRunning - Class Operation (3.5.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google.LongRunning - Class Operation (3.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.5.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation)
  * [ 3.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/3.4.0/Google.LongRunning.Operation)
  * [ 3.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/3.3.0/Google.LongRunning.Operation)
  * [ 3.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/3.2.0/Google.LongRunning.Operation)
  * [ 3.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/3.1.0/Google.LongRunning.Operation)
  * [ 3.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/3.0.0/Google.LongRunning.Operation)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/2.3.0/Google.LongRunning.Operation)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/2.2.0/Google.LongRunning.Operation)


    
    
    public sealed class Operation : IMessage<Operation>, IEquatable<Operation>, IDeepCloneable<Operation>, IBufferMessage, IMessage

Reference documentation and code samples for the Google.LongRunning class Operation.

This resource represents a long-running operation that is the result of a network API call.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Operation

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning)

## Assembly

Google.LongRunning.dll

## Constructors 

### Operation()
    
    
    public Operation()

### Operation(Operation)
    
    
    public Operation(Operation other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation)`  
  
  
## Properties 

### Done
    
    
    public bool Done { get; set; }

If the value is `false`, it means the operation is still in progress. If `true`, the operation is completed, and either `error` or `response` is available.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Error
    
    
    public Status Error { get; set; }

The error result of the operation in case of failure or cancellation.

**Property Value**  
---  
**Type** | **Description**  
`[Status](https://cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Status.html)` |   
  
### Metadata
    
    
    public Any Metadata { get; set; }

Service-specific metadata associated with the operation. It typically contains progress information and common metadata such as create time. Some services might not provide such metadata. Any method that returns a long-running operation should document the metadata type, if any.

**Property Value**  
---  
**Type** | **Description**  
`[Any](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Any.html)` |   
  
### Name
    
    
    public string Name { get; set; }

The server-assigned name, which is only unique within the same service that originally returns it. If you use the default HTTP mapping, the `name` should be a resource name ending with `operations/{unique_id}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Response
    
    
    public Any Response { get; set; }

The normal, successful response of the operation. If the original method returns no data on success, such as `Delete`, the response is `google.protobuf.Empty`. If the original method is standard `Get`/`Create`/`Update`, the response should be the resource. For other methods, the response should have the type `XxxResponse`, where `Xxx` is the original method name. For example, if the original method name is `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

**Property Value**  
---  
**Type** | **Description**  
`[Any](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Any.html)` |   
  
### ResultCase
    
    
    public Operation.ResultOneofCase ResultCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation)[ResultOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.ResultOneofCase)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
