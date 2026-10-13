---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryDatabaseResourceGroupsRequest
title: Database Center v1beta API - Class QueryDatabaseResourceGroupsRequest (1.0.0-beta08) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:34:59.239756+00:00
---

# Database Center v1beta API - Class QueryDatabaseResourceGroupsRequest (1.0.0-beta08)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryDatabaseResourceGroupsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Database Center v1beta API - Class QueryDatabaseResourceGroupsRequest (1.0.0-beta08) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta08 (latest)  1.0.0-beta07 
    
    
    public sealed class QueryDatabaseResourceGroupsRequest : IPageRequest, IMessage<QueryDatabaseResourceGroupsRequest>, IEquatable<QueryDatabaseResourceGroupsRequest>, IDeepCloneable<QueryDatabaseResourceGroupsRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Database Center v1beta API class QueryDatabaseResourceGroupsRequest.

QueryDatabaseResourceGroupsRequest is the request to get a list of database groups.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > QueryDatabaseResourceGroupsRequest

## Implements

[IPageRequest](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageRequest.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[QueryDatabaseResourceGroupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryDatabaseResourceGroupsRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[QueryDatabaseResourceGroupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryDatabaseResourceGroupsRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[QueryDatabaseResourceGroupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryDatabaseResourceGroupsRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DatabaseCenter.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta)

## Assembly

Google.Cloud.DatabaseCenter.V1Beta.dll

## Constructors 

### QueryDatabaseResourceGroupsRequest()
    
    
    public QueryDatabaseResourceGroupsRequest()

### QueryDatabaseResourceGroupsRequest(QueryDatabaseResourceGroupsRequest)
    
    
    public QueryDatabaseResourceGroupsRequest(QueryDatabaseResourceGroupsRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[QueryDatabaseResourceGroupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryDatabaseResourceGroupsRequest)`  
  
  
## Properties 

### Filter
    
    
    public string Filter { get; set; }

Optional. The expression to filter resources.

The following fields are filterable:

  * full_resource_name
  * resource_type
  * container
  * product.type
  * product.engine
  * product.version
  * location
  * labels
  * resource_category
  * machine_config.cpu_count
  * machine_config.memory_size_bytes
  * machine_config.shard_count
  * resource_name
  * tags
  * backupdr_config.backupdr_managed
  * edition



The expression is a list of zero or more restrictions combined via logical operators `AND` and `OR`. When `AND` and `OR` are both used in the expression, parentheses must be appropriately used to group the combinations.

Example: `location="us-east1"` Example: `container="projects/123" OR container="projects/456"` Example: `(container="projects/123" OR container="projects/456") AND location="us-east1"` Example: `full_resource_name=~"test"` Example: `full_resource_name=~"test.*master"`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OrderBy
    
    
    public string OrderBy { get; set; }

Optional. A field that specifies the sort order of the results.

The following fields are sortable:

  * full_resource_name
  * product.type
  * product.engine
  * product.version
  * container
  * issue_count
  * machine_config.vcpu_count
  * machine_config.memory_size_bytes
  * machine_config.shard_count
  * resource_name
  * issue_severity
  * signal_type
  * location
  * resource_type
  * instance_type
  * edition
  * metrics.p99_cpu_utilization
  * metrics.p95_cpu_utilization
  * metrics.current_storage_used_bytes
  * metrics.node_count
  * metrics.processing_unit_count
  * metrics.current_memory_used_bytes
  * metrics.peak_storage_utilization
  * metrics.peak_number_connections
  * metrics.peak_memory_utilization



The default order is ascending. Add "DESC" after the field name to indicate descending order. Add "ASC" after the field name to indicate ascending order. It only supports a single field at a time.

For example: `order_by = "full_resource_name"` sorts response in ascending order `order_by = "full_resource_name DESC"` sorts response in descending order `order_by = "issue_count DESC"` sorts response in descending order of count of all issues associated with a resource.

More explicitly, `order_by = "full_resource_name, product"` is not supported.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PageSize
    
    
    public int PageSize { get; set; }

Optional. If unspecified, at most 50 resource groups will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PageToken
    
    
    public string PageToken { get; set; }

Optional. A page token, received from a previous `QueryDatabaseResourceGroupsRequest` call. Provide this to retrieve the subsequent page. All parameters except page_token should match the parameters in the call that provided the page page token.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. Parent can be a project, a folder, or an organization. The search is limited to the resources within the `scope`.

The allowed values are:

  * projects/{PROJECT_ID} (e.g., "projects/foo-bar")
  * projects/{PROJECT_NUMBER} (e.g., "projects/12345678")
  * folders/{FOLDER_NUMBER} (e.g., "folders/1234567")
  * organizations/{ORGANIZATION_NUMBER} (e.g., "organizations/123456")



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SignalFilters
    
    
    public RepeatedField<SignalFilter> SignalFilters { get; }

Optional. Filters based on signals. The list will be ORed together and then ANDed with the `filters` field above.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[SignalFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.SignalFilter)` |   
  
### SignalTypeGroups
    
    
    public RepeatedField<SignalTypeGroup> SignalTypeGroups { get; }

Optional. Groups of signal types that are requested.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[SignalTypeGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.SignalTypeGroup)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
