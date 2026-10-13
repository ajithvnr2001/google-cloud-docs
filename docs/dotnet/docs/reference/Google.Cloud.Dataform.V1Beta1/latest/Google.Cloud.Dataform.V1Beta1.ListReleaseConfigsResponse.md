---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListReleaseConfigsResponse
title: Dataform v1beta1 API - Class ListReleaseConfigsResponse (1.0.0-beta15) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:48:25.494374+00:00
---

# Dataform v1beta1 API - Class ListReleaseConfigsResponse (1.0.0-beta15)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListReleaseConfigsResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Dataform v1beta1 API - Class ListReleaseConfigsResponse (1.0.0-beta15) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta15 (latest)  1.0.0-beta14 
    
    
    public sealed class ListReleaseConfigsResponse : IMessage<ListReleaseConfigsResponse>, IEquatable<ListReleaseConfigsResponse>, IDeepCloneable<ListReleaseConfigsResponse>, IBufferMessage, IMessage, IPageResponse<ReleaseConfig>, IEnumerable<ReleaseConfig>, IEnumerable

Reference documentation and code samples for the Dataform v1beta1 API class ListReleaseConfigsResponse.

`ListReleaseConfigs` response message.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListReleaseConfigsResponse

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListReleaseConfigsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListReleaseConfigsResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListReleaseConfigsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListReleaseConfigsResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListReleaseConfigsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListReleaseConfigsResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html), [IPageResponse](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageResponse-1.html)[ReleaseConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReleaseConfig), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[ReleaseConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReleaseConfig), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dataform.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1)

## Assembly

Google.Cloud.Dataform.V1Beta1.dll

## Constructors 

### ListReleaseConfigsResponse()
    
    
    public ListReleaseConfigsResponse()

### ListReleaseConfigsResponse(ListReleaseConfigsResponse)
    
    
    public ListReleaseConfigsResponse(ListReleaseConfigsResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListReleaseConfigsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListReleaseConfigsResponse)`  
  
  
## Properties 

### NextPageToken
    
    
    public string NextPageToken { get; set; }

A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ReleaseConfigs
    
    
    public RepeatedField<ReleaseConfig> ReleaseConfigs { get; }

List of release configs.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[ReleaseConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReleaseConfig)` |   
  
### Unreachable
    
    
    public RepeatedField<string> Unreachable { get; }

Locations which could not be reached.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
## Methods 

### GetEnumerator()
    
    
    public IEnumerator<ReleaseConfig> GetEnumerator()

Returns an enumerator that iterates through the resources in this response.

**Returns**  
---  
**Type** | **Description**  
`[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1)[ReleaseConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReleaseConfig)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
