---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Context.AttributeContext.Types.Api
title: Class AttributeContext.Types.Api (2.17.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:36:06.473537+00:00
---

# Class AttributeContext.Types.Api (2.17.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Context.AttributeContext.Types.Api

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Class AttributeContext.Types.Api (2.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.17.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Context.AttributeContext.Types.Api)
  * [ 2.15.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.15.0/Google.Rpc.Context.AttributeContext.Types.Api)
  * [ 2.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.10.0/Google.Rpc.Context.AttributeContext.Types.Api)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.2.0/Google.Rpc.Context.AttributeContext.Types.Api)


    
    
    public sealed class AttributeContext.Types.Api : IMessage<AttributeContext.Types.Api>, IEquatable<AttributeContext.Types.Api>, IDeepCloneable<AttributeContext.Types.Api>, IBufferMessage, IMessage

This message defines attributes associated with API operations, such as a network API request. The terminology is based on the conventions used by Google APIs, Istio, and OpenAPI.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AttributeContext.Types.Api

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AttributeContext](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Context.AttributeContext)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Context.AttributeContext.Types)[Api](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Context.AttributeContext.Types.Api), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AttributeContext](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Context.AttributeContext)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Context.AttributeContext.Types)[Api](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Context.AttributeContext.Types.Api), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AttributeContext](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Context.AttributeContext)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Context.AttributeContext.Types)[Api](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Context.AttributeContext.Types.Api), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals\(system-object-system-object\))

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals)

## Namespace

[Google.Rpc.Context](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Context)

## Assembly

Google.Api.CommonProtos.dll

## Constructors 

### Api()
    
    
    public Api()

### Api(Api)
    
    
    public Api(AttributeContext.Types.Api other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AttributeContext](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Context.AttributeContext)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Context.AttributeContext.Types)[Api](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Context.AttributeContext.Types.Api)`  
  
  
## Fields 

### OperationFieldNumber
    
    
    public const int OperationFieldNumber = 2

Field number for the "operation" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### ProtocolFieldNumber
    
    
    public const int ProtocolFieldNumber = 3

Field number for the "protocol" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### ServiceFieldNumber
    
    
    public const int ServiceFieldNumber = 1

Field number for the "service" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### VersionFieldNumber
    
    
    public const int VersionFieldNumber = 4

Field number for the "version" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
## Properties 

### Descriptor
    
    
    public static MessageDescriptor Descriptor { get; }

**Property Value**  
---  
**Type** | **Description**  
`[MessageDescriptor](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Reflection.MessageDescriptor.html)` |   
  
### Operation
    
    
    public string Operation { get; set; }

The API operation name. For gRPC requests, it is the fully qualified API method name, such as "google.pubsub.v1.Publisher.Publish". For OpenAPI requests, it is the `operationId`, such as "getPet".

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parser
    
    
    public static MessageParser<AttributeContext.Types.Api> Parser { get; }

**Property Value**  
---  
**Type** | **Description**  
`[MessageParser](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.MessageParser-1.html)[AttributeContext](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Context.AttributeContext)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Context.AttributeContext.Types)[Api](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Context.AttributeContext.Types.Api)` |   
  
### Protocol
    
    
    public string Protocol { get; set; }

The API protocol used for sending the request, such as "http", "https", "grpc", or "internal".

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Service
    
    
    public string Service { get; set; }

The API service name. It is a logical identifier for a networked API, such as "pubsub.googleapis.com". The naming syntax depends on the API management system being used for handling the request.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Version
    
    
    public string Version { get; set; }

The API version associated with the API operation above, such as "v1" or "v1alpha1".

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
## Methods 

### CalculateSize()
    
    
    public int CalculateSize()

**Returns**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### Clone()
    
    
    public AttributeContext.Types.Api Clone()

**Returns**  
---  
**Type** | **Description**  
`[AttributeContext](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Context.AttributeContext)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Context.AttributeContext.Types)[Api](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Context.AttributeContext.Types.Api)` |   
  
### Equals(Api)
    
    
    public bool Equals(AttributeContext.Types.Api other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AttributeContext](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Context.AttributeContext)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Context.AttributeContext.Types)[Api](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Context.AttributeContext.Types.Api)`  
  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Equals(object)
    
    
    public override bool Equals(object other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[object](https://learn.microsoft.com/dotnet/api/system.object)`  
  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
**Overrides**

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals\(system-object\))

### GetHashCode()
    
    
    public override int GetHashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
**Overrides**

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

### MergeFrom(CodedInputStream)
    
    
    public void MergeFrom(CodedInputStream input)

**Parameter**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.CodedInputStream.html)`  
  
  
### MergeFrom(Api)
    
    
    public void MergeFrom(AttributeContext.Types.Api other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AttributeContext](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Context.AttributeContext)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Context.AttributeContext.Types)[Api](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Context.AttributeContext.Types.Api)`  
  
  
### ToString()
    
    
    public override string ToString()

**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Overrides**

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

### WriteTo(CodedOutputStream)
    
    
    public void WriteTo(CodedOutputStream output)

**Parameter**  
---  
**Name** | **Description**  
`output` | `[CodedOutputStream](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.CodedOutputStream.html)`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
