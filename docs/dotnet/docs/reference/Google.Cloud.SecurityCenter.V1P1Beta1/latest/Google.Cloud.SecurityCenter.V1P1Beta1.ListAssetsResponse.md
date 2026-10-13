---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.ListAssetsResponse
title: Google Cloud Security Command Center v1p1beta1 API - Class ListAssetsResponse (3.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:20:17.890655+00:00
---

# Google Cloud Security Command Center v1p1beta1 API - Class ListAssetsResponse (3.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.ListAssetsResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Security Command Center v1p1beta1 API - Class ListAssetsResponse (3.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.0.0-beta06 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.ListAssetsResponse)
  * [ 3.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/3.0.0-beta05/Google.Cloud.SecurityCenter.V1P1Beta1.ListAssetsResponse)
  * [ 2.0.0-beta07 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/2.0.0-beta07/Google.Cloud.SecurityCenter.V1P1Beta1.ListAssetsResponse)


    
    
    public sealed class ListAssetsResponse : IPageResponse<ListAssetsResponse.Types.ListAssetsResult>, IEnumerable<ListAssetsResponse.Types.ListAssetsResult>, IEnumerable, IMessage<ListAssetsResponse>, IEquatable<ListAssetsResponse>, IDeepCloneable<ListAssetsResponse>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Security Command Center v1p1beta1 API class ListAssetsResponse.

Response message for listing assets.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListAssetsResponse

## Implements

[IPageResponse](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageResponse-1.html)[ListAssetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.ListAssetsResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.ListAssetsResponse.Types)[ListAssetsResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.ListAssetsResponse.Types.ListAssetsResult), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[ListAssetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.ListAssetsResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.ListAssetsResponse.Types)[ListAssetsResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.ListAssetsResponse.Types.ListAssetsResult), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListAssetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.ListAssetsResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListAssetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.ListAssetsResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListAssetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.ListAssetsResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.SecurityCenter.V1P1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1)

## Assembly

Google.Cloud.SecurityCenter.V1P1Beta1.dll

## Constructors 

### ListAssetsResponse()
    
    
    public ListAssetsResponse()

### ListAssetsResponse(ListAssetsResponse)
    
    
    public ListAssetsResponse(ListAssetsResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListAssetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.ListAssetsResponse)`  
  
  
## Properties 

### ListAssetsResults
    
    
    public RepeatedField<ListAssetsResponse.Types.ListAssetsResult> ListAssetsResults { get; }

Assets matching the list request.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[ListAssetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.ListAssetsResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.ListAssetsResponse.Types)[ListAssetsResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.ListAssetsResponse.Types.ListAssetsResult)` |   
  
### NextPageToken
    
    
    public string NextPageToken { get; set; }

Token to retrieve the next page of results, or empty if there are no more results.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ReadTime
    
    
    public Timestamp ReadTime { get; set; }

Time used for executing the list request.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### TotalSize
    
    
    public int TotalSize { get; set; }

The total number of assets matching the query.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
## Methods 

### GetEnumerator()
    
    
    public IEnumerator<ListAssetsResponse.Types.ListAssetsResult> GetEnumerator()

Returns an enumerator that iterates through the resources in this response.

**Returns**  
---  
**Type** | **Description**  
`[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1)[ListAssetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.ListAssetsResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.ListAssetsResponse.Types)[ListAssetsResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.ListAssetsResponse.Types.ListAssetsResult)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
