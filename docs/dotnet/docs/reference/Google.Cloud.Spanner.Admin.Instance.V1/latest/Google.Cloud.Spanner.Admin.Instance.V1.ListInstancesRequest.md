---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.ListInstancesRequest
title: Google Cloud Spanner Instance Administration v1 API - Class ListInstancesRequest (5.13.0-beta11) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:29:52.670530+00:00
---

# Google Cloud Spanner Instance Administration v1 API - Class ListInstancesRequest (5.13.0-beta11)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.ListInstancesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Spanner Instance Administration v1 API - Class ListInstancesRequest (5.13.0-beta11) Stay organized with collections  Save and categorize content based on your preferences. 

5.13.0-beta11  5.13.0-beta10  5.12.0 (latest)  5.11.0  5.10.0  5.9.0  5.8.0  5.7.0  5.6.0  5.5.0  5.4.0  5.3.0  5.2.0  5.1.0  5.0.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.15.1  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0 
    
    
    public sealed class ListInstancesRequest : IPageRequest, IMessage<ListInstancesRequest>, IEquatable<ListInstancesRequest>, IDeepCloneable<ListInstancesRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Spanner Instance Administration v1 API class ListInstancesRequest.

The request for [ListInstances][google.spanner.admin.instance.v1.InstanceAdmin.ListInstances].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListInstancesRequest

## Implements

[IPageRequest](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageRequest.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.ListInstancesRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.ListInstancesRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.ListInstancesRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Spanner.Admin.Instance.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1)

## Assembly

Google.Cloud.Spanner.Admin.Instance.V1.dll

## Constructors 

### ListInstancesRequest()
    
    
    public ListInstancesRequest()

### ListInstancesRequest(ListInstancesRequest)
    
    
    public ListInstancesRequest(ListInstancesRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.ListInstancesRequest)`  
  
  
## Properties 

### Filter
    
    
    public string Filter { get; set; }

An expression for filtering the results of the request. Filter rules are case insensitive. The fields eligible for filtering are:

  * `name`
  * `display_name`
  * `labels.key` where key is the name of a label



Some examples of using filters are:

  * `name:*` \--> The instance has a name.
  * `name:Howl` \--> The instance's name contains the string "howl".
  * `name:HOWL` \--> Equivalent to above.
  * `NAME:howl` \--> Equivalent to above.
  * `labels.env:*` \--> The instance has the label "env".
  * `labels.env:dev` \--> The instance has the label "env" and the value of the label contains the string "dev".
  * `name:howl labels.env:dev` \--> The instance's name contains "howl" and it has the label "env" with its value containing "dev".



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### InstanceDeadline
    
    
    public Timestamp InstanceDeadline { get; set; }

Deadline used while retrieving metadata for instances. Instances whose metadata cannot be retrieved within this deadline will be added to [unreachable][google.spanner.admin.instance.v1.ListInstancesResponse.unreachable] in [ListInstancesResponse][google.spanner.admin.instance.v1.ListInstancesResponse].

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### PageSize
    
    
    public int PageSize { get; set; }

Number of instances to be returned in the response. If 0 or less, defaults to the server's maximum allowed page size.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PageToken
    
    
    public string PageToken { get; set; }

If non-empty, `page_token` should contain a [next_page_token][google.spanner.admin.instance.v1.ListInstancesResponse.next_page_token] from a previous [ListInstancesResponse][google.spanner.admin.instance.v1.ListInstancesResponse].

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The name of the project for which a list of instances is requested. Values are of the form `projects/<project>`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsProjectName
    
    
    public ProjectName ParentAsProjectName { get; set; }

[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.ListInstancesRequest#Google_Cloud_Spanner_Admin_Instance_V1_ListInstancesRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
