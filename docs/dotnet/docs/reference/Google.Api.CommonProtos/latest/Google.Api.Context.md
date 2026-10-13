---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Context
title: Class Context (2.17.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:15:05.162608+00:00
---

# Class Context (2.17.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Context

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Class Context (2.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.17.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Context)
  * [ 2.15.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.15.0/Google.Api.Context)
  * [ 2.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.10.0/Google.Api.Context)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.2.0/Google.Api.Context)


    
    
    public sealed class Context : IMessage<Context>, IEquatable<Context>, IDeepCloneable<Context>, IBufferMessage, IMessage

`Context` defines which contexts an API requests.

Example:
    
    
    context:
      rules:
      - selector: "*"
        requested:
        - google.rpc.context.ProjectContext
        - google.rpc.context.OriginContext
    

The above specifies that all methods in the API request `google.rpc.context.ProjectContext` and `google.rpc.context.OriginContext`.

Available context types are defined in package `google.rpc.context`.

This also provides mechanism to allowlist any protobuf message extension that can be sent in grpc metadata using “x-goog-ext-<extension_id>-bin” and “x-goog-ext-<extension_id>-jspb” format. For example, list any service specific protobuf types that can appear in grpc metadata as follows in your yaml file:

Example:
    
    
    context:
      rules:
       - selector: "google.example.library.v1.LibraryService.CreateBook"
         allowed_request_extensions:
         - google.foo.v1.NewExtension
         allowed_response_extensions:
         - google.foo.v1.NewExtension
    

You can also specify extension ID instead of fully qualified extension name here.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Context

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Context](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Context), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Context](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Context), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Context](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Context), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals\(system-object-system-object\))

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals)

## Namespace

[Google.Api](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api)

## Assembly

Google.Api.CommonProtos.dll

## Constructors 

### Context()
    
    
    public Context()

### Context(Context)
    
    
    public Context(Context other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Context](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Context)`  
  
  
## Fields 

### RulesFieldNumber
    
    
    public const int RulesFieldNumber = 1

Field number for the "rules" field.

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
  
### Parser
    
    
    public static MessageParser<Context> Parser { get; }

**Property Value**  
---  
**Type** | **Description**  
`[MessageParser](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.MessageParser-1.html)[Context](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Context)` |   
  
### Rules
    
    
    public RepeatedField<ContextRule> Rules { get; }

A list of RPC context rules that apply to individual API methods.

**NOTE:** All service configuration rules follow "last one wins" order.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[ContextRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ContextRule)` |   
  
## Methods 

### CalculateSize()
    
    
    public int CalculateSize()

**Returns**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### Clone()
    
    
    public Context Clone()

**Returns**  
---  
**Type** | **Description**  
`[Context](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Context)` |   
  
### Equals(Context)
    
    
    public bool Equals(Context other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Context](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Context)`  
  
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

### MergeFrom(Context)
    
    
    public void MergeFrom(Context other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Context](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Context)`  
  
  
### MergeFrom(CodedInputStream)
    
    
    public void MergeFrom(CodedInputStream input)

**Parameter**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.CodedInputStream.html)`  
  
  
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
