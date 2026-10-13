---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Admin.V2/latest/Google.Cloud.Bigtable.Admin.V2.ListTablesRequest
title: Google Cloud Bigtable Administration v2 API - Class ListTablesRequest (3.36.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:44:09.761517+00:00
---

# Google Cloud Bigtable Administration v2 API - Class ListTablesRequest (3.36.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Admin.V2/latest/Google.Cloud.Bigtable.Admin.V2.ListTablesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Bigtable Administration v2 API - Class ListTablesRequest (3.36.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.36.0 (latest)  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0 
    
    
    public sealed class ListTablesRequest : IMessage<ListTablesRequest>, IEquatable<ListTablesRequest>, IDeepCloneable<ListTablesRequest>, IBufferMessage, IMessage, IPageRequest

Reference documentation and code samples for the Google Cloud Bigtable Administration v2 API class ListTablesRequest.

Request message for [google.bigtable.admin.v2.BigtableTableAdmin.ListTables][google.bigtable.admin.v2.BigtableTableAdmin.ListTables]

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListTablesRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListTablesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Admin.V2/latest/Google.Cloud.Bigtable.Admin.V2.ListTablesRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListTablesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Admin.V2/latest/Google.Cloud.Bigtable.Admin.V2.ListTablesRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListTablesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Admin.V2/latest/Google.Cloud.Bigtable.Admin.V2.ListTablesRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html), [IPageRequest](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageRequest.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Bigtable.Admin.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Admin.V2/latest/Google.Cloud.Bigtable.Admin.V2)

## Assembly

Google.Cloud.Bigtable.Admin.V2.dll

## Constructors 

### ListTablesRequest()
    
    
    public ListTablesRequest()

### ListTablesRequest(ListTablesRequest)
    
    
    public ListTablesRequest(ListTablesRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListTablesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Admin.V2/latest/Google.Cloud.Bigtable.Admin.V2.ListTablesRequest)`  
  
  
## Properties 

### PageSize
    
    
    public int PageSize { get; set; }

Maximum number of results per page.

A page_size of zero lets the server choose the number of items to return. A page_size which is strictly positive will return at most that many items. A negative page_size will cause an error.

Following the first request, subsequent paginated calls are not required to pass a page_size. If a page_size is set in subsequent calls, it must match the page_size given in the first request.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PageToken
    
    
    public string PageToken { get; set; }

The value of `next_page_token` returned by a previous call.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The unique name of the instance for which tables should be listed. Values are of the form `projects/{project}/instances/{instance}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsInstanceName
    
    
    public InstanceName ParentAsInstanceName { get; set; }

[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.InstanceName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Admin.V2/latest/Google.Cloud.Bigtable.Admin.V2.ListTablesRequest#Google_Cloud_Bigtable_Admin_V2_ListTablesRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.InstanceName.html)` |   
  
### View
    
    
    public Table.Types.View View { get; set; }

The view to be applied to the returned tables' fields. NAME_ONLY view (default) and REPLICATION_VIEW are supported.

**Property Value**  
---  
**Type** | **Description**  
`[Table](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Admin.V2/latest/Google.Cloud.Bigtable.Admin.V2.Table)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Admin.V2/latest/Google.Cloud.Bigtable.Admin.V2.Table.Types)[View](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Admin.V2/latest/Google.Cloud.Bigtable.Admin.V2.Table.Types.View)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
