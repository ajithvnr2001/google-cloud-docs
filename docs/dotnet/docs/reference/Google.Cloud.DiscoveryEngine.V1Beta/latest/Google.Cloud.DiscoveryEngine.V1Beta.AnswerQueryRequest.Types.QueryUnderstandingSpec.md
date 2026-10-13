---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest.Types.QueryUnderstandingSpec
title: Discovery Engine v1beta API - Class AnswerQueryRequest.Types.QueryUnderstandingSpec (1.0.0-beta25) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:24:51.619978+00:00
---

# Discovery Engine v1beta API - Class AnswerQueryRequest.Types.QueryUnderstandingSpec (1.0.0-beta25)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest.Types.QueryUnderstandingSpec

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Discovery Engine v1beta API - Class AnswerQueryRequest.Types.QueryUnderstandingSpec (1.0.0-beta25) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta25 (latest)  1.0.0-beta24 
    
    
    public sealed class AnswerQueryRequest.Types.QueryUnderstandingSpec : IMessage<AnswerQueryRequest.Types.QueryUnderstandingSpec>, IEquatable<AnswerQueryRequest.Types.QueryUnderstandingSpec>, IDeepCloneable<AnswerQueryRequest.Types.QueryUnderstandingSpec>, IBufferMessage, IMessage

Reference documentation and code samples for the Discovery Engine v1beta API class AnswerQueryRequest.Types.QueryUnderstandingSpec.

Query understanding specification.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AnswerQueryRequest.Types.QueryUnderstandingSpec

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AnswerQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest.Types)[QueryUnderstandingSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest.Types.QueryUnderstandingSpec), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AnswerQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest.Types)[QueryUnderstandingSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest.Types.QueryUnderstandingSpec), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AnswerQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest.Types)[QueryUnderstandingSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest.Types.QueryUnderstandingSpec), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DiscoveryEngine.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta)

## Assembly

Google.Cloud.DiscoveryEngine.V1Beta.dll

## Constructors 

### QueryUnderstandingSpec()
    
    
    public QueryUnderstandingSpec()

### QueryUnderstandingSpec(QueryUnderstandingSpec)
    
    
    public QueryUnderstandingSpec(AnswerQueryRequest.Types.QueryUnderstandingSpec other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AnswerQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest.Types)[QueryUnderstandingSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest.Types.QueryUnderstandingSpec)`  
  
  
## Properties 

### DisableSpellCorrection
    
    
    public bool DisableSpellCorrection { get; set; }

Optional. Whether to disable spell correction. The default value is `false`.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### QueryClassificationSpec
    
    
    public AnswerQueryRequest.Types.QueryUnderstandingSpec.Types.QueryClassificationSpec QueryClassificationSpec { get; set; }

Query classification specification.

**Property Value**  
---  
**Type** | **Description**  
`[AnswerQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest.Types)[QueryUnderstandingSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest.Types.QueryUnderstandingSpec)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest.Types.QueryUnderstandingSpec.Types)[QueryClassificationSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest.Types.QueryUnderstandingSpec.Types.QueryClassificationSpec)` |   
  
### QueryRephraserSpec
    
    
    public AnswerQueryRequest.Types.QueryUnderstandingSpec.Types.QueryRephraserSpec QueryRephraserSpec { get; set; }

Query rephraser specification.

**Property Value**  
---  
**Type** | **Description**  
`[AnswerQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest.Types)[QueryUnderstandingSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest.Types.QueryUnderstandingSpec)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest.Types.QueryUnderstandingSpec.Types)[QueryRephraserSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest.Types.QueryUnderstandingSpec.Types.QueryRephraserSpec)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-24 UTC."],[],[]] 
