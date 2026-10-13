---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.ListInstanceConfigsRequest
title: Google Cloud Spanner Instance Administration v1 API - Class ListInstanceConfigsRequest (5.13.0-beta11) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:19:05.097916+00:00
---

# Google Cloud Spanner Instance Administration v1 API - Class ListInstanceConfigsRequest (5.13.0-beta11)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.ListInstanceConfigsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Spanner Instance Administration v1 API - Class ListInstanceConfigsRequest (5.13.0-beta11) Stay organized with collections  Save and categorize content based on your preferences. 

5.13.0-beta11  5.13.0-beta10  5.12.0 (latest)  5.11.0  5.10.0  5.9.0  5.8.0  5.7.0  5.6.0  5.5.0  5.4.0  5.3.0  5.2.0  5.1.0  5.0.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.15.1  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0 
    
    
    public sealed class ListInstanceConfigsRequest : IPageRequest, IMessage<ListInstanceConfigsRequest>, IEquatable<ListInstanceConfigsRequest>, IDeepCloneable<ListInstanceConfigsRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Spanner Instance Administration v1 API class ListInstanceConfigsRequest.

The request for [ListInstanceConfigs][google.spanner.admin.instance.v1.InstanceAdmin.ListInstanceConfigs].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListInstanceConfigsRequest

## Implements

[IPageRequest](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageRequest.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListInstanceConfigsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.ListInstanceConfigsRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListInstanceConfigsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.ListInstanceConfigsRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListInstanceConfigsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.ListInstanceConfigsRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Spanner.Admin.Instance.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1)

## Assembly

Google.Cloud.Spanner.Admin.Instance.V1.dll

## Constructors 

### ListInstanceConfigsRequest()
    
    
    public ListInstanceConfigsRequest()

### ListInstanceConfigsRequest(ListInstanceConfigsRequest)
    
    
    public ListInstanceConfigsRequest(ListInstanceConfigsRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListInstanceConfigsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.ListInstanceConfigsRequest)`  
  
  
## Properties 

### PageSize
    
    
    public int PageSize { get; set; }

Number of instance configurations to be returned in the response. If 0 or less, defaults to the server's maximum allowed page size.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PageToken
    
    
    public string PageToken { get; set; }

If non-empty, `page_token` should contain a [next_page_token][google.spanner.admin.instance.v1.ListInstanceConfigsResponse.next_page_token] from a previous [ListInstanceConfigsResponse][google.spanner.admin.instance.v1.ListInstanceConfigsResponse].

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The name of the project for which a list of supported instance configurations is requested. Values are of the form `projects/<project>`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsProjectName
    
    
    public ProjectName ParentAsProjectName { get; set; }

[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.ListInstanceConfigsRequest#Google_Cloud_Spanner_Admin_Instance_V1_ListInstanceConfigsRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
