---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Decimal
title: Class Decimal (2.17.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:15:04.182097+00:00
---

# Class Decimal (2.17.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Decimal

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Class Decimal (2.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.17.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Decimal)
  * [ 2.15.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.15.0/Google.Type.Decimal)
  * [ 2.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.10.0/Google.Type.Decimal)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.2.0/Google.Type.Decimal)


    
    
    public sealed class Decimal : IMessage<Decimal>, IEquatable<Decimal>, IDeepCloneable<Decimal>, IBufferMessage, IMessage

A representation of a decimal value, such as 2.5. Clients may convert values into language-native decimal formats, such as Java's [BigDecimal][] or Python's [decimal.Decimal](https://docs.python.org/3/library/decimal.html).

[BigDecimal]: <https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/math/BigDecimal.html>

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Decimal

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Decimal](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Decimal), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Decimal](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Decimal), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Decimal](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Decimal), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals\(system-object-system-object\))

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals)

## Namespace

[Google.Type](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type)

## Assembly

Google.Api.CommonProtos.dll

## Constructors 

### Decimal()
    
    
    public Decimal()

### Decimal(Decimal)
    
    
    public Decimal(Decimal other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Decimal](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Decimal)`  
  
  
## Fields 

### ValueFieldNumber
    
    
    public const int ValueFieldNumber = 1

Field number for the "value" field.

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
    
    
    public static MessageParser<Decimal> Parser { get; }

**Property Value**  
---  
**Type** | **Description**  
`[MessageParser](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.MessageParser-1.html)[Decimal](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Decimal)` |   
  
### Value
    
    
    public string Value { get; set; }

The decimal value, as a string.

The string representation consists of an optional sign, `+` (`U+002B`) or `-` (`U+002D`), followed by a sequence of zero or more decimal digits ("the integer"), optionally followed by a fraction, optionally followed by an exponent.

The fraction consists of a decimal point followed by zero or more decimal digits. The string must contain at least one digit in either the integer or the fraction. The number formed by the sign, the integer and the fraction is referred to as the significand.

The exponent consists of the character `e` (`U+0065`) or `E` (`U+0045`) followed by one or more decimal digits.

Services **should** normalize decimal values before storing them by:

  * Removing an explicitly-provided `+` sign (`+2.5` -> `2.5`).
  * Replacing a zero-length integer value with `0` (`.5` -> `0.5`).
  * Coercing the exponent character to lower-case (`2.5E8` -> `2.5e8`).
  * Removing an explicitly-provided zero exponent (`2.5e0` -> `2.5`).



Services **may** perform additional normalization based on its own needs and the internal decimal implementation selected, such as shifting the decimal point and exponent value together (example: `2.5e-1` <-> `0.25`). Additionally, services **may** preserve trailing zeroes in the fraction to indicate increased precision, but are not required to do so.

Note that only the `.` character is supported to divide the integer and the fraction; `,` **should not** be supported regardless of locale. Additionally, thousand separators **should not** be supported. If a service does support them, values **must** be normalized.

The ENBF grammar is:
    
    
    DecimalString =
      [Sign] Significand [Exponent];
    
    Sign = '+' | '-';
    
    Significand =
      Digits ['.'] [Digits] | [Digits] '.' Digits;
    
    Exponent = ('e' | 'E') [Sign] Digits;
    
    Digits = { '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' };
    

Services **should** clearly document the range of supported values, the maximum supported precision (total number of digits), and, if applicable, the scale (number of digits after the decimal point), as well as how it behaves when receiving out-of-bounds values.

Services **may** choose to accept values passed as input even when the value has a higher precision or scale than the service supports, and **should** round the value to fit the supported scale. Alternatively, the service **may** error with `400 Bad Request` (`INVALID_ARGUMENT` in gRPC) if precision would be lost.

Services **should** error with `400 Bad Request` (`INVALID_ARGUMENT` in gRPC) if the service receives a value outside of the supported range.

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
    
    
    public Decimal Clone()

**Returns**  
---  
**Type** | **Description**  
`[Decimal](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Decimal)` |   
  
### Equals(Decimal)
    
    
    public bool Equals(Decimal other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Decimal](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Decimal)`  
  
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

### FromClrDecimal(decimal)
    
    
    public static Decimal FromClrDecimal(decimal value)

Converts the given [decimal](https://learn.microsoft.com/dotnet/api/system.decimal) value to the protobuf [Decimal](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Decimal) representation. If the input value naturally contains trailing decimal zeroes (e.g. "1.00") these are preserved in the protobuf representation.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[decimal](https://learn.microsoft.com/dotnet/api/system.decimal)`  
The value to convert.  
**Returns**  
---  
**Type** | **Description**  
`[Decimal](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Decimal)` | The protobuf representation.  
  
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
  
  
### MergeFrom(Decimal)
    
    
    public void MergeFrom(Decimal other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Decimal](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Decimal)`  
  
  
### ToClrDecimal()
    
    
    public decimal ToClrDecimal()

Converts this protobuf [Decimal](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Decimal) value to a CLR [decimal](https://learn.microsoft.com/dotnet/api/system.decimal) value. If the value is within the range of [decimal](https://learn.microsoft.com/dotnet/api/system.decimal) but contains more than 29 significant digits, the returned value is truncated towards zero.

**Returns**  
---  
**Type** | **Description**  
`[decimal](https://learn.microsoft.com/dotnet/api/system.decimal)` | The CLR representation of this value.  
**Exceptions**  
---  
**Type** | **Description**  
`[FormatException](https://learn.microsoft.com/dotnet/api/system.formatexception)` | This protobuf value is invalid, either because [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Decimal#Google_Type_Decimal_Value) has not been set, or because it does not represent a valid decimal value.  
`[OverflowException](https://learn.microsoft.com/dotnet/api/system.overflowexception)` | The protobuf value is too large or small to be represented by [decimal](https://learn.microsoft.com/dotnet/api/system.decimal).  
  
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
