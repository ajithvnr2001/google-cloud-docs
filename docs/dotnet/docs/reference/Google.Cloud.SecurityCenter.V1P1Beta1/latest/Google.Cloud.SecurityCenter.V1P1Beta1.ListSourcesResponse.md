---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.ListSourcesResponse
title: Google Cloud Security Command Center v1p1beta1 API - Class ListSourcesResponse (3.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:10:36.505744+00:00
---

# Google Cloud Security Command Center v1p1beta1 API - Class ListSourcesResponse (3.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.ListSourcesResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Security Command Center v1p1beta1 API - Class ListSourcesResponse (3.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.0.0-beta06 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.ListSourcesResponse)
  * [ 3.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/3.0.0-beta05/Google.Cloud.SecurityCenter.V1P1Beta1.ListSourcesResponse)
  * [ 2.0.0-beta07 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/2.0.0-beta07/Google.Cloud.SecurityCenter.V1P1Beta1.ListSourcesResponse)


    
    
    public sealed class ListSourcesResponse : IPageResponse<Source>, IEnumerable<Source>, IEnumerable, IMessage<ListSourcesResponse>, IEquatable<ListSourcesResponse>, IDeepCloneable<ListSourcesResponse>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Security Command Center v1p1beta1 API class ListSourcesResponse.

Response message for listing sources.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListSourcesResponse

## Implements

[IPageResponse](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageResponse-1.html)[Source](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.Source), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Source](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.Source), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListSourcesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.ListSourcesResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListSourcesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.ListSourcesResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListSourcesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.ListSourcesResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.SecurityCenter.V1P1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1)

## Assembly

Google.Cloud.SecurityCenter.V1P1Beta1.dll

## Constructors 

### ListSourcesResponse()
    
    
    public ListSourcesResponse()

### ListSourcesResponse(ListSourcesResponse)
    
    
    public ListSourcesResponse(ListSourcesResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListSourcesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.ListSourcesResponse)`  
  
  
## Properties 

### NextPageToken
    
    
    public string NextPageToken { get; set; }

Token to retrieve the next page of results, or empty if there are no more results.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Sources
    
    
    public RepeatedField<Source> Sources { get; }

Sources belonging to the requested parent.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Source](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.Source)` |   
  
## Methods 

### GetEnumerator()
    
    
    public IEnumerator<Source> GetEnumerator()

Returns an enumerator that iterates through the resources in this response.

**Returns**  
---  
**Type** | **Description**  
`[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1)[Source](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.Source)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
