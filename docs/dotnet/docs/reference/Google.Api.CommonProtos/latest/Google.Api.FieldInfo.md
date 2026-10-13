---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.FieldInfo
title: Class FieldInfo (2.17.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:48.549864+00:00
---

# Class FieldInfo (2.17.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.FieldInfo

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Class FieldInfo (2.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.17.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.FieldInfo)
  * [ 2.15.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.15.0/Google.Api.FieldInfo)
  * [ 2.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.10.0/Google.Api.FieldInfo)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.2.0/Google.Api.FieldInfo)


    
    
    public sealed class FieldInfo : IMessage<FieldInfo>, IEquatable<FieldInfo>, IDeepCloneable<FieldInfo>, IBufferMessage, IMessage

Rich semantic information of an API field beyond basic typing.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > FieldInfo

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[FieldInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.FieldInfo), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[FieldInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.FieldInfo), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[FieldInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.FieldInfo), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals\(system-object-system-object\))

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals)

## Namespace

[Google.Api](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api)

## Assembly

Google.Api.CommonProtos.dll

## Constructors 

### FieldInfo()
    
    
    public FieldInfo()

### FieldInfo(FieldInfo)
    
    
    public FieldInfo(FieldInfo other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[FieldInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.FieldInfo)`  
  
  
## Fields 

### FormatFieldNumber
    
    
    public const int FormatFieldNumber = 1

Field number for the "format" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### ReferencedTypesFieldNumber
    
    
    public const int ReferencedTypesFieldNumber = 2

Field number for the "referenced_types" field.

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
  
### Format
    
    
    public FieldInfo.Types.Format Format { get; set; }

The standard format of a field value. This does not explicitly configure any API consumer, just documents the API's format for the field it is applied to.

**Property Value**  
---  
**Type** | **Description**  
`[FieldInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.FieldInfo)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.FieldInfo.Types)[Format](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.FieldInfo.Types.Format)` |   
  
### Parser
    
    
    public static MessageParser<FieldInfo> Parser { get; }

**Property Value**  
---  
**Type** | **Description**  
`[MessageParser](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.MessageParser-1.html)[FieldInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.FieldInfo)` |   
  
### ReferencedTypes
    
    
    public RepeatedField<TypeReference> ReferencedTypes { get; }

The type(s) that the annotated, generic field may represent.

Currently, this must only be used on fields of type `google.protobuf.Any`. Supporting other generic types may be considered in the future.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[TypeReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.TypeReference)` |   
  
## Methods 

### CalculateSize()
    
    
    public int CalculateSize()

**Returns**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### Clone()
    
    
    public FieldInfo Clone()

**Returns**  
---  
**Type** | **Description**  
`[FieldInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.FieldInfo)` |   
  
### Equals(FieldInfo)
    
    
    public bool Equals(FieldInfo other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[FieldInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.FieldInfo)`  
  
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

### MergeFrom(FieldInfo)
    
    
    public void MergeFrom(FieldInfo other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[FieldInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.FieldInfo)`  
  
  
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
