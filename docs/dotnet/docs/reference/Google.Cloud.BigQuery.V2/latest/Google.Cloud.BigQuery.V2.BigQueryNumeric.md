---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric
title: Google BigQuery v2 API - Struct BigQueryNumeric (3.12.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:51:09.082240+00:00
---

# Google BigQuery v2 API - Struct BigQueryNumeric (3.12.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google BigQuery v2 API - Struct BigQueryNumeric (3.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.4.0  2.3.0  2.2.0 
    
    
    public struct BigQueryNumeric : IEquatable<BigQueryNumeric>, IComparable<BigQueryNumeric>, IComparable

Reference documentation and code samples for the Google BigQuery v2 API struct BigQueryNumeric.

Representation of the BigQuery NUMERIC type, which has 38 digits of precision, and a fixed scale of 9 decimal places to the right of the decimal point

## Implements

[IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[BigQueryNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric), [IComparable](https://learn.microsoft.com/dotnet/api/system.icomparable-1)[BigQueryNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric), [IComparable](https://learn.microsoft.com/dotnet/api/system.icomparable)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.BigQuery.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2)

## Assembly

Google.Cloud.BigQuery.V2.dll

## Properties 

### Epsilon
    
    
    public static BigQueryNumeric Epsilon { get; }

The smallest positive value for [BigQueryNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric), equal to 0.000000001.

**Property Value**  
---  
**Type** | **Description**  
`[BigQueryNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric)` |   
  
### MaxValue
    
    
    public static BigQueryNumeric MaxValue { get; }

The maximum valid value for [BigQueryNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric), equal to 99999999999999999999999999999.999999999.

**Property Value**  
---  
**Type** | **Description**  
`[BigQueryNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric)` |   
  
### MinValue
    
    
    public static BigQueryNumeric MinValue { get; }

The minimum valid value for [BigQueryNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric), equal to -99999999999999999999999999999.999999999.

**Property Value**  
---  
**Type** | **Description**  
`[BigQueryNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric)` |   
  
### Zero
    
    
    public static BigQueryNumeric Zero { get; }

Zero represented as a [BigQueryNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric). This is the default value for the type.

**Property Value**  
---  
**Type** | **Description**  
`[BigQueryNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric)` |   
  
## Methods 

### CompareTo(BigQueryNumeric)
    
    
    public int CompareTo(BigQueryNumeric other)

Compares this value with `other`.

**Parameter**  
---  
**Name** | **Description**  
`other` | `[BigQueryNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric)`  
The value to compare with this one  
**Returns**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` | A negative integer if this value is less than `other`; a positive integer if it's greater than `other`; zero if they're equal.  
  
### FromDecimal(decimal, LossOfPrecisionHandling)
    
    
    public static BigQueryNumeric FromDecimal(decimal value, LossOfPrecisionHandling lossOfPrecisionHandling)

Converts a [decimal](https://learn.microsoft.com/dotnet/api/system.decimal) value to [BigQueryNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric),

**Parameters**  
---  
**Name** | **Description**  
`value` | `[decimal](https://learn.microsoft.com/dotnet/api/system.decimal)`  
The value to convert  
`lossOfPrecisionHandling` | `[LossOfPrecisionHandling](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.LossOfPrecisionHandling)`  
How to handle values with signficant digits that would be lost by the conversion.  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric)` | The converted value.  
**Remarks**

This conversion may silently lose precision, depending on `lossOfPrecisionHandling`.

### GetHashCode()
    
    
    public override int GetHashCode()

Returns a hash code for this value.

**Returns**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` | A hash code for this value.  
**Overrides**

[ValueType.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.valuetype.gethashcode)

### Parse(string)
    
    
    public static BigQueryNumeric Parse(string text)

Parses a textual representation as a [BigQueryNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric).

**Parameter**  
---  
**Name** | **Description**  
`text` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The text to parse. Must not be null.  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric)` | The parsed value.  
**Remarks**

`text` must be a representation of a decimal value which can be represented by [BigQueryNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric), using "." as a decimal place where one is specified, and a leading "-" for negative values. Leading zeroes and insignificant trailing digits are permitted. 

**Exceptions**  
---  
**Type** | **Description**  
`[FormatException](https://learn.microsoft.com/dotnet/api/system.formatexception)` | The value could not be parsed as a [BigQueryNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric).  
  
### ToDecimal(LossOfPrecisionHandling)
    
    
    public decimal ToDecimal(LossOfPrecisionHandling lossOfPrecisionHandling)

Converts this value to [BigQueryNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric),

**Parameter**  
---  
**Name** | **Description**  
`lossOfPrecisionHandling` | `[LossOfPrecisionHandling](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.LossOfPrecisionHandling)`  
How to handle values with signficant digits that would be lost by the conversion.  
**Returns**  
---  
**Type** | **Description**  
`[decimal](https://learn.microsoft.com/dotnet/api/system.decimal)` | The converted value.  
**Remarks**

This conversion may silently lose precision, depending on `lossOfPrecisionHandling`, but will always throw [OverflowException](https://learn.microsoft.com/dotnet/api/system.overflowexception) if value is out of the range of [decimal](https://learn.microsoft.com/dotnet/api/system.decimal).

**Exceptions**  
---  
**Type** | **Description**  
`[OverflowException](https://learn.microsoft.com/dotnet/api/system.overflowexception)` | This value is outside the range of [decimal](https://learn.microsoft.com/dotnet/api/system.decimal).  
  
### ToString()
    
    
    public override string ToString()

Returns a canonical string representation of this value. This always uses "." as a decimal point, and only includes as many decimal places as are required to completely represent the value. If the value is between -1 and 1 exclusive, a "0" character is included before the decimal point.

**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | A canonical string representation of this value.  
**Overrides**

[ValueType.ToString()](https://learn.microsoft.com/dotnet/api/system.valuetype.tostring)

### TryParse(string, out BigQueryNumeric)
    
    
    public static bool TryParse(string text, out BigQueryNumeric value)

Attempts to parse a textual representation of a [BigQueryNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric) value.

**Parameters**  
---  
**Name** | **Description**  
`text` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The text to parse. Must not be null.  
`value` | `[BigQueryNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric)`  
The parsed value, or 0 on failure.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if `text` was parsed successfully; `false` otherwise.  
**Remarks**

See [Parse(string)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric#Google_Cloud_BigQuery_V2_BigQueryNumeric_Parse_System_String_) for format details. This method will return `true` if and only if [Parse(string)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric#Google_Cloud_BigQuery_V2_BigQueryNumeric_Parse_System_String_) would return without an exception.

## Operators 

### operator +(BigQueryNumeric, BigQueryNumeric)
    
    
    public static BigQueryNumeric operator +(BigQueryNumeric lhs, BigQueryNumeric rhs)

Returns the result of adding two [BigQueryNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric) values together.

**Parameters**  
---  
**Name** | **Description**  
`lhs` | `[BigQueryNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric)`  
The first value to add.  
`rhs` | `[BigQueryNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric)`  
The second value to add.  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric)` | The result of adding the two values.  
  
### operator ==(BigQueryNumeric, BigQueryNumeric)
    
    
    public static bool operator ==(BigQueryNumeric lhs, BigQueryNumeric rhs)

Compares two values for equality.

**Parameters**  
---  
**Name** | **Description**  
`lhs` | `[BigQueryNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric)`  
The first value to compare.  
`rhs` | `[BigQueryNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric)`  
The second value to compare.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the two arguments are equal; `false` otherwise.  
  
### explicit operator decimal(BigQueryNumeric)
    
    
    public static explicit operator decimal(BigQueryNumeric value)

Explicit conversion from [BigQueryNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric) to [decimal](https://learn.microsoft.com/dotnet/api/system.decimal).

**Parameter**  
---  
**Name** | **Description**  
`value` | `[BigQueryNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric)`  
The numeric value to convert.  
**Returns**  
---  
**Type** | **Description**  
`[decimal](https://learn.microsoft.com/dotnet/api/system.decimal)` | The result of the conversion.  
**Remarks**

This conversion may silently lose precision, but will throw [OverflowException](https://learn.microsoft.com/dotnet/api/system.overflowexception) if the value is out of range of [decimal](https://learn.microsoft.com/dotnet/api/system.decimal). Use [ToDecimal(LossOfPrecisionHandling)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric#Google_Cloud_BigQuery_V2_BigQueryNumeric_ToDecimal_Google_Cloud_BigQuery_V2_LossOfPrecisionHandling_) passing in [Throw](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.LossOfPrecisionHandling#Google_Cloud_BigQuery_V2_LossOfPrecisionHandling_Throw) for the second argument to avoid any information loss.

### explicit operator BigQueryNumeric(decimal)
    
    
    public static explicit operator BigQueryNumeric(decimal value)

Explicit conversion from [decimal](https://learn.microsoft.com/dotnet/api/system.decimal) to [BigQueryNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric).

**Parameter**  
---  
**Name** | **Description**  
`value` | `[decimal](https://learn.microsoft.com/dotnet/api/system.decimal)`  
The decimal value to convert.  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric)` | The result of the conversion.  
**Remarks**

This conversion may silently lose precision. Use [FromDecimal(decimal, LossOfPrecisionHandling)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric#Google_Cloud_BigQuery_V2_BigQueryNumeric_FromDecimal_System_Decimal_Google_Cloud_BigQuery_V2_LossOfPrecisionHandling_) passing in [Throw](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.LossOfPrecisionHandling#Google_Cloud_BigQuery_V2_LossOfPrecisionHandling_Throw) for the second argument to avoid any information loss.

### implicit operator BigQueryNumeric(int)
    
    
    public static implicit operator BigQueryNumeric(int value)

Implicit conversion from [int](https://learn.microsoft.com/dotnet/api/system.int32) to [BigQueryNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric).

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The integer value to convert.  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric)` | The result of the conversion.  
**Remarks**

This conversion exists to avoid ambiguity between the 64-bit conversions when using an integer literal.

### implicit operator BigQueryNumeric(long)
    
    
    public static implicit operator BigQueryNumeric(long value)

Implicit conversion from [long](https://learn.microsoft.com/dotnet/api/system.int64) to [BigQueryNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric).

**Parameter**  
---  
**Name** | **Description**  
`value` | `[long](https://learn.microsoft.com/dotnet/api/system.int64)`  
The integer value to convert.  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric)` | The result of the conversion.  
  
### implicit operator BigQueryNumeric(ulong)
    
    
    public static implicit operator BigQueryNumeric(ulong value)

Implicit conversion from [ulong](https://learn.microsoft.com/dotnet/api/system.uint64) to [BigQueryNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric).

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ulong](https://learn.microsoft.com/dotnet/api/system.uint64)`  
The integer value to convert.  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric)` | The result of the conversion.  
  
### operator !=(BigQueryNumeric, BigQueryNumeric)
    
    
    public static bool operator !=(BigQueryNumeric lhs, BigQueryNumeric rhs)

Compares two values for inequality.

**Parameters**  
---  
**Name** | **Description**  
`lhs` | `[BigQueryNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric)`  
The first value to compare.  
`rhs` | `[BigQueryNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric)`  
The second value to compare.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `false` if the two arguments are equal; `true` otherwise.  
  
### operator -(BigQueryNumeric, BigQueryNumeric)
    
    
    public static BigQueryNumeric operator -(BigQueryNumeric lhs, BigQueryNumeric rhs)

Returns the result of subtracting one [BigQueryNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric) value from another.

**Parameters**  
---  
**Name** | **Description**  
`lhs` | `[BigQueryNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric)`  
The value to subtract from.  
`rhs` | `[BigQueryNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric)`  
The value to subtract.  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric)` | The result of subtracting `rhs` from `lhs`.  
  
### operator -(BigQueryNumeric)
    
    
    public static BigQueryNumeric operator -(BigQueryNumeric value)

The unary negation operator.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[BigQueryNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric)`  
The value to negate.  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric)` | The negation of `value`.  
  
### operator +(BigQueryNumeric)
    
    
    public static BigQueryNumeric operator +(BigQueryNumeric value)

The unary plus operator, provided mainly for consistency.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[BigQueryNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric)`  
The value to return.  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryNumeric)` | The original value.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
