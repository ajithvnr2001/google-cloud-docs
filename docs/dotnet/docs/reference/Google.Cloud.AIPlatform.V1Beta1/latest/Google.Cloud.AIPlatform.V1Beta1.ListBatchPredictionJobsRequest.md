---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListBatchPredictionJobsRequest
title: Vertex AI v1beta1 API - Class ListBatchPredictionJobsRequest (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:23:28.816069+00:00
---

# Vertex AI v1beta1 API - Class ListBatchPredictionJobsRequest (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListBatchPredictionJobsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class ListBatchPredictionJobsRequest (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public sealed class ListBatchPredictionJobsRequest : IMessage<ListBatchPredictionJobsRequest>, IEquatable<ListBatchPredictionJobsRequest>, IDeepCloneable<ListBatchPredictionJobsRequest>, IBufferMessage, IMessage, IPageRequest

Reference documentation and code samples for the Vertex AI v1beta1 API class ListBatchPredictionJobsRequest.

Request message for [JobService.ListBatchPredictionJobs][google.cloud.aiplatform.v1beta1.JobService.ListBatchPredictionJobs].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListBatchPredictionJobsRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListBatchPredictionJobsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListBatchPredictionJobsRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListBatchPredictionJobsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListBatchPredictionJobsRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListBatchPredictionJobsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListBatchPredictionJobsRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html), [IPageRequest](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageRequest.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Constructors 

### ListBatchPredictionJobsRequest()
    
    
    public ListBatchPredictionJobsRequest()

### ListBatchPredictionJobsRequest(ListBatchPredictionJobsRequest)
    
    
    public ListBatchPredictionJobsRequest(ListBatchPredictionJobsRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListBatchPredictionJobsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListBatchPredictionJobsRequest)`  
  
  
## Properties 

### Filter
    
    
    public string Filter { get; set; }

The standard list filter.

Supported fields:

  * `display_name` supports `=`, `!=` comparisons, and `:` wildcard.
  * `model_display_name` supports `=`, `!=` comparisons.
  * `state` supports `=`, `!=` comparisons.
  * `create_time` supports `=`, `!=`,`<`, `<=`,`>`, `>=` comparisons. `create_time` must be in RFC 3339 format.
  * `labels` supports general map functions that is: `labels.key=value` \- key:value equality `labels.key:* - key existence



Some examples of using the filter are:

  * `state="JOB_STATE_SUCCEEDED" AND display_name:"my_job_*"`
  * `state!="JOB_STATE_FAILED" OR display_name="my_job"`
  * `NOT display_name="my_job"`
  * `create_time>"2021-05-18T00:00:00Z"`
  * `labels.keyA=valueA`
  * `labels.keyB:*`



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PageSize
    
    
    public int PageSize { get; set; }

The standard list page size.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PageToken
    
    
    public string PageToken { get; set; }

The standard list page token. Typically obtained via [ListBatchPredictionJobsResponse.next_page_token][google.cloud.aiplatform.v1beta1.ListBatchPredictionJobsResponse.next_page_token] of the previous [JobService.ListBatchPredictionJobs][google.cloud.aiplatform.v1beta1.JobService.ListBatchPredictionJobs] call.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The resource name of the Location to list the BatchPredictionJobs from. Format: `projects/{project}/locations/{location}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsLocationName
    
    
    public LocationName ParentAsLocationName { get; set; }

[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListBatchPredictionJobsRequest#Google_Cloud_AIPlatform_V1Beta1_ListBatchPredictionJobsRequest_Parent) resource name property.

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
