---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowRange
title: Google Bigtable v2 API - Class RowRange (3.33.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:43:06.923125+00:00
---

# Google Bigtable v2 API - Class RowRange (3.33.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowRange

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Bigtable v2 API - Class RowRange (3.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.33.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class RowRange : IMessage<RowRange>, IEquatable<RowRange>, IDeepCloneable<RowRange>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Bigtable v2 API class RowRange.

Specifies a contiguous range of rows.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > RowRange

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[RowRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowRange), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[RowRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowRange), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[RowRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowRange), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Bigtable.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2)

## Assembly

Google.Cloud.Bigtable.V2.dll

## Constructors 

### RowRange()
    
    
    public RowRange()

### RowRange(RowRange)
    
    
    public RowRange(RowRange other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[RowRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowRange)`  
  
  
## Properties 

### EndKeyCase
    
    
    public RowRange.EndKeyOneofCase EndKeyCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[RowRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowRange)[EndKeyOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowRange.EndKeyOneofCase)` |   
  
### EndKeyClosed
    
    
    public ByteString EndKeyClosed { get; set; }

Used when giving an inclusive upper bound for the range.

**Property Value**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)` |   
  
### EndKeyOpen
    
    
    public ByteString EndKeyOpen { get; set; }

Used when giving an exclusive upper bound for the range.

**Property Value**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)` |   
  
### HasEndKeyClosed
    
    
    public bool HasEndKeyClosed { get; }

Gets whether the "end_key_closed" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasEndKeyOpen
    
    
    public bool HasEndKeyOpen { get; }

Gets whether the "end_key_open" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasStartKeyClosed
    
    
    public bool HasStartKeyClosed { get; }

Gets whether the "start_key_closed" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasStartKeyOpen
    
    
    public bool HasStartKeyOpen { get; }

Gets whether the "start_key_open" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### StartKeyCase
    
    
    public RowRange.StartKeyOneofCase StartKeyCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[RowRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowRange)[StartKeyOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowRange.StartKeyOneofCase)` |   
  
### StartKeyClosed
    
    
    public ByteString StartKeyClosed { get; set; }

Used when giving an inclusive lower bound for the range.

**Property Value**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)` |   
  
### StartKeyOpen
    
    
    public ByteString StartKeyOpen { get; set; }

Used when giving an exclusive lower bound for the range.

**Property Value**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)` |   
  
## Methods 

### Closed(BigtableByteString?, BigtableByteString?)
    
    
    public static RowRange Closed(BigtableByteString? startKeyClosed, BigtableByteString? endKeyClosed)

Creates a [RowRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowRange) instance with inclusive bounds.

**Parameters**  
---  
**Name** | **Description**  
`startKeyClosed` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html)`  
The inclusive lower bound for the range. If null or empty, it is interpreted as the empty string.  
`endKeyClosed` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html)`  
The inclusive upper bound for the range. If null or empty, it is interpreted as the infinite row key.  
**Returns**  
---  
**Type** | **Description**  
`[RowRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowRange)` | The created range.  
**Remarks**

Note that string is implicitly convertible to [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html), so the ranges can be specified using strings as well and their UTF-8 representations will be used for the key. 

### ClosedOpen(BigtableByteString?, BigtableByteString?)
    
    
    public static RowRange ClosedOpen(BigtableByteString? startKeyClosed, BigtableByteString? endKeyOpen)

Creates a [RowRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowRange) instance with an inclusive lower bound and an exclusive upper bound.

**Parameters**  
---  
**Name** | **Description**  
`startKeyClosed` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html)`  
The inclusive lower bound for the range. If null or empty, it is interpreted as the empty string.  
`endKeyOpen` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html)`  
The exclusive upper bound for the range. If null or empty, it is interpreted as the infinite row key.  
**Returns**  
---  
**Type** | **Description**  
`[RowRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowRange)` | The created range.  
**Remarks**

Note that string is implicitly convertible to [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html), so the ranges can be specified using strings as well and their UTF-8 representations will be used for the key. 

### Open(BigtableByteString?, BigtableByteString?)
    
    
    public static RowRange Open(BigtableByteString? startKeyOpen, BigtableByteString? endKeyOpen)

Creates a [RowRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowRange) instance with exclusive bounds.

**Parameters**  
---  
**Name** | **Description**  
`startKeyOpen` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html)`  
The exclusive lower bound for the range. If null or empty, it is interpreted as the empty string.  
`endKeyOpen` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html)`  
The exclusive upper bound for the range. If null or empty, it is interpreted as the infinite row key.  
**Returns**  
---  
**Type** | **Description**  
`[RowRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowRange)` | The created range.  
**Remarks**

Note that string is implicitly convertible to [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html), so the ranges can be specified using strings as well and their UTF-8 representations will be used for the key. 

### OpenClosed(BigtableByteString?, BigtableByteString?)
    
    
    public static RowRange OpenClosed(BigtableByteString? startKeyOpen, BigtableByteString? endKeyClosed)

Creates a [RowRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowRange) instance with an exclusive lower bound and an inclusive upper bound.

**Parameters**  
---  
**Name** | **Description**  
`startKeyOpen` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html)`  
The exclusive lower bound for the range. If null or empty, it is interpreted as the empty string.  
`endKeyClosed` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html)`  
The inclusive upper bound for the range. If null or empty, it is interpreted as the infinite row key.  
**Returns**  
---  
**Type** | **Description**  
`[RowRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowRange)` | The created range.  
**Remarks**

Note that string is implicitly convertible to [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html), so the ranges can be specified using strings as well and their UTF-8 representations will be used for the key. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
