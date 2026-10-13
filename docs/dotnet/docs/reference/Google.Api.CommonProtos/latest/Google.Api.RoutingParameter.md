---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.RoutingParameter
title: Class RoutingParameter (2.17.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:59:00.368631+00:00
---

# Class RoutingParameter (2.17.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.RoutingParameter

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Class RoutingParameter (2.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.17.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.RoutingParameter)
  * [ 2.15.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.15.0/Google.Api.RoutingParameter)
  * [ 2.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.10.0/Google.Api.RoutingParameter)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.2.0/Google.Api.RoutingParameter)


    
    
    public sealed class RoutingParameter : IMessage<RoutingParameter>, IEquatable<RoutingParameter>, IDeepCloneable<RoutingParameter>, IBufferMessage, IMessage

A projection from an input message to the GRPC or REST header.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > RoutingParameter

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[RoutingParameter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.RoutingParameter), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[RoutingParameter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.RoutingParameter), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[RoutingParameter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.RoutingParameter), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals\(system-object-system-object\))

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals)

## Namespace

[Google.Api](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api)

## Assembly

Google.Api.CommonProtos.dll

## Constructors 

### RoutingParameter()
    
    
    public RoutingParameter()

### RoutingParameter(RoutingParameter)
    
    
    public RoutingParameter(RoutingParameter other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[RoutingParameter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.RoutingParameter)`  
  
  
## Fields 

### FieldFieldNumber
    
    
    public const int FieldFieldNumber = 1

Field number for the "field" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PathTemplateFieldNumber
    
    
    public const int PathTemplateFieldNumber = 2

Field number for the "path_template" field.

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
  
### Field
    
    
    public string Field { get; set; }

A request field to extract the header key-value pair from.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parser
    
    
    public static MessageParser<RoutingParameter> Parser { get; }

**Property Value**  
---  
**Type** | **Description**  
`[MessageParser](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.MessageParser-1.html)[RoutingParameter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.RoutingParameter)` |   
  
### PathTemplate
    
    
    public string PathTemplate { get; set; }

A pattern matching the key-value field. Optional. If not specified, the whole field specified in the `field` field will be taken as value, and its name used as key. If specified, it MUST contain exactly one named segment (along with any number of unnamed segments) The pattern will be matched over the field specified in the `field` field, then if the match is successful:

  * the name of the single named segment will be used as a header name,
  * the match value of the segment will be used as a header value; if the match is NOT successful, nothing will be sent.



Example:
    
    
              -- This is a field in the request message
             |   that the header value will be extracted from.
             |
             |                     -- This is the key name in the
             |                    |   routing header.
             V                    |
    field: "table_name"           v
    path_template: "projects/*/{table_location=instances/*}/tables/*"
                                               ^            ^
                                               |            |
      In the {} brackets is the pattern that --             |
      specifies what to extract from the                    |
      field as a value to be sent.                          |
                                                            |
     The string in the field must match the whole pattern --
     before brackets, inside brackets, after brackets.
    

When looking at this specific example, we can see that:

  * A key-value pair with the key `table_location` and the value matching `instances/*` should be added to the x-goog-request-params routing header.
  * The value is extracted from the request message's `table_name` field if it matches the full pattern specified: `projects/*/instances/*/tables/*`.



**NB:** If the `path_template` field is not provided, the key name is equal to the field name, and the whole field should be sent as a value. This makes the pattern for the field and the value functionally equivalent to `**`, and the configuration
    
    
    {
      field: "table_name"
    }
    

is a functionally equivalent shorthand to:
    
    
    {
      field: "table_name"
      path_template: "{table_name=**}"
    }
    

See Example 1 for more details.

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
    
    
    public RoutingParameter Clone()

**Returns**  
---  
**Type** | **Description**  
`[RoutingParameter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.RoutingParameter)` |   
  
### Equals(RoutingParameter)
    
    
    public bool Equals(RoutingParameter other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[RoutingParameter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.RoutingParameter)`  
  
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

### MergeFrom(RoutingParameter)
    
    
    public void MergeFrom(RoutingParameter other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[RoutingParameter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.RoutingParameter)`  
  
  
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
