---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V2/latest/Google.Cloud.Trace.V2.Span.Types.TimeEvent
title: Google Cloud Trace v2 API - Class Span.Types.TimeEvent (3.7.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:37:25.857384+00:00
---

# Google Cloud Trace v2 API - Class Span.Types.TimeEvent (3.7.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V2/latest/Google.Cloud.Trace.V2.Span.Types.TimeEvent

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Trace v2 API - Class Span.Types.TimeEvent (3.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.7.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V2/latest/Google.Cloud.Trace.V2.Span.Types.TimeEvent)
  * [ 3.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V2/3.6.0/Google.Cloud.Trace.V2.Span.Types.TimeEvent)
  * [ 3.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V2/3.5.0/Google.Cloud.Trace.V2.Span.Types.TimeEvent)
  * [ 3.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V2/3.4.0/Google.Cloud.Trace.V2.Span.Types.TimeEvent)
  * [ 3.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V2/3.3.0/Google.Cloud.Trace.V2.Span.Types.TimeEvent)
  * [ 3.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V2/3.2.0/Google.Cloud.Trace.V2.Span.Types.TimeEvent)
  * [ 3.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V2/3.1.0/Google.Cloud.Trace.V2.Span.Types.TimeEvent)
  * [ 3.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V2/3.0.0/Google.Cloud.Trace.V2.Span.Types.TimeEvent)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V2/2.3.0/Google.Cloud.Trace.V2.Span.Types.TimeEvent)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V2/2.2.0/Google.Cloud.Trace.V2.Span.Types.TimeEvent)


    
    
    public sealed class Span.Types.TimeEvent : IMessage<Span.Types.TimeEvent>, IEquatable<Span.Types.TimeEvent>, IDeepCloneable<Span.Types.TimeEvent>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Trace v2 API class Span.Types.TimeEvent.

A time-stamped annotation or message event in the Span.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Span.Types.TimeEvent

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Span](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V2/latest/Google.Cloud.Trace.V2.Span)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V2/latest/Google.Cloud.Trace.V2.Span.Types)[TimeEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V2/latest/Google.Cloud.Trace.V2.Span.Types.TimeEvent), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Span](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V2/latest/Google.Cloud.Trace.V2.Span)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V2/latest/Google.Cloud.Trace.V2.Span.Types)[TimeEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V2/latest/Google.Cloud.Trace.V2.Span.Types.TimeEvent), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Span](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V2/latest/Google.Cloud.Trace.V2.Span)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V2/latest/Google.Cloud.Trace.V2.Span.Types)[TimeEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V2/latest/Google.Cloud.Trace.V2.Span.Types.TimeEvent), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Trace.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V2/latest/Google.Cloud.Trace.V2)

## Assembly

Google.Cloud.Trace.V2.dll

## Constructors 

### TimeEvent()
    
    
    public TimeEvent()

### TimeEvent(TimeEvent)
    
    
    public TimeEvent(Span.Types.TimeEvent other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Span](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V2/latest/Google.Cloud.Trace.V2.Span)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V2/latest/Google.Cloud.Trace.V2.Span.Types)[TimeEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V2/latest/Google.Cloud.Trace.V2.Span.Types.TimeEvent)`  
  
  
## Properties 

### Annotation
    
    
    public Span.Types.TimeEvent.Types.Annotation Annotation { get; set; }

Text annotation with a set of attributes.

**Property Value**  
---  
**Type** | **Description**  
`[Span](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V2/latest/Google.Cloud.Trace.V2.Span)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V2/latest/Google.Cloud.Trace.V2.Span.Types)[TimeEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V2/latest/Google.Cloud.Trace.V2.Span.Types.TimeEvent)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V2/latest/Google.Cloud.Trace.V2.Span.Types.TimeEvent.Types)[Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V2/latest/Google.Cloud.Trace.V2.Span.Types.TimeEvent.Types.Annotation)` |   
  
### MessageEvent
    
    
    public Span.Types.TimeEvent.Types.MessageEvent MessageEvent { get; set; }

An event describing a message sent/received between Spans.

**Property Value**  
---  
**Type** | **Description**  
`[Span](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V2/latest/Google.Cloud.Trace.V2.Span)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V2/latest/Google.Cloud.Trace.V2.Span.Types)[TimeEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V2/latest/Google.Cloud.Trace.V2.Span.Types.TimeEvent)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V2/latest/Google.Cloud.Trace.V2.Span.Types.TimeEvent.Types)[MessageEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V2/latest/Google.Cloud.Trace.V2.Span.Types.TimeEvent.Types.MessageEvent)` |   
  
### Time
    
    
    public Timestamp Time { get; set; }

The timestamp indicating the time the event occurred.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### ValueCase
    
    
    public Span.Types.TimeEvent.ValueOneofCase ValueCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[Span](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V2/latest/Google.Cloud.Trace.V2.Span)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V2/latest/Google.Cloud.Trace.V2.Span.Types)[TimeEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V2/latest/Google.Cloud.Trace.V2.Span.Types.TimeEvent)[ValueOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Trace.V2/latest/Google.Cloud.Trace.V2.Span.Types.TimeEvent.ValueOneofCase)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
