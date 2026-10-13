---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListPreviewsResponse
title: Infrastructure Manager v1 API - Class ListPreviewsResponse (1.13.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:32:53.469768+00:00
---

# Infrastructure Manager v1 API - Class ListPreviewsResponse (1.13.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListPreviewsResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Infrastructure Manager v1 API - Class ListPreviewsResponse (1.13.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.13.0 (latest)  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class ListPreviewsResponse : IMessage<ListPreviewsResponse>, IEquatable<ListPreviewsResponse>, IDeepCloneable<ListPreviewsResponse>, IBufferMessage, IMessage, IPageResponse<Preview>, IEnumerable<Preview>, IEnumerable

Reference documentation and code samples for the Infrastructure Manager v1 API class ListPreviewsResponse.

A response to a `ListPreviews` call. Contains a list of Previews.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListPreviewsResponse

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListPreviewsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListPreviewsResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListPreviewsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListPreviewsResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListPreviewsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListPreviewsResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html), [IPageResponse](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageResponse-1.html)[Preview](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Preview), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Preview](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Preview), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Config.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1)

## Assembly

Google.Cloud.Config.V1.dll

## Constructors 

### ListPreviewsResponse()
    
    
    public ListPreviewsResponse()

### ListPreviewsResponse(ListPreviewsResponse)
    
    
    public ListPreviewsResponse(ListPreviewsResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListPreviewsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ListPreviewsResponse)`  
  
  
## Properties 

### NextPageToken
    
    
    public string NextPageToken { get; set; }

Token to be supplied to the next ListPreviews request via `page_token` to obtain the next set of results.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Previews
    
    
    public RepeatedField<Preview> Previews { get; }

List of [Previews][google.cloud.config.v1.Preview].

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Preview](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Preview)` |   
  
### Unreachable
    
    
    public RepeatedField<string> Unreachable { get; }

Locations that could not be reached.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
## Methods 

### GetEnumerator()
    
    
    public IEnumerator<Preview> GetEnumerator()

Returns an enumerator that iterates through the resources in this response.

**Returns**  
---  
**Type** | **Description**  
`[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1)[Preview](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Preview)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-25 UTC."],[],[]] 
