---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListReasoningEngineRuntimeRevisionsResponse
title: Vertex AI v1beta1 API - Class ListReasoningEngineRuntimeRevisionsResponse (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:48:30.378589+00:00
---

# Vertex AI v1beta1 API - Class ListReasoningEngineRuntimeRevisionsResponse (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListReasoningEngineRuntimeRevisionsResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class ListReasoningEngineRuntimeRevisionsResponse (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public sealed class ListReasoningEngineRuntimeRevisionsResponse : IMessage<ListReasoningEngineRuntimeRevisionsResponse>, IEquatable<ListReasoningEngineRuntimeRevisionsResponse>, IDeepCloneable<ListReasoningEngineRuntimeRevisionsResponse>, IBufferMessage, IMessage, IPageResponse<ReasoningEngineRuntimeRevision>, IEnumerable<ReasoningEngineRuntimeRevision>, IEnumerable

Reference documentation and code samples for the Vertex AI v1beta1 API class ListReasoningEngineRuntimeRevisionsResponse.

Response message for [ReasoningEngineRuntimeRevisionService.ListReasoningEngineRuntimeRevisions][google.cloud.aiplatform.v1beta1.ReasoningEngineRuntimeRevisionService.ListReasoningEngineRuntimeRevisions]

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListReasoningEngineRuntimeRevisionsResponse

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListReasoningEngineRuntimeRevisionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListReasoningEngineRuntimeRevisionsResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListReasoningEngineRuntimeRevisionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListReasoningEngineRuntimeRevisionsResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListReasoningEngineRuntimeRevisionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListReasoningEngineRuntimeRevisionsResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html), [IPageResponse](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageResponse-1.html)[ReasoningEngineRuntimeRevision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineRuntimeRevision), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[ReasoningEngineRuntimeRevision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineRuntimeRevision), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Constructors 

### ListReasoningEngineRuntimeRevisionsResponse()
    
    
    public ListReasoningEngineRuntimeRevisionsResponse()

### ListReasoningEngineRuntimeRevisionsResponse(ListReasoningEngineRuntimeRevisionsResponse)
    
    
    public ListReasoningEngineRuntimeRevisionsResponse(ListReasoningEngineRuntimeRevisionsResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListReasoningEngineRuntimeRevisionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListReasoningEngineRuntimeRevisionsResponse)`  
  
  
## Properties 

### NextPageToken
    
    
    public string NextPageToken { get; set; }

A token to retrieve the next page of results. Pass to [ListReasoningEngineRuntimeRevisionsRequest.page_token][google.cloud.aiplatform.v1beta1.ListReasoningEngineRuntimeRevisionsRequest.page_token] to obtain that page.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ReasoningEngineRuntimeRevisions
    
    
    public RepeatedField<ReasoningEngineRuntimeRevision> ReasoningEngineRuntimeRevisions { get; }

List of ReasoningEngineRuntimeRevisions in the requested page.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[ReasoningEngineRuntimeRevision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineRuntimeRevision)` |   
  
## Methods 

### GetEnumerator()
    
    
    public IEnumerator<ReasoningEngineRuntimeRevision> GetEnumerator()

Returns an enumerator that iterates through the resources in this response.

**Returns**  
---  
**Type** | **Description**  
`[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1)[ReasoningEngineRuntimeRevision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineRuntimeRevision)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
