---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersionRange
title: Google Bigtable v2 API - Class BigtableVersionRange (3.33.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:42:42.495580+00:00
---

# Google Bigtable v2 API - Class BigtableVersionRange (3.33.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersionRange

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Bigtable v2 API - Class BigtableVersionRange (3.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.33.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public class BigtableVersionRange : IEquatable<BigtableVersionRange>

Reference documentation and code samples for the Google Bigtable v2 API class BigtableVersionRange.

A contiguous range of versions.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > BigtableVersionRange

## Implements

[IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[BigtableVersionRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersionRange)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

## Namespace

[Google.Cloud.Bigtable.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2)

## Assembly

Google.Cloud.Bigtable.V2.dll

## Remarks

Note: version values are stored on the server as if they are microseconds since the Unix epoch. However, the server only supports millisecond granularity, so the server only allows microseconds in multiples of 1,000. [BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion) attempts to hide this complexity by exposing its underlying [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion#Google_Cloud_Bigtable_V2_BigtableVersion_Value) in terms of milliseconds, so if desired, a custom versioning scheme of 1, 2, ... can be used rather than 1000, 2000, ... However, access to the underlying microsecond value is still provided via [Micros](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion#Google_Cloud_Bigtable_V2_BigtableVersion_Micros). 

Note: when using ReadModifyWriteRow, modified columns automatically use a server version, which is based on the current timestamp since the Unix epoch. For those columns, other reads and writes should use [BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion) values constructed from DateTime values, as opposed to using a custom versioning scheme with 64-bit values. 

## Constructors 

### BigtableVersionRange(BigtableVersion?, BigtableVersion?)
    
    
    public BigtableVersionRange(BigtableVersion? start, BigtableVersion? end)

Creates a new [BigtableVersionRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersionRange).

**Parameters**  
---  
**Name** | **Description**  
`start` | `[BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion)`  
Inclusive lower bound. If null, interpreted as 0.  
`end` | `[BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion)`  
Exclusive upper bound. If null, interpreted as infinity.  
  
### BigtableVersionRange(DateTime?, DateTime?)
    
    
    public BigtableVersionRange(DateTime? startTimestamp, DateTime? endTimestamp)

Creates a new [BigtableVersionRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersionRange).

**Parameters**  
---  
**Name** | **Description**  
`startTimestamp` | `[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)`  
Inclusive lower bound timestamp whose milliseconds since the Unix epoch should be used as the version value. If null, interpreted as 0. It must be specified in UTC.  
`endTimestamp` | `[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)`  
Exclusive upper bound timestamp whose milliseconds since the Unix epoch should be used as the version value. If null, interpreted as infinity. It must be specified in UTC.  
**Remarks**

Note: version values are stored on the server as if they are microseconds since the Unix epoch. However, the server only supports millisecond granularity, so the server only allows microseconds in multiples of 1,000. [BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion) attempts to hide this complexity by exposing its underlying [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion#Google_Cloud_Bigtable_V2_BigtableVersion_Value) in terms of milliseconds, so if desired, a custom versioning scheme of 1, 2, ... can be used rather than 1000, 2000, ... However, access to the underlying microsecond value is still provided via [Micros](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion#Google_Cloud_Bigtable_V2_BigtableVersion_Micros). 

Note: when using ReadModifyWriteRow, modified columns automatically use a server version, which is based on the current timestamp since the Unix epoch. For those columns, other reads and writes should use [BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion) values constructed from DateTime values, as opposed to using a custom versioning scheme with 64-bit values. 

### BigtableVersionRange(long?, long?)
    
    
    public BigtableVersionRange(long? start, long? end)

Creates a new [BigtableVersionRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersionRange).

**Parameters**  
---  
**Name** | **Description**  
`start` | `[long](https://learn.microsoft.com/dotnet/api/system.int64)`  
Inclusive lower bound non-negative version value, or -1 to initialize from the milliseconds of DateTime.UtcNow. Must be less than or equal to 9223372036854775. If null, interpreted as 0.  
`end` | `[long](https://learn.microsoft.com/dotnet/api/system.int64)`  
Exclusive upper bound non-negative version value, or -1 to initialize from the milliseconds of DateTime.UtcNow. Must be less than or equal to 9223372036854775. If null, interpreted as infinity.  
**Remarks**

Note: version values are stored on the server as if they are microseconds since the Unix epoch. However, the server only supports millisecond granularity, so the server only allows microseconds in multiples of 1,000. [BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion) attempts to hide this complexity by exposing its underlying [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion#Google_Cloud_Bigtable_V2_BigtableVersion_Value) in terms of milliseconds, so if desired, a custom versioning scheme of 1, 2, ... can be used rather than 1000, 2000, ... However, access to the underlying microsecond value is still provided via [Micros](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion#Google_Cloud_Bigtable_V2_BigtableVersion_Micros). 

Note: when using ReadModifyWriteRow, modified columns automatically use a server version, which is based on the current timestamp since the Unix epoch. For those columns, other reads and writes should use [BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion) values constructed from DateTime values, as opposed to using a custom versioning scheme with 64-bit values. 

## Properties 

### End
    
    
    public BigtableVersion? End { get; }

Gets the exclusive upper bound. If null, interpreted as infinity.

**Property Value**  
---  
**Type** | **Description**  
`[BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion)` |   
  
### Start
    
    
    public BigtableVersion? Start { get; }

Gets the inclusive lower bound. If null, interpreted as 0.

**Property Value**  
---  
**Type** | **Description**  
`[BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion)` |   
  
## Methods 

### GetHashCode()
    
    
    public override int GetHashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
**Overrides**

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

### ToString()
    
    
    public override string ToString()

**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Overrides**

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
