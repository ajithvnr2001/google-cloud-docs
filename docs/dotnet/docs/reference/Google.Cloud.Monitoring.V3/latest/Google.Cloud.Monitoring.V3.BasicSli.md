---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.BasicSli
title: Google Cloud Monitoring v3 API - Class BasicSli (3.16.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:32:57.050126+00:00
---

# Google Cloud Monitoring v3 API - Class BasicSli (3.16.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.BasicSli

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Monitoring v3 API - Class BasicSli (3.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.16.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.BasicSli)
  * [ 3.15.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.15.0/Google.Cloud.Monitoring.V3.BasicSli)
  * [ 3.14.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.14.0/Google.Cloud.Monitoring.V3.BasicSli)
  * [ 3.13.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.13.0/Google.Cloud.Monitoring.V3.BasicSli)
  * [ 3.12.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.12.0/Google.Cloud.Monitoring.V3.BasicSli)
  * [ 3.11.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.11.0/Google.Cloud.Monitoring.V3.BasicSli)
  * [ 3.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.10.0/Google.Cloud.Monitoring.V3.BasicSli)
  * [ 3.9.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.9.0/Google.Cloud.Monitoring.V3.BasicSli)
  * [ 3.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.8.0/Google.Cloud.Monitoring.V3.BasicSli)
  * [ 3.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.7.0/Google.Cloud.Monitoring.V3.BasicSli)
  * [ 3.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.6.0/Google.Cloud.Monitoring.V3.BasicSli)
  * [ 3.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.5.0/Google.Cloud.Monitoring.V3.BasicSli)
  * [ 3.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.4.0/Google.Cloud.Monitoring.V3.BasicSli)
  * [ 3.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.3.0/Google.Cloud.Monitoring.V3.BasicSli)
  * [ 3.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.2.0/Google.Cloud.Monitoring.V3.BasicSli)
  * [ 3.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.1.0/Google.Cloud.Monitoring.V3.BasicSli)
  * [ 3.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.0.0/Google.Cloud.Monitoring.V3.BasicSli)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/2.6.0/Google.Cloud.Monitoring.V3.BasicSli)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/2.5.0/Google.Cloud.Monitoring.V3.BasicSli)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/2.4.0/Google.Cloud.Monitoring.V3.BasicSli)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/2.3.0/Google.Cloud.Monitoring.V3.BasicSli)


    
    
    public sealed class BasicSli : IMessage<BasicSli>, IEquatable<BasicSli>, IDeepCloneable<BasicSli>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Monitoring v3 API class BasicSli.

An SLI measuring performance on a well-known service type. Performance will be computed on the basis of pre-defined metrics. The type of the `service_resource` determines the metrics to use and the `service_resource.labels` and `metric_labels` are used to construct a monitoring filter to filter that metric down to just the data relevant to this service.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > BasicSli

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[BasicSli](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.BasicSli), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[BasicSli](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.BasicSli), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[BasicSli](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.BasicSli), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Monitoring.V3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3)

## Assembly

Google.Cloud.Monitoring.V3.dll

## Constructors 

### BasicSli()
    
    
    public BasicSli()

### BasicSli(BasicSli)
    
    
    public BasicSli(BasicSli other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[BasicSli](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.BasicSli)`  
  
  
## Properties 

### Availability
    
    
    public BasicSli.Types.AvailabilityCriteria Availability { get; set; }

Good service is defined to be the count of requests made to this service that return successfully.

**Property Value**  
---  
**Type** | **Description**  
`[BasicSli](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.BasicSli)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.BasicSli.Types)[AvailabilityCriteria](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.BasicSli.Types.AvailabilityCriteria)` |   
  
### Latency
    
    
    public BasicSli.Types.LatencyCriteria Latency { get; set; }

Good service is defined to be the count of requests made to this service that are fast enough with respect to `latency.threshold`.

**Property Value**  
---  
**Type** | **Description**  
`[BasicSli](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.BasicSli)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.BasicSli.Types)[LatencyCriteria](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.BasicSli.Types.LatencyCriteria)` |   
  
### Location
    
    
    public RepeatedField<string> Location { get; }

OPTIONAL: The set of locations to which this SLI is relevant. Telemetry from other locations will not be used to calculate performance for this SLI. If omitted, this SLI applies to all locations in which the Service has activity. For service types that don't support breaking down by location, setting this field will result in an error.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Method
    
    
    public RepeatedField<string> Method { get; }

OPTIONAL: The set of RPCs to which this SLI is relevant. Telemetry from other methods will not be used to calculate performance for this SLI. If omitted, this SLI applies to all the Service's methods. For service types that don't support breaking down by method, setting this field will result in an error.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SliCriteriaCase
    
    
    public BasicSli.SliCriteriaOneofCase SliCriteriaCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[BasicSli](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.BasicSli)[SliCriteriaOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.BasicSli.SliCriteriaOneofCase)` |   
  
### Version
    
    
    public RepeatedField<string> Version { get; }

OPTIONAL: The set of API versions to which this SLI is relevant. Telemetry from other API versions will not be used to calculate performance for this SLI. If omitted, this SLI applies to all API versions. For service types that don't support breaking down by version, setting this field will result in an error.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
