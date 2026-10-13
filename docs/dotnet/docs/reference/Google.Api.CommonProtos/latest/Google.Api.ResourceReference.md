---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ResourceReference
title: Class ResourceReference (2.17.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:23:32.084996+00:00
---

# Class ResourceReference (2.17.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ResourceReference

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Class ResourceReference (2.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.17.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ResourceReference)
  * [ 2.15.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.15.0/Google.Api.ResourceReference)
  * [ 2.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.10.0/Google.Api.ResourceReference)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.2.0/Google.Api.ResourceReference)


    
    
    public sealed class ResourceReference : IMessage<ResourceReference>, IEquatable<ResourceReference>, IDeepCloneable<ResourceReference>, IBufferMessage, IMessage

Defines a proto annotation that describes a string field that refers to an API resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ResourceReference

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ResourceReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ResourceReference), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ResourceReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ResourceReference), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ResourceReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ResourceReference), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals\(system-object-system-object\))

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals)

## Namespace

[Google.Api](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api)

## Assembly

Google.Api.CommonProtos.dll

## Constructors 

### ResourceReference()
    
    
    public ResourceReference()

### ResourceReference(ResourceReference)
    
    
    public ResourceReference(ResourceReference other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ResourceReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ResourceReference)`  
  
  
## Fields 

### ChildTypeFieldNumber
    
    
    public const int ChildTypeFieldNumber = 2

Field number for the "child_type" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### TypeFieldNumber
    
    
    public const int TypeFieldNumber = 1

Field number for the "type" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
## Properties 

### ChildType
    
    
    public string ChildType { get; set; }

The resource type of a child collection that the annotated field references. This is useful for annotating the `parent` field that doesn't have a fixed resource type.

Example:
    
    
    message ListLogEntriesRequest {
      string parent = 1 [(google.api.resource_reference) = {
        child_type: "logging.googleapis.com/LogEntry"
      };
    }
    

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Descriptor
    
    
    public static MessageDescriptor Descriptor { get; }

**Property Value**  
---  
**Type** | **Description**  
`[MessageDescriptor](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Reflection.MessageDescriptor.html)` |   
  
### Parser
    
    
    public static MessageParser<ResourceReference> Parser { get; }

**Property Value**  
---  
**Type** | **Description**  
`[MessageParser](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.MessageParser-1.html)[ResourceReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ResourceReference)` |   
  
### Type
    
    
    public string Type { get; set; }

The resource type that the annotated field references.

Example:
    
    
    message Subscription {
      string topic = 2 [(google.api.resource_reference) = {
        type: "pubsub.googleapis.com/Topic"
      }];
    }
    

Occasionally, a field may reference an arbitrary resource. In this case, APIs use the special value * in their resource reference.

Example:
    
    
    message GetIamPolicyRequest {
      string resource = 2 [(google.api.resource_reference) = {
        type: "*"
      }];
    }
    

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
    
    
    public ResourceReference Clone()

**Returns**  
---  
**Type** | **Description**  
`[ResourceReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ResourceReference)` |   
  
### Equals(ResourceReference)
    
    
    public bool Equals(ResourceReference other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ResourceReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ResourceReference)`  
  
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

### MergeFrom(ResourceReference)
    
    
    public void MergeFrom(ResourceReference other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ResourceReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ResourceReference)`  
  
  
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
