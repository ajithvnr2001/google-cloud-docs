---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.DocumentTransform.Types.FieldTransform
title: Firestore v1 API - Class DocumentTransform.Types.FieldTransform (4.5.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:36:25.322593+00:00
---

# Firestore v1 API - Class DocumentTransform.Types.FieldTransform (4.5.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.DocumentTransform.Types.FieldTransform

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Firestore v1 API - Class DocumentTransform.Types.FieldTransform (4.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.5.0 (latest)  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.1  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.5.0  2.4.0  2.3.0 
    
    
    public sealed class DocumentTransform.Types.FieldTransform : IMessage<DocumentTransform.Types.FieldTransform>, IEquatable<DocumentTransform.Types.FieldTransform>, IDeepCloneable<DocumentTransform.Types.FieldTransform>, IBufferMessage, IMessage

Reference documentation and code samples for the Firestore v1 API class DocumentTransform.Types.FieldTransform.

A transformation of a field of the document.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DocumentTransform.Types.FieldTransform

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DocumentTransform](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.DocumentTransform)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.DocumentTransform.Types)[FieldTransform](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.DocumentTransform.Types.FieldTransform), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DocumentTransform](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.DocumentTransform)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.DocumentTransform.Types)[FieldTransform](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.DocumentTransform.Types.FieldTransform), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DocumentTransform](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.DocumentTransform)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.DocumentTransform.Types)[FieldTransform](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.DocumentTransform.Types.FieldTransform), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Firestore.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1)

## Assembly

Google.Cloud.Firestore.V1.dll

## Constructors 

### FieldTransform()
    
    
    public FieldTransform()

### FieldTransform(FieldTransform)
    
    
    public FieldTransform(DocumentTransform.Types.FieldTransform other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DocumentTransform](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.DocumentTransform)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.DocumentTransform.Types)[FieldTransform](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.DocumentTransform.Types.FieldTransform)`  
  
  
## Properties 

### AppendMissingElements
    
    
    public ArrayValue AppendMissingElements { get; set; }

Append the given elements in order if they are not already present in the current field value. If the field is not an array, or if the field does not yet exist, it is first set to the empty array.

Equivalent numbers of different types (e.g. 3L and 3.0) are considered equal when checking if a value is missing. NaN is equal to NaN, and Null is equal to Null. If the input contains multiple equivalent values, only the first will be considered.

The corresponding transform_result will be the null value.

**Property Value**  
---  
**Type** | **Description**  
`[ArrayValue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.ArrayValue)` |   
  
### FieldPath
    
    
    public string FieldPath { get; set; }

The path of the field. See [Document.fields][google.firestore.v1.Document.fields] for the field path syntax reference.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### HasSetToServerValue
    
    
    public bool HasSetToServerValue { get; }

Gets whether the "set_to_server_value" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Increment
    
    
    public Value Increment { get; set; }

Adds the given value to the field's current value.

This must be an integer or a double value. If the field is not an integer or double, or if the field does not yet exist, the transformation will set the field to the given value. If either of the given value or the current field value are doubles, both values will be interpreted as doubles. Double arithmetic and representation of double values follow IEEE 754 semantics. If there is positive/negative integer overflow, the field is resolved to the largest magnitude positive/negative integer.

**Property Value**  
---  
**Type** | **Description**  
`[Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.Value)` |   
  
### Maximum
    
    
    public Value Maximum { get; set; }

Sets the field to the maximum of its current value and the given value.

This must be an integer or a double value. If the field is not an integer or double, or if the field does not yet exist, the transformation will set the field to the given value. If a maximum operation is applied where the field and the input value are of mixed types (that is - one is an integer and one is a double) the field takes on the type of the larger operand. If the operands are equivalent (e.g. 3 and 3.0), the field does not change. 0, 0.0, and -0.0 are all zero. The maximum of a zero stored value and zero input value is always the stored value. The maximum of any numeric value x and NaN is NaN.

**Property Value**  
---  
**Type** | **Description**  
`[Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.Value)` |   
  
### Minimum
    
    
    public Value Minimum { get; set; }

Sets the field to the minimum of its current value and the given value.

This must be an integer or a double value. If the field is not an integer or double, or if the field does not yet exist, the transformation will set the field to the input value. If a minimum operation is applied where the field and the input value are of mixed types (that is - one is an integer and one is a double) the field takes on the type of the smaller operand. If the operands are equivalent (e.g. 3 and 3.0), the field does not change. 0, 0.0, and -0.0 are all zero. The minimum of a zero stored value and zero input value is always the stored value. The minimum of any numeric value x and NaN is NaN.

**Property Value**  
---  
**Type** | **Description**  
`[Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.Value)` |   
  
### RemoveAllFromArray
    
    
    public ArrayValue RemoveAllFromArray { get; set; }

Remove all of the given elements from the array in the field. If the field is not an array, or if the field does not yet exist, it is set to the empty array.

Equivalent numbers of the different types (e.g. 3L and 3.0) are considered equal when deciding whether an element should be removed. NaN is equal to NaN, and Null is equal to Null. This will remove all equivalent values if there are duplicates.

The corresponding transform_result will be the null value.

**Property Value**  
---  
**Type** | **Description**  
`[ArrayValue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.ArrayValue)` |   
  
### SetToServerValue
    
    
    public DocumentTransform.Types.FieldTransform.Types.ServerValue SetToServerValue { get; set; }

Sets the field to the given server value.

**Property Value**  
---  
**Type** | **Description**  
`[DocumentTransform](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.DocumentTransform)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.DocumentTransform.Types)[FieldTransform](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.DocumentTransform.Types.FieldTransform)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.DocumentTransform.Types.FieldTransform.Types)[ServerValue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.DocumentTransform.Types.FieldTransform.Types.ServerValue)` |   
  
### TransformTypeCase
    
    
    public DocumentTransform.Types.FieldTransform.TransformTypeOneofCase TransformTypeCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[DocumentTransform](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.DocumentTransform)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.DocumentTransform.Types)[FieldTransform](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.DocumentTransform.Types.FieldTransform)[TransformTypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.DocumentTransform.Types.FieldTransform.TransformTypeOneofCase)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
