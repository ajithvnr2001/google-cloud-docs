---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeRecommender.V1/latest/Google.Cloud.GkeRecommender.V1.PerformanceRange
title: GKE Recommender v1 API - Class PerformanceRange (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:01:45.419342+00:00
---

# GKE Recommender v1 API - Class PerformanceRange (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeRecommender.V1/latest/Google.Cloud.GkeRecommender.V1.PerformanceRange

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  GKE Recommender v1 API - Class PerformanceRange (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta01 
    
    
    public sealed class PerformanceRange : IMessage<PerformanceRange>, IEquatable<PerformanceRange>, IDeepCloneable<PerformanceRange>, IBufferMessage, IMessage

Reference documentation and code samples for the GKE Recommender v1 API class PerformanceRange.

Performance range for a model deployment.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > PerformanceRange

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[PerformanceRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeRecommender.V1/latest/Google.Cloud.GkeRecommender.V1.PerformanceRange), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[PerformanceRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeRecommender.V1/latest/Google.Cloud.GkeRecommender.V1.PerformanceRange), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[PerformanceRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeRecommender.V1/latest/Google.Cloud.GkeRecommender.V1.PerformanceRange), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.GkeRecommender.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeRecommender.V1/latest/Google.Cloud.GkeRecommender.V1)

## Assembly

Google.Cloud.GkeRecommender.V1.dll

## Constructors 

### PerformanceRange()
    
    
    public PerformanceRange()

### PerformanceRange(PerformanceRange)
    
    
    public PerformanceRange(PerformanceRange other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[PerformanceRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeRecommender.V1/latest/Google.Cloud.GkeRecommender.V1.PerformanceRange)`  
  
  
## Properties 

### NtpotRange
    
    
    public MillisecondRange NtpotRange { get; set; }

Output only. The range of NTPOT (Normalized Time Per Output Token) in milliseconds. NTPOT is the request latency normalized by the number of output tokens, measured as request_latency / total_output_tokens.

**Property Value**  
---  
**Type** | **Description**  
`[MillisecondRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeRecommender.V1/latest/Google.Cloud.GkeRecommender.V1.MillisecondRange)` |   
  
### ThroughputOutputRange
    
    
    public TokensPerSecondRange ThroughputOutputRange { get; set; }

Output only. The range of throughput in output tokens per second. This is measured as total_output_tokens_generated_by_server / elapsed_time_in_seconds.

**Property Value**  
---  
**Type** | **Description**  
`[TokensPerSecondRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeRecommender.V1/latest/Google.Cloud.GkeRecommender.V1.TokensPerSecondRange)` |   
  
### TtftRange
    
    
    public MillisecondRange TtftRange { get; set; }

Output only. The range of TTFT (Time To First Token) in milliseconds. TTFT is the time it takes to generate the first token for a request.

**Property Value**  
---  
**Type** | **Description**  
`[MillisecondRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeRecommender.V1/latest/Google.Cloud.GkeRecommender.V1.MillisecondRange)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
