---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.SpanContext
title: Google Cloud Monitoring v3 API - Class SpanContext (3.16.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:12:41.804271+00:00
---

# Google Cloud Monitoring v3 API - Class SpanContext (3.16.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.SpanContext

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Monitoring v3 API - Class SpanContext (3.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.16.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.SpanContext)
  * [ 3.15.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.15.0/Google.Cloud.Monitoring.V3.SpanContext)
  * [ 3.14.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.14.0/Google.Cloud.Monitoring.V3.SpanContext)
  * [ 3.13.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.13.0/Google.Cloud.Monitoring.V3.SpanContext)
  * [ 3.12.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.12.0/Google.Cloud.Monitoring.V3.SpanContext)
  * [ 3.11.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.11.0/Google.Cloud.Monitoring.V3.SpanContext)
  * [ 3.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.10.0/Google.Cloud.Monitoring.V3.SpanContext)
  * [ 3.9.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.9.0/Google.Cloud.Monitoring.V3.SpanContext)
  * [ 3.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.8.0/Google.Cloud.Monitoring.V3.SpanContext)
  * [ 3.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.7.0/Google.Cloud.Monitoring.V3.SpanContext)
  * [ 3.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.6.0/Google.Cloud.Monitoring.V3.SpanContext)
  * [ 3.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.5.0/Google.Cloud.Monitoring.V3.SpanContext)
  * [ 3.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.4.0/Google.Cloud.Monitoring.V3.SpanContext)
  * [ 3.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.3.0/Google.Cloud.Monitoring.V3.SpanContext)
  * [ 3.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.2.0/Google.Cloud.Monitoring.V3.SpanContext)
  * [ 3.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.1.0/Google.Cloud.Monitoring.V3.SpanContext)
  * [ 3.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/3.0.0/Google.Cloud.Monitoring.V3.SpanContext)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/2.6.0/Google.Cloud.Monitoring.V3.SpanContext)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/2.5.0/Google.Cloud.Monitoring.V3.SpanContext)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/2.4.0/Google.Cloud.Monitoring.V3.SpanContext)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/2.3.0/Google.Cloud.Monitoring.V3.SpanContext)


    
    
    public sealed class SpanContext : IMessage<SpanContext>, IEquatable<SpanContext>, IDeepCloneable<SpanContext>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Monitoring v3 API class SpanContext.

The context of a span. This is attached to an [Exemplar][google.api.Distribution.Exemplar] in [Distribution][google.api.Distribution] values during aggregation.

It contains the name of a span with format:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/traces/[TRACE_ID]/spans/[SPAN_ID]
    

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SpanContext

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[SpanContext](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.SpanContext), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[SpanContext](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.SpanContext), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[SpanContext](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.SpanContext), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Monitoring.V3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3)

## Assembly

Google.Cloud.Monitoring.V3.dll

## Constructors 

### SpanContext()
    
    
    public SpanContext()

### SpanContext(SpanContext)
    
    
    public SpanContext(SpanContext other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[SpanContext](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.SpanContext)`  
  
  
## Properties 

### SpanName
    
    
    public string SpanName { get; set; }

The resource name of the span. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/traces/[TRACE_ID]/spans/[SPAN_ID]
    

`[TRACE_ID]` is a unique identifier for a trace within a project; it is a 32-character hexadecimal encoding of a 16-byte array.

`[SPAN_ID]` is a unique identifier for a span within a trace; it is a 16-character hexadecimal encoding of an 8-byte array.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
