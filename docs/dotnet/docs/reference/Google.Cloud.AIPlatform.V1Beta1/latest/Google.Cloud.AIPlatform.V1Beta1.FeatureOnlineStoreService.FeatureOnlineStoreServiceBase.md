---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureOnlineStoreService.FeatureOnlineStoreServiceBase
title: Vertex AI v1beta1 API - Class FeatureOnlineStoreService.FeatureOnlineStoreServiceBase (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:42:12.426919+00:00
---

# Vertex AI v1beta1 API - Class FeatureOnlineStoreService.FeatureOnlineStoreServiceBase (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureOnlineStoreService.FeatureOnlineStoreServiceBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class FeatureOnlineStoreService.FeatureOnlineStoreServiceBase (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    [BindServiceMethod(typeof(FeatureOnlineStoreService), "BindService")]
    public abstract class FeatureOnlineStoreService.FeatureOnlineStoreServiceBase

Reference documentation and code samples for the Vertex AI v1beta1 API class FeatureOnlineStoreService.FeatureOnlineStoreServiceBase.

Base class for server-side implementations of FeatureOnlineStoreService

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > FeatureOnlineStoreService.FeatureOnlineStoreServiceBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Methods 

### FeatureViewDirectWrite(IAsyncStreamReader<FeatureViewDirectWriteRequest>, IServerStreamWriter<FeatureViewDirectWriteResponse>, ServerCallContext)
    
    
    public virtual Task FeatureViewDirectWrite(IAsyncStreamReader<FeatureViewDirectWriteRequest> requestStream, IServerStreamWriter<FeatureViewDirectWriteResponse> responseStream, ServerCallContext context)

Bidirectional streaming RPC to directly write to feature values in a feature view. Requests may not have a one-to-one mapping to responses and responses may be returned out-of-order to reduce latency.

**Parameters**  
---  
**Name** | **Description**  
`requestStream` | `[IAsyncStreamReader](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.IAsyncStreamReader-1.html)[FeatureViewDirectWriteRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureViewDirectWriteRequest)`  
Used for reading requests from the client.  
`responseStream` | `[IServerStreamWriter](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.IServerStreamWriter-1.html)[FeatureViewDirectWriteResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureViewDirectWriteResponse)`  
Used for sending responses back to the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task indicating completion of the handler.  
  
### FetchFeatureValues(FetchFeatureValuesRequest, ServerCallContext)
    
    
    public virtual Task<FetchFeatureValuesResponse> FetchFeatureValues(FetchFeatureValuesRequest request, ServerCallContext context)

Fetch feature values under a FeatureView.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchFeatureValuesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FetchFeatureValuesRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FetchFeatureValuesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FetchFeatureValuesResponse)` | The response to send back to the client (wrapped by a task).  
  
### GenerateFetchAccessToken(GenerateFetchAccessTokenRequest, ServerCallContext)
    
    
    public virtual Task<GenerateFetchAccessTokenResponse> GenerateFetchAccessToken(GenerateFetchAccessTokenRequest request, ServerCallContext context)

RPC to generate an access token for the given feature view. FeatureViews under the same FeatureOnlineStore share the same access token.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateFetchAccessTokenRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GenerateFetchAccessTokenRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerateFetchAccessTokenResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GenerateFetchAccessTokenResponse)` | The response to send back to the client (wrapped by a task).  
  
### SearchNearestEntities(SearchNearestEntitiesRequest, ServerCallContext)
    
    
    public virtual Task<SearchNearestEntitiesResponse> SearchNearestEntities(SearchNearestEntitiesRequest request, ServerCallContext context)

Search the nearest entities under a FeatureView. Search only works for indexable feature view; if a feature view isn't indexable, returns Invalid argument response.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchNearestEntitiesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.SearchNearestEntitiesRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SearchNearestEntitiesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.SearchNearestEntitiesResponse)` | The response to send back to the client (wrapped by a task).  
  
### StreamingFetchFeatureValues(IAsyncStreamReader<StreamingFetchFeatureValuesRequest>, IServerStreamWriter<StreamingFetchFeatureValuesResponse>, ServerCallContext)
    
    
    public virtual Task StreamingFetchFeatureValues(IAsyncStreamReader<StreamingFetchFeatureValuesRequest> requestStream, IServerStreamWriter<StreamingFetchFeatureValuesResponse> responseStream, ServerCallContext context)

Bidirectional streaming RPC to fetch feature values under a FeatureView. Requests may not have a one-to-one mapping to responses and responses may be returned out-of-order to reduce latency.

**Parameters**  
---  
**Name** | **Description**  
`requestStream` | `[IAsyncStreamReader](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.IAsyncStreamReader-1.html)[StreamingFetchFeatureValuesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.StreamingFetchFeatureValuesRequest)`  
Used for reading requests from the client.  
`responseStream` | `[IServerStreamWriter](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.IServerStreamWriter-1.html)[StreamingFetchFeatureValuesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.StreamingFetchFeatureValuesResponse)`  
Used for sending responses back to the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task indicating completion of the handler.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
