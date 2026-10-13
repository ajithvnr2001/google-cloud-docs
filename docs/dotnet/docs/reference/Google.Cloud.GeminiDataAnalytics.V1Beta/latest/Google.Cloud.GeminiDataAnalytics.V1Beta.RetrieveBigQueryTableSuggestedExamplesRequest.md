---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta.RetrieveBigQueryTableSuggestedExamplesRequest
title: Data Analytics API with Gemini v1beta API - Class RetrieveBigQueryTableSuggestedExamplesRequest (1.0.0-beta01) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:07:13.073001+00:00
---

# Data Analytics API with Gemini v1beta API - Class RetrieveBigQueryTableSuggestedExamplesRequest (1.0.0-beta01)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta.RetrieveBigQueryTableSuggestedExamplesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Data Analytics API with Gemini v1beta API - Class RetrieveBigQueryTableSuggestedExamplesRequest (1.0.0-beta01) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta12 (latest)  1.0.0-beta11 
    
    
    public sealed class RetrieveBigQueryTableSuggestedExamplesRequest : IMessage<RetrieveBigQueryTableSuggestedExamplesRequest>, IEquatable<RetrieveBigQueryTableSuggestedExamplesRequest>, IDeepCloneable<RetrieveBigQueryTableSuggestedExamplesRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Data Analytics API with Gemini v1beta API class RetrieveBigQueryTableSuggestedExamplesRequest.

Request for retrieving BigQuery table schema with suggested NL-SQL examples.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > RetrieveBigQueryTableSuggestedExamplesRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[RetrieveBigQueryTableSuggestedExamplesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta.RetrieveBigQueryTableSuggestedExamplesRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[RetrieveBigQueryTableSuggestedExamplesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta.RetrieveBigQueryTableSuggestedExamplesRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[RetrieveBigQueryTableSuggestedExamplesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta.RetrieveBigQueryTableSuggestedExamplesRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.GeminiDataAnalytics.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta)

## Assembly

Google.Cloud.GeminiDataAnalytics.V1Beta.dll

## Constructors 

### RetrieveBigQueryTableSuggestedExamplesRequest()
    
    
    public RetrieveBigQueryTableSuggestedExamplesRequest()

### RetrieveBigQueryTableSuggestedExamplesRequest(RetrieveBigQueryTableSuggestedExamplesRequest)
    
    
    public RetrieveBigQueryTableSuggestedExamplesRequest(RetrieveBigQueryTableSuggestedExamplesRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[RetrieveBigQueryTableSuggestedExamplesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta.RetrieveBigQueryTableSuggestedExamplesRequest)`  
  
  
## Properties 

### DirectLookup
    
    
    public RepeatedField<DirectLookup> DirectLookup { get; }

Optional. A list of direct lookup parameters.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[DirectLookup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta.DirectLookup)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. Parent value for RetrieveBigQueryTableSuggestedExamplesRequest. Pattern: `projects/{project}/locations/{location}` For location, use "global" for now. Regional location value will be supported in the future.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
