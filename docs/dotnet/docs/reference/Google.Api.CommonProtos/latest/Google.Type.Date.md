---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Date
title: Class Date (2.17.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:59:11.129042+00:00
---

# Class Date (2.17.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Date

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Class Date (2.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.17.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Date)
  * [ 2.15.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.15.0/Google.Type.Date)
  * [ 2.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.10.0/Google.Type.Date)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.2.0/Google.Type.Date)


    
    
    public sealed class Date : IMessage<Date>, IEquatable<Date>, IDeepCloneable<Date>, IBufferMessage, IMessage

Represents a whole or partial calendar date, such as a birthday. The time of day and time zone are either specified elsewhere or are insignificant. The date is relative to the Gregorian Calendar. This can represent one of the following:

  * A full date, with non-zero year, month, and day values
  * A month and day value, with a zero year, such as an anniversary
  * A year on its own, with zero month and day values
  * A year and month value, with a zero day, such as a credit card expiration date



Related types are [google.type.TimeOfDay][google.type.TimeOfDay] and `google.protobuf.Timestamp`.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Date

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Date](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Date), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Date](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Date), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Date](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Date), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals\(system-object-system-object\))

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals)

## Namespace

[Google.Type](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type)

## Assembly

Google.Api.CommonProtos.dll

## Constructors 

### Date()
    
    
    public Date()

### Date(Date)
    
    
    public Date(Date other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Date](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Date)`  
  
  
## Fields 

### DayFieldNumber
    
    
    public const int DayFieldNumber = 3

Field number for the "day" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### MonthFieldNumber
    
    
    public const int MonthFieldNumber = 2

Field number for the "month" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### YearFieldNumber
    
    
    public const int YearFieldNumber = 1

Field number for the "year" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
## Properties 

### Day
    
    
    public int Day { get; set; }

Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn't significant.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### Descriptor
    
    
    public static MessageDescriptor Descriptor { get; }

**Property Value**  
---  
**Type** | **Description**  
`[MessageDescriptor](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Reflection.MessageDescriptor.html)` |   
  
### Month
    
    
    public int Month { get; set; }

Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### Parser
    
    
    public static MessageParser<Date> Parser { get; }

**Property Value**  
---  
**Type** | **Description**  
`[MessageParser](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.MessageParser-1.html)[Date](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Date)` |   
  
### Year
    
    
    public int Year { get; set; }

Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
## Methods 

### CalculateSize()
    
    
    public int CalculateSize()

**Returns**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### Clone()
    
    
    public Date Clone()

**Returns**  
---  
**Type** | **Description**  
`[Date](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Date)` |   
  
### Equals(Date)
    
    
    public bool Equals(Date other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Date](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Date)`  
  
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

### FromDateTime(DateTime)
    
    
    public static Date FromDateTime(DateTime dateTime)

Creates a [Date](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Date) instance from the [Date](https://learn.microsoft.com/dotnet/api/system.datetime.date) part of [DateTime](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.DateTime).

**Parameter**  
---  
**Name** | **Description**  
`dateTime` | `[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)`  
The [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime) value being converted.  
**Returns**  
---  
**Type** | **Description**  
`[Date](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Date)` | The created [Date](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Date).  
  
### FromDateTimeOffset(DateTimeOffset)
    
    
    public static Date FromDateTimeOffset(DateTimeOffset dateTimeOffset)

Creates a [Date](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Date) instance from the [Date](https://learn.microsoft.com/dotnet/api/system.datetimeoffset.date) part of [DateTimeOffset](https://learn.microsoft.com/dotnet/api/system.datetimeoffset).

**Parameter**  
---  
**Name** | **Description**  
`dateTimeOffset` | `[DateTimeOffset](https://learn.microsoft.com/dotnet/api/system.datetimeoffset)`  
The [DateTimeOffset](https://learn.microsoft.com/dotnet/api/system.datetimeoffset) value being converted.  
**Returns**  
---  
**Type** | **Description**  
`[Date](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Date)` | The created [Date](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Date).  
  
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
  
  
### MergeFrom(Date)
    
    
    public void MergeFrom(Date other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Date](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Date)`  
  
  
### ToDateTime()
    
    
    public DateTime ToDateTime()

Converts [Date](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Date) to [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime).

**Returns**  
---  
**Type** | **Description**  
`[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)` | The converted [DateTime](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.DateTime) with time at midnight and [Kind](https://learn.microsoft.com/dotnet/api/system.datetime.kind) of [Unspecified](https://learn.microsoft.com/dotnet/api/system.datetimekind#system-datetimekind-unspecified).  
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidOperationException](https://learn.microsoft.com/dotnet/api/system.invalidoperationexception)` | Thrown when [Year](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Date#Google_Type_Date_Year), [Month](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Date#Google_Type_Date_Month), and/or [Day](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Date#Google_Type_Date_Day) are not within the valid range.  
  
### ToDateTimeOffset()
    
    
    public DateTimeOffset ToDateTimeOffset()

Converts [Date](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Date) to [DateTimeOffset](https://learn.microsoft.com/dotnet/api/system.datetimeoffset).

**Returns**  
---  
**Type** | **Description**  
`[DateTimeOffset](https://learn.microsoft.com/dotnet/api/system.datetimeoffset)` | The converted [DateTimeOffset](https://learn.microsoft.com/dotnet/api/system.datetimeoffset) with time at midnight, [Kind](https://learn.microsoft.com/dotnet/api/system.datetime.kind) of [Unspecified](https://learn.microsoft.com/dotnet/api/system.datetimekind#system-datetimekind-unspecified), and an [Offset](https://learn.microsoft.com/dotnet/api/system.datetimeoffset.offset) of [Zero](https://learn.microsoft.com/dotnet/api/system.timespan.zero).  
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidOperationException](https://learn.microsoft.com/dotnet/api/system.invalidoperationexception)` | Thrown when [Year](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Date#Google_Type_Date_Year), [Month](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Date#Google_Type_Date_Month), and/or [Day](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Date#Google_Type_Date_Day) are not within the valid range.  
  
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
