---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.KeyRecipe.Types.Part
title: Google Cloud Spanner v1 API - Class KeyRecipe.Types.Part (5.13.0-beta11) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:59:25.675010+00:00
---

# Google Cloud Spanner v1 API - Class KeyRecipe.Types.Part (5.13.0-beta11)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.KeyRecipe.Types.Part

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Spanner v1 API - Class KeyRecipe.Types.Part (5.13.0-beta11) Stay organized with collections  Save and categorize content based on your preferences. 

5.13.0-beta11  5.13.0-beta10  5.12.0 (latest)  5.11.0  5.10.0  5.9.0  5.8.0  5.7.0  5.6.0  5.5.0  5.4.0  5.3.0  5.2.0  5.1.0  5.0.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.15.1  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0 
    
    
    public sealed class KeyRecipe.Types.Part : IMessage<KeyRecipe.Types.Part>, IEquatable<KeyRecipe.Types.Part>, IDeepCloneable<KeyRecipe.Types.Part>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Spanner v1 API class KeyRecipe.Types.Part.

An ssformat key is composed of a sequence of tag numbers and key column values. `Part` represents a single tag or key column value.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > KeyRecipe.Types.Part

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[KeyRecipe](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.KeyRecipe)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.KeyRecipe.Types)[Part](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.KeyRecipe.Types.Part), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[KeyRecipe](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.KeyRecipe)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.KeyRecipe.Types)[Part](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.KeyRecipe.Types.Part), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[KeyRecipe](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.KeyRecipe)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.KeyRecipe.Types)[Part](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.KeyRecipe.Types.Part), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Spanner.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1)

## Assembly

Google.Cloud.Spanner.V1.dll

## Constructors 

### Part()
    
    
    public Part()

### Part(Part)
    
    
    public Part(KeyRecipe.Types.Part other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[KeyRecipe](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.KeyRecipe)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.KeyRecipe.Types)[Part](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.KeyRecipe.Types.Part)`  
  
  
## Properties 

### HasIdentifier
    
    
    public bool HasIdentifier { get; }

Gets whether the "identifier" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasRandom
    
    
    public bool HasRandom { get; }

Gets whether the "random" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Identifier
    
    
    public string Identifier { get; set; }

`identifier` is the name of the column or query parameter.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### NullOrder
    
    
    public KeyRecipe.Types.Part.Types.NullOrder NullOrder { get; set; }

How NULLs are represented in the encoded key part. Only present if `tag` is zero.

**Property Value**  
---  
**Type** | **Description**  
`[KeyRecipe](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.KeyRecipe)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.KeyRecipe.Types)[Part](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.KeyRecipe.Types.Part)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.KeyRecipe.Types.Part.Types)[NullOrder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.KeyRecipe.Types.Part.Types.NullOrder)` |   
  
### Order
    
    
    public KeyRecipe.Types.Part.Types.Order Order { get; set; }

Whether the key column is sorted ascending or descending. Only present if `tag` is zero.

**Property Value**  
---  
**Type** | **Description**  
`[KeyRecipe](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.KeyRecipe)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.KeyRecipe.Types)[Part](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.KeyRecipe.Types.Part)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.KeyRecipe.Types.Part.Types)[Order](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.KeyRecipe.Types.Part.Types.Order)` |   
  
### Random
    
    
    public bool Random { get; set; }

If true, the client is responsible to fill in the value randomly. It's relevant only for the INT64 type.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### StructIdentifiers
    
    
    public RepeatedField<int> StructIdentifiers { get; }

It is a repeated field to support fetching key columns from nested structs, such as `STRUCT` query parameters.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### Tag
    
    
    public uint Tag { get; set; }

If non-zero, `tag` is the only field present in this `Part`. The part is encoded by appending `tag` to the ssformat key.

**Property Value**  
---  
**Type** | **Description**  
`[uint](https://learn.microsoft.com/dotnet/api/system.uint32)` |   
  
### Type
    
    
    public Type Type { get; set; }

The type of the key part. Only present if `tag` is zero.

**Property Value**  
---  
**Type** | **Description**  
`[Type](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.Type)` |   
  
### Value
    
    
    public Value Value { get; set; }

The constant value of the key part. It is present when query uses a constant as a part of the key.

**Property Value**  
---  
**Type** | **Description**  
`[Value](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Value.html)` |   
  
### ValueTypeCase
    
    
    public KeyRecipe.Types.Part.ValueTypeOneofCase ValueTypeCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[KeyRecipe](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.KeyRecipe)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.KeyRecipe.Types)[Part](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.KeyRecipe.Types.Part)[ValueTypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.KeyRecipe.Types.Part.ValueTypeOneofCase)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
