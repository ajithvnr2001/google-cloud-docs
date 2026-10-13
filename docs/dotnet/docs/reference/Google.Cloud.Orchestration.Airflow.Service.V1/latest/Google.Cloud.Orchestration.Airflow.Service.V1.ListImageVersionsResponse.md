---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListImageVersionsResponse
title: Cloud Composer v1 API - Class ListImageVersionsResponse (2.10.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:36:25.958314+00:00
---

# Cloud Composer v1 API - Class ListImageVersionsResponse (2.10.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListImageVersionsResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Composer v1 API - Class ListImageVersionsResponse (2.10.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.10.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListImageVersionsResponse)
  * [ 2.9.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/2.9.0/Google.Cloud.Orchestration.Airflow.Service.V1.ListImageVersionsResponse)
  * [ 2.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/2.8.0/Google.Cloud.Orchestration.Airflow.Service.V1.ListImageVersionsResponse)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/2.7.0/Google.Cloud.Orchestration.Airflow.Service.V1.ListImageVersionsResponse)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/2.6.0/Google.Cloud.Orchestration.Airflow.Service.V1.ListImageVersionsResponse)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/2.5.0/Google.Cloud.Orchestration.Airflow.Service.V1.ListImageVersionsResponse)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/2.4.0/Google.Cloud.Orchestration.Airflow.Service.V1.ListImageVersionsResponse)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/2.3.0/Google.Cloud.Orchestration.Airflow.Service.V1.ListImageVersionsResponse)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/2.2.0/Google.Cloud.Orchestration.Airflow.Service.V1.ListImageVersionsResponse)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/2.1.0/Google.Cloud.Orchestration.Airflow.Service.V1.ListImageVersionsResponse)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/2.0.0/Google.Cloud.Orchestration.Airflow.Service.V1.ListImageVersionsResponse)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/1.0.0/Google.Cloud.Orchestration.Airflow.Service.V1.ListImageVersionsResponse)


    
    
    public sealed class ListImageVersionsResponse : IMessage<ListImageVersionsResponse>, IEquatable<ListImageVersionsResponse>, IDeepCloneable<ListImageVersionsResponse>, IBufferMessage, IMessage, IPageResponse<ImageVersion>, IEnumerable<ImageVersion>, IEnumerable

Reference documentation and code samples for the Cloud Composer v1 API class ListImageVersionsResponse.

The ImageVersions in a project and location.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListImageVersionsResponse

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListImageVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListImageVersionsResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListImageVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListImageVersionsResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListImageVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListImageVersionsResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html), [IPageResponse](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageResponse-1.html)[ImageVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ImageVersion), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[ImageVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ImageVersion), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Orchestration.Airflow.Service.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1)

## Assembly

Google.Cloud.Orchestration.Airflow.Service.V1.dll

## Constructors 

### ListImageVersionsResponse()
    
    
    public ListImageVersionsResponse()

### ListImageVersionsResponse(ListImageVersionsResponse)
    
    
    public ListImageVersionsResponse(ListImageVersionsResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListImageVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListImageVersionsResponse)`  
  
  
## Properties 

### ImageVersions
    
    
    public RepeatedField<ImageVersion> ImageVersions { get; }

The list of supported ImageVersions in a location.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[ImageVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ImageVersion)` |   
  
### NextPageToken
    
    
    public string NextPageToken { get; set; }

The page token used to query for the next page if one exists.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
## Methods 

### GetEnumerator()
    
    
    public IEnumerator<ImageVersion> GetEnumerator()

Returns an enumerator that iterates through the resources in this response.

**Returns**  
---  
**Type** | **Description**  
`[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1)[ImageVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ImageVersion)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
