---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AggregatedMetrics.Types.TurnLatencyMetrics
title: Gemini Enterprise for Customer Experience v1beta API - Class AggregatedMetrics.Types.TurnLatencyMetrics (1.0.0-beta09) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:39:52.655208+00:00
---

# Gemini Enterprise for Customer Experience v1beta API - Class AggregatedMetrics.Types.TurnLatencyMetrics (1.0.0-beta09)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AggregatedMetrics.Types.TurnLatencyMetrics

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Gemini Enterprise for Customer Experience v1beta API - Class AggregatedMetrics.Types.TurnLatencyMetrics (1.0.0-beta09) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta09 (latest)  1.0.0-beta08 
    
    
    public sealed class AggregatedMetrics.Types.TurnLatencyMetrics : IMessage<AggregatedMetrics.Types.TurnLatencyMetrics>, IEquatable<AggregatedMetrics.Types.TurnLatencyMetrics>, IDeepCloneable<AggregatedMetrics.Types.TurnLatencyMetrics>, IBufferMessage, IMessage

Reference documentation and code samples for the Gemini Enterprise for Customer Experience v1beta API class AggregatedMetrics.Types.TurnLatencyMetrics.

Metrics for turn latency.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AggregatedMetrics.Types.TurnLatencyMetrics

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AggregatedMetrics](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AggregatedMetrics)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AggregatedMetrics.Types)[TurnLatencyMetrics](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AggregatedMetrics.Types.TurnLatencyMetrics), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AggregatedMetrics](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AggregatedMetrics)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AggregatedMetrics.Types)[TurnLatencyMetrics](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AggregatedMetrics.Types.TurnLatencyMetrics), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AggregatedMetrics](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AggregatedMetrics)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AggregatedMetrics.Types)[TurnLatencyMetrics](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AggregatedMetrics.Types.TurnLatencyMetrics), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Ces.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta)

## Assembly

Google.Cloud.Ces.V1Beta.dll

## Constructors 

### TurnLatencyMetrics()
    
    
    public TurnLatencyMetrics()

### TurnLatencyMetrics(TurnLatencyMetrics)
    
    
    public TurnLatencyMetrics(AggregatedMetrics.Types.TurnLatencyMetrics other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AggregatedMetrics](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AggregatedMetrics)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AggregatedMetrics.Types)[TurnLatencyMetrics](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AggregatedMetrics.Types.TurnLatencyMetrics)`  
  
  
## Properties 

### AverageLatency
    
    
    public Duration AverageLatency { get; set; }

Output only. The average latency of the turns.

**Property Value**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
