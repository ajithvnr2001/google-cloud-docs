---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ColumnRange
title: Google Bigtable v2 API - Class ColumnRange (3.33.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:42:44.977556+00:00
---

# Google Bigtable v2 API - Class ColumnRange (3.33.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ColumnRange

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Bigtable v2 API - Class ColumnRange (3.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.33.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class ColumnRange : IMessage<ColumnRange>, IEquatable<ColumnRange>, IDeepCloneable<ColumnRange>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Bigtable v2 API class ColumnRange.

Specifies a contiguous range of columns within a single column family. The range spans from &lt;column_family&gt;:&lt;start_qualifier&gt; to &lt;column_family&gt;:&lt;end_qualifier&gt;, where both bounds can be either inclusive or exclusive.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ColumnRange

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ColumnRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ColumnRange), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ColumnRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ColumnRange), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ColumnRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ColumnRange), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Bigtable.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2)

## Assembly

Google.Cloud.Bigtable.V2.dll

## Constructors 

### ColumnRange()
    
    
    public ColumnRange()

### ColumnRange(ColumnRange)
    
    
    public ColumnRange(ColumnRange other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ColumnRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ColumnRange)`  
  
  
## Properties 

### EndQualifierCase
    
    
    public ColumnRange.EndQualifierOneofCase EndQualifierCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[ColumnRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ColumnRange)[EndQualifierOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ColumnRange.EndQualifierOneofCase)` |   
  
### EndQualifierClosed
    
    
    public ByteString EndQualifierClosed { get; set; }

Used when giving an inclusive upper bound for the range.

**Property Value**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)` |   
  
### EndQualifierOpen
    
    
    public ByteString EndQualifierOpen { get; set; }

Used when giving an exclusive upper bound for the range.

**Property Value**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)` |   
  
### FamilyName
    
    
    public string FamilyName { get; set; }

The name of the column family within which this range falls.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### HasEndQualifierClosed
    
    
    public bool HasEndQualifierClosed { get; }

Gets whether the "end_qualifier_closed" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasEndQualifierOpen
    
    
    public bool HasEndQualifierOpen { get; }

Gets whether the "end_qualifier_open" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasStartQualifierClosed
    
    
    public bool HasStartQualifierClosed { get; }

Gets whether the "start_qualifier_closed" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasStartQualifierOpen
    
    
    public bool HasStartQualifierOpen { get; }

Gets whether the "start_qualifier_open" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### StartQualifierCase
    
    
    public ColumnRange.StartQualifierOneofCase StartQualifierCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[ColumnRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ColumnRange)[StartQualifierOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ColumnRange.StartQualifierOneofCase)` |   
  
### StartQualifierClosed
    
    
    public ByteString StartQualifierClosed { get; set; }

Used when giving an inclusive lower bound for the range.

**Property Value**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)` |   
  
### StartQualifierOpen
    
    
    public ByteString StartQualifierOpen { get; set; }

Used when giving an exclusive lower bound for the range.

**Property Value**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)` |   
  
## Methods 

### Closed(string, BigtableByteString?, BigtableByteString?)
    
    
    public static ColumnRange Closed(string familyName, BigtableByteString? startQualifierClosed, BigtableByteString? endQualifierClosed)

Creates a [ColumnRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ColumnRange) instance with inclusive bounds.

**Parameters**  
---  
**Name** | **Description**  
`familyName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the column family within which this range falls. Must match `[-_.a-zA-Z0-9]+`  
`startQualifierClosed` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html)`  
The inclusive lower bound for the range. If null or empty, it is interpreted as the empty string.  
`endQualifierClosed` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html)`  
The inclusive upper bound for the range. If null or empty, it is interpreted as the infinite qualifier.  
**Returns**  
---  
**Type** | **Description**  
`[ColumnRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ColumnRange)` | The created range.  
**Remarks**

Note that string is implicitly convertible to [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html), so the ranges can be specified using strings as well and their UTF-8 representations will be used for the qualifier. 

### ClosedOpen(string, BigtableByteString?, BigtableByteString?)
    
    
    public static ColumnRange ClosedOpen(string familyName, BigtableByteString? startQualifierClosed, BigtableByteString? endQualifierOpen)

Creates a [ColumnRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ColumnRange) instance with an inclusive lower bound and an exclusive upper bound.

**Parameters**  
---  
**Name** | **Description**  
`familyName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the column family within which this range falls. Must match `[-_.a-zA-Z0-9]+`  
`startQualifierClosed` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html)`  
The inclusive lower bound for the range. If null or empty, it is interpreted as the empty string.  
`endQualifierOpen` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html)`  
The exclusive upper bound for the range. If null or empty, it is interpreted as the infinite qualifier.  
**Returns**  
---  
**Type** | **Description**  
`[ColumnRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ColumnRange)` | The created range.  
**Remarks**

Note that string is implicitly convertible to [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html), so the ranges can be specified using strings as well and their UTF-8 representations will be used for the qualifier. 

### Open(string, BigtableByteString?, BigtableByteString?)
    
    
    public static ColumnRange Open(string familyName, BigtableByteString? startQualifierOpen, BigtableByteString? endQualifierOpen)

Creates a [ColumnRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ColumnRange) instance with exclusive bounds.

**Parameters**  
---  
**Name** | **Description**  
`familyName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the column family within which this range falls. Must match `[-_.a-zA-Z0-9]+`  
`startQualifierOpen` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html)`  
The exclusive lower bound for the range. If null or empty, it is interpreted as the empty string.  
`endQualifierOpen` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html)`  
The exclusive upper bound for the range. If null or empty, it is interpreted as the infinite qualifier.  
**Returns**  
---  
**Type** | **Description**  
`[ColumnRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ColumnRange)` | The created range.  
**Remarks**

Note that string is implicitly convertible to [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html), so the ranges can be specified using strings as well and their UTF-8 representations will be used for the qualifier. 

### OpenClosed(string, BigtableByteString?, BigtableByteString?)
    
    
    public static ColumnRange OpenClosed(string familyName, BigtableByteString? startQualifierOpen, BigtableByteString? endQualifierClosed)

Creates a [ColumnRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ColumnRange) instance with an exclusive lower bound and an inclusive upper bound.

**Parameters**  
---  
**Name** | **Description**  
`familyName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the column family within which this range falls. Must match `[-_.a-zA-Z0-9]+`  
`startQualifierOpen` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html)`  
The exclusive lower bound for the range. If null or empty, it is interpreted as the empty string.  
`endQualifierClosed` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html)`  
The inclusive upper bound for the range. If null or empty, it is interpreted as the infinite qualifier.  
**Returns**  
---  
**Type** | **Description**  
`[ColumnRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ColumnRange)` | The created range.  
**Remarks**

Note that string is implicitly convertible to [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html), so the ranges can be specified using strings as well and their UTF-8 representations will be used for the qualifier. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
