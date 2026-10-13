---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.BadRequest.Types.FieldViolation
title: Class BadRequest.Types.FieldViolation (2.17.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:59:04.366719+00:00
---

# Class BadRequest.Types.FieldViolation (2.17.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.BadRequest.Types.FieldViolation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Class BadRequest.Types.FieldViolation (2.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.17.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.BadRequest.Types.FieldViolation)
  * [ 2.15.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.15.0/Google.Rpc.BadRequest.Types.FieldViolation)
  * [ 2.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.10.0/Google.Rpc.BadRequest.Types.FieldViolation)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.2.0/Google.Rpc.BadRequest.Types.FieldViolation)


    
    
    public sealed class BadRequest.Types.FieldViolation : IMessage<BadRequest.Types.FieldViolation>, IEquatable<BadRequest.Types.FieldViolation>, IDeepCloneable<BadRequest.Types.FieldViolation>, IBufferMessage, IMessage

A message type used to describe a single bad request field.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > BadRequest.Types.FieldViolation

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[BadRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.BadRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.BadRequest.Types)[FieldViolation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.BadRequest.Types.FieldViolation), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[BadRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.BadRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.BadRequest.Types)[FieldViolation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.BadRequest.Types.FieldViolation), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[BadRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.BadRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.BadRequest.Types)[FieldViolation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.BadRequest.Types.FieldViolation), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals\(system-object-system-object\))

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals)

## Namespace

[Google.Rpc](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc)

## Assembly

Google.Api.CommonProtos.dll

## Constructors 

### FieldViolation()
    
    
    public FieldViolation()

### FieldViolation(FieldViolation)
    
    
    public FieldViolation(BadRequest.Types.FieldViolation other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[BadRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.BadRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.BadRequest.Types)[FieldViolation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.BadRequest.Types.FieldViolation)`  
  
  
## Fields 

### DescriptionFieldNumber
    
    
    public const int DescriptionFieldNumber = 2

Field number for the "description" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### FieldFieldNumber
    
    
    public const int FieldFieldNumber = 1

Field number for the "field" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### LocalizedMessageFieldNumber
    
    
    public const int LocalizedMessageFieldNumber = 4

Field number for the "localized_message" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### ReasonFieldNumber
    
    
    public const int ReasonFieldNumber = 3

Field number for the "reason" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
## Properties 

### Description
    
    
    public string Description { get; set; }

A description of why the request element is bad.

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
  
### Field
    
    
    public string Field { get; set; }

A path that leads to a field in the request body. The value will be a sequence of dot-separated identifiers that identify a protocol buffer field.

Consider the following:
    
    
    message CreateContactRequest {
      message EmailAddress {
        enum Type {
          TYPE_UNSPECIFIED = 0;
          HOME = 1;
          WORK = 2;
        }
    
        optional string email = 1;
        repeated EmailType type = 2;
      }
    
      string full_name = 1;
      repeated EmailAddress email_addresses = 2;
    }
    

In this example, in proto `field` could take one of the following values:

  * `full_name` for a violation in the `full_name` value
  * `email_addresses[1].email` for a violation in the `email` field of the first `email_addresses` message
  * `email_addresses[3].type[2]` for a violation in the second `type` value in the third `email_addresses` message.



In JSON, the same values are represented as:

  * `fullName` for a violation in the `fullName` value
  * `emailAddresses[1].email` for a violation in the `email` field of the first `emailAddresses` message
  * `emailAddresses[3].type[2]` for a violation in the second `type` value in the third `emailAddresses` message.



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### LocalizedMessage
    
    
    public LocalizedMessage LocalizedMessage { get; set; }

Provides a localized error message for field-level errors that is safe to return to the API consumer.

**Property Value**  
---  
**Type** | **Description**  
`[LocalizedMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.LocalizedMessage)` |   
  
### Parser
    
    
    public static MessageParser<BadRequest.Types.FieldViolation> Parser { get; }

**Property Value**  
---  
**Type** | **Description**  
`[MessageParser](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.MessageParser-1.html)[BadRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.BadRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.BadRequest.Types)[FieldViolation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.BadRequest.Types.FieldViolation)` |   
  
### Reason
    
    
    public string Reason { get; set; }

The reason of the field-level error. This is a constant value that identifies the proximate cause of the field-level error. It should uniquely identify the type of the FieldViolation within the scope of the google.rpc.ErrorInfo.domain. This should be at most 63 characters and match a regular expression of `[A-Z][A-Z0-9_]+[A-Z0-9]`, which represents UPPER_SNAKE_CASE.

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
    
    
    public BadRequest.Types.FieldViolation Clone()

**Returns**  
---  
**Type** | **Description**  
`[BadRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.BadRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.BadRequest.Types)[FieldViolation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.BadRequest.Types.FieldViolation)` |   
  
### Equals(FieldViolation)
    
    
    public bool Equals(BadRequest.Types.FieldViolation other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[BadRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.BadRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.BadRequest.Types)[FieldViolation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.BadRequest.Types.FieldViolation)`  
  
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
  
  
### MergeFrom(FieldViolation)
    
    
    public void MergeFrom(BadRequest.Types.FieldViolation other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[BadRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.BadRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.BadRequest.Types)[FieldViolation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.BadRequest.Types.FieldViolation)`  
  
  
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
