---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeaturestoresRequest
title: Vertex AI v1beta1 API - Class ListFeaturestoresRequest (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:45:20.415585+00:00
---

# Vertex AI v1beta1 API - Class ListFeaturestoresRequest (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeaturestoresRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class ListFeaturestoresRequest (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public sealed class ListFeaturestoresRequest : IMessage<ListFeaturestoresRequest>, IEquatable<ListFeaturestoresRequest>, IDeepCloneable<ListFeaturestoresRequest>, IBufferMessage, IMessage, IPageRequest

Reference documentation and code samples for the Vertex AI v1beta1 API class ListFeaturestoresRequest.

Request message for [FeaturestoreService.ListFeaturestores][google.cloud.aiplatform.v1beta1.FeaturestoreService.ListFeaturestores].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListFeaturestoresRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListFeaturestoresRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeaturestoresRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListFeaturestoresRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeaturestoresRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListFeaturestoresRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeaturestoresRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html), [IPageRequest](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageRequest.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Constructors 

### ListFeaturestoresRequest()
    
    
    public ListFeaturestoresRequest()

### ListFeaturestoresRequest(ListFeaturestoresRequest)
    
    
    public ListFeaturestoresRequest(ListFeaturestoresRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListFeaturestoresRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeaturestoresRequest)`  
  
  
## Properties 

### Filter
    
    
    public string Filter { get; set; }

Lists the featurestores that match the filter expression. The following fields are supported:

  * `create_time`: Supports `=`, `!=`, `<`, `>`, `<=`, and `>=` comparisons. Values must be in RFC 3339 format.
  * `update_time`: Supports `=`, `!=`, `<`, `>`, `<=`, and `>=` comparisons. Values must be in RFC 3339 format.
  * `online_serving_config.fixed_node_count`: Supports `=`, `!=`, `<`, `>`, `<=`, and `>=` comparisons.
  * `labels`: Supports key-value equality and key presence.



Examples:

  * `create_time > "2020-01-01" OR update_time > "2020-01-01"` Featurestores created or updated after 2020-01-01.
  * `labels.env = "prod"` Featurestores with label "env" set to "prod".



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OrderBy
    
    
    public string OrderBy { get; set; }

A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending. Supported Fields:

  * `create_time`
  * `update_time`
  * `online_serving_config.fixed_node_count`



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PageSize
    
    
    public int PageSize { get; set; }

The maximum number of Featurestores to return. The service may return fewer than this value. If unspecified, at most 100 Featurestores will be returned. The maximum value is 100; any value greater than 100 will be coerced to 100.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PageToken
    
    
    public string PageToken { get; set; }

A page token, received from a previous [FeaturestoreService.ListFeaturestores][google.cloud.aiplatform.v1beta1.FeaturestoreService.ListFeaturestores] call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to [FeaturestoreService.ListFeaturestores][google.cloud.aiplatform.v1beta1.FeaturestoreService.ListFeaturestores] must match the call that provided the page token.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The resource name of the Location to list Featurestores. Format: `projects/{project}/locations/{location}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsLocationName
    
    
    public LocationName ParentAsLocationName { get; set; }

[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeaturestoresRequest#Google_Cloud_AIPlatform_V1Beta1_ListFeaturestoresRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)` |   
  
### ReadMask
    
    
    public FieldMask ReadMask { get; set; }

Mask specifying which fields to read.

**Property Value**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
