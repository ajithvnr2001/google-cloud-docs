---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Quaternion
title: Class Quaternion (2.17.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:59:17.190084+00:00
---

# Class Quaternion (2.17.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Quaternion

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Class Quaternion (2.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.17.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Quaternion)
  * [ 2.15.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.15.0/Google.Type.Quaternion)
  * [ 2.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.10.0/Google.Type.Quaternion)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.2.0/Google.Type.Quaternion)


    
    
    public sealed class Quaternion : IMessage<Quaternion>, IEquatable<Quaternion>, IDeepCloneable<Quaternion>, IBufferMessage, IMessage

A quaternion is defined as the quotient of two directed lines in a three-dimensional space or equivalently as the quotient of two Euclidean vectors (<https://en.wikipedia.org/wiki/Quaternion>).

Quaternions are often used in calculations involving three-dimensional rotations (<https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation>), as they provide greater mathematical robustness by avoiding the gimbal lock problems that can be encountered when using Euler angles (<https://en.wikipedia.org/wiki/Gimbal_lock>).

Quaternions are generally represented in this form:
    
    
    w + xi + yj + zk
    

where x, y, z, and w are real numbers, and i, j, and k are three imaginary numbers.

Our naming choice `(x, y, z, w)` comes from the desire to avoid confusion for those interested in the geometric properties of the quaternion in the 3D Cartesian space. Other texts often use alternative names or subscripts, such as `(a, b, c, d)`, `(1, i, j, k)`, or `(0, 1, 2, 3)`, which are perhaps better suited for mathematical interpretations.

To avoid any confusion, as well as to maintain compatibility with a large number of software libraries, the quaternions represented using the protocol buffer below _must_ follow the Hamilton convention, which defines `ij = k` (i.e. a right-handed algebra), and therefore:
    
    
    i^2 = j^2 = k^2 = ijk = −1
    ij = −ji = k
    jk = −kj = i
    ki = −ik = j
    

Please DO NOT use this to represent quaternions that follow the JPL convention, or any of the other quaternion flavors out there.

Definitions:

  * Quaternion norm (or magnitude): `sqrt(x^2 + y^2 + z^2 + w^2)`.
  * Unit (or normalized) quaternion: a quaternion whose norm is 1.
  * Pure quaternion: a quaternion whose scalar component (`w`) is 0.
  * Rotation quaternion: a unit quaternion used to represent rotation.
  * Orientation quaternion: a unit quaternion used to represent orientation.



A quaternion can be normalized by dividing it by its norm. The resulting quaternion maintains the same direction, but has a norm of 1, i.e. it moves on the unit sphere. This is generally necessary for rotation and orientation quaternions, to avoid rounding errors: <https://en.wikipedia.org/wiki/Rotation_formalisms_in_three_dimensions>

Note that `(x, y, z, w)` and `(-x, -y, -z, -w)` represent the same rotation, but normalization would be even more useful, e.g. for comparison purposes, if it would produce a unique representation. It is thus recommended that `w` be kept positive, which can be achieved by changing all the signs when `w` is negative.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Quaternion

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Quaternion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Quaternion), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Quaternion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Quaternion), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Quaternion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Quaternion), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals\(system-object-system-object\))

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals)

## Namespace

[Google.Type](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type)

## Assembly

Google.Api.CommonProtos.dll

## Constructors 

### Quaternion()
    
    
    public Quaternion()

### Quaternion(Quaternion)
    
    
    public Quaternion(Quaternion other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Quaternion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Quaternion)`  
  
  
## Fields 

### WFieldNumber
    
    
    public const int WFieldNumber = 4

Field number for the "w" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### XFieldNumber
    
    
    public const int XFieldNumber = 1

Field number for the "x" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### YFieldNumber
    
    
    public const int YFieldNumber = 2

Field number for the "y" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### ZFieldNumber
    
    
    public const int ZFieldNumber = 3

Field number for the "z" field.

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
    
    
    public static MessageParser<Quaternion> Parser { get; }

**Property Value**  
---  
**Type** | **Description**  
`[MessageParser](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.MessageParser-1.html)[Quaternion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Quaternion)` |   
  
### W
    
    
    public double W { get; set; }

The scalar component.

**Property Value**  
---  
**Type** | **Description**  
`[double](https://learn.microsoft.com/dotnet/api/system.double)` |   
  
### X
    
    
    public double X { get; set; }

The x component.

**Property Value**  
---  
**Type** | **Description**  
`[double](https://learn.microsoft.com/dotnet/api/system.double)` |   
  
### Y
    
    
    public double Y { get; set; }

The y component.

**Property Value**  
---  
**Type** | **Description**  
`[double](https://learn.microsoft.com/dotnet/api/system.double)` |   
  
### Z
    
    
    public double Z { get; set; }

The z component.

**Property Value**  
---  
**Type** | **Description**  
`[double](https://learn.microsoft.com/dotnet/api/system.double)` |   
  
## Methods 

### CalculateSize()
    
    
    public int CalculateSize()

**Returns**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### Clone()
    
    
    public Quaternion Clone()

**Returns**  
---  
**Type** | **Description**  
`[Quaternion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Quaternion)` |   
  
### Equals(Quaternion)
    
    
    public bool Equals(Quaternion other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Quaternion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Quaternion)`  
  
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
  
  
### MergeFrom(Quaternion)
    
    
    public void MergeFrom(Quaternion other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Quaternion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Quaternion)`  
  
  
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
