---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.TimeSeriesDescriptor.Types.ValueDescriptor
title: Google Cloud Monitoring v3 API - Class TimeSeriesDescriptor.Types.ValueDescriptor (3.16.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:22:48.262983+00:00
---

# Google Cloud Monitoring v3 API - Class TimeSeriesDescriptor.Types.ValueDescriptor (3.16.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.TimeSeriesDescriptor.Types.ValueDescriptor

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Monitoring v3 API - Class TimeSeriesDescriptor.Types.ValueDescriptor (3.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.16.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.TimeSeriesDescriptor.Types.ValueDescriptor)
  * [ 3.15.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.15.0/Google.Cloud.Monitoring.V3.TimeSeriesDescriptor.Types.ValueDescriptor)
  * [ 3.14.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.14.0/Google.Cloud.Monitoring.V3.TimeSeriesDescriptor.Types.ValueDescriptor)
  * [ 3.13.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.13.0/Google.Cloud.Monitoring.V3.TimeSeriesDescriptor.Types.ValueDescriptor)
  * [ 3.12.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.12.0/Google.Cloud.Monitoring.V3.TimeSeriesDescriptor.Types.ValueDescriptor)
  * [ 3.11.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.11.0/Google.Cloud.Monitoring.V3.TimeSeriesDescriptor.Types.ValueDescriptor)
  * [ 3.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.10.0/Google.Cloud.Monitoring.V3.TimeSeriesDescriptor.Types.ValueDescriptor)
  * [ 3.9.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.9.0/Google.Cloud.Monitoring.V3.TimeSeriesDescriptor.Types.ValueDescriptor)
  * [ 3.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.8.0/Google.Cloud.Monitoring.V3.TimeSeriesDescriptor.Types.ValueDescriptor)
  * [ 3.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.7.0/Google.Cloud.Monitoring.V3.TimeSeriesDescriptor.Types.ValueDescriptor)
  * [ 3.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.6.0/Google.Cloud.Monitoring.V3.TimeSeriesDescriptor.Types.ValueDescriptor)
  * [ 3.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.5.0/Google.Cloud.Monitoring.V3.TimeSeriesDescriptor.Types.ValueDescriptor)
  * [ 3.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.4.0/Google.Cloud.Monitoring.V3.TimeSeriesDescriptor.Types.ValueDescriptor)
  * [ 3.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.3.0/Google.Cloud.Monitoring.V3.TimeSeriesDescriptor.Types.ValueDescriptor)
  * [ 3.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.2.0/Google.Cloud.Monitoring.V3.TimeSeriesDescriptor.Types.ValueDescriptor)
  * [ 3.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.1.0/Google.Cloud.Monitoring.V3.TimeSeriesDescriptor.Types.ValueDescriptor)
  * [ 3.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.0.0/Google.Cloud.Monitoring.V3.TimeSeriesDescriptor.Types.ValueDescriptor)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/2.6.0/Google.Cloud.Monitoring.V3.TimeSeriesDescriptor.Types.ValueDescriptor)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/2.5.0/Google.Cloud.Monitoring.V3.TimeSeriesDescriptor.Types.ValueDescriptor)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/2.4.0/Google.Cloud.Monitoring.V3.TimeSeriesDescriptor.Types.ValueDescriptor)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/2.3.0/Google.Cloud.Monitoring.V3.TimeSeriesDescriptor.Types.ValueDescriptor)


    
    
    public sealed class TimeSeriesDescriptor.Types.ValueDescriptor : IMessage<TimeSeriesDescriptor.Types.ValueDescriptor>, IEquatable<TimeSeriesDescriptor.Types.ValueDescriptor>, IDeepCloneable<TimeSeriesDescriptor.Types.ValueDescriptor>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Monitoring v3 API class TimeSeriesDescriptor.Types.ValueDescriptor.

A descriptor for the value columns in a data point.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > TimeSeriesDescriptor.Types.ValueDescriptor

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[TimeSeriesDescriptor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.TimeSeriesDescriptor)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.TimeSeriesDescriptor.Types)[ValueDescriptor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.TimeSeriesDescriptor.Types.ValueDescriptor), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[TimeSeriesDescriptor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.TimeSeriesDescriptor)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.TimeSeriesDescriptor.Types)[ValueDescriptor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.TimeSeriesDescriptor.Types.ValueDescriptor), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[TimeSeriesDescriptor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.TimeSeriesDescriptor)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.TimeSeriesDescriptor.Types)[ValueDescriptor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.TimeSeriesDescriptor.Types.ValueDescriptor), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Monitoring.V3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3)

## Assembly

Google.Cloud.Monitoring.V3.dll

## Constructors 

### ValueDescriptor()
    
    
    public ValueDescriptor()

### ValueDescriptor(ValueDescriptor)
    
    
    public ValueDescriptor(TimeSeriesDescriptor.Types.ValueDescriptor other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[TimeSeriesDescriptor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.TimeSeriesDescriptor)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.TimeSeriesDescriptor.Types)[ValueDescriptor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.TimeSeriesDescriptor.Types.ValueDescriptor)`  
  
  
## Properties 

### Key
    
    
    public string Key { get; set; }

The value key.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### MetricKind
    
    
    public MetricDescriptor.Types.MetricKind MetricKind { get; set; }

The value stream kind.

**Property Value**  
---  
**Type** | **Description**  
`[MetricDescriptor](https://cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.MetricDescriptor.html)[Types](https://cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.MetricDescriptor.Types.html)[MetricKind](https://cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.MetricDescriptor.Types.MetricKind.html)` |   
  
### Unit
    
    
    public string Unit { get; set; }

The unit in which `time_series` point values are reported. `unit` follows the UCUM format for units as seen in <https://unitsofmeasure.org/ucum.html>. `unit` is only valid if `value_type` is INTEGER, DOUBLE, DISTRIBUTION.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ValueType
    
    
    public MetricDescriptor.Types.ValueType ValueType { get; set; }

The value type.

**Property Value**  
---  
**Type** | **Description**  
`[MetricDescriptor](https://cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.MetricDescriptor.html)[Types](https://cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.MetricDescriptor.Types.html)[ValueType](https://cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.MetricDescriptor.Types.ValueType.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
