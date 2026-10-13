---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion
title: Google Bigtable v2 API - Struct BigtableVersion (3.33.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:42:42.107381+00:00
---

# Google Bigtable v2 API - Struct BigtableVersion (3.33.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Bigtable v2 API - Struct BigtableVersion (3.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.33.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public struct BigtableVersion : IComparable, IComparable<BigtableVersion>, IEquatable<BigtableVersion>

Reference documentation and code samples for the Google Bigtable v2 API struct BigtableVersion.

A version which uniquely identifies a cell within a column.

## Implements

[IComparable](https://learn.microsoft.com/dotnet/api/system.icomparable), [IComparable](https://learn.microsoft.com/dotnet/api/system.icomparable-1)[BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.Bigtable.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2)

## Assembly

Google.Cloud.Bigtable.V2.dll

## Remarks

Note: version values are stored on the server as if they are microseconds since the Unix epoch. However, the server only supports millisecond granularity, so the server only allows microseconds in multiples of 1,000. [BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion) attempts to hide this complexity by exposing its underlying [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion#Google_Cloud_Bigtable_V2_BigtableVersion_Value) in terms of milliseconds, so if desired, a custom versioning scheme of 1, 2, ... can be used rather than 1000, 2000, ... However, access to the underlying microsecond value is still provided via [Micros](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion#Google_Cloud_Bigtable_V2_BigtableVersion_Micros). 

Note: when using ReadModifyWriteRow, modified columns automatically use a server version, which is based on the current timestamp since the Unix epoch. For those columns, other reads and writes should use [BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion) values constructed from DateTime values, as opposed to using a custom versioning scheme with 64-bit values. 

## Constructors 

### BigtableVersion(DateTime)
    
    
    public BigtableVersion(DateTime timestamp)

Creates a new [BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion) value from the milliseconds of a timestamp since the Unix epoch.

**Parameter**  
---  
**Name** | **Description**  
`timestamp` | `[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)`  
The timestamp whose milliseconds since the Unix epoch should be used as the version value. It must be specified in UTC.  
**Remarks**

Note: version values are stored on the server as if they are microseconds since the Unix epoch. However, the server only supports millisecond granularity, so the server only allows microseconds in multiples of 1,000. [BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion) attempts to hide this complexity by exposing its underlying [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion#Google_Cloud_Bigtable_V2_BigtableVersion_Value) in terms of milliseconds, so if desired, a custom versioning scheme of 1, 2, ... can be used rather than 1000, 2000, ... However, access to the underlying microsecond value is still provided via [Micros](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion#Google_Cloud_Bigtable_V2_BigtableVersion_Micros). 

Note: when using ReadModifyWriteRow, modified columns automatically use a server version, which is based on the current timestamp since the Unix epoch. For those columns, other reads and writes should use [BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion) values constructed from DateTime values, as opposed to using a custom versioning scheme with 64-bit values. 

### BigtableVersion(long)
    
    
    public BigtableVersion(long value)

Creates a new [BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion) value from a 64-bit value.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[long](https://learn.microsoft.com/dotnet/api/system.int64)`  
The non-negative version value, or -1 to initialize from the milliseconds of DateTime.UtcNow. Must be less than or equal to 9223372036854775.  
**Remarks**

Note: version values are stored on the server as if they are microseconds since the Unix epoch. However, the server only supports millisecond granularity, so the server only allows microseconds in multiples of 1,000. [BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion) attempts to hide this complexity by exposing its underlying [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion#Google_Cloud_Bigtable_V2_BigtableVersion_Value) in terms of milliseconds, so if desired, a custom versioning scheme of 1, 2, ... can be used rather than 1000, 2000, ... However, access to the underlying microsecond value is still provided via [Micros](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion#Google_Cloud_Bigtable_V2_BigtableVersion_Micros). 

Note: when using ReadModifyWriteRow, modified columns automatically use a server version, which is based on the current timestamp since the Unix epoch. For those columns, other reads and writes should use [BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion) values constructed from DateTime values, as opposed to using a custom versioning scheme with 64-bit values. 

## Properties 

### Micros
    
    
    public long Micros { get; }

Gets the version value interpreted as microseconds of a timestamp since the Unix epoch. Greater version values indicate newer cell values.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### Value
    
    
    public long Value { get; }

Gets the version value. Greater version values indicate newer cell values.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
**Remarks**

If timestamps are used as versions, this would be the milliseconds since the Unix epoch.

## Methods 

### Compare(BigtableVersion?, BigtableVersion?)
    
    
    public static int Compare(BigtableVersion? x, BigtableVersion? y)

Compares two nullable [BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion) values.

**Parameters**  
---  
**Name** | **Description**  
`x` | `[BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion)`  
Left value to compare  
`y` | `[BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion)`  
Right value to compare  
**Returns**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` | true if `x` is less than `y`; otherwise false.  
  
### CompareTo(BigtableVersion)
    
    
    public int CompareTo(BigtableVersion other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion)`  
  
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
  
### GetHashCode()
    
    
    public override int GetHashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
**Overrides**

[ValueType.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.valuetype.gethashcode)

### ToDateTime()
    
    
    public DateTime ToDateTime()

Gets the DateTime equivalent to the version assuming the value is a timestamp milliseconds value since the Unix epoch.

**Returns**  
---  
**Type** | **Description**  
`[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)` | The DateTime representing the version timestamp.  
  
### ToString()
    
    
    public override string ToString()

**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Overrides**

[ValueType.ToString()](https://learn.microsoft.com/dotnet/api/system.valuetype.tostring)

## Operators 

### operator ==(BigtableVersion, BigtableVersion)
    
    
    public static bool operator ==(BigtableVersion x, BigtableVersion y)

Operator overload to compare two [BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion) values for equality.

**Parameters**  
---  
**Name** | **Description**  
`x` | `[BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion)`  
Left value to compare  
`y` | `[BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion)`  
Right value to compare  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if `x` is equal to `y`; otherwise false.  
  
### operator >(BigtableVersion, BigtableVersion)
    
    
    public static bool operator >(BigtableVersion x, BigtableVersion y)

Operator overload to compare two [BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion) values.

**Parameters**  
---  
**Name** | **Description**  
`x` | `[BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion)`  
Left value to compare  
`y` | `[BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion)`  
Right value to compare  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if `x` is greater than `y`; otherwise false.  
  
### operator >=(BigtableVersion, BigtableVersion)
    
    
    public static bool operator >=(BigtableVersion x, BigtableVersion y)

Operator overload to compare two [BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion) values.

**Parameters**  
---  
**Name** | **Description**  
`x` | `[BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion)`  
Left value to compare  
`y` | `[BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion)`  
Right value to compare  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if `x` is greater than or equal `y`; otherwise false.  
  
### operator !=(BigtableVersion, BigtableVersion)
    
    
    public static bool operator !=(BigtableVersion x, BigtableVersion y)

Operator overload to compare two [BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion) values for inequality.

**Parameters**  
---  
**Name** | **Description**  
`x` | `[BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion)`  
Left value to compare  
`y` | `[BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion)`  
Right value to compare  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if `x` is not equal to `y`; otherwise false.  
  
### operator <(BigtableVersion, BigtableVersion)
    
    
    public static bool operator <(BigtableVersion x, BigtableVersion y)

Operator overload to compare two [BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion) values.

**Parameters**  
---  
**Name** | **Description**  
`x` | `[BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion)`  
Left value to compare  
`y` | `[BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion)`  
Right value to compare  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if `x` is less than `y`; otherwise false.  
  
### operator <=(BigtableVersion, BigtableVersion)
    
    
    public static bool operator <=(BigtableVersion x, BigtableVersion y)

Operator overload to compare two [BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion) values.

**Parameters**  
---  
**Name** | **Description**  
`x` | `[BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion)`  
Left value to compare  
`y` | `[BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion)`  
Right value to compare  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if `x` is less than or equal `y`; otherwise false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
