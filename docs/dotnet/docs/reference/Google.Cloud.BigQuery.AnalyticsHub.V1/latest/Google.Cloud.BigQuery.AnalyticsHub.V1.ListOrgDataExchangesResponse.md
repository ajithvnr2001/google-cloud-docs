---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.AnalyticsHub.V1/latest/Google.Cloud.BigQuery.AnalyticsHub.V1.ListOrgDataExchangesResponse
title: Analytics Hub v1 API - Class ListOrgDataExchangesResponse (1.12.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:37:42.894963+00:00
---

# Analytics Hub v1 API - Class ListOrgDataExchangesResponse (1.12.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.AnalyticsHub.V1/latest/Google.Cloud.BigQuery.AnalyticsHub.V1.ListOrgDataExchangesResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Analytics Hub v1 API - Class ListOrgDataExchangesResponse (1.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.12.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.AnalyticsHub.V1/latest/Google.Cloud.BigQuery.AnalyticsHub.V1.ListOrgDataExchangesResponse)
  * [ 1.11.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.AnalyticsHub.V1/1.11.0/Google.Cloud.BigQuery.AnalyticsHub.V1.ListOrgDataExchangesResponse)
  * [ 1.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.AnalyticsHub.V1/1.10.0/Google.Cloud.BigQuery.AnalyticsHub.V1.ListOrgDataExchangesResponse)
  * [ 1.9.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.AnalyticsHub.V1/1.9.0/Google.Cloud.BigQuery.AnalyticsHub.V1.ListOrgDataExchangesResponse)
  * [ 1.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.AnalyticsHub.V1/1.8.0/Google.Cloud.BigQuery.AnalyticsHub.V1.ListOrgDataExchangesResponse)
  * [ 1.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.AnalyticsHub.V1/1.7.0/Google.Cloud.BigQuery.AnalyticsHub.V1.ListOrgDataExchangesResponse)
  * [ 1.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.AnalyticsHub.V1/1.6.0/Google.Cloud.BigQuery.AnalyticsHub.V1.ListOrgDataExchangesResponse)
  * [ 1.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.AnalyticsHub.V1/1.5.0/Google.Cloud.BigQuery.AnalyticsHub.V1.ListOrgDataExchangesResponse)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.AnalyticsHub.V1/1.4.0/Google.Cloud.BigQuery.AnalyticsHub.V1.ListOrgDataExchangesResponse)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.AnalyticsHub.V1/1.3.0/Google.Cloud.BigQuery.AnalyticsHub.V1.ListOrgDataExchangesResponse)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.AnalyticsHub.V1/1.2.0/Google.Cloud.BigQuery.AnalyticsHub.V1.ListOrgDataExchangesResponse)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.AnalyticsHub.V1/1.1.0/Google.Cloud.BigQuery.AnalyticsHub.V1.ListOrgDataExchangesResponse)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.AnalyticsHub.V1/1.0.0/Google.Cloud.BigQuery.AnalyticsHub.V1.ListOrgDataExchangesResponse)


    
    
    public sealed class ListOrgDataExchangesResponse : IMessage<ListOrgDataExchangesResponse>, IEquatable<ListOrgDataExchangesResponse>, IDeepCloneable<ListOrgDataExchangesResponse>, IBufferMessage, IMessage, IPageResponse<DataExchange>, IEnumerable<DataExchange>, IEnumerable

Reference documentation and code samples for the Analytics Hub v1 API class ListOrgDataExchangesResponse.

Message for response to listing data exchanges in an organization and location.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListOrgDataExchangesResponse

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListOrgDataExchangesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.AnalyticsHub.V1/latest/Google.Cloud.BigQuery.AnalyticsHub.V1.ListOrgDataExchangesResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListOrgDataExchangesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.AnalyticsHub.V1/latest/Google.Cloud.BigQuery.AnalyticsHub.V1.ListOrgDataExchangesResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListOrgDataExchangesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.AnalyticsHub.V1/latest/Google.Cloud.BigQuery.AnalyticsHub.V1.ListOrgDataExchangesResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html), [IPageResponse](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageResponse-1.html)[DataExchange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.AnalyticsHub.V1/latest/Google.Cloud.BigQuery.AnalyticsHub.V1.DataExchange), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[DataExchange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.AnalyticsHub.V1/latest/Google.Cloud.BigQuery.AnalyticsHub.V1.DataExchange), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.BigQuery.AnalyticsHub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.AnalyticsHub.V1/latest/Google.Cloud.BigQuery.AnalyticsHub.V1)

## Assembly

Google.Cloud.BigQuery.AnalyticsHub.V1.dll

## Constructors 

### ListOrgDataExchangesResponse()
    
    
    public ListOrgDataExchangesResponse()

### ListOrgDataExchangesResponse(ListOrgDataExchangesResponse)
    
    
    public ListOrgDataExchangesResponse(ListOrgDataExchangesResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListOrgDataExchangesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.AnalyticsHub.V1/latest/Google.Cloud.BigQuery.AnalyticsHub.V1.ListOrgDataExchangesResponse)`  
  
  
## Properties 

### DataExchanges
    
    
    public RepeatedField<DataExchange> DataExchanges { get; }

The list of data exchanges.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[DataExchange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.AnalyticsHub.V1/latest/Google.Cloud.BigQuery.AnalyticsHub.V1.DataExchange)` |   
  
### NextPageToken
    
    
    public string NextPageToken { get; set; }

A token to request the next page of results.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
## Methods 

### GetEnumerator()
    
    
    public IEnumerator<DataExchange> GetEnumerator()

Returns an enumerator that iterates through the resources in this response.

**Returns**  
---  
**Type** | **Description**  
`[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1)[DataExchange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.AnalyticsHub.V1/latest/Google.Cloud.BigQuery.AnalyticsHub.V1.DataExchange)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
