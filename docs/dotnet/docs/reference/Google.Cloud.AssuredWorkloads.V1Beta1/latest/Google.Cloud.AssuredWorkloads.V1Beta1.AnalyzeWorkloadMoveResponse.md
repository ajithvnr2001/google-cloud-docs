---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1Beta1/latest/Google.Cloud.AssuredWorkloads.V1Beta1.AnalyzeWorkloadMoveResponse
title: Assured Workloads v1beta1 API - Class AnalyzeWorkloadMoveResponse (2.0.0-beta09) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:06:48.569296+00:00
---

# Assured Workloads v1beta1 API - Class AnalyzeWorkloadMoveResponse (2.0.0-beta09)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1Beta1/latest/Google.Cloud.AssuredWorkloads.V1Beta1.AnalyzeWorkloadMoveResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Assured Workloads v1beta1 API - Class AnalyzeWorkloadMoveResponse (2.0.0-beta09) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta09 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1Beta1/latest/Google.Cloud.AssuredWorkloads.V1Beta1.AnalyzeWorkloadMoveResponse)
  * [ 2.0.0-beta08 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1Beta1/2.0.0-beta08/Google.Cloud.AssuredWorkloads.V1Beta1.AnalyzeWorkloadMoveResponse)
  * [ 1.0.0-beta08 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1Beta1/1.0.0-beta08/Google.Cloud.AssuredWorkloads.V1Beta1.AnalyzeWorkloadMoveResponse)


    
    
    public sealed class AnalyzeWorkloadMoveResponse : IMessage<AnalyzeWorkloadMoveResponse>, IEquatable<AnalyzeWorkloadMoveResponse>, IDeepCloneable<AnalyzeWorkloadMoveResponse>, IBufferMessage, IMessage

Reference documentation and code samples for the Assured Workloads v1beta1 API class AnalyzeWorkloadMoveResponse.

A response that includes the analysis of the hypothetical resource move.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AnalyzeWorkloadMoveResponse

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AnalyzeWorkloadMoveResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1Beta1/latest/Google.Cloud.AssuredWorkloads.V1Beta1.AnalyzeWorkloadMoveResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AnalyzeWorkloadMoveResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1Beta1/latest/Google.Cloud.AssuredWorkloads.V1Beta1.AnalyzeWorkloadMoveResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AnalyzeWorkloadMoveResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1Beta1/latest/Google.Cloud.AssuredWorkloads.V1Beta1.AnalyzeWorkloadMoveResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AssuredWorkloads.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1Beta1/latest/Google.Cloud.AssuredWorkloads.V1Beta1)

## Assembly

Google.Cloud.AssuredWorkloads.V1Beta1.dll

## Constructors 

### AnalyzeWorkloadMoveResponse()
    
    
    public AnalyzeWorkloadMoveResponse()

### AnalyzeWorkloadMoveResponse(AnalyzeWorkloadMoveResponse)
    
    
    public AnalyzeWorkloadMoveResponse(AnalyzeWorkloadMoveResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AnalyzeWorkloadMoveResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1Beta1/latest/Google.Cloud.AssuredWorkloads.V1Beta1.AnalyzeWorkloadMoveResponse)`  
  
  
## Properties 

### Blockers
    
    
    public RepeatedField<string> Blockers { get; }

A list of blockers that should be addressed before moving the source project or project-based workload to the destination folder-based workload.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
