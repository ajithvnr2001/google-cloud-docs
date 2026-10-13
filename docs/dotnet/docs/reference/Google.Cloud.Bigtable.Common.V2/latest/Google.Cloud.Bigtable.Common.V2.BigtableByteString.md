---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString
title: Google.Cloud.Bigtable.Common.V2 - Struct BigtableByteString (3.3.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:34:08.149698+00:00
---

# Google.Cloud.Bigtable.Common.V2 - Struct BigtableByteString (3.3.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google.Cloud.Bigtable.Common.V2 - Struct BigtableByteString (3.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.3.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString)
  * [ 3.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/3.2.0/Google.Cloud.Bigtable.Common.V2.BigtableByteString)
  * [ 3.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/3.1.0/Google.Cloud.Bigtable.Common.V2.BigtableByteString)
  * [ 3.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/3.0.0/Google.Cloud.Bigtable.Common.V2.BigtableByteString)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/2.1.0/Google.Cloud.Bigtable.Common.V2.BigtableByteString)


    
    
    public struct BigtableByteString : IComparable, IComparable<BigtableByteString>, IEquatable<BigtableByteString>, IEnumerable<byte>, IEnumerable

Reference documentation and code samples for the Google.Cloud.Bigtable.Common.V2 struct BigtableByteString.

A sequence of bytes which can be used for a row key, column qualifier, or cell value.

## Implements

[IComparable](https://learn.microsoft.com/dotnet/api/system.icomparable), [IComparable](https://learn.microsoft.com/dotnet/api/system.icomparable-1)[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[byte](https://learn.microsoft.com/dotnet/api/system.byte), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.Bigtable.Common.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2)

## Assembly

Google.Cloud.Bigtable.Common.V2.dll

## Constructors 

### BigtableByteString(ByteString)
    
    
    public BigtableByteString(ByteString value)

Creates a [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString) value from a byte string.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)`  
The byte string making up the value. May be null in which case the empty byte string is used.  
  
### BigtableByteString(params byte[])
    
    
    public BigtableByteString(params byte[] value)

Creates a [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString) value from an array of bytes.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[byte](https://learn.microsoft.com/dotnet/api/system.byte)`  
The bytes making up the byte string. May be null in which case the empty byte string is used.  
  
### BigtableByteString(long)
    
    
    public BigtableByteString(long value)

Creates a [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString) value from the big-endian encoding of a signed 64-bit value.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[long](https://learn.microsoft.com/dotnet/api/system.int64)`  
The 64-bit value which should be used to initialize the byte string.  
  
### BigtableByteString(string)
    
    
    public BigtableByteString(string valueAsUtf8)

Creates a [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString) value from the UTF-8 encoding of a string.

**Parameter**  
---  
**Name** | **Description**  
`valueAsUtf8` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The value whose UTF-8 representation should be used to initialize the byte string. May be null in which case the empty byte string is used.  
  
## Properties 

### IsEmpty
    
    
    public bool IsEmpty { get; }

Returns true if the byte string is empty, false otherwise.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### this[int]
    
    
    public byte this[int index] { get; }

Returns the byte at index `index`.

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The index in the byte string to return. Must be greater than or equal to 0, and less than [Length](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString#Google_Cloud_Bigtable_Common_V2_BigtableByteString_Length).  
**Property Value**  
---  
**Type** | **Description**  
`[byte](https://learn.microsoft.com/dotnet/api/system.byte)` | The byte at index `index`.  
  
### Length
    
    
    public int Length { get; }

Gets the number of bytes in the byte string.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### Value
    
    
    public ByteString Value { get; }

Gets the underlying byte string.

**Property Value**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)` |   
  
## Methods 

### Compare(BigtableByteString, BigtableByteString)
    
    
    public static int Compare(BigtableByteString x, BigtableByteString y)

Compares two [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString) values lexicographically.

**Parameters**  
---  
**Name** | **Description**  
`x` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString)`  
Left value to compare  
`y` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString)`  
Right value to compare  
**Returns**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` | true if `x` is less than `y`; otherwise false.  
  
### CompareTo(BigtableByteString)
    
    
    public int CompareTo(BigtableByteString other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### CompareTo(object)
    
    
    public int CompareTo(object obj)

**Parameter**  
---  
**Name** | **Description**  
`obj` | `[object](https://learn.microsoft.com/dotnet/api/system.object)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### GetEnumerator()
    
    
    public IEnumerator<byte> GetEnumerator()

**Returns**  
---  
**Type** | **Description**  
`[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1)[byte](https://learn.microsoft.com/dotnet/api/system.byte)` |   
  
### GetHashCode()
    
    
    public override int GetHashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
**Overrides**

[ValueType.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.valuetype.gethashcode)

### ToString()
    
    
    public override string ToString()

**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Overrides**

[ValueType.ToString()](https://learn.microsoft.com/dotnet/api/system.valuetype.tostring)

## Operators 

### operator ==(BigtableByteString, BigtableByteString)
    
    
    public static bool operator ==(BigtableByteString x, BigtableByteString y)

Operator overload to compare two [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString) values for equality.

**Parameters**  
---  
**Name** | **Description**  
`x` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString)`  
Left value to compare  
`y` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString)`  
Right value to compare  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if `x` is equal to `y`; otherwise false.  
  
### explicit operator ByteString(BigtableByteString)
    
    
    public static explicit operator ByteString(BigtableByteString value)

Converts the [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString) value to its underlying byte string.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString)`  
The BigtableByteString value to convert.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)` |   
  
### explicit operator byte[](BigtableByteString)
    
    
    public static explicit operator byte[](BigtableByteString value)

Converts the [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString) value to its underlying byte array.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString)`  
The BigtableByteString value to convert.  
**Returns**  
---  
**Type** | **Description**  
`[byte](https://learn.microsoft.com/dotnet/api/system.byte)` |   
  
### explicit operator long(BigtableByteString)
    
    
    public static explicit operator long(BigtableByteString value)

Converts the [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString) value to its a signed 64-bit value assuming it is big-endian encoded.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString)`  
The BigtableByteString value to convert.  
**Returns**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### explicit operator string(BigtableByteString)
    
    
    public static explicit operator string(BigtableByteString value)

Converts the [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString) value to a string assuming it is UTF-8 encoded.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString)`  
The BigtableByteString value to convert.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### operator >(BigtableByteString, BigtableByteString)
    
    
    public static bool operator >(BigtableByteString x, BigtableByteString y)

Operator overload to compare two [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString) values.

**Parameters**  
---  
**Name** | **Description**  
`x` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString)`  
Left value to compare  
`y` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString)`  
Right value to compare  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if `x` is greater than `y`; otherwise false.  
  
### operator >=(BigtableByteString, BigtableByteString)
    
    
    public static bool operator >=(BigtableByteString x, BigtableByteString y)

Operator overload to compare two [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString) values.

**Parameters**  
---  
**Name** | **Description**  
`x` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString)`  
Left value to compare  
`y` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString)`  
Right value to compare  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if `x` is greater than or equal `y`; otherwise false.  
  
### implicit operator BigtableByteString(ByteString)
    
    
    public static implicit operator BigtableByteString(ByteString value)

Converts a byte string to a [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString) value.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)`  
The byte string making up the value. May be null in which case the empty byte string is used.  
**Returns**  
---  
**Type** | **Description**  
`[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString)` |   
  
### implicit operator BigtableByteString(byte[])
    
    
    public static implicit operator BigtableByteString(byte[] value)

Converts a byte array to a [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString) value.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[byte](https://learn.microsoft.com/dotnet/api/system.byte)`  
The bytes making up the byte string. May be null in which case the empty byte string is used.  
**Returns**  
---  
**Type** | **Description**  
`[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString)` |   
  
### implicit operator BigtableByteString(long)
    
    
    public static implicit operator BigtableByteString(long value)

Converts the big-endian encoding of a signed 64-bit value to a [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString) value.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[long](https://learn.microsoft.com/dotnet/api/system.int64)`  
The 64-bit value which should be used to initialize the byte string.  
**Returns**  
---  
**Type** | **Description**  
`[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString)` |   
  
### implicit operator BigtableByteString(string)
    
    
    public static implicit operator BigtableByteString(string valueAsUtf8)

Converts the UTF-8 encoding of a string to a [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString) value.

**Parameter**  
---  
**Name** | **Description**  
`valueAsUtf8` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The value whose UTF-8 representation should be used to initialize the byte string. May be null in which case the empty byte string is used.  
**Returns**  
---  
**Type** | **Description**  
`[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString)` |   
  
### operator !=(BigtableByteString, BigtableByteString)
    
    
    public static bool operator !=(BigtableByteString x, BigtableByteString y)

Operator overload to compare two [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString) values for inequality.

**Parameters**  
---  
**Name** | **Description**  
`x` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString)`  
Left value to compare  
`y` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString)`  
Right value to compare  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if `x` is not equal to `y`; otherwise false.  
  
### operator <(BigtableByteString, BigtableByteString)
    
    
    public static bool operator <(BigtableByteString x, BigtableByteString y)

Operator overload to compare two [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString) values.

**Parameters**  
---  
**Name** | **Description**  
`x` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString)`  
Left value to compare  
`y` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString)`  
Right value to compare  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if `x` is less than `y`; otherwise false.  
  
### operator <=(BigtableByteString, BigtableByteString)
    
    
    public static bool operator <=(BigtableByteString x, BigtableByteString y)

Operator overload to compare two [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString) values.

**Parameters**  
---  
**Name** | **Description**  
`x` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString)`  
Left value to compare  
`y` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString)`  
Right value to compare  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if `x` is less than or equal `y`; otherwise false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
